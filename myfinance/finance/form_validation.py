from django.forms import Form, fields, widgets
from django.core.exceptions import ValidationError
from datetime import date

class InputForm(Form):

    value = fields.DecimalField(
        label='Сумма',
        decimal_places=2,
        required=True,
        widget=widgets.NumberInput()
    )
    charge_date = fields.DateField(
        label='Дата',
        required=True,
        widget=widgets.DateInput()
    )

    def clean(self):

        value = self.clean_value()
        charge_date = self.clean_date()
        print(value)

        print(charge_date)
        if (value <= 0)and(charge_date >= date.today()):
            raise ValidationError('Нельзя потратить деньги в будущем')


    def clean_date(self):
        try:
            charge_date = self.cleaned_data.get('charge_date')
        except:
            raise ValidationError('Неверный денежный формат')
        return charge_date

    def clean_value(self):
        try:
            value = self.cleaned_data.get('value')
        except:
            raise ValidationError('Неверный формат даты')
        return value
