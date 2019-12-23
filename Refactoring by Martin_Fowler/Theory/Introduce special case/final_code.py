from builtins import print
from dataclasses import dataclass
from typing import TypeVar

"""
A utility company installs its services in sites.
Most of the time, a site has a customer, but sometimes the customer is None. 
When this happens, the data record replace the customer field with the string "unknown". 
Clients of the site need to be able to handle an unknown customer so they check on his value and manage requests.

Source code inspired by The book at 
https://memberservices.informit.com/my_account/webedition/9780135425664/html/introducespecialcase.html 
"""


@dataclass
class BasicPlan(object):
    pass


@dataclass
class Customer(object):
    name: str
    payment_history = {'weeks': 0}
    billing_plan = BasicPlan

    @property
    def is_unknown(self) -> bool:
        return False


@dataclass
class UnknownCustomer(Customer):
    name: str = 'unknown'

    @property
    def is_unknown(self) -> bool:
        return True


class Site(object):
    def __init__(self, customer: [str, Customer]):
        self._customer = customer if customer != 'unknown' else UnknownCustomer()

    @property
    def customer(self):
        return self._customer


def is_customer_unknown(aCustomer):
    if type(aCustomer) not in [Customer, UnknownCustomer]:
        raise ValueError("Value '{}' unsupported".format(aCustomer))

    return aCustomer.is_unknown


def client_1(site: Site) -> None:
    aCustomer = site.customer
    name = aCustomer.name if not is_customer_unknown(aCustomer) else "occupant"
    print(name)


def client_2(site: Site) -> None:
    aCustomer = site.customer
    plan = BasicPlan if is_customer_unknown(aCustomer) else aCustomer.billing_plan
    print(plan)


def client_3(site: Site) -> None:
    aCustomer = site.customer
    weeks = 0 if is_customer_unknown(aCustomer) else aCustomer.payment_history['weeks']
    print(weeks)


if __name__ == '__main__':
    site = Site(customer='unknown')
    client_1(site=site)
    client_2(site=site)
    client_3(site=site)

    print(is_customer_unknown(Customer('John smith')))
    print(is_customer_unknown(UnknownCustomer()))
