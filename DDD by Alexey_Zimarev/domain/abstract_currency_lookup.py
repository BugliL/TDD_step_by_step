from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


# The in_use attribute is used to check both
#  - the dummy default object to avoid all null check
#  - the validity of the money value

@dataclass
class CurrencyDetail:
    currency_code: str = field(default='FAKE')
    in_use: bool = field(default=False)
    decimal_places: int = field(default=2)


# this is a domain service
class AbstractCurrencyLookup(ABC):

    @staticmethod
    def find(self, currency_code: str) -> CurrencyDetail:
        pass
