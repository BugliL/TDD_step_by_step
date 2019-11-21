from typing import List

from tell_dont_ask.cell import Cell


class Board(object):

    def __init__(self, cells: List[Cell]):
        self.cells = cells

    def evolve(self):
        # Created 2 functions to wrap behavior

        self._set_future_states()
        self._evolve_cells()

    def _evolve_cells(self):
        for cell in self.cells:
            cell.evolve()

    def _set_future_states(self):
        for cell in self.cells:
            n = len([c for c in cell.neighbours if c.is_alive])
            if n < 2:
                cell.die_in_future()
            elif n == 2:
                cell.stay_in_future()
            elif n == 3:
                cell.be_alive_in_future()
            elif n > 3:
                cell.die_in_future()
