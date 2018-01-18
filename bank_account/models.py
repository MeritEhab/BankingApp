from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class BankAccount(models.Model):
    user = models.ForeignKey(User)
    iban = models.CharField(max_length=35, verbose_name=("IBAN"))
