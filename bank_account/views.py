from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "bank_account/home.html"