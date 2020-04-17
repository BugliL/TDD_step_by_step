from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Union

DecimalCompliant = Union[str, int, float, Decimal]


@dataclass(frozen=True)
class Money:
    amount: Decimal = field(default=Decimal(0))

    def __post_init__(self):
        if self.amount is None:
            raise ValueError('Amount must be not None')

        if Decimal(self.amount) < 0:
            raise ValueError('Amount must be positive')

    @classmethod
    def create(cls, amount: DecimalCompliant) -> Money:
        return Money(amount=(Decimal(amount) if amount is not None else None))


if __name__ == '__main__':
    x = Money.create(amount=12)
    print(x.amount)  # prints 12

    x = Money.create(amount='12')
    print(x.amount)  # prints 12

    x = Money.create(amount=Decimal(12))
    print(x.amount)  # prints 12

    y = Money.create(amount=0)
    print(y.amount + 9)
    print(y)  # prints 9

    # Raise an error
    # y = Money(amount=None)
