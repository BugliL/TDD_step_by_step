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


# Chapter 16 - No need to do anything :)
# as I thought this implementation was simpler
# than the Book one

# I will do a little extra, add multiplication

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
        same_amount = (self.__amount == other.__amount * rate)
        return same_amount

    def __add__(self, other):
        amount = self.__amount + other.convert(self.currency).__amount
        return Money(amount, self.currency)

    def __mul__(self, other):
        return Money(self.__amount * other, self.currency)

    def times(self, t):
        return Money(self.__amount * t, self.currency)

    def convert(self, currency):
        rate = self.__ratechange.get_rate(self, currency)
        return Money(self.__amount * rate, currency)

    def __str__(self):
        return f"{self.__amount}{self.currency}"

    # @property
    # def amount(self):
    #     return self.__amount
    #
    # @amount.setter
    # def amount(self, value):
    #     pass

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
