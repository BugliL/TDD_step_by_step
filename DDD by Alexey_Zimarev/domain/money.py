from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Union

from domain.abstract_currency_lookup import AbstractCurrencyLookup, CurrencyDetails

DecimalCompliant = Union[str, int, float, Decimal]


@dataclass(frozen=True)
class Money:
    DEFAULT_CURRENCY = "EUR"

    amount: Decimal = field(default=Decimal(0))
    currency: str = field(default=DEFAULT_CURRENCY, init=True)

    def __post_init__(self):
        if self.amount is None:
            raise ValueError('Amount must be not None')

        if self.amount < 0:
            raise ValueError('Amount must be positive')

        if not (self.amount.as_tuple().exponent >= -2):
            raise ValueError('Only 2 decimal places allowed')

    @classmethod
    def create(cls, amount: DecimalCompliant, currency: str = DEFAULT_CURRENCY):
        return cls(amount=(Decimal(amount) if amount is not None else None), currency=currency)

    def __add__(self, other):
        self._operation_check(other)
        return Money.create(amount=(other.amount + self.amount))

    def __sub__(self, other):
        self._operation_check(other)
        return Money.create(amount=(self.amount - other.amount))

    def _operation_check(self, other):
        if type(other) != type(self):
            raise TypeError("{} is not {}, can't perform operation".format(type(other), type(self)))

        if other.currency != self.currency:
            raise TypeError("{} is not {}, can't perform operation".format(other.currency, self.currency))


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
