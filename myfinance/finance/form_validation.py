from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from django.forms import ModelForm
from django.db.models import F
from finance.models import Charge, Account


class ChargeForm(ModelForm):
    class Meta:
        model = Charge
        fields = ['value', 'date', 'purpose', 'category']

    def clean_date(self):
        try:
            date = self.cleaned_data.get('date')
        except:
            raise ValidationError('Invalid data input')
        return date

    def clean_value(self):
        try:
            value = self.cleaned_data.get('value')
        except:
            raise ValidationError('Invalid money input')
        return value

    def clean(self):

        value = self.clean_value()
        date = self.clean_date()
        print(value)
        print(date)

        if (value <= 0)and(date >= date.today()):
            raise ValidationError('You can not spend money in the future')


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['name','total']

    def clean_name(self):
        try:
            name = self.cleaned_data.get('name')
        except:
            raise ValidationError('Invalid name input')
        return name

    def clean_total(self):
        try:
            total = self.cleaned_data.get('total')
            if total < 0:
                raise ValidationError('Invalid total input')
        except:
            raise ValidationError('Invalid total input')
        return total


class GetAccountsListForm(forms.Form):
    account = forms.ModelChoiceField(queryset=Account.objects.all(), initial=0, to_field_name='account_number')

