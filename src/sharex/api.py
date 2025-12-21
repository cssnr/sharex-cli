import json
import mimetypes
import os
import warnings
from json import JSONDecodeError
from pathlib import Path
from typing import IO, Optional

import requests
from jsonpath_ng.ext import parse

from ._version import __version__


session = requests.Session()

session.headers.update({"user-agent": f"requests/sharex-{__version__}"})


def upload_file(config, file_name: str, file_data: IO, path: Optional[Path] = None) -> str:
    """Upload a File from an SXCU Config"""
    url = config["RequestURL"]
    # print(f"{url=}")
    method = config["RequestMethod"]
    name = config["FileFormName"]
    headers = config["Headers"]
    key = config["URL"]

    # path = Path(file_name)
    mime_type = get_type(path)
    # print(f"{mime_type=}")

    files = {name: (file_name, file_data, mime_type)}
    r = session.request(method, url, headers=headers, files=files)  # nosec
    if not r.ok:  # pragma: no cover
        print(f"{r.status_code=}")
        print(f"{r.text=}")
        r.raise_for_status()

    data = r.json()
    # print(f"{data=}")

    key_path = key.strip("{}").split(":")[1]
    # print(f"{key_path=}")

    jsonpath_expr = parse(key_path)
    match = [match.value for match in jsonpath_expr.find(data)]
    # print(f"{match=}")
    return match[0]


def get_config(config_path: Optional[Path] = None, env_var: str = "", create_empty: bool = True):
    """Parse a JSON config from Env or Path or return None"""
    if env_var:
        var = os.environ.get(env_var, None)
        if var:
            try:
                return json.loads(var)
            except JSONDecodeError:
                pass
    if not config_path:
        return None
    if not config_path.is_file():
        if create_empty:
            config_path.touch()
        return None
    try:
        with open(config_path, "r") as f:
            return json.loads(f.read())
    except JSONDecodeError:
        return None


def get_type(path: Optional[Path] = None) -> str:  # NOSONAR
    """
    Get MIME type from guess_type or by reading magic headers
    https://en.wikipedia.org/wiki/List_of_file_signatures

    Deprecated since version 3.13: Passing a file path instead of URL is soft deprecated. Use guess_file_type() for this.
    https://docs.python.org/3/library/mimetypes.html#mimetypes.guess_type
    """
    if not path:
        return "text/plain"

    mime_type, _ = mimetypes.guess_type(path, strict=False)
    if mime_type:
        return mime_type

    if not path.is_file():
        return "text/plain"

    with open(path, "rb") as file:
        chunk = file.read(512)

    # print(f"chunk: {type(chunk)} - {chunk[:20]}")
    # print(f"test chunk: {chunk[8:11]}")

    if isinstance(chunk, str):  # pragma: no cover
        warnings.warn("This condition should not be True...", stacklevel=2)
        return "text/plain"

    # Images
    if chunk[0:3] == b"\xff\xd8\xff" or chunk[6:10] in (b"JFIF", b"Exif"):
        return "image/jpeg"
    elif chunk.startswith(b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a"):
        return "image/png"
    elif chunk.startswith(b"RIFF") and chunk[8:12] == b"WEBP":
        return "image/webp"
    elif chunk.startswith((b"\x47\x49\x46\x38\x37\x61", b"\x47\x49\x46\x38\x39\x61")):
        return "image/gif"
    elif chunk.startswith(b"\x66\x74\x79\x70\x68\x65\x69\x63\x66\x74\79\70\6d") or chunk[4:12] == b"ftypheic":
        return "image/heic"
    elif chunk.startswith(b"\x00\x00\x01\x00"):
        return "image/ico"
    elif chunk.startswith(b"II*") or chunk.startswith(b"II+") or chunk.startswith(b"MM"):
        return "image/tiff"
    elif chunk.startswith(b"BM"):
        return "image/bmp"
    elif chunk[4:12] == b"ftypavif":
        return "image/avif"

    # Video
    elif chunk[4:12] == b"ftypisom" or chunk[4:12] == b"ftypMSNV" or chunk[4:12] == b"ftypmp42":
        return "video/mp4"
    elif chunk[3:11] in (b"\x66\x74\x79\x70\x4d\x53\x4e\x56", b"\x66\x74\x79\x70\x69\x73\x6f\x6d"):
        return "video/mp4"
    elif chunk.startswith(b"\x1a\x45\xdf\xa3"):
        # https://www.loc.gov/preservation/digital/formats//fdd/fdd000342.shtml
        return "video/x-matroska"
    elif chunk.startswith(b"RIFF") and chunk[8:11] == b"AVI":
        return "video/x-msvideo"
    elif chunk.startswith(b"\x30\x26\xb2\x75\x8e\x66\xcf\x11\xa6\xd9\x00\xaa\x00\x62\xce\x6c"):
        # https://www.loc.gov/preservation/digital/formats/fdd/fdd000091.shtml
        return "video/x-ms-asf"
    elif chunk.startswith(b"\x6d\x6f\x6f\x76") or chunk[4:10] == b"ftypqt":
        # https://www.file-recovery.com/mov-signature-format.htm
        return "video/quicktime"

    # Audio
    elif chunk.startswith((b"\xff\xfb", b"\xff\xfb", b"\xff\xfb", b"\x49\x44\x33")):
        return "audio/mp3"
    elif chunk.startswith(b"RIFF") and chunk[8:12] == b"WAVE":
        return "audio/wav"
    elif chunk.startswith(b"OggS"):
        return "application/ogg"

    # Fallback
    try:
        chunk.decode("utf-8")
        return "text/plain"
    except UnicodeDecodeError:
        return "application/octet-stream"
