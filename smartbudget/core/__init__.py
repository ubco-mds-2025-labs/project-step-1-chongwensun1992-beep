"""
Core package for SmartBudget.
Exports menu functions and controller modules.
"""

from .controller_menu import print_menu, run
from .controller_records import (
    add_income,
    add_expense,
    show_summary,
    show_income_details,
    show_expense_details,
)
from .controller_system import (
    save_data,
    load_data,
    show_files,
    delete_backup_file,
)

__all__ = [
    # menu
    "print_menu",
    "run",

    # record controllers
    "add_income",
    "add_expense",
    "show_summary",
    "show_income_details",
    "show_expense_details",

    # system controllers
    "save_data",
    "load_data",
    "show_files",
    "delete_backup_file",
]
