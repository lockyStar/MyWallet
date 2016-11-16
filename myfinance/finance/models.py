from django.db import models


class Account(models.Model):

    name = models.CharField(max_length=100)
    total = models.DecimalField(decimal_places=2)
    account_number = models.BigIntegerField()

    class Meta:
        db_table = 'accounts'


class Charge(models.Model):
    value = models.DecimalField(decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=100)
    purpose = models.CharField(max_length=150)
    account_id = models.ForeignKey(Account, related_name='account_number')

    class Meta:
        db_table = 'charges'