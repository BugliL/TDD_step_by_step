from typing import Iterable


class Cell(object):
    AliveStatus = True
    DeadStatus = False

    def __init__(self, status: bool, neighbours: Iterable):
        self.neighbours = neighbours
        self.is_alive = status
        self.future_state = False
