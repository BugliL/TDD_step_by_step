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
    - Multiply amounts
    - Amount private
    - Check side effects
    - Money rounding

"""

import unittest


class Dollar(object):
    def __init__(self, amount):
        self.amount = amount

    # i am resolving the RED signal by forcing values
    # without touching tests
    # ( in the book is much more slower in writing code,
    # i'm jumping some passages and distorcing others)
    # Now is GREEN
    def times(self, t):
        self.amount *= t
        return self.amount


class TestCurrency(unittest.TestCase):

    # let's focus on multiplying first
    def test_moltiplication(self):
        x = Dollar(5)
        x.times(2)
        self.assertEqual(x.amount, 10)

    # adding another test that fails
    # solved code to make it work
    def test_moltiplication2(self):
        x = Dollar(7)
        x.times(2)
        self.assertEqual(x.amount, 2 * 7)
