"""
Multi concurrency problem

We have a DB with prices of things and we want to add a different currency

For example something like this (same as the book)
=================+=====================================
|    Instrument  |   Shares  |   Prices  |   Total    |
==================+====================================
|    IBM         | 1000      | 25        | 25,000     |
+-----------------------------------------------------+
|    GE          | 400       | 100       | 40,000     |
+-----------------------------------------------------+
                             | Total     | 65,000     |
                             +------------------------+


This is the result when adding different currencies
=================+=====================================
|    Instrument  |   Shares  |   Prices  |   Total    |
==================+====================================
|    IBM         | 1000      | 25 USD    | 25,000 USD |
+-----------------------------------------------------+
|    GE          | 400       | 150 CHF   | 60,000 CHF |
+-----------------------------------------------------+
                             | Total     | 65,000 USD |
                             +------------------------+


Doing this, we need to define a change rate of money
=================+===================
|   From    |   To      |   Rate    |
==================+==================
|    CHF    |   USD     |   1.5     |
+-----------------------------------+

So the basic function is
    $5 + 10CHF = $10 if rate is 2:1
    $5 * 2 = $10


TODO LIST
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
    - $5 + 10CHF = $10 if rate is 2:1
    * $5 * 2 = $10
"""

import unittest


class Money(object):
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    def __eq__(self, other):
        same_currency = (self.__currency == other.__currency)
        same_amount = (self.__amount == other.__amount)
        return same_amount and same_currency

    def times(self, t):
        var = self.__class__
        return var(self.__amount * t)


class MoneyFactory(object):
    class __Dollar(Money):
        def __init__(self, amount):
            super().__init__(amount, 'USD')

    class __Franc(Money):
        def __init__(self, amount):
            super().__init__(amount, 'CHD')

    @staticmethod
    def dollar(amount):
        return MoneyFactory.__Dollar(amount)

    @staticmethod
    def franc(amount):
        return MoneyFactory.__Franc(amount)


# Test names refactor using the model "given, when, than"
# to clarify code and what they test
# renaming tests it's clear that some functionality are tested multiple times
# from different tests cases, this is a waste of testing and these tests have to be refactored
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

    def test_given_5USD_when_called_times2_than_eq_10USD(self):
        x = MoneyFactory.dollar(5)
        self.assertEqual(x.times(2), MoneyFactory.dollar(10))

    def test_given_7USD_when_called_times2_than_eq_14USD(self):
        x = MoneyFactory.dollar(7)
        self.assertEqual(x.times(2), MoneyFactory.dollar(2 * 7))

    def test_given_5USD_when_called_times2_and_times3_than_eq_10USD_and_15USD(self):
        x = MoneyFactory.dollar(5)
        self.assertEqual(x.times(2), MoneyFactory.dollar(10))
        self.assertEqual(x.times(3), MoneyFactory.dollar(15))

    def test_given_5USD_when_created_than_eq_5USD_and_neq_6USD(self):
        self.assertEqual(MoneyFactory.dollar(5), MoneyFactory.dollar(5))
        self.assertNotEqual(MoneyFactory.dollar(6), MoneyFactory.dollar(5))
