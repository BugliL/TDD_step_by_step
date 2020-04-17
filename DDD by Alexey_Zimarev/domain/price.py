from dataclasses import dataclass
from decimal import Decimal

from domain.money import Money


@dataclass(frozen=True)
class Price(Money):

    def __post_init__(self):
        if Decimal(self.amount) == 0:
            raise ValueError('Amount must be non-zero')
