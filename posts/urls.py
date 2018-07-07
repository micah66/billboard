from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

urlpatterns = [
    url(r'^$', views.posts, name='posts'),
    url(r'^registration', views.registration, name='registration'),
    url(r'^login', login, kwargs = {'template_name': 'billboard/login.html'}, name='login'),
    url(r'^logout', logout, kwargs = {'next_page': '/posts'}, name='logout'),
]
