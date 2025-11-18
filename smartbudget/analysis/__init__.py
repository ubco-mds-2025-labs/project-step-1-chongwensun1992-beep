"""
Analysis subpackage: summary statistics and income/expense insights.
"""

from .summary import (
    total_income,
    total_expenses,
    budget_balance
)

from .insights import (
    expense_details,
    income_details
)

__all__ = [
    "total_income",
    "total_expenses",
    "budget_balance",

    # expense functions
    "expense_details",
    "largest_expenses",

    # income functions
    "income_details",
    "largest_incomes",

    # utility
    "print_records",
]
