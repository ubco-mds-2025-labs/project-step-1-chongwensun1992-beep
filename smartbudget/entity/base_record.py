from smartbudget.entity.constants import Limits


class RecordBase:
    """Base class for all income/expense records."""

    def __init__(self, name: str, amount: float):
        self._validate_name(name)


        self.name = name
        self.amount = float(amount)

    # ------------------ Validation ------------------ #



    def _validate_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if len(name) > Limits.MAX_NAME_LEN:
            raise ValueError(
                f"Name cannot exceed {Limits.MAX_NAME_LEN} characters."
            )

    # ------------------ Public Methods ------------------ #

    def show(self) -> str:
        return f"{self.name}: {self.amount:.2f}"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "amount": self.amount,
            "type": self.__class__.__name__,
        }
