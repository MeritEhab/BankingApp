from bank_account.views import (
    HomeView, UserCreate, UserDelete,
    UserDetail, UserUpdate, UsersList
    )

from django.conf.urls import url
from django.contrib.auth.decorators import login_required


app_name = 'bank_account'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^users/add/$', login_required(UserCreate.as_view()), name='create_user'),
    url(r'^users/list/$', login_required(UsersList.as_view()), name='list_user'),
    url(r'^users/(?P<pk>[0-9]+)/$', login_required(UserDetail.as_view()), name='profile'),
    url(r'^users/(?P<pk>[0-9]+)/edit/$', login_required(UserUpdate.as_view()), name='user_edit'),
    url(r'^users/(?P<pk>[0-9]+)/delete/$', login_required(UserDelete.as_view()), name='user_delete'),
]
