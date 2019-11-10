from typing import TypeVar

"""
A utility company installs its services in sites.
Most of the time, a site has a customer, but sometimes the customer is None. 
When this happens, the data record replace the customer field with the string "unknown". 
Clients of the site need to be able to handle an unknown customer so they check on his value and manage requests.

Source code inspired by The book at 
https://memberservices.informit.com/my_account/webedition/9780135425664/html/introducespecialcase.html 
"""


class Customer(object):

    @property
    def name(self):
        pass

    @property
    def payment_history(self):
        pass

    def billing_plan(self, **kwargs):
        pass


class Site(object):
    def __init__(self):
        self._get_customer = Customer()

    @property
    def customer(self):
        return self._get_customer


def client_1(site: Site) -> None:
    aCustomer = site.customer
    name = aCustomer.name if (aCustomer != "unknown") else "occupant"


def client_2(site: Site) -> None:
    BasicPlan = TypeVar("BasicPlan")
    aCustomer = site.customer
    plan = BasicPlan if (aCustomer == "unknown") else aCustomer.billing_plan


def client_3(site: Site) -> None:
    aCustomer = site.customer
    weeks = 0 if (aCustomer == "unknown") else aCustomer.payment_history['weeks']
