from django.conf.urls import url
from help import views

# TEMPLATE URLS!
app_name = 'help'

urlpatterns = [
    url(r'^$', views.index, name='index')
]
