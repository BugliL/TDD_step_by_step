import unittest
from .cell import Cell
from .board import Board


class CellShould(unittest.TestCase):
    """
        - Acceptance tests: after an evolution phase
            - Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            - Any live cell with two or three live neighbours lives on to the next generation.
            - Any live cell with more than three live neighbours dies, as if by overpopulation.
            - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
    """
    """
        - Extended Acceptance tests: after an evolution phase
            + Any live cell with 0 or 1 live neighbours dies, as if by underpopulation.
            + Any live cell with 2 or 3 live neighbours lives on to the next generation.
            + Any live cell with 4 or more live neighbours dies, as if by overpopulation.
            + Any dead cell with 3 live neighbours becomes a live cell, as if by reproduction
    """

    def test_die_by_underpopulation_if_next_to_less_than_2_alive_cells(self):
        cell1 = Cell(status=Cell.AliveStatus, neighbours=[])
        cell2 = Cell(status=Cell.AliveStatus, neighbours=[cell1])
        board = Board([cell1, cell2, ])

        self.assertEqual(Cell.AliveStatus, cell1)
        self.assertEqual(Cell.AliveStatus, cell2)

        board.evolve()

        self.assertEqual(Cell.DeadStatus, cell1)
        self.assertEqual(Cell.DeadStatus, cell2)

    def test_survive_if_next_to_2_or_3_alive_cells(self):
        cell1 = Cell(status=Cell.AliveStatus, neighbours=[])
        cell2 = Cell(status=Cell.AliveStatus, neighbours=[cell1])
        cell3 = Cell(status=Cell.AliveStatus, neighbours=[cell1, cell2])
        cell4 = Cell(status=Cell.AliveStatus, neighbours=[cell1, cell2, cell3])
        board = Board([cell1, cell2, cell3, cell4])

        self.assertEqual(Cell.AliveStatus, cell1.is_alive)
        self.assertEqual(Cell.AliveStatus, cell2.is_alive)
        self.assertEqual(Cell.AliveStatus, cell3.is_alive)
        self.assertEqual(Cell.AliveStatus, cell4.is_alive)

        board.evolve()

        self.assertEqual(Cell.AliveStatus, cell1.is_alive)
        self.assertEqual(Cell.AliveStatus, cell2.is_alive)
        self.assertEqual(Cell.AliveStatus, cell3.is_alive)
        self.assertEqual(Cell.AliveStatus, cell4.is_alive)

    def test_die_by_overpopulation_if_next_to_4_or_more_alive_cells(self):
        cell1 = Cell(status=Cell.AliveStatus, neighbours=[])
        cell2 = Cell(status=Cell.AliveStatus, neighbours=[cell1])
        cell3 = Cell(status=Cell.AliveStatus, neighbours=[cell1, cell2])
        cell4 = Cell(status=Cell.AliveStatus, neighbours=[cell1, cell2, cell3])
        cell5 = Cell(status=Cell.DeadStatus, neighbours=[cell1, cell2, cell3, cell4])
        cell6 = Cell(status=Cell.DeadStatus, neighbours=[cell2, cell3, cell4, cell5])
        board = Board([cell1, cell2, cell3, cell4, cell5, cell6])

        self.assertEqual(Cell.AliveStatus, cell1.is_alive)
        self.assertEqual(Cell.AliveStatus, cell2.is_alive)
        self.assertEqual(Cell.AliveStatus, cell3.is_alive)
        self.assertEqual(Cell.AliveStatus, cell4.is_alive)
        self.assertEqual(Cell.AliveStatus, cell5.is_alive)
        self.assertEqual(Cell.AliveStatus, cell6.is_alive)

        board.evolve()

        self.assertEqual(Cell.DeadStatus, cell1.is_alive)
        self.assertEqual(Cell.DeadStatus, cell2.is_alive)
        self.assertEqual(Cell.AliveStatus, cell3.is_alive)
        self.assertEqual(Cell.AliveStatus, cell4.is_alive)
        self.assertEqual(Cell.DeadStatus, cell5.is_alive)
        self.assertEqual(Cell.DeadStatus, cell6.is_alive)

    def test_born_if_next_to_4_or_more_alive_cells(self):
        cell1 = Cell(status=Cell.AliveStatus, neighbours=[])
        cell2 = Cell(status=Cell.AliveStatus, neighbours=[cell1])
        cell3 = Cell(status=Cell.AliveStatus, neighbours=[cell1, cell2])
        cell4 = Cell(status=Cell.AliveStatus, neighbours=[cell1, cell2, cell3])
        board = Board([cell1, cell2, cell3, cell4])

        self.assertEqual(Cell.AliveStatus, cell1.is_alive)
        self.assertEqual(Cell.AliveStatus, cell2.is_alive)
        self.assertEqual(Cell.AliveStatus, cell3.is_alive)
        self.assertEqual(Cell.AliveStatus, cell4.is_alive)

        board.evolve()

        self.assertEqual(Cell.AliveStatus, cell1.is_alive)
        self.assertEqual(Cell.AliveStatus, cell2.is_alive)
        self.assertEqual(Cell.AliveStatus, cell3.is_alive)
        self.assertEqual(Cell.AliveStatus, cell4.is_alive)
