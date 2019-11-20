from typing import Iterable


class Cell(object):
    AliveStatus = True
    DeadStatus = False

    def __init__(self, status: bool, neighbours: Iterable):
        self._set_neighbours(neighbours)
        self.is_alive = status
        self.future_state = False

    def _set_neighbours(self, neighbours):
        self.neighbours = neighbours
        for cell in self.neighbours:
            if self not in cell.neighbours:
                cell.neighbours.append(self)

    def die_in_future(self):
        self.future_state = self.DeadStatus

    def be_alive_in_future(self):
        self.future_state = self.AliveStatus

    def stay_in_future(self):
        self.future_state = self.is_alive

    def evolve(self):
        self.is_alive = self.future_state
