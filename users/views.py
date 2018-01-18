from bank_account.models import BankAccount

from django.contrib.auth import authenticate, login

from django.shortcuts import redirect, render
from django.views.generic import View

from users.forms import RegistrationForm


class Registration(View):
    form_class = RegistrationForm
    template_name = 'registration/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            iban = form.cleaned_data['iban']
            user.set_password(password)
            user.save()
            bank_account = BankAccount.objects.create(user=user, iban=iban)
            bank_account.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')

        return render(request, self.template_name, {'form': form})
