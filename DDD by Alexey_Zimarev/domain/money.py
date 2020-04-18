from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Union, Type

from domain.abstract_currency_lookup import AbstractCurrencyLookup, CurrencyDetails

DecimalCompliant = Union[str, int, float, Decimal]


@dataclass(frozen=True)
class Money:
    DEFAULT_CURRENCY = "EUR"

    amount: Decimal = field(default=Decimal(0))
    currency: str = field(default=DEFAULT_CURRENCY, init=True)
    currency_details: CurrencyDetails = field(default=CurrencyDetails.NoneCurrency(), init=True, compare=False)

    def __post_init__(self):
        if self.amount is None:
            raise ValueError('Amount must be not None')

        if self.amount < 0:
            raise ValueError('Amount must be positive')

        if not (self.amount.as_tuple().exponent >= -2):
            raise ValueError('Only 2 decimal places allowed')

        if not self.currency_details.in_use:
            raise ValueError('Money must be in use')

    def __add__(self, other):
        self._operation_check(other)
        return Money(
            amount=(other.amount + self.amount),
            currency=self.currency,
            currency_details=self.currency_details
        )

    def __sub__(self, other):
        self._operation_check(other)
        return Money(
            amount=(self.amount - other.amount),
            currency=self.currency,
            currency_details=self.currency_details
        )

    def _operation_check(self, other):
        if type(other) != type(self):
            raise TypeError("{} is not {}, can't perform operation".format(type(other), type(self)))

        if other.currency != self.currency:
            raise TypeError("{} is not {}, can't perform operation".format(other.currency, self.currency))

    @classmethod
    def create(cls, amount: DecimalCompliant, currency: str, lookup: Type[AbstractCurrencyLookup]):
        if not lookup:
            raise ValueError('CurrencyLookup must be specifed correctly')

        currency_details = lookup.find(currency)

        return cls(
            amount=(Decimal(amount) if amount is not None else None),
            currency=currency_details.currency_code,
            currency_details=currency_details
        )
