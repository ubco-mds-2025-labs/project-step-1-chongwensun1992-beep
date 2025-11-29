"""
Expense class — stores positive amount.
Negative conversion is handled in analysis.summary.
"""

from .base_record import RecordBase


class Expense(RecordBase):
    """Represents an expense (money going out)."""

    def __init__(self, name: str, amount: float, category: str):
        super().__init__(name, abs(amount))   # ALWAYS POSITIVE
        self.category = category

    def describe(self) -> str:
        return f"Expense '{self.name}' in category '{self.category}': {self.amount:.2f}"

    def to_dict(self) -> dict:
        return {
            "type": "Expense",
            "name": self.name,
            "amount": self.amount,
            "category": self.category,
        }
