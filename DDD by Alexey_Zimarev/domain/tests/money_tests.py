import unittest

from domain.money import Money


class MoneyTests(unittest.TestCase):

    def test_given_money_with_same_amount_should_be_equal(self):
        # Dataclass manage this behavior
        x, y = Money.create(10), Money.create(10)
        z = Money.create(5)

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
