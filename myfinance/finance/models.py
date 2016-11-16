from django.db import models
from django.forms import ModelForm
from datetime import date
from django.core.exceptions import ValidationError


class Account(models.Model):

    name = models.CharField(max_length=100)
    total = models.DecimalField(decimal_places=2,max_digits=15)
    account_number = models.BigIntegerField()

    class Meta:
        db_table = 'accounts'


class Charge(models.Model):
    value = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField()
    category = models.CharField(max_length=100)
    purpose = models.CharField(max_length=150)
    account_id = models.ForeignKey(Account, related_name='+')

    class Meta:
        db_table = 'charges'