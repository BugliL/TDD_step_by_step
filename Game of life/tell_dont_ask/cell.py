import itertools
from typing import Iterable


class Cell(object):
    AliveStatus = True
    DeadStatus = False

    def __init__(this, status: bool, neighbours: Iterable):
        this.neighbours = set(neighbours)
        this.is_alive = status
        this.future_state = False
        for cell in this.neighbours:
            cell.add_neighbour(this)

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
            len(list(filter(lambda x: x.is_alive, self.neighbours))),
            self.die_in_future
        )

        strategy_by_neighbours()
