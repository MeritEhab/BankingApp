from django import forms
from django.contrib.auth.models import User

from localflavor.generic.forms import IBANFormField


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    iban = IBANFormField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
