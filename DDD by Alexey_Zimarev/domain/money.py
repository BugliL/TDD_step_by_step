from dataclasses import dataclass, field
from decimal import Decimal
from typing import Union


# The class was splitted in 2 things
#  - dataclass MoneyClass
#  - factory method Money
# This was the best method I found to let MoneyClass be IMMUTABLE and
# to initialize the amount to a default Decimal type

@dataclass(frozen=True)
class MoneyClass:
    amount: Decimal = field(default=Decimal(0))


DecimalCompliant = Union[str, int, float, Decimal]


def Money(amount: DecimalCompliant = Decimal(0)) -> MoneyClass:
    if amount is None:
        raise ValueError('Amount must be not None')

    return MoneyClass(amount=Decimal(amount))


if __name__ == '__main__':
    x = Money(amount=12)
    print(x.amount)

    x = Money(amount='12')
    print(x.amount)

    x = Money(amount=Decimal(12))
    print(x.amount)

    y = Money()
    print(y.amount + 9)
    print(y)

    # Raise an error
    # y = Money(amount=None)
