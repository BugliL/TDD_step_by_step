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


@dataclass
class Site(object):
    customer = Customer('John Smith')


def client_1(site: Site) -> None:
    aCustomer = site.customer
    name = aCustomer.name if (aCustomer != "unknown") else "occupant"
    print(name)


def client_2(site: Site) -> None:
    aCustomer = site.customer
    plan = BasicPlan if (aCustomer == "unknown") else aCustomer.billing_plan
    print(plan)


def client_3(site: Site) -> None:
    aCustomer = site.customer
    weeks = 0 if (aCustomer == "unknown") else aCustomer.payment_history['weeks']
    print(weeks)


if __name__ == '__main__':
    site = Site()
    client_1(site=site)
    client_2(site=site)
    client_3(site=site)
