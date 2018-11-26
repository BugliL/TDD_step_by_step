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

"""


# Kent Back introduced an interface to do the job here
# the interface Expression where is defined the "plus" method
# and modified the plus method in money to return an Expression
# objects and Money implements the interface Expression

# I can't do an interface in python of course
# so let's do this with small steps
# This code is in green state
class Money(object):

    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    def __eq__(self, other):
        same_currency = (self.__currency == other.__currency)
        same_amount = (self.__amount == other.__amount)
        return same_amount and same_currency

    def __add__(self, other):
        amount = self.__amount + other.__amount
        return Money(amount, self.__currency)

    def times(self, t):
        return Money(self.__amount * t, self.__currency)
        # this method can be changed like above with no fear
        # var = self.__class__
        # if var == Money:
        #     return var(self.__amount * t, self.__currency)
        # else:
        #     return var(self.__amount * t)

    def __str__(self):
        return f"{self.__amount}{self.__currency}"


class MoneyFactory(object):

    @staticmethod
    def dollar(amount):
        return Money(amount=amount, currency='USD')

    @staticmethod
    def franc(amount):
        return Money(amount=amount, currency='CHD')


class Bank(object):
    @staticmethod
    def reduce(expression, param):
        return MoneyFactory.franc(10)
