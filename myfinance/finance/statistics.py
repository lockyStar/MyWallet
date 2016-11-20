import matplotlib.pyplot as plt
from finance.models import Charge, Account
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages


def getTotalLine (charges, total):
    # charges = list(Charge.objects.filter(account=account_number).orderby('-date'))
    # total = list(Account.objects.filter(account_number=account_number))
    x = [];
    y = [];
    for charge in reversed(charges):
        x.append(charge.date)
        y.append(total)
        total -= charge.value
    filename = 'total.pdf'
    pp = PdfPages(filename)
    plt.plot(x,y)
    pp.savefig()
    pp.close()
    return filename
