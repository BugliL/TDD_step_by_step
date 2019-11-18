from typing import Iterable


class Cell(object):
    AliveStatus = True
    DeadStatus = False

    def __init__(self, status: bool, neighbours: Iterable):
        self.is_alive = status
