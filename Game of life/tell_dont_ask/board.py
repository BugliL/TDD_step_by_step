from typing import List

from tell_dont_ask.cell import Cell


class Board(object):

    def __init__(self, cells: List[Cell]):
        self.cells = cells

    def evolve(self):
        self._set_future_states()
        self._evolve_cells()

    def _evolve_cells(self):
        for cell in self.cells:  # type: Cell
            cell.evolve()

    def _set_future_states(self):
        # Now this method has to be refactored to tell don't ask principle
        # to we need to move the method inside cell class
        for cell in self.cells:
            cell.set_future_state()
