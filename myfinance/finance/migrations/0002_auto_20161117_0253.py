# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 23:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='charge',
            old_name='account_id',
            new_name='account',
        ),
        migrations.AlterField(
            model_name='account',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]