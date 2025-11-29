"""
I/O subpackage for SmartBudget.

This module exposes convenient helper functions for:
- JSON reading/writing operations
- Basic file-system utilities (checking files, listing files, deleting files)

These functions are imported from the underlying json_io.py and file_utils.py
modules so that users can access them directly from smartbudget.io.
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
    "json_pretty_print",

    # File utilities
    "file_exists",
    "delete_file",
    "list_files",
]
