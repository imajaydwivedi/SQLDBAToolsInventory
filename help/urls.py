from django.conf.urls import url
from help import views

urlpatterns = [
    url(r'^$', views.index, name='helpindex')
]
