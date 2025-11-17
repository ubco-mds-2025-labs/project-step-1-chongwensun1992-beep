"""
SmartBudget: A simple household budget / smart budgeting package.

Subpackages:
- core: core record classes for incomes and expenses.
- analysis: functions for summaries and trends.
- io: helper functions to save and load data.
"""

from .core.transaction import Expense, Income
from .analysis.summary import total_income, total_expenses, budget_balance

__all__ = [
    "Expense",
    "Income",
    "total_income",
    "total_expenses",
    "budget_balance",
]
