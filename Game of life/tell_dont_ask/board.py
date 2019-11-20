from typing import List

from tell_dont_ask.cell import Cell


class Board(object):

    def __init__(self, cells: List[Cell]):
        self.cells = cells

    def evolve(self):
        # This is the most modified method in the whole program

        for cell in self.cells:
            n = len([c for c in cell.neighbours if c.is_alive])
            if n < 2:
                # Old version
                # cell.future_state = Cell.DeadStatus
                cell.die_in_future()
            elif n == 2:
                # Old version
                # cell.future_state = cell.is_alive
                cell.stay_in_future()
            elif n == 3:
                # Old version
                # cell.future_state = Cell.AliveStatus
                cell.be_alive_in_future()
            elif n > 3:
                # Old version
                # cell.future_state = Cell.DeadStatus
                cell.die_in_future()

        for cell in self.cells:
            # Old version
            # cell.is_alive = cell.future_state
            cell.evolve()
