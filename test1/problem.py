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
|    CHF    |   USD     |   test1.5     |
+-----------------------------------+

"""


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

    # As the book I implemented the toString method
    # but i prefer to test it because is written in the parent
    # class instead of the children
    def __str__(self):
        return f"{self.__amount}{self.__currency}"


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