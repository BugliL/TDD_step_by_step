from dataclasses import dataclass, field
from datetime import datetime
from typing import Union


@dataclass
class Priority:
    value: str

    def __str__(self) -> str:
        return self.value

    def __post_init__(self):
        if self.value not in ['high', 'low']:
            raise ValueError("{} is not a valid priority".format(self.value))

@dataclass
class Order:
    ID: int
    date: datetime
    description: str
    priority: Union[str, Priority]

    _priority: Priority = field(init=False, repr=False)

    @property
    def priority(self) -> Priority:
        return self._priority

    @priority.setter
    def priority(self, value: Union[str, Priority]):
        self._priority = Priority(value) if type(value) != Priority else value


if __name__ == '__main__':
    orders = [
        Order(
            ID=1,
            date=datetime.now(),
            description="Foo bar",
            priority='low'
        ),
        Order(
            ID=2,
            date=datetime.now(),
            description="Foo bar",
            priority='low'
        )
    ]

    high_priority = Priority('high')
    low_priority = Priority('low')
    orders[0].priority = 'high'
    orders[0].priority = high_priority

    filtered_orders = list(filter(lambda x: x.priority == high_priority, orders))
    assert len(filtered_orders) == 1
    assert filtered_orders[0].priority == high_priority
