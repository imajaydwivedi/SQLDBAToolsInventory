# from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
# from django.conf.urls import include
from inventory import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'test', views.test, name='test'),
]
