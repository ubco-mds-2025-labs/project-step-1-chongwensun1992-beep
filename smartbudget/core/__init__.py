"""
Core subpackage: base record classes and transaction models.
"""

from .base_record import RecordBase
from .transaction import Expense, Income

__all__ = ["RecordBase", "Expense", "Income"]
