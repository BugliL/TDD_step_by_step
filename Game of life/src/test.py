import unittest


class CellShouid(unittest.TestCase):
    """
        - Acceptance tests
            - Any live cell with two or three neighbors survives.
            - Any dead cell with three live neighbors becomes a live cell.
            - All other live cells die in the next generation. Similarly, all other dead cells stay dead.
    """
    pass
