from django.shortcuts import render
from finance import controller
from finance.form_validation import InputForm
from decimal import Decimal
from datetime import date


def home(request):
    return render(request, 'home.html')


def random_example(request):
    account = controller.random_account()
    return render(
        request, 'table.html',
        {'account': account}
    )


def add_charge(request):
    if request.method == 'POST':
        print(2)
        form = InputForm(request.POST)
        info = 'Форма заполнена, но некорректна'

        if form.is_valid():
            info = 'Форма заполнена и корректна'

    else:
        info = 'Форма не заполнена'
        form = InputForm(initial={'value': Decimal(100), 'charge_date': date.today()})
    return render(
        request, 'input.html',
        {'form': form, 'info': info}
    )


# Create your views here.
