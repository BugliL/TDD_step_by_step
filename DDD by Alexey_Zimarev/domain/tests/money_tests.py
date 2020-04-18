import unittest

from domain.abstract_currency_lookup import AbstractCurrencyLookup, CurrencyDetails
from domain.money import Money


class FakeCurrencyLookup(AbstractCurrencyLookup):

    @classmethod
    def currencies(cls):
        return [
            CurrencyDetails(currency_code="EUR", in_use=True, decimal_places=2),
            CurrencyDetails(currency_code="USD", in_use=True, decimal_places=2),
            CurrencyDetails(currency_code="JPY", in_use=True, decimal_places=0),
            CurrencyDetails(currency_code="DEM", in_use=False, decimal_places=2),
        ]

    @classmethod
    def find(cls, code: str):
        return next(
            (x for x in cls.currencies() if x.currency_code == code),
            CurrencyDetails.NoneCurrency()
        )


class CurrencyLookupTest(unittest.TestCase):
    def setUp(self) -> None:
        self.lookup = FakeCurrencyLookup()

    def test_given_not_present_money_should_return_NoneCurrency(self):
        currrency = CurrencyDetails.NoneCurrency()
        self.assertEqual(currrency, self.lookup.find('XXX'))

    def test_given_present_money_should_return_datails(self):
        EUR = CurrencyDetails(currency_code="EUR", in_use=True, decimal_places=2)
        self.assertEqual(EUR, self.lookup.find('EUR'))


class MoneyTests(unittest.TestCase):

    def test_given_money_with_same_amount_should_be_equal(self):
        # Dataclass manage this behavior
        EUR = "EUR"
        lookup = FakeCurrencyLookup()
        x, y = Money.create(10, EUR, lookup), Money.create(10, EUR, lookup)
        z = Money.create(5, EUR, lookup)

        self.assertEqual(x, y)
        self.assertTrue(x == y)

        self.assertNotEqual(x, z)
        self.assertFalse(x == z)

    def test_given_creating_negative_money_should_raise_error(self):
        with self.assertRaises(ValueError):
            Money.create(amount=-1)

    def test_given_creating_or_null_money_should_raise_error(self):
        with self.assertRaises(ValueError):
            Money.create(amount=None)

    def test_given_2_plus_3_money_should_return_5(self):
        x = Money.create(2)
        y = Money.create(3)
        self.assertEqual(Money.create(5), x + y)

    def test_given_2_plus_3_different_money_currency_should_raise_error(self):
        with self.assertRaises(TypeError):
            x = Money.create(amount=2, currency="EUR")
            y = Money.create(amount=2, currency="USD")
            z = x + y

    def test_given_2_less_3_different_money_currency_should_raise_error(self):
        with self.assertRaises(TypeError):
            x = Money.create(amount=3, currency="EUR")
            y = Money.create(amount=2, currency="USD")
            z = x - y

    def test_given_2_less_1_money_should_return_1(self):
        x = Money.create(2)
        y = Money.create(1)
        self.assertEqual(Money.create(1), x - y)

    def test_given_more_than_2_decimals_should_raise_error(self):
        with self.assertRaises(ValueError):
            Money.create(0.001)


if __name__ == '__main__':
    pass
