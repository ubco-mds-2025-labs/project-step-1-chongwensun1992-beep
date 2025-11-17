"""
Base record class for SmartBudget.
All financial records inherit from this minimal base.
"""

class RecordBase:
    """Base class for all income/expense records."""

    def __init__(self, name: str, amount: float):
        self.name = name
        self.amount = float(amount)

    def show(self) -> str:
        return f"{self.name}: {self.amount:.2f}"

    def is_positive(self) -> bool:
        return self.amount > 0

    def to_dict(self) -> dict:
        """
        Basic serialization.
        Subclasses (Income/Expense) will override this to include extra fields.
        """
        return {
            "name": self.name,
            "amount": self.amount,
            "type": "RecordBase"   # for safety fallback
        }
