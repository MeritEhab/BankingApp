from bank_account.views import HomeView

from django.conf.urls import url

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]
