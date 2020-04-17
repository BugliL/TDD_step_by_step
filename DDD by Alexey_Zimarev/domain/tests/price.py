import unittest

from domain.price import Price


class PriceTests(unittest.TestCase):

    def test_zero_price_not_allowed(self):
        with self.assertRaises(ValueError):
            Price.create(0)


if __name__ == '__main__':
    x = Price.create(4)

    # Raise ValueError
    x = Price.create(0)
