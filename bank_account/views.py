from bank_account.models import BankAccountUser

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import (CreateView, DeleteView, DetailView,
    ListView, TemplateView, UpdateView)

from users.forms import RegistrationForm, UserEditForm


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


class UserDetail(DetailView):
    model = BankAccountUser
    template_name = "bank_account/profile.html"

    def get(self, request, *args, **kwargs):
        obj = self.get_object()

        if (request.user.is_admin and obj.creator == request.user) or(
         obj.id == request.user.id) or (request.user.is_superuser):
            return render(request, self.template_name, {'object': obj})
        else:
            return render(request, "bank_account/no_permission.html")


class UserUpdate(UpdateView):
    form_class = UserEditForm
    model = BankAccountUser
    template_name = "bank_account/edit_user.html"
    success_url = reverse_lazy("bank_account:list_user")

    def get(self, request, *args, **kwargs):
        obj = self.get_object()

        if request.user.is_admin and obj.creator == request.user:
            return self.post(request, *args, **kwargs)
        else:
            return render(request, "bank_account/no_permission.html")


class UserDelete(DeleteView):
    model = BankAccountUser
    success_url = reverse_lazy("bank_account:list_user")

    def get(self, request, *args, **kwargs):
        obj = self.get_object()

        if request.user.is_admin and obj.creator == request.user:
            return self.post(request, *args, **kwargs)
        else:
            return render(request, "bank_account/no_permission.html")
