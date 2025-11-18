"""
Analysis helpers for SmartBudget.
Provides simple income/expense details and sorting.
"""

from typing import List
from smartbudget.entity.transaction import Expense, Income
from smartbudget.io.json_io import load_from_json


# ======================================
# Internal helper: always load file data
# ======================================

def _load_split():
    """Load records from records.json and split into incomes/expenses."""
    records = load_from_json()

    incomes = [r for r in records if isinstance(r, Income)]
    expenses = [r for r in records if isinstance(r, Expense)]

    return incomes, expenses


# ============================
# expense
# ============================

def expense_details() -> List[str]:
    """Return formatted descriptions of all expenses from records.json."""
    _, expenses = _load_split()
    return [e.describe() for e in expenses]




# ============================
# income
# ============================

def income_details() -> List[str]:
    """Return formatted descriptions of all incomes from records.json."""
    incomes, _ = _load_split()
    return [i.describe() for i in incomes]


