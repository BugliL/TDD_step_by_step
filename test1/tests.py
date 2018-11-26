"""
.TODO LIST
    - Add amount of different values
    - Money rounding

    - equals
        - Equal null
        - Equal object
    - hashCode
    - $5 + 10CHF = $10 if rate is 2:test1
    - $5 + $5 = $10

    * Multiply amounts Dollars
    * Multiply amounts Franc
    * Amount private
    * Check side effects
    * equals
        * common equal
    * compare dollars and francs
    * $5 * 2 = $10
    * Dollar / Franc duplication


"""

import unittest

from test1.problem import MoneyFactory


class TestFrancDollarComparing(unittest.TestCase):
    def test_given_dollars_and_francs_when_compared_result_different(self):
        self.assertNotEqual(MoneyFactory.dollar(5), MoneyFactory.franc(5))


class TestFranc(unittest.TestCase):
    def test_given_5franc_when_called_times2_than_eq_10franc(self):
        x = MoneyFactory.franc(5)
        self.assertEqual(x.times(2), MoneyFactory.franc(10))

    # The whole addition of Francs and Dollars can't be made in 1 step
    # so it's better to try first to sum values of same currency
    # 5CHD + 5CHD = 10CHD
    def test_given_5CHD_and_5CHD_when_sum_than_return_10CHD(self):
        f1 = MoneyFactory.franc(5)
        f2 = MoneyFactory.franc(5)
        self.assertEqual(f1 + f2, MoneyFactory.franc(10))

    def test_given_5franc_when_created_than_eq_5franc_and_neq_6franc(self):
        self.assertEqual(MoneyFactory.franc(5), MoneyFactory.franc(5))
        self.assertNotEqual(MoneyFactory.franc(6), MoneyFactory.franc(5))


class TestDollar(unittest.TestCase):
    # knowing my code I know that this test is green because it works
    # for francs as well now
    def test_given_5USD_and_5USD_when_sum_than_return_10USD(self):
        d1 = MoneyFactory.dollar(5)
        d2 = MoneyFactory.dollar(5)
        self.assertEqual(d1 + d2, MoneyFactory.dollar(10))

    def test_given_5USD_when_called_times2_and_times3_than_eq_10USD(self):
        x = MoneyFactory.dollar(5)
        self.assertEqual(x.times(3), MoneyFactory.dollar(15))

    def test_given_5USD_when_created_than_eq_5USD_and_neq_6USD(self):
        self.assertEqual(MoneyFactory.dollar(5), MoneyFactory.dollar(5))
        self.assertNotEqual(MoneyFactory.dollar(6), MoneyFactory.dollar(5))


class TestPrint(unittest.TestCase):
    def test_given_aDollar_when_string_converted_than_print_amount_and_USD(self):
        x = MoneyFactory.dollar(5)
        self.assertEqual(str(x), "5USD")
