from typing import Iterable


class Cell(object):
    AliveStatus = True
    DeadStatus = False

    def __init__(self, status: bool, neighbours: Iterable):
        self.neighbours = neighbours
        for cell in self.neighbours:
            if self not in cell.neighbours:
                cell.neighbours.append(self)

        self.is_alive = status
        self.future_state = False
