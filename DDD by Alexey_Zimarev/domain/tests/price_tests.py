import unittest

from domain.price import Price
from domain.tests.money_tests import FakeCurrencyLookup


class PriceTests(unittest.TestCase):

    def test_zero_price_not_allowed(self):
        with self.assertRaises(ValueError):
            Price.create(0, "EUR", FakeCurrencyLookup)

