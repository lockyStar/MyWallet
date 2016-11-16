from django.shortcuts import render
from finance import controller
from decimal import Decimal
from datetime import date
from finance.form_validation import ChargeForm


def home(request):
    return render(request, 'home.html')


def random_example(request):
    account = controller.random_account()
    return render(
        request, 'table.html',
        {'account': account}
    )


def account_status(request, account_id=0):
    account = controller.random_account()
    return render(
        request, 'table.html',
        {'account': account, 'account_id': account_id}
    )


def add_charge(request, account_id=0):
    if request.method == 'POST':
        print(2)
        form = ChargeForm(request.POST)
        info = 'Form is filled, but not correct'

        if form.is_valid():
            info = 'Form is filled and correct'

    else:
        info = 'Form is not filled'
        form = ChargeForm(initial={'value': Decimal(100), 'date': date.today()})

    return render(
        request, 'input.html',
        {'form': form, 'info': info, 'account_id': account_id}
    )


# Create your views here.
