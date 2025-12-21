import json
import os
import shutil
import sys
import tempfile
from json import JSONDecodeError
from pathlib import Path
from typing import Any, Dict, List, Optional

import click
import pyperclip
import typer
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from typing_extensions import Annotated

from . import __doc__ as package_doc
from . import api, utils
from ._version import __version__


app = typer.Typer(
    context_settings={"help_option_names": ["-h", "--help"]},
    pretty_exceptions_show_locals=False,
    add_completion=False,
)

console = Console(stderr=True)

state = {"verbose": False, "copy": True}


def vprint(*objects: Any, sep="\n", **kwargs):
    if state.get("verbose"):
        print(*objects, file=sys.stderr, sep=sep, **kwargs)


def copy_text(text: str):
    if state.get("copy"):
        try:
            pyperclip.copy(text)
        except pyperclip.PyperclipException as error:
            vprint(f"[yellow bold]Clipboard Warning[/yellow bold]: {error}")


def get_config_path(name: str = "sharex-cli", create: bool = False) -> Path:
    app_path = Path(typer.get_app_dir(name))
    if not app_path.is_dir():
        app_path.mkdir(parents=True)
    config_path = app_path / "config.json"
    if create:
        config_path.touch()
    return config_path


def update_config(config_path: Path, config_files: List[Path]):
    console.rule("[bold green]ShareX CLI Configuration", style="cyan bold")
    vprint(f"{config_path=}", f"{config_files=}")
    user_config = None

    if config_files and config_files[0].is_file():
        vprint(f"{config_files[0]=}")
        user_config = json.loads(config_files[0].read_text())
        vprint(f"1 {user_config=}")

    if not user_config:
        print(
            "\nDownload your servers ShareX Custom Uploader (*.sxcu) configuration, then:\n\n"
            " - Type or Paste the config [cyan bold]file path[/cyan bold].\n"
            " - Press [green bold]Enter[/green bold] to open a [cyan bold]text editor[/cyan bold].\n"
            " - Or press [yellow bold]Ctrl+C[/yellow bold] to abort.\n"
        )
        input_file = Path(typer.prompt("File Path", default="", show_default=False))
        vprint(f"{input_file=}")
        if input_file.is_file():
            user_config = json.loads(input_file.read_text())
            vprint(f"2 {user_config=}")

    if not user_config:
        res: Optional[str] = click.edit()
        vprint(f"{res=}")
        if res:
            user_config = json.loads(res)
            vprint(f"3 {user_config=}")

    if user_config and isinstance(user_config, dict):
        config_path.write_text(json.dumps(user_config))
        print(f"\n[green bold]Config Saved/Updated[/green bold]: [cyan bold]{config_path.absolute()}\n")
    else:
        raise click.ClickException("Error Saving Config")


def archive_dir(config, params: Dict[str, Any], dir_path: Path):
    vprint(f"{params}", f"{dir_path=}", f"{os.getcwd()=}")
    file_name = dir_path.name
    vprint(f"{file_name=}")
    if _name := params.get("_name"):
        file_name = _name
        if file_name.lower().endswith(".zip"):
            file_name = file_name[:-4]
    vprint(f"{file_name=}")
    table = Table(title="Archive Details")
    table.add_column("File Name", style="magenta bold", no_wrap=True)
    table.add_column("Path", style="cyan bold")
    table.add_row(file_name + ".zip", dir_path.absolute().as_posix())
    console.print(table)
    if not params.get("_yes"):
        typer.confirm("Create and Upload Archive?", abort=True)

    with tempfile.TemporaryDirectory() as d:
        vprint(f"{d=}")
        path = Path(d)
        archive = path / file_name
        vprint(f"{archive.absolute()=}")
        with console.status(f"Creating Archive: [cyan bold]{archive.absolute()}"):
            name = shutil.make_archive(archive.absolute().as_posix(), "zip", dir_path)
        vprint(f"{name=}")
        final_path = path / name
        vprint(f"{final_path=}", f"{final_path.name=}")
        size = utils.fmt_bytes(final_path.stat().st_size)
        with console.status(
            f"Uploading File: [green bold]{click.format_filename(final_path.name)}[/green bold] - [yellow bold]{size}"
        ):
            with open(final_path, "rb") as f:
                url = api.upload_file(config, final_path.name, f, final_path)
    print(url)
    copy_text(url)
    raise typer.Exit()


def version_callback(value: bool):
    if value:
        if package_doc:
            print(package_doc.lstrip("\n"), file=sys.stderr)
        print(f"[white bold]{__version__}")
        raise typer.Exit()


