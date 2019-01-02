# from django.contrib import admin
# from django.urls import path
from django.conf.urls import url
# from django.conf.urls import include
from quiz import views


# TEMPLATE URLS!
app_name = 'quiz'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
