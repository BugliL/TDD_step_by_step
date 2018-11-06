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
"""

import unittest


class Money(object):
    def __init__(self, amount):
        self.__amount = amount

    # checking classes too, make the new test working
    # and the others passing
    def __eq__(self, other):
        same_class = (other.__class__ == self.__class__)
        same_amount = (self.__amount == other.__amount)
        return same_class and same_amount

    def times(self, t):
        var = self.__class__
        return var(self.__amount * t)


class Dollar(Money):
    pass


class Franc(Money):
    pass


# green thanks to the new check in the
# __eq__ method, checking the class type
class TestFrancDollarComparing(unittest.TestCase):
    def test_equality(self):
        self.assertNotEqual(Dollar(5), Franc(5))


class TestFranc(unittest.TestCase):
    def test_multiplication(self):
        x = Franc(5)
        self.assertEqual(x.times(2), Franc(10))

    def test_equality(self):
        self.assertEqual(Franc(5), Franc(5))
        self.assertNotEqual(Franc(6), Franc(5))


class TestDollar(unittest.TestCase):

    def test_multiplication(self):
        x = Dollar(5)
        self.assertEqual(x.times(2), Dollar(10))

    def test_multiplication2(self):
        x = Dollar(7)
        self.assertEqual(x.times(2), Dollar(2 * 7))

    def test_twice_times(self):
        x = Dollar(5)
        self.assertEqual(x.times(2), Dollar(10))
        self.assertEqual(x.times(3), Dollar(15))

    def test_equality(self):
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(6), Dollar(5))