@app.command()
def main(  # NOSONAR
    ctx: typer.Context,
    files: Annotated[Optional[List[Path]], typer.Argument(help="Files or Directory...", exists=True)] = None,
    _name: Annotated[
        Optional[str], typer.Option("-n", "--name", metavar="", help="File Name (sent with upload).")
    ] = None,
    _glob: Annotated[
        str, typer.Option("-g", "--glob", metavar="", help="Directory Files Glob (use ** to recurse).")
    ] = "*",
    _archive: Annotated[
        bool, typer.Option("-a", "--archive", help="Directory Create Archive (no glob support).")
    ] = False,
    _yes: Annotated[
        bool, typer.Option("-y", "--yes", metavar="", help="Answer YES to Prompts.", envvar="SHAREX_YES")
    ] = False,
    _copy: Annotated[
        bool, typer.Option("--copy/--no-copy", "-c/-nc", help="Copy URL to Clipboard.", envvar="SHAREX_COPY")
    ] = True,
    _launch: Annotated[
        bool,
        typer.Option("--launch/--no-launch", "-l/-nl", help="Launch URL in Browser.", envvar="SHAREX_LAUNCH"),
    ] = True,
    _verbose: Annotated[
        bool, typer.Option("-v", "--verbose", help="Verbose Output.", envvar="SHAREX_VERBOSE")
    ] = False,
    _config: Annotated[bool, typer.Option("-C", "--config", help="Update Configuration.")] = False,
    _version: Annotated[
        Optional[bool],
        typer.Option("-V", "--version", callback=version_callback, help="Show Installed Version."),
    ] = None,
):
    """
    Files: A File, Multiple Files or a Directory.

    Docs: https://cssnr.github.io/sharex-cli/
    """
    # vprint(f"{dir(ctx)=}")
    vprint(f"{ctx.params=}")
    state["verbose"], state["copy"] = _verbose, _copy
    # state.update({"verbose": _verbose, "copy": _copy})
    vprint(f"{state=}")

    _files = files or []
    vprint(f"{_files=}")
    show_confirm = len(_files) > 1
    vprint(f"{show_confirm=}")

    config_path = get_config_path()
    vprint(f"config_path: [cyan bold]{config_path.resolve()}")

    config = api.get_config(config_path, "SHAREX_CONFIG")
    vprint(f"config loaded: {bool(config)}")

    vprint(f"{_config=}")
    if not config or _config:
        # Process Configuration
        try:
            update_config(config_path, _files)
            raise typer.Exit()
        except JSONDecodeError as error:
            vprint(f"{error=}")
            raise click.ClickException(f"Error Decoding Config: {error.msg}")  # noqa: B904

    tty = sys.stdin.isatty()
    vprint(f"{tty=}")

    if not tty or not _files:
        # Process STDIN
        file_name = _name or f"{utils.gen_rand(8)}.txt"
        vprint(f"{file_name=}")
        content = click.get_text_stream("stdin")
        url = api.upload_file(config, file_name, content)
        print(url)
        copy_text(url)
        if _launch:
            typer.launch(url)
        raise typer.Exit()

    if len(_files) == 1 and _files[0].is_dir():
        # Process Directory
        vprint(f"{_archive=}", f"{_yes=}")
        vprint(f"Processing Directory: [cyan bold]{_files[0].name}")
        if _archive:
            archive_dir(config, ctx.params, _files[0])
            raise typer.Exit()
        _files = [p for p in _files[0].glob(_glob.strip('"`')) if p.is_file()]
        show_confirm = True
        vprint(f"{_files=}")
    else:
        # Remove Directories
        files, dirs = [], []
        for fp in _files:
            files.append(fp) if fp.is_file() else dirs.append(fp)
        if dirs:
            _files = files
            text = "[yellow]" + "\n".join(p.absolute().as_posix() for p in dirs)
            print(Panel.fit(text, title=f"Directories Removed: [white]{len(dirs)}", style="red", title_align="left"))
            print("[yellow bold]Warning[/yellow bold]: Directories can be processed individually.\n", file=sys.stderr)

    # Process Files
    if not _files:
        raise click.ClickException("No Files to Process...")
    table = Table(title=f"Processing {len(_files)} File{utils.s(_files)}")
    table.add_column("File Name", style="magenta bold", no_wrap=True)
    table.add_column("Size", style="yellow bold")
    table.add_column("Path", style="cyan bold")
    for path in _files:
        table.add_row(path.name, utils.fmt_bytes(path.stat().st_size), path.absolute().as_posix())
    console.print(table)

    vprint(f"{show_confirm=}")
    if show_confirm and not _yes:
        typer.confirm(f"Confirm Uploading {len(_files)} Files?", abort=True)

    for i, file in enumerate(_files, 1):
        if file.is_dir():
            print(f"[yellow bold]Skipping directory[yellow bold]: [cyan bold]{file.absolute()}", file=sys.stderr)
            continue
        size = utils.fmt_bytes(file.stat().st_size)
        with console.status(
            f"Uploading {i}/{len(_files)}: [green bold]{click.format_filename(file.name)}[/green bold] - [yellow bold]{size}"
        ):
            file_name = _name if _name and len(_files) == 1 else file.name
            with open(file, "rb") as f:
                url = api.upload_file(config, file_name, f, file)
        print(url)
        copy_text(url)
        if _launch and len(_files) == 1 and url:
            typer.launch(url)
    raise typer.Exit()


if __name__ == "__main__":
    app()
