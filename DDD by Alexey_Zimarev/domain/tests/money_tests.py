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


if __name__ == '__main__':
    pass
