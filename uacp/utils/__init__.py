import os
import tempfile


def convert_backslashes(path: str):
    """Convert all \\ to / of file path."""
    return path.replace("\\", "/")


def get_default_storage_path(module_name: str = "") -> str:
    storage_path = os.path.expanduser("~/.ecjtu")

    if module_name:
        storage_path = os.path.join(storage_path, module_name)

    # Try to create the storage path (with module subdirectory if specified)
    # Use a temporary directory instead if permission is denied,
    try:
        os.makedirs(storage_path, exist_ok=True)
    except PermissionError:
        storage_path = os.path.join(tempfile.gettempdir(), "ecjtu", module_name)
        os.makedirs(storage_path, exist_ok=True)

    return convert_backslashes(storage_path)
