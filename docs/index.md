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

=== "pip"

    ```shell
    pip install sharex-cli
    ```

=== "uv"

    ```shell
    uv tool install sharex-cli
    ```

=== "brew"

    ```shell
    brew install cssnr/tap/sharex-cli
    ```

=== "download"

    - [windows-amd64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/windows-amd64.zip)
    - [macos-amd64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/macos-amd64.zip)
    - [macos-arm64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/macos-arm64.zip)
    - [linux-amd64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/linux-amd64.zip)
    - [linux-arm64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/linux-arm64.zip)

    To install the binary see the [Download](cli.md#download) section.

See the [Quick Start](#quick-start) section to get started...

!!! tip "There are detailed [Install](cli.md#install), [Configure](cli.md#configure) and [Upload](cli.md#upload) guides available."

If you run into any issues or have any questions, [support](support.md) is available.

**:lucide-sparkles: [Features](#features)**  
**:lucide-plane-takeoff: [Quick Start](#quick-start)**  
**:lucide-server: [Server Support](#server-support)**

## :lucide-sparkles: Features

- Use a ShareX Custom Uploader `*.sxcu` config.
- Upload a file or multiple files.
- Specify a custom file name.
- Upload files in a directory with optional glob.
- Upload a directory as an archive.
- Automatically open the URL in browser.
- Automatically copy the URL to the clipboard.
- Display confirmation before uploading multiple files.
- Override all options with flags or env vars.

## :lucide-plane-takeoff: Quick Start

First, install from [PyPI :lucide-arrow-up-right:](https://pypi.org/p/sharex-cli)
or [GitHub :lucide-arrow-up-right:](https://github.com/cssnr/sharex-cli/releases/latest).

=== "pip"

    ```shell
    pip install sharex-cli
    ```

=== "uv"

    ```shell
    uv tool install sharex-cli
    ```

=== "download"

    - [windows-amd64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/windows-amd64.zip)
    - [macos-amd64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/macos-amd64.zip)
    - [macos-arm64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/macos-arm64.zip)
    - [linux-amd64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/linux-amd64.zip)
    - [linux-arm64.zip](https://github.com/cssnr/sharex-cli/releases/latest/download/linux-arm64.zip)

    To install the binary see the [Download](cli.md#download) section.

See the [Install](cli.md#install) guide for more options.

Next, download your server's ShareX [Custom Uploader :lucide-arrow-up-right:](https://getsharex.com/docs/custom-uploader) `*.sxcu` configuration.

Using the `--config` option you can enter a file path or open a text editor.

```shell
sharex --config
```

See the [Configure](cli.md#configure) guide for more details.

Finally, upload a file, multiple files, or a directory.

```shell
sharex screenshot.jpg
```

See the [Upload](cli.md#upload) guide for more examples.

[:lucide-square-terminal: View Uploading Guide](cli.md#upload){ .md-button .md-button--primary }

&nbsp;

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

## :lucide-server: Server Support

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

!!! success "Server Support Request"

     If your server is not supported, please submit [Server Support :lucide-arrow-up-right:](https://github.com/cssnr/sharex-cli/issues/new?template=2-server.yaml) feature request.

&nbsp;

[![Features](https://img.shields.io/badge/features-brightgreen?style=for-the-badge&logo=googleanalytics&logoColor=white)](https://github.com/cssnr/sharex-cli/issues/new?template=1-feature.yaml)
[![Issues](https://img.shields.io/badge/issues-red?style=for-the-badge&logo=southwestairlines&logoColor=white)](https://github.com/cssnr/sharex-cli/issues)
[![Discussions](https://img.shields.io/badge/discussions-blue?style=for-the-badge&logo=rocketdotchat&logoColor=white)](https://github.com/cssnr/sharex-cli/discussions)
[![Discord](https://img.shields.io/badge/discord-yellow?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/wXy6m2X8wY)

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!
