"""
Income class — stores positive money value.
"""

from .base_record import RecordBase


class Income(RecordBase):
    """Represents an income (money coming in)."""

    def __init__(self, name: str, amount: float, source: str):
        super().__init__(name, abs(amount))
        self.source = source

    def describe(self) -> str:
        return f"Income '{self.name}' from source '{self.source}': {self.amount:.2f}"

    def to_dict(self) -> dict:
        return {
            "type": "Income",
            "name": self.name,
            "amount": self.amount,
            "source": self.source,
        }
