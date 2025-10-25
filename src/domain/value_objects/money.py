from dataclasses import dataclass
from typing import Literal

CURRENCY_TYPES = Literal["USD", "INR"]


@dataclass(frozen=True)
class Money:
    amount: float
    currency: CURRENCY_TYPES = "INR"

    def __post_init__(self):
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")
        if not self.currency:
            raise ValueError("Currency cannot be empty")