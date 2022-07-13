import os


def get_script_from_local_bin(name: str) -> str:
    return f"{_get_local_bin_path()}/{name}"


def _get_local_bin_path() -> str:
    return f"{os.environ['HOME']}/.local/bin"
