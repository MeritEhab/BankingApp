from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.db import models


class BankAccountUser(AbstractUser):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    iban = models.CharField(max_length=35, verbose_name=("IBAN"))
    is_admin = models.BooleanField(default=True)
