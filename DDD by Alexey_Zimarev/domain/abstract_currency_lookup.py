from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class CurrencyDetails:
    currency_code: str = field(init=True)
    in_use: bool = field(init=True)
    decimal_places: int = field(init=True)

    @classmethod
    def NoneCurrency(cls):
        return cls(currency_code='FAKE', in_use=False, decimal_places=2)


class AbstractCurrencyLookup(ABC):

    @classmethod
    @abstractmethod
    def find(cls, currency_code: str) -> CurrencyDetails:
        pass
