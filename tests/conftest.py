import subprocess
from pathlib import Path

test_files_repo = "https://github.com/smashedr/test-files"


def pytest_runtest_setup(*args):
    path = Path(__file__).parent / "files"
    # print(f"path: {path}")
    if not path.is_dir():
        print("Checking Out Test Files...")
        get_test_files(path)


def get_test_files(path: Path):
    subprocess.run(["git", "clone", "--depth", "1", test_files_repo, path.absolute().as_posix()])
    print(f"get_test_files: {path}")
    folder: Path
    for folder in path.glob("*"):
        print(f"folder: {folder.name}")
        if not folder.is_dir():
            continue
        if folder.name.startswith("."):
            continue
        for file in folder.glob("*"):
            print(f"file: {file.name}")
            if "." not in file.name:
                continue
            parts = file.name.rsplit(".", 1)
            new_name = f"{parts[0]}-{parts[1]}"
            print(f"new_name: {new_name}")
            new_path = file.with_name(new_name)
            print(f"new_path: {new_path}")
            file.rename(new_path)
