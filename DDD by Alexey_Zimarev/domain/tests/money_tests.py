import unittest

from domain.money import CreateMoney


class MoneyTests(unittest.TestCase):

    def test_given_money_with_same_amount_should_be_equal(self):
        # Dataclass manage this behavior
        x, y = CreateMoney(10), CreateMoney(10)
        z = CreateMoney(5)

        self.assertEqual(x, y)
        self.assertTrue(x == y)

        self.assertNotEqual(x, z)
        self.assertFalse(x == z)

    def test_given_creating_negative_or_null_money_should_raise_error(self):
        self.assertRaises(ValueError, lambda: CreateMoney(amount=-1))
        self.assertRaises(ValueError, lambda: CreateMoney(amount=None))


if __name__ == '__main__':
    pass
