[![PyPI Version](https://img.shields.io/pypi/v/sharex-cli?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/sharex-cli/)
[![GitHub Release Version](https://img.shields.io/github/v/release/cssnr/sharex-cli?logo=github)](https://github.com/cssnr/sharex-cli/releases)
[![TOML Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcssnr%2Fsharex-cli%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=%24.project.requires-python&logo=python&logoColor=white&label=python)](https://github.com/cssnr/sharex-cli?tab=readme-ov-file#readme)
[![PyPI Downloads](https://img.shields.io/pypi/dm/sharex-cli?logo=pypi&logoColor=white)](https://pypistats.org/packages/sharex-cli)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/sharex-cli?logo=pypi&logoColor=white&label=total)](https://clickpy.clickhouse.com/dashboard/sharex-cli)
[![Codecov](https://codecov.io/gh/cssnr/sharex-cli/graph/badge.svg?token=A8NDHZ393X)](https://codecov.io/gh/cssnr/sharex-cli)
[![Workflow Lint](https://img.shields.io/github/actions/workflow/status/cssnr/sharex-cli/lint.yaml?logo=cachet&label=lint)](https://github.com/cssnr/sharex-cli/actions/workflows/lint.yaml)
[![Workflow Test](https://img.shields.io/github/actions/workflow/status/cssnr/sharex-cli/test.yaml?logo=cachet&label=test)](https://github.com/cssnr/sharex-cli/actions/workflows/test.yaml)
[![Deployment PyPi](https://img.shields.io/github/deployments/cssnr/sharex-cli/pypi?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/sharex-cli/)
[![Deployment Docs](https://img.shields.io/github/deployments/cssnr/sharex-cli/docs?logo=materialformkdocs&logoColor=white&label=docs)](https://cssnr.github.io/sharex-cli/)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/sharex-cli?logo=github&label=updated)](https://github.com/cssnr/sharex-cli/pulse)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/cssnr/sharex-cli?logo=bookstack&logoColor=white&label=repo%20size)](https://github.com/cssnr/sharex-cli)
[![GitHub Top Language](https://img.shields.io/github/languages/top/cssnr/sharex-cli?logo=htmx&logoColor=white)](https://github.com/cssnr/sharex-cli?tab=readme-ov-file#readme)
[![GitHub Contributors](https://img.shields.io/github/contributors-anon/cssnr/sharex-cli?logo=github)](https://github.com/cssnr/sharex-cli/graphs/contributors)
[![GitHub Issues](https://img.shields.io/github/issues/cssnr/sharex-cli?logo=github)](https://github.com/cssnr/sharex-cli/issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/cssnr/sharex-cli?logo=github)](https://github.com/cssnr/sharex-cli/discussions)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/sharex-cli?style=flat&logo=github)](https://github.com/cssnr/sharex-cli/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/sharex-cli?style=flat&logo=github)](https://github.com/cssnr/sharex-cli/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

# ShareX CLI

<a title="ShareX CLI" href="https://cssnr.github.io/sharex-cli/" target="_blank">
<img alt="ShareX CLI" align="right" width="128" height="auto" src="https://cssnr.github.io/sharex-cli/assets/images/logo.svg"></a>

- [Features](#features)
- [Install](#install)
- [Configure](#configure)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

Command Line Interface to Upload Files to a ShareX Server using a ShareX Custom Uploader `.sxcu` configuration.

Upload any file, multiple files, directories, use globs, create archives and much more...

To get started [Install](#install) the app, [Configure](#configure) your server and view the [Usage](#usage).

If you run into any issues or have any questions, [support](#support) is available.

[![View Documentation](https://img.shields.io/badge/view_documentation-blue?style=for-the-badge&logo=googledocs&logoColor=white)](https://cssnr.github.io/sharex-cli/)

## Features<a id="features"></a>

- Use a ShareX Custom Uploader `*.sxcu` config.
- Upload a file or multiple files.
- Specify a custom file name.
- Upload files in a directory with optional glob.
- Upload a directory as an archive.
- Automatically open the URL in browser.
- Automatically copy the URL to the clipboard.
- Display confirmation before uploading multiple files.
- Override all options with flags or env vars.

## Install<a id="install"></a>

From PyPI: <https://pypi.org/p/sharex-cli>

```shell
pip install sharex-cli
```

```shell
uv tool install sharex-cli
```

From GitHub: [https://github.com/cssnr/sharex-cli](https://github.com/cssnr/sharex-cli?tab=readme-ov-file#readme)

```shell
pip install git+https://github.com/cssnr/sharex-cli.git
```

```shell
uv tool install git+https://github.com/cssnr/sharex-cli.git
```

[![View Install Guide](https://img.shields.io/badge/view_install_guide-blue?style=for-the-badge&logo=googledocs&logoColor=white)](https://cssnr.github.io/sharex-cli/cli/#install)

## Configure<a id="configure"></a>

To configure you need your server's ShareX Custom Uploader `*.sxcu` configuration JSON.

The `--config` command allows you to enter the file path, or open a text editor.

```shell
sharex --config
```

Or pass the config path directly to `--config`.

```shell
sharex --config path/to/config.sxcu
```

[![View Configure Guide](https://img.shields.io/badge/view_configure_guide-blue?style=for-the-badge&logo=googledocs&logoColor=white)](https://cssnr.github.io/sharex-cli/cli/#configure)

## Usage<a id="usage"></a>

To use run the `sharex` command with the path to the file to upload.

```shell
sharex file.txt
sharex file1.txt file2.txt
sharex file.txt -n name.txt
```

Directories can be uploaded as files using a glob (default `*`) or as an archive.

```shell
sharex dir1  # non-recursive
sharex dir1 -g '**'  # recursive
sharex dir1 -a  # create an archive
```

Tip: you will be shown a confirmation before files are uploaded.

[![View Upload Guide](https://img.shields.io/badge/view_upload_guide-blue?style=for-the-badge&logo=googledocs&logoColor=white)](https://cssnr.github.io/sharex-cli/cli/#upload)

## Support<a id="support"></a>

If you run into any issues or need help getting started, please do one of the following:

- Report an Issue: <https://github.com/cssnr/sharex-cli/issues>
- Q&A Discussion: <https://github.com/cssnr/sharex-cli/discussions/categories/q-a>
- Request a Feature: <https://github.com/cssnr/sharex-cli/issues/new?template=1-feature.yaml>
- Request Server Support: <https://github.com/cssnr/sharex-cli/issues/new?template=2-server.yaml>
- Chat with us on Discord: <https://discord.gg/wXy6m2X8wY>

[![Features](https://img.shields.io/badge/features-brightgreen?style=for-the-badge&logo=googleanalytics&logoColor=white)](https://github.com/cssnr/sharex-cli/issues/new?template=1-feature.yaml)
[![Issues](https://img.shields.io/badge/issues-red?style=for-the-badge&logo=southwestairlines&logoColor=white)](https://github.com/cssnr/sharex-cli/issues)
[![Discussions](https://img.shields.io/badge/discussions-blue?style=for-the-badge&logo=rocketdotchat&logoColor=white)](https://github.com/cssnr/sharex-cli/discussions)
[![Discord](https://img.shields.io/badge/discord-yellow?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/wXy6m2X8wY)

## Contributing<a id="contributing"></a>

If you would like to submit a PR, please review the [CONTRIBUTING.md](#contributing-ov-file).

Please consider making a donation to support the development of this project
and [additional](https://cssnr.com/) open source projects.

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/cssnr)

For a full list of current projects visit: [https://cssnr.github.io/](https://cssnr.github.io/)
