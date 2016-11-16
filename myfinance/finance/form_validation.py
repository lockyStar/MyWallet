from django.forms import Form, fields, widgets
from django.core.exceptions import ValidationError
from datetime import date
from django.forms import ModelForm
from finance.models import Charge, Account


class ChargeForm(ModelForm):
    class Meta:
        model = Charge
        fields = ['value', 'date']

    def clean_date(self):
        try:
            date = self.cleaned_data.get('date')
        except:
            raise ValidationError('Неверный формат даты')
        return date

    def clean_value(self):
        try:
            value = self.cleaned_data.get('value')
        except:
            raise ValidationError('Неверный денежный формат')
        return value

    def clean(self):

        value = self.clean_value()
        date = self.clean_date()
        print(value)
        print(date)
        if (value <= 0)and(date >= date.today()):
            raise ValidationError('Нельзя потратить деньги в будущем')


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['name']
