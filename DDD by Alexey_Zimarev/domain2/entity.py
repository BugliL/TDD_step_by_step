from dataclasses import dataclass, field
from typing import List, Type


class Event:
    pass


@dataclass
class EntityEvent:
    events: List = field(init=False, default_factory=list)
    callbacks: dict = field(init=False, default_factory=dict)

    def ensure_valid_state(self):
        pass

    def apply(self, event: Event):
        self.when(event)
        self.ensure_valid_state()
        self.events.append(event)

    def when(self, event: Event):
        fn = self.callbacks.get(event.__class__)
        fn(self, event)
