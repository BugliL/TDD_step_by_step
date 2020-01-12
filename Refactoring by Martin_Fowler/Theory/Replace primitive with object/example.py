from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Order:
    ID: int
    date: datetime
    description: str
    priority: str

    _priority: str = field(init=False, repr=False)

    @property
    def priority(self) -> str:
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value


@dataclass
class Priority:
    value: str

    def __str__(self) -> str:
        return self.value


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

    priority = Priority('high')

    filtered_orders = list(filter(lambda x: x.priority == 'high', orders))
    assert len(filtered_orders) == 1
    assert filtered_orders[0].priority == 'high'
