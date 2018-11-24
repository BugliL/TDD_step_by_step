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

    # checking a class type is not pythonist
    # so i try to refactor this without changing tests
    # a way to distinguish money from each other
    # it is to add a parameter in both classes
    # that can be checked in the __eq__ method
    def __eq__(self, other):
        same_currency = (self.__currency == other.__currency)
        same_amount = (self.__amount == other.__amount)
        return same_amount and same_currency

    def times(self, t):
        var = self.__class__
        return var(self.__amount * t)


class MoneyFactory(object):
    # __init___ methods added to
    # distinguish them from base class using the param

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


# All tests are changed to use the factory method
class TestFrancDollarComparing(unittest.TestCase):
    def test_equality(self):
        self.assertNotEqual(MoneyFactory.dollar(5), MoneyFactory.franc(5))


class TestFranc(unittest.TestCase):
    def test_multiplication(self):
        x = MoneyFactory.franc(5)
        self.assertEqual(x.times(2), MoneyFactory.franc(10))

    def test_equality(self):
        self.assertEqual(MoneyFactory.franc(5), MoneyFactory.franc(5))
        self.assertNotEqual(MoneyFactory.franc(6), MoneyFactory.franc(5))


class TestDollar(unittest.TestCase):

    def test_multiplication(self):
        x = MoneyFactory.dollar(5)
        self.assertEqual(x.times(2), MoneyFactory.dollar(10))

    def test_multiplication2(self):
        x = MoneyFactory.dollar(7)
        self.assertEqual(x.times(2), MoneyFactory.dollar(2 * 7))

    def test_twice_times(self):
        x = MoneyFactory.dollar(5)
        self.assertEqual(x.times(2), MoneyFactory.dollar(10))
        self.assertEqual(x.times(3), MoneyFactory.dollar(15))

    def test_equality(self):
        self.assertEqual(MoneyFactory.dollar(5), MoneyFactory.dollar(5))
        self.assertNotEqual(MoneyFactory.dollar(6), MoneyFactory.dollar(5))
