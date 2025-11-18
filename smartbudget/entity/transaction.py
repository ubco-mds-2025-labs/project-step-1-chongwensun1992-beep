"""
Income and Expense classes for SmartBudget.
Now includes proper to_dict() so data can be saved & restored fully.
"""

from .base_record import RecordBase


class Expense(RecordBase):
    """Represents an expense (money going out)."""

    def __init__(self, name: str, amount: float, category: str):
        # Store negative to keep consistent with summary calculations
        super().__init__(name, -abs(amount))
        self.category = category

    def describe(self) -> str:
        return f"Expense '{self.name}' in category '{self.category}': {self.amount:.2f}"

    def to_dict(self) -> dict:
        """
        Override RecordBase.to_dict() so JSON includes category.
        """
        return {
            "name": self.name,
            "amount": self.amount,
            "category": self.category,
            "type": "Expense"
        }


class Income(RecordBase):
    """Represents an income (money coming in)."""

    def __init__(self, name: str, amount: float, source: str):
        super().__init__(name, abs(amount))
        self.source = source

    def describe(self) -> str:
        return f"Income '{self.name}' from source '{self.source}': {self.amount:.2f}"

    def to_dict(self) -> dict:
        """
        Override RecordBase.to_dict() so JSON includes source.
        """
        return {
            "name": self.name,
            "amount": self.amount,
            "source": self.source,
            "type": "Income"
        }
