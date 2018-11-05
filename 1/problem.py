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
    - Amount private
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
        self.amount = amount

    def times(self, t):
        return Dollar(self.amount * t)

    def __eq__(self, other):
        return self.amount == other.amount


class TestCurrency(unittest.TestCase):

    # now that there's an equal condition
    # to compare Dollar instances let's update
    # the times test condition using it
    def test_moltiplication(self):
        x = Dollar(5)
        y = x.times(2)
        self.assertEqual(y, Dollar(10))

    def test_moltiplication2(self):
        x = Dollar(7)
        y = x.times(2)
        self.assertEqual(y, Dollar(2 * 7))

    def test_twice_times(self):
        x = Dollar(5)
        y = x.times(2)
        self.assertEqual(y, Dollar(10))
        y = x.times(3)
        self.assertEqual(y, Dollar(15))

    def test_equality(self):
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(6), Dollar(5))
