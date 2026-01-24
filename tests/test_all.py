import io
from pathlib import Path
from typing import TextIO

from sharex import api

path = Path(__file__).parent

print(f"{path=}")


def test_api(monkeypatch):
    fake_path = path / "fake.json"
    if fake_path.is_file():
        fake_path.unlink()
    assert not api.get_config()
    assert not api.get_config(fake_path)
    assert not api.get_config(fake_path)
    monkeypatch.setenv("TEST_CONFIG", "invalid")
    assert not api.get_config(fake_path, "TEST_CONFIG")
    monkeypatch.setenv("TEST_CONFIG", "{}")
    assert api.get_config(fake_path, "TEST_CONFIG") == {}
    config_path = path / "config.json"
    print(f"{config_path.absolute()=}")
    config = api.get_config(config_path)
    print(f"{config=}")
    data: TextIO = io.StringIO("yes")
    url = api.upload_file(config, "no", data)
    print(f"{url=}")
    assert url == "response"


def test_types(pytestconfig):
    """WIP"""
    # print(f"{pytestconfig.files=}")
    files_dir = "files"
    files = {
        # - Images
        "images/avif-avif": "image/avif",
        "images/bmp-bmp": "image/bmp",
        "images/gif-gif": "image/gif",
        # "images/heic-heic": "image/heic",
        "images/ico-ico": "image/ico",
        "images/jpg-jpg": "image/jpeg",
        "images/png-png": "image/png",
        "images/tiff-tiff": "image/tiff",
        "images/webp-webp": "image/webp",
        # - Video
        # "video/avi-avi": "video/x-msvideo",
        # "video/mkv-mkv": "video/x-matroska",
        # "video/mov-mov": "video/quicktime",
        "video/h264-mp4": "video/mp4",
        "video/ms-asf-wmv": "video/x-ms-asf",
        # - Audio
        "audio/mp3-mp3": "audio/mp3",
        "audio/ogg-ogg": "application/ogg",
        "audio/wav-wav": "audio/wav",
        # - Other
        "other/text-txt": "text/plain",
        "other/zip-zip": "application/octet-stream",
    }
    for file, mime_type in files.items():
        file_path = path / f"{files_dir}/{file}"
        if not file_path.is_file():
            raise ValueError(f"Not a File: {file_path.absolute()}")
        mime = api.get_type(file_path)
        print(f"file: {file} - {mime}")
        assert mime_type == mime

    xpy = api.get_type(Path(__file__))
    print(f"py file - {xpy}")
    assert xpy == "text/x-python"

    fake = api.get_type(Path("fake"))
    print(f"string - {fake}")
    assert fake == "text/plain"
