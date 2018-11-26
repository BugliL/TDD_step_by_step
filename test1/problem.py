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

# He uses a Sum class to add things, but he has to
# access the __amount to do that, so i decided to use a property
# to let the attribute be accessed but not set
# same for currency

# I do not like using the interface that Kent Beck is using
# and I think that I can simplify that without using different classes
# but just dividing the methods to reduce Money responsibility of
# aritmetic operations

# so i changed tests to something more familiar to me
# instead of doing a chapter on a Sum object that wrap the operation

# Class to refactor the rate change
# in the Money class
# better if we pass objects instead of currencies

# this is much more different from the book
# but this is python and not formally-correct-object-structuring Java

# next step is to change the code of __eq__
# to check different currencies

# now is time to implement an add of different things

class RateChange(object):
    def __init__(self, rates=None):
        self.rates = rates or {
            'USD': {
                'CHD': 2,
            },
            'CHD': {
                'USD': .5,
            }
        }

    def get_rate(self, source, dest):
        return 1 if source.currency == dest else self.rates[source.currency][dest]


class Money(object):
    def __init__(self, amount, currency, ratechange=RateChange()):
        self.__amount = amount
        self.__currency = currency
        self.__ratechange = ratechange

    def __eq__(self, other):
        rate = self.__ratechange.get_rate(other, self.currency)
        same_amount = (self.amount == other.amount * rate)
        return same_amount

    def __add__(self, other):
        amount = self.amount + other.convert(self.currency).amount
        return Money(amount, self.currency)

    def times(self, t):
        return Money(self.amount * t, self.currency)

    def convert(self, currency):
        rate = self.__ratechange.get_rate(self, currency)
        return Money(self.amount * rate, currency)

    def __str__(self):
        return f"{self.amount}{self.currency}"

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        pass

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        pass


class MoneyFactory(object):

    @staticmethod
    def dollar(amount):
        return Money(amount=amount, currency='USD')

    @staticmethod
    def franc(amount):
        return Money(amount=amount, currency='CHD')
