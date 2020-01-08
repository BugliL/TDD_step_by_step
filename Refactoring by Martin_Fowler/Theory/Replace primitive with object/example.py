from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    ID: int
    date: datetime
    description: str
    priority: str


if __name__ == '__main__':
    orders = [
        Order(
            ID=1,
            date=datetime.now(),
            description="Foo bar",
            priority='high'
        ),
        Order(
            ID=2,
            date=datetime.now(),
            description="Foo bar",
            priority='low'
        )
    ]

    filtered_orders = list(filter(lambda x: x.priority == 'high', orders))
    assert len(filtered_orders) == 1
    assert filtered_orders[0].priority == 'high'
