from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from django.forms import ModelForm
from django.db.models import F
from finance.models import Charge, Account


class ChargeForm(ModelForm):
    class Meta:
        model = Charge
        fields = ['value', 'date']

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
        fields = ['name']


class GetAccountsListForm(forms.Form):
    account = forms.ModelChoiceField(queryset=Account.objects.all(), initial=0, to_field_name='name', required=True)


class DropDown(forms.Form):
    account = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        self.categories = kwargs.pop("categories", None)
        super(DropDown, self).__init__(*args, **kwargs)

        CHOICES = ()

        for category in self.categories:
            # CHOICES for ChoiceField needs to be a list of tuples (value, representation),
            # with value=actual value of choice and representation=how it will be displayed
            CHOICES += ((category, category),)

        self.fields["account"].choices = CHOICES
