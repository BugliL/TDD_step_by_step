from typing import Iterable


class Cell(object):
    AliveStatus = True
    DeadStatus = False

    def __init__(self, status: bool, neighbours: Iterable, future_state: bool = False):
        self.neighbours = tuple(neighbours)
        list(map(lambda x: x.add_neighbour(self), self.neighbours))

        self.is_alive = status
        self.future_state = future_state

    def add_neighbour(self, cell):
        if cell not in self.neighbours:
            self.neighbours += (cell,)
