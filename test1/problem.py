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

    def __str__(self):
        return f"{self.__amount}{self.__currency}"


class MoneyFactory(object):
    # I am in green status
    # I don't like to have duplication in these
    # classes and all the behavior in the parent class
    # they differs just from a parameter, so why not
    # eliminating changing the factory method
    # using just the class money

    class __Dollar(Money):
        def __init__(self, amount):
            super().__init__(amount, 'USD')

    class __Franc(Money):
        def __init__(self, amount):
            super().__init__(amount, 'CHD')

    @staticmethod
    def dollar(amount):
        return MoneyFactory.__Dollar(amount)
        # if i change above line with this one
        # return Money(amount=amount, currency='USD')
        # a test fails even the code is correct because
        # the times method try to create a Money object
        # without a Currency param

        # so first let's refactor the class Money
        # To let times work wiothout problems

    @staticmethod
    def franc(amount):
        return MoneyFactory.__Franc(amount)
