# from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls import url
# from django.conf.urls import include
from . import views

# TEMPLATE URLS!
app_name = 'mssql'

# https://docs.djangoproject.com/en/2.1/ref/urls/
# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    # url(r'^$', index, name='index'),
    path('', views.index, name='index'),
    # url(r'server2', views.server2, name='server2'),
    path('server/', views.server, name='server'),
    path('server/add/', views.serveradd, name='serveradd'),
    # url(r'server/add', views.serveradd, name='serveradd'),
    # url(r'server', views.server, name='server'),
    # url(r'test', views.test, name='test'),
    # path('bio/<username>/', views.bio, name='bio'),
    # path('articles/<slug:title>/', views.article, name='article-detail'),
    # path('articles/<slug:title>/<int:section>/', views.section, name='article-section'),
    # path('articles/2003/', views.special_case_2003),
    # path('articles/<int:year>/', views.year_archive),
    # path('articles/<int:year>/<int:month>/', views.month_archive),
    # path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]
