from django.conf.urls import url

from django.contrib.auth import views as auth_views

from users.views import Registration


urlpatterns = [
    url(r'^register/$', Registration.as_view(), name='registreration'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
