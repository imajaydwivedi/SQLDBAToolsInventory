"""SQLDBATools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from inventory import views as inv_views
from quiz import views as quiz_views
from help import views as help_views
from SQLDBATools import views


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^inventory/', include('inventory.urls'), name='inventory'),
    url(r'^quiz/', include('quiz.urls'), name='quiz'),
    url(r'^help/', include('help.urls'), name='help'),
    path('admin/', admin.site.urls),
    url(r'^users/', include('users.urls'), name='users'),
]

# https://stackoverflow.com/a/24983231/4449743
# https://stackoverflow.com/a/26011790/4449743
admin.site.site_header = 'TiVoSQL administration'
