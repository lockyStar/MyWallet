import matplotlib.pyplot as plt
from finance.models import Charge, Account
import numpy as np
from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncYear
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import datetime


def getTotalLine (charges, total):
    # charges = list(Charge.objects.filter(account=account_number).order_by('-date'))
    # total = list(Account.objects.filter(account_number=account_number))
    x = []
    y = []
    for charge in reversed(charges):
        x.append(charge.date)
        y.append(total)
        total -= charge.value
    filename = 'total.jpg'
    plt.plot(x, y)
    plt.savefig('total.png', format='png')
    return filename


def getTotalTable (account_number):
    acc = Account.objects.get(account_number=account_number)
    charges = list(Charge.objects.filter(account=acc.id)
                   .annotate(mon=TruncMonth('date'))
                   .values('mon')
                   .order_by('-mon')
                   .annotate(year=TruncYear('date'))
                   .annotate(subtotal=Sum('value'))
                   # .values('', 'subtotal')
                   )
    # print(charges)
    total = acc.total
    for charge in charges:
        charge['year'] = charge['year'].year
        charge['mon'] = charge['mon'].month
        temp = charge['subtotal']
        charge['subtotal'] = total
        total = total - temp
    return charges

