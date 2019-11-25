import itertools
from typing import Iterable


class Cell(object):
    AliveStatus = True
    DeadStatus = False

    def __init__(self, status: bool, neighbours: Iterable):
        # self._set_neighbours(neighbours)
        self.is_alive = status
        self.future_state = False
        self.neighbours = set(neighbours)
        for cell in self.neighbours:
            cell.add_neighbour(self)

    def add_neighbour(self, cell):
        self.neighbours = set(itertools.chain(self.neighbours, [cell]))

    def die_in_future(self):
        self.future_state = self.DeadStatus

    def be_alive_in_future(self):
        self.future_state = self.AliveStatus

    def stay_in_future(self):
        self.future_state = self.is_alive

    def evolve(self):
        self.is_alive = self.future_state

    def set_future_state(self):
        strategy_by_neighbours = {
            2: self.stay_in_future,
            3: self.be_alive_in_future,
        }.get(
            # TypeError: get() takes no keyword arguments
            len(list(filter(lambda x: x.is_alive, self.neighbours))),
            self.die_in_future
        )

        strategy_by_neighbours()
