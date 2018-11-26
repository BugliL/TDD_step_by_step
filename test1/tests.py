"""
.TODO LIST
    - Add amount of different values
    * Multiply amounts Dollars
    * Multiply amounts Franc
    * Amount private
    * Check side effects
    - Money rounding
    * equals
        - Equal null
        - Equal object
        * common equal
    - hashCode
    - compare dollars and francs
    - $5 + 10CHF = $10 if rate is 2:test1
    * $5 * 2 = $10

    - Dollar / Franc duplication
"""

import unittest
import sys

from test1.problem import MoneyFactory, Money


class TestMoneyClass(unittest.TestCase):
    def test_given_aMoney_when_times_called_it_returns_double_money(self):
        self.assertEqual(Money(5, 'USD').times(2), Money(10, 'USD'))


class TestFrancDollarComparing(unittest.TestCase):
    def test_given_dollars_and_francs_when_compared_result_different(self):
        self.assertNotEqual(MoneyFactory.dollar(5), MoneyFactory.franc(5))


class TestFranc(unittest.TestCase):
    def test_given_5franc_when_called_times2_than_eq_10franc(self):
        x = MoneyFactory.franc(5)
        self.assertEqual(x.times(2), MoneyFactory.franc(10))

    def test_given_5franc_when_created_than_eq_5franc(self):
        self.assertEqual(MoneyFactory.franc(5), MoneyFactory.franc(5))
        self.assertNotEqual(MoneyFactory.franc(6), MoneyFactory.franc(5))


class TestDollar(unittest.TestCase):

    def test_given_5USD_when_called_times2_and_times3_than_eq_10USD_and_15USD(self):
        x = MoneyFactory.dollar(5)
        self.assertEqual(x.times(2), MoneyFactory.dollar(10))
        self.assertEqual(x.times(3), MoneyFactory.dollar(15))

    def test_given_5USD_when_created_than_eq_5USD_and_neq_6USD(self):
        self.assertEqual(MoneyFactory.dollar(5), MoneyFactory.dollar(5))
        self.assertNotEqual(MoneyFactory.dollar(6), MoneyFactory.dollar(5))


class TestPrint(unittest.TestCase):
    def test_given_aDollar_when_string_converted_than_print_amount_and_USD(self):
        x = MoneyFactory.dollar(5)
        self.assertEqual(str(x), "5USD")

    def test_given_aDollar_when_string_converted_than_print_amount_and_CHD(self):
        x = MoneyFactory.franc(5)
        self.assertEqual(str(x), "5CHD")
