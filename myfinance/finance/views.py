from django.shortcuts import render
from django.shortcuts import redirect
from finance import controller
from decimal import Decimal
from datetime import date
from finance.models import Account
from finance.form_validation import ChargeForm, GetAccountsListForm, AccountForm
from random import randint

def home(request):
    print(Account.objects.only('total').values('total'))
    if request.method == 'POST':
        form = ChargeForm(request.POST)

        if form.is_valid():
            return redirect('status', form.account)
    else:
        form = GetAccountsListForm()

    return render(request, 'home.html',
                  )


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
            acc = Account.objects.get(account_number=account_id)
            charg = form.save(commit=False)
            charg.account_id = acc.id
            charg.save()

    else:
        info = 'Form is not filled'
        form = ChargeForm(initial={'value': Decimal(100), 'date': date.today()})

    return render(
        request, 'input.html',
        {'form': form, 'info': info, 'account_id': account_id}
    )

def add_Account(request):
    if request.method=='POST':
        print(3)
        form = Account_Form(request.POST)
        info = 'Account is filled, but not correct'
        if form.is_valid():

            info = 'Account is filled and correct'
            name = AccountForm.clean_name(form)
            total=AccountForm.clean_total(form)
            account_number=randint(0,100000)



            b=Account_Form(name=name, total=total, account_number=account_number)
            b.save()
    else:
        info = 'Account is not filled'
        form = AccountForm()
    return render(
        request, 'inputAccount.html',
        {'form': form, 'info': info,}
        )


# Create your views here.
