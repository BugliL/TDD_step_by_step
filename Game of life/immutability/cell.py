from typing import Iterable


class Cell(object):
    AliveStatus = True
    DeadStatus = False

    def __init__(self, status: bool, neighbours: Iterable, future_state: bool = False):
        self.neighbours = tuple(neighbours)
        for cell in self.neighbours:
            if self not in cell.neighbours:
                cell.add_neighbour(self)

        self.is_alive = status
        self.future_state = future_state

    def add_neighbour(self, cell):
        self.neighbours += (cell, )
