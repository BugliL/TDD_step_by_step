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
    * Multiply amounts
    * Amount private
    * Check side effects
    - Money rounding
    * equals
        - Equal null
        - Equal object
    - hashCode
"""

import unittest


class Dollar(object):

    def __init__(self, amount):
        self.__amount = amount

    def times(self, t):
        return Dollar(self.__amount * t)

    def __eq__(self, other):
        return self.__amount == other.__amount


# To manage task 1 in list, first of all
# copy and paste the first test and the class
# renaming it correctly to make things work

# copy and paste is bad but it's the smallest step
# to write code that works and make the following test
# on green state

class Franc(object):
    def __init__(self, amount):
        self.__amount = amount

    def times(self, t):
        return Franc(self.__amount * t)

    def __eq__(self, other):
        return self.__amount == other.__amount


class TestFranc(unittest.TestCase):
    def test_multiplication(self):
        x = Franc(5)
        self.assertEqual(x.times(2), Franc(10))


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
