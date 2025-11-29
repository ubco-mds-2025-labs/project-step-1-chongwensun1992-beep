"""
JSON input/output helpers for SmartBudget.

This module provides utility functions for saving and loading financial
records (Income, Expense, or generic RecordBase) into/from JSON files.
All files are stored inside the SmartBudget 'files/' directory.
"""

import json
import os
from smartbudget.io.file_utils import FILES_DIR, ensure_files_dir
from smartbudget.core.transaction import Income, Expense
from smartbudget.core.base_record import RecordBase


def save_to_json(records, filename):
    """Save a list of record objects (Income, Expense, or RecordBase)
    into a JSON file inside the 'files/' directory."""
    ensure_files_dir()
    path = os.path.join(FILES_DIR, filename)

    data = [r.to_dict() for r in records]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def load_from_json(filename):
    """Load from files/filename."""
    ensure_files_dir()
    path = os.path.join(FILES_DIR, filename)

    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    objects = []
    for item in raw:
        if item.get("type") == "Income":
            obj = Income(item["name"], item["amount"], item.get("source", "Unknown"))
        elif item.get("type") == "Expense":
            obj = Expense(item["name"], abs(item["amount"]), item.get("category", "Unknown"))
        else:
            obj = RecordBase(item["name"], item["amount"])
        objects.append(obj)

    return objects
