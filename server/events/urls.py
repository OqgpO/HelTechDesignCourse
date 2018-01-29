# coding=utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^authorize$', views.authorize, name='authorize'),
    url(r'^auth_page_token$', views.authorize_page, name='authorize_page'),
    url(r'^elevate_token$', views.elevate_page_token, name='elevate_page_token'),
    url(r'^select/(?P<wname>[A-Za-z0-9.]+)$', views.select_page, name='select_page'),
]
