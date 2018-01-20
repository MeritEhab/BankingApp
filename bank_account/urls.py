from bank_account.views import HomeView, UserCreate, UsersList


from django.conf.urls import url
from django.contrib.auth.decorators import login_required


app_name = 'bank_account'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^users/add/$', login_required(UserCreate.as_view()), name='create_user'),
    url(r'^users/list/$', login_required(UsersList.as_view()), name='list_user'),
]
