"""
Summary functions for incomes and expenses.
"""

from typing import Iterable
from smartbudget.entity.transaction import Income, Expense
from smartbudget.io.json_io import load_from_json
from smartbudget.analysis.insights import _load_split



def total_income() -> float:
    incomes, _ = _load_split()
    return sum(item.amount for item in incomes)


def total_expenses() -> float:
    _, expenses = _load_split()
    return sum(item.amount for item in expenses)


def budget_balance() -> float:
    return total_income() + total_expenses()