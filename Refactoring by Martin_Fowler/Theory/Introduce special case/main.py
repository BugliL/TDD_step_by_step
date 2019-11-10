from dataclasses import dataclass, field
from typing import TypeVar

"""
A utility company installs its services in sites.
Most of the time, a site has a customer, but sometimes the customer is None. 
When this happens, the data record replace the customer field with the string "unknown". 
Clients of the site need to be able to handle an unknown customer so they check on his value and manage requests.

Source code inspired by The book at 
https://memberservices.informit.com/my_account/webedition/9780135425664/html/introducespecialcase.html 
"""


@dataclass(frozen=True)
class PaymentHistory(object):
    history: tuple = field(default_factory=tuple)
    is_null: bool = False

    def __getitem__(self, item):
        if item != 'weeks':
            raise KeyError("{} not defined as key".format(item))
        return self._get_weeks()

    def _get_weeks(self) -> int:
        return len(self.history)


@dataclass(frozen=True)
class NullPaymentHistory(PaymentHistory):
    history: tuple = ()
    is_null: bool = True


class Customer(object):

    def __init__(self, name: str, payment_history: [dict, PaymentHistory], billing_plan: str):
        self._billing_plan = billing_plan
        self._payment_history = payment_history
        self._name = name

    @property
    def isUnknown(self):
        return False

    @property
    def name(self):
        return self._name

    @property
    def payment_history(self):
        return self._payment_history

    @property
    def billing_plan(self):
        return self._billing_plan

    @billing_plan.setter
    def billing_plan(self, new_plan: str):
        self._billing_plan = new_plan


class NullCustomer(Customer):
    def __init__(self):
        super().__init__(
            name="occupant",
            payment_history=NullPaymentHistory(),
            billing_plan=TypeVar("basic_plan")
        )

    @property
    def isUnknown(self):
        return True


class Site(object):
    def __init__(self):
        self._customer = Customer(
            name='Bob',
            payment_history=PaymentHistory(history=('one', 'two', 'tree')),
            billing_plan='Standard plan'
        )

    @staticmethod
    def is_unknown(aCustomer: [Customer, NullCustomer]):
        if not aCustomer or (type(aCustomer) not in [Customer, NullCustomer]):
            raise ValueError("Customer {} not valid ".format(aCustomer))

        return aCustomer.isUnknown

    @property
    def customer(self):
        return self._customer if not Site.is_unknown(self._customer) else NullCustomer()

    @customer.setter
    def customer(self, value: [str, Customer]):
        self._customer = value if value != "unknown" else NullCustomer()


def client_1(site: Site) -> None:
    aCustomer = site.customer
    name = aCustomer.name
    print(name)


def client_2(site: Site) -> None:
    aCustomer = site.customer
    plan = aCustomer.billing_plan
    print(plan)


def client_3(site: Site) -> None:
    aCustomer = site.customer
    weeks = aCustomer.payment_history['weeks']
    print(weeks)


if __name__ == '__main__':
    print("\nCorrect user")
    site1 = Site()
    assert type(site1.customer) != NullCustomer
    client_1(site=site1)
    client_2(site=site1)
    client_3(site=site1)

    print("\nNull user")
    site2 = Site()
    site2.customer = 'unknown'
    assert type(site2.customer) == NullCustomer
    client_1(site=site2)
    client_2(site=site2)
    client_3(site=site2)

    x = NullPaymentHistory()
