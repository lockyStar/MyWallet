from decimal import Decimal
from random import random

def rounded(fn):
    def wrapped(*args, **kwargs):
        return round(Decimal(fn(*args, **kwargs)), 2)
    return wrapped


class Money(object):
    def __init__(self,value=0, is_editable=True):
        self.isEditable = is_editable
        self._value = value

    @rounded
    def get_value(self):
        return self._value

    def __str__(self):
        return str(self.get_value())


class Charge(object):

    def __init__(self, value=0):
        self._value = Money(is_editable=False, value=value)

    def value(self):
        return self._value.get_value()


class Account(object):

    def __init__(self, total=0, charges=None):
        self._total = Money(is_editable=True, value=total)
        self._charges = list(charges)

    def append(self, charge):
        if self._total + charge > 0:
            temp_charge = Charge(charge)
            self._charges.append(temp_charge)
            self._total += charge
        else:
            raise ValueError('Your account value can not be negative')

    def get_total(self):
        return self._total.get_value()

    def __iter__(self):
        return iter(self._charges)


def random_account(charges_amount=7, scale=1000.00):
    charges = []
    for i in range(charges_amount):
        charges.append(Charge(random()*scale))
    account = Account(total=random()*scale, charges=charges)
    return account
