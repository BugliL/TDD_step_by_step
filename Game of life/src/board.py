from typing import List

from cell import Cell


class Board(object):

    def __init__(self, cells: List[Cell]):
        self.cells = cells

    def evolve(self):
        for cell in self.cells:
            n = len([c for c in cell.neighbours if c.is_alive])
            if n < 2:
                cell.future_state = Cell.DeadStatus
            elif n == 2:
                cell.future_state = cell.is_alive
            elif n == 3:
                cell.future_state = Cell.AliveStatus

        for cell in self.cells:
            cell.is_alive = cell.future_state
