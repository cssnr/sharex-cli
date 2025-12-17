---
icon: lucide/rocket
---

# :lucide-rocket: Get Started

[![ShareX CLI](assets/images/logo.svg){ align=right width=96 }](https://github.com/cssnr/sharex-cli?tab=readme-ov-file#readme)

[![PyPI Version](https://img.shields.io/pypi/v/sharex-cli?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/sharex-cli/)
[![TOML Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcssnr%2Fsharex-cli%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=%24.project.requires-python&logo=python&logoColor=white&label=python)](https://github.com/cssnr/sharex-cli?tab=readme-ov-file#readme)
[![PyPI Downloads](https://img.shields.io/pypi/dm/sharex-cli?logo=pypi&logoColor=white)](https://pypistats.org/packages/sharex-cli)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/sharex-cli?logo=pypi&logoColor=white&label=total)](https://clickpy.clickhouse.com/dashboard/sharex-cli)
[![Codecov](https://codecov.io/gh/cssnr/sharex-cli/graph/badge.svg?token=A8NDHZ393X)](https://codecov.io/gh/cssnr/sharex-cli)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/sharex-cli?logo=github&label=updated)](https://github.com/cssnr/sharex-cli/pulse)
[![GitHub Issues](https://img.shields.io/github/issues/cssnr/sharex-cli?logo=github)](https://github.com/cssnr/sharex-cli/issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/cssnr/sharex-cli?logo=github)](https://github.com/cssnr/sharex-cli/discussions)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/sharex-cli?style=flat&logo=github)](https://github.com/cssnr/sharex-cli/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/sharex-cli?style=flat&logo=github)](https://github.com/cssnr/sharex-cli/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

Command Line Interface to Upload Files to a ShareX Server using a ShareX Custom Uploader `.sxcu` configuration file.

Upload any file, multiple files, directories, use globs, create archives and much more...

!!! tip "To get started [Install](#install) the app and view the [Usage](#usage)."

If you run into any issues or have any questions, [support](support.md) is available.

- [Features](#features)
- [Install](#install)
- [Setup](#setup)
- [Usage](#usage)
- [Support](#support)

## Features

- Use a ShareX Custom Uploader `*.sxcu` config.
- Upload a file or multiple files.
- Specify a custom file name.
- Upload files in a directory with optional glob.
- Upload a directory as an archive.
- Automatically open the URL in browser.
- Automatically copy the URL to the clipboard.
- Display confirmation before uploading multiple files.
- Override all options with flags or env vars.

## Install

From PyPI: <https://pypi.org/p/sharex-cli>

=== "pip"

    ```shell
    pip install sharex-cli
    ```

=== "uv"

    ```shell
    uv tool install sharex-cli
    ```

From GitHub.

=== "pip"

    ```shell
    pip install git+https://github.com/cssnr/sharex-cli.git
    ```

=== "uv"

    ```shell
    uv tool install git+https://github.com/cssnr/sharex-cli.git
    ```

[:lucide-square-terminal: View Install Guide](cli.md#install){ .md-button .md-button--primary }

## Setup

To configure you need your server's ShareX [Custom Uploader :lucide-arrow-up-right:](https://getsharex.com/docs/custom-uploader) `*.sxcu` configuration JSON.

The `--config` command allows you to enter the file path, or open a text editor.

```shell
sharex --config
```

Or pass the config path directly to `--config`.

```shell
sharex --config path/to/config.sxcu
```

See the detailed [Setup](cli.md#setup) guide for more details.

[:lucide-square-terminal: View Setup Guide](cli.md#setup){ .md-button .md-button--primary }

## Usage

After [Setup](#setup) you can upload a file, or multiple.

```shell
sharex file1 file2
```

Or upload the contents of a directory, default glob is `*`.

```shell
sharex dir1
```

Or create an archive of the directory with the `--archive` flag.

See the [Uploading](cli.md#uploading) examples for more details.

[:lucide-square-terminal: View Uploading Guide](cli.md#uploading){ .md-button .md-button--primary }

Additionally, you can import the module into your Python project.

```python
from pathlib import Path
from sharex import api

config = api.get_config(Path("path/to/config.file"))  # (1)!
with open("filename", "rb") as f:
    url = api.upload_file(config, "filename", f)
print(f"{url=}")
```

1. ShareX Custom Uploader Config JSON.

:fontawesome-brands-python: View the [Module Documentation](module.md) for more details.

## Support

Supports the following ShareX [Custom Uploader :lucide-arrow-up-right:](https://getsharex.com/docs/custom-uploader) `*.sxcu` configurations.

Response Type Support:

- `json`

Upload Type Support:

- `MultipartFormData`

Partial Configuration Example.

```json
{
  "URL": "{json:files[0].url}", // (1)!
  "Body": "MultipartFormData" // (2)!
}
```

1.  Should include `json:` in the URL.
2.  Should be `MultipartFormData`.

If you don't have Python you can [get it here :lucide-arrow-up-right:](https://www.python.org/downloads/).

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!
