# from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
# from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'Server', views.server, name='server'),
    url(r'server/add', views.serveradd, name='ServerAdd'),
]
