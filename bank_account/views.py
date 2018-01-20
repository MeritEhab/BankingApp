from bank_account.models import BankAccountUser

from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, TemplateView

from users.forms import RegistrationForm


class HomeView(TemplateView):
    template_name = "bank_account/home.html"


class UsersList(ListView):
    template_name = "bank_account/users_list.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return BankAccountUser.objects.all()
        else:
            return BankAccountUser.objects.filter(creator=self.request.user)


class UserCreate(CreateView):
    template_name = "bank_account/add_user.html"
    form_class = RegistrationForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.creator = request.user
            user.is_admin = False
            user.save()
            return redirect('/')

        return render(request, self.template_name, {'form': form})
