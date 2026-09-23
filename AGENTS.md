# Agents

ShareX CLI, a Python CLI to Upload Files to a ShareX Server using a ShareX Custom Uploader (.sxcu) Configuration File.

- Docs: https://cssnr.github.io/sharex-cli/
- Repo: https://github.com/cssnr/sharex-cli

## Structure

- [src/sharex](src/sharex) - Package
  - `cli.py` - Typer CLI (entry points `sharex.cli:app` / `sharex-cli.cli:app`)
  - `api.py` - Uploader (`upload_file`, `get_config`) and MIME type detection from magic bytes (`get_type`)
  - `utils.py` - Helpers (random names, human file sizes)
  - `_version.py` - Version (falls back to `0.0.1`)
  - `__init__.py`, `py.typed`
- [src/app.py](src/app.py) - PyInstaller entry point (Windows binary)
- [tests](tests) - Pytest; `conftest.py` auto-clones sample files from `smashedr/test-files` into `tests/files/`
- [docs](docs) - Zensical (MkDocs fork), see `zensical.toml`
- [assets](assets) - `win-version.yaml` for the Windows version resource
- [installer.iss](installer.iss) - Inno Setup script (Windows installer)
- [.github/workflows](.github/workflows) - build, docs, draft, homebrew, issue, labeler, lint, preview, pyinstaller, release, snapcraft, test
- [pyproject.toml](pyproject.toml) - Project config and `[tool.scripts]`

## Environment

- Use `uv` (repo root `.venv`). Install/sync dev dependencies with `uv sync` after editing `[dependency-groups].dev`.
- All scripts below are run via `uv run <name>` (or `run <name>` from toml-run).
- Global tools on PATH (not in the dev group): `zensical`, `prettier`.
- Windows installers need Inno Setup (`iscc.exe`) on PATH; PathMgr is fetched by the `pathmgr` script.

## Commands

Scripts are run via [toml-run](https://github.com/cssnr/toml-run) from [pyproject.toml](pyproject.toml):

| Command              | What it does                                              |
| -------------------- | --------------------------------------------------------- |
| `uv run test`        | Coverage run + report                                     |
| `uv run format`      | Full format: always run before finishing work             |
| `uv run lint`        | Full lint: always run before finishing work               |
| `uv run build`       | `hatch build` (wheel + sdist to `dist/`)                  |
| `uv run docs`        | `zensical serve --open --dev-addr 0.0.0.0:8000`           |
| `uv run docs-build`  | `zensical build --clean`                                  |
| `uv run pyinstaller` | PyInstaller Windows binary (uses `src/app.py`)            |
| `uv run win-version` | Generate `win-version.txt` from `assets/win-version.yaml` |
| `uv run inno`        | Inno Setup compile (`iscc.exe installer.iss`)             |

Sub-scripts (also runnable individually): `bandit`, `mypy`, `ruff`, `validate` (validate-pyproject), `yamllint`. Add `-v` for verbose output (e.g. `uv run lint -v`).

## Runtime Config

- The CLI reads config from the platform app dir (via `typer.get_app_dir("sharex-cli")`, e.g. `%APPDATA%\sharex-cli\config.json` on Windows). Run with `--config` to update it interactively.
- The config is a ShareX Custom Uploader (`.sxcu`) JSON: `RequestURL`, `RequestMethod`, `FileFormName`, `Headers`, `URL` (a jsonpath expression into the response).
- Env vars: `SHAREX_CONFIG` (JSON config string), `SHAREX_YES`, `SHAREX_COPY`, `SHAREX_LAUNCH`, `SHAREX_VERBOSE`.

## Notes

- `api.get_type` detects MIME from magic bytes; use the samples in `tests/files/` (auto-cloned by conftest) to test uploads.
- Windows release flow: `pyinstaller` builds the binary, `win-version` + `inno` build the installer with version info from `assets/win-version.yaml`.
