"""
SmartBudget: A simple household budget / smart budgeting package.

Subpackages:
- entity: entity record classes for incomes and expenses.
- analysis: functions for summaries and trends.
- io: helper functions to save and load data.
"""

from .entity.transaction import Expense, Income
from .analysis.summary import total_income, total_expenses, budget_balance

__all__ = [
    "Expense",
    "Income",
    "total_income",
    "total_expenses",
    "budget_balance",
]
