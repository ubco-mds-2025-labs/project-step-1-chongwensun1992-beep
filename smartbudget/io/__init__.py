"""
I/O subpackage for SmartBudget.

Provides:
- JSON input/output utilities
- File system utilities
"""

from .json_io import (
    save_to_json,
    load_from_json,
    append_to_json,   # ← 新增
)

from .file_utils import (
    file_exists,
    delete_file,
    list_files
)

__all__ = [
    # JSON I/O
    "save_to_json",
    "load_from_json",
    "append_to_json",

    # File utilities
    "file_exists",
    "delete_file",
    "list_files",
]