"""
I/O subpackage for SmartBudget.

Provides:
- JSON input/output utilities
- File system utilities
"""

from .json_io import (
    save_to_json,
    load_from_json
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
    # "json_pretty_print",

    # File utilities
    "file_exists",
    "delete_file",
    "list_files",
]
