# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-20 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0003_auto_20180119_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccountuser',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
    ]
