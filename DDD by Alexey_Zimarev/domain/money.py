from dataclasses import dataclass, field
from decimal import Decimal


@dataclass(frozen=True)
class Money:
    amount: Decimal = field(default=Decimal(0))

    def __post_init__(self):
        if self.amount is None:
            raise ValueError('Amount must be not None')


if __name__ == '__main__':
    x = Money(amount=12)
    print(x.amount + 19)

    y = Money()
    print(y.amount + 9)
    print(y)

    # Raise an error
    # y = Money(amount=None)
