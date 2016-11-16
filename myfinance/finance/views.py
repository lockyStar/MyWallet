from django.shortcuts import render
from django.shortcuts import redirect
from finance import controller
from decimal import Decimal
from datetime import date
from finance.models import Account
from finance.form_validation import ChargeForm, GetAccountsListForm

def home(request):
    if request.method == 'POST':
        form = GetAccountsListForm(request.POST)
        if form.is_valid():
            return redirect('status', form.cleaned_data.get('account').account_number)
    else:
        form = GetAccountsListForm()
    return render(request, 'home.html',
                  {'form': form})


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
