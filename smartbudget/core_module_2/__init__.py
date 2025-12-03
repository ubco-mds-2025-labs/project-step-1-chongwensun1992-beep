"""
Core package for SmartBudget.
Exports menu functions and controller modules.
"""

from .app_menu_controller import print_menu, run
from .budget_record_controller import (
    add_income,
    add_expense,
    show_summary,
    show_income_details,
    show_expense_details,
)
from .file_io_data_controller import (
    save_data,
    load_data,
    show_files,
    clear_data,
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
    "clear_data",
    "load_data",
    "show_files",
    "delete_backup_file",
]
