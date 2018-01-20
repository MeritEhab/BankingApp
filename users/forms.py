from bank_account.models import BankAccountUser

from django import forms

from localflavor.generic.forms import IBANFormField


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    iban = IBANFormField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = BankAccountUser
        fields = ['username', 'first_name', 'last_name', 'password', 'iban']
