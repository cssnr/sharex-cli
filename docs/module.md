---
icon: fontawesome/brands/python
---

# :fontawesome-brands-python: Python Module

[![ShareX CLI](assets/images/logo.svg){ align=right width=96 }](https://github.com/cssnr/sharex-cli?tab=readme-ov-file#readme)

Python projects can import the module directly.

First add the package to your project.

From PyPI: <https://pypi.org/p/sharex-cli>

=== "pip"

    ```shell
    pip install --group dev sharex-cli
    ```

=== "uv"

    ```shell
    uv add --dev sharex-cli
    ```

The `config` object must be a dictionary loaded from the ShareX `.sxcu` JSON.

The `get_config` method loads this from a file or environment variable, or returns None.

```python
from pathlib import Path
from sharex import api

config = api.get_config(Path("path/to/config.file"), 'SHAREX_CONFIG')  # (1)!
with open("filename", "rb") as f:
    url = api.upload_file(config, "filename", f)
print(f"{url=}")
```

1. ShareX Custom Uploader Config JSON.

Or import the modules individually.

```python
from sharex import get_config, upload_file
```

For more details see the [api.py :lucide-arrow-up-right:](https://github.com/cssnr/sharex-cli/blob/master/src/sharex/api.py) source code.

!!! warning "This API is incomplete and may change in the future."

    The API exist to support the [CLI](cli.md) and will adapt to fit those needs.

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!
