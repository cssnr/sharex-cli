---
icon: lucide/square-terminal
---

# :lucide-square-terminal: Command Line Interface

[![ShareX CLI](assets/images/logo.svg){ align=right width=96 }](https://github.com/cssnr/sharex-cli?tab=readme-ov-file#readme)

With the CLI you can easily upload any files or folders with globs or as an archive.

To view the source code, see the [cli.py :lucide-arrow-up-right:](https://github.com/cssnr/sharex-cli/blob/master/src/sharex/cli.py) on GitHub.

To use run the `sharex` command from your terminal.

```shell
sharex [OPTIONS] [FILES]...  # (1)!
```

1. :lucide-lightbulb: Tip: Save your options with [Environment](#environment) variables.

<!-- 1 -->

- [Install](#install)
- [Configure](#configure)
- [Upload](#upload)
- [Environment](#environment)

## Install

[Python](#python) is recommended if you have
[Python :lucide-arrow-up-right:](https://www.python.org/downloads/) or
[astral-sh/uv :lucide-arrow-up-right:](https://docs.astral.sh/uv/) installed.

Linux and macOS users can install with [Homebrew](#homebrew).

Alternatively, you can [Download](#download) a binary release.

### :simple-pypi: Python

From PyPI: <https://pypi.org/p/sharex-cli>

=== "pip"

    ```shell
    pip install sharex-cli
    ```

=== "uv"

    ```shell
    uv tool install sharex-cli
    ```

From GitHub: [https://github.com/cssnr/sharex-cli](https://github.com/cssnr/sharex-cli?tab=readme-ov-file#readme)

=== "pip"

    ```shell
    pip install git+https://github.com/cssnr/sharex-cli.git
    ```

=== "uv"

    ```shell
    uv tool install git+https://github.com/cssnr/sharex-cli.git
    ```

From source.

=== "pip"

    ```shell
    git clone https://github.com/cssnr/sharex-cli.git
    pip install sharex-cli
    ```

=== "uv"

    ```shell
    git clone https://github.com/cssnr/sharex-cli.git
    uv pip install install sharex-cli
    ```

Upgrade.

=== "pip"

    ```shell
    pip install -U sharex-cli
    ```

=== "uv"

    ```shell
    uv tool upgrade sharex-cli
    ```

Uninstall.

=== "pip"

    ```shell
    pip uninstall sharex-cli
    ```

=== "uv"

    ```shell
    uv tool uninstall sharex-cli
    ```

### :simple-homebrew: Homebrew

Install the formula _(package)_.

```shell
brew install cssnr/tap/sharex-cli
```

Upgrade.

```shell
brew update && brew install sharex-cli
```

Uninstall.

```shell
brew uninstall sharex-cli
```

For more details see: <https://docs.brew.sh/>

Tap Source: <https://github.com/cssnr/homebrew-tap>

### :lucide-download: Download

From GitHub: <https://github.com/cssnr/sharex-cli/releases/latest>

- [windows-amd64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/windows-amd64.zip)
- [macos-amd64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/macos-amd64.zip)
- [macos-arm64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/macos-arm64.zip)
- [linux-amd64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/linux-amd64.zip)
- [linux-arm64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/linux-arm64.zip)

To install a binary release, unzip the archive and place the file in your `PATH`.

Unix: the file should already be executable, if not run `chmod +x sharex`.

If you need additional help, [support](support.md) is available.

## Configure

To configure you need your server's ShareX Custom Uploader `*.sxcu` configuration JSON.

The app will automatically enter configuration on the first run.

```shell
sharex
```

This allows you to enter a file path, or open a text editor to enter the contents.

To re-configure pass the `--config` flag.

```shell
sharex --config
```

You can also pass the path to the config file.

```shell
sharex --config path/to/config.sxcu
```

You can then press Enter to open a text editor or paste the config path.

```text
$ sharex

Download your servers ShareX Custom Uploader (*.sxcu) configuration, then:

 - Type or Paste the config file path.
 - Press Enter to open a text editor.
 - Or press Ctrl+C to abort.

File Path:
```

!!! success "Server Support Request"

     If your server is not supported, please submit [Server Support :lucide-arrow-up-right:](https://github.com/cssnr/sharex-cli/issues/new?template=2-server.yaml) feature request.

## Upload

Upload a file run the `sharex` command with the path to the file to upload.

```shell
sharex file.txt
```

Upload a file with a custom filename.

```shell
sharex file.txt -n other.txt
```

Upload multiple files.

```shell
sharex file1.txt file2.txt
```

Upload files in a directory (default glob: `*`).

```shell
sharex dir1
```

Upload files in a directory matching a glob.

```shell
sharex dir1 -g '*.md'
```

Upload files in a directory recursively (use any recursive glob).

```shell
sharex dir1 -g '**'
```

Create an archive of a directory to upload.

```shell
sharex dir1 -a
```

Don't launch the file in the browser.

```shell
sharex file.txt -nl  # (1)!
```

1. :lucide-lightbulb: Tip: Save your options with [Environment](#environment) variables.

Create text file from standard input.

```shell
echo "test text" | sharex -n test.txt
```

Create text file from clipboard or text.

```shell
sharex
# Paste or type contents here followed by a newline
# Then press Ctrl+D (Windows press Ctrl+Z then Enter)
```

## Environment

Many options support setting environment variable defaults.

| Environment&nbsp;Variable | Default | Type | Description           |
| :------------------------ | :-----: | :--: | :-------------------- |
| `SHAREX_COPY`             |    1    | bool | Copy URL to Clipboard |
| `SHAREX_LAUNCH`           |    1    | bool | Launch URL in Browser |
| `SHAREX_YES`              |    0    | bool | Answer YES to Prompts |
| `SHAREX_VERBOSE`          |    0    | bool | Verbose Output        |
| `SHAREX_CONFIG`           |    -    | str  | JSON Config Data      |

Allowed boolean values, case-insensitive.

```plain
0, 1, f, false, n, no, off, on, t, true, y, yes
```

You can set variables on the command line.

=== "Unix"

    ```shell
    export SHAREX_VERBOSE=1
    ```

=== "Windows"

    ```pwsh
    $env:SHAREX_VERBOSE=1
    ```

&nbsp;

To see the help use the `--help` flag.

```text
$ sharex --help

 Usage: sharex [OPTIONS] [FILES]...

 Files: A File, Multiple Files or a Directory.

┌─ Arguments ──────────────────────────────────────────────────────────────────────┐
│   files      [FILES]...  Files or Directory...                                   │
└──────────────────────────────────────────────────────────────────────────────────┘
┌─ Options ────────────────────────────────────────────────────────────────────────┐
│ --name     -n                    File Name (sent with upload).                   │
│ --glob     -g                    Directory Files Glob (use ** to recurse).       │
│                                  [default: *]                                    │
│ --archive  -a                    Directory Create Archive (no glob support).     │
│ --yes      -y                    Answer YES to Prompts. [env var: SHAREX_YES]    │
│ --copy     -c  --no-copy    -nc  Copy URL to Clipboard. [env var: SHAREX_COPY]   │
│                                  [default: copy]                                 │
│ --launch   -l  --no-launch  -nl  Launch URL in Browser. [env var: SHAREX_LAUNCH] │
│                                  [default: launch]                               │
│ --verbose  -v                    Verbose Output. [env var: SHAREX_VERBOSE]       │
│ --config   -C                    Update Configuration.                           │
│ --version  -V                    Show Installed Version.                         │
│ --help     -h                    Show this message and exit.                     │
└──────────────────────────────────────────────────────────────────────────────────┘
```

!!! tip "In the terminal output is scaled and displays properly."

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!
