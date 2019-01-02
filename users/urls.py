from django.conf.urls import url
from django.urls import path, re_path
from users import views

# TEMPLATE URLS!
app_name = 'users'

urlpatterns = [
    url(r'^$', views.index, name='usersindex'),
    # url(r'signup', views.signup, name='signup'),
    url(r'^register/$', views.register, name='register'),
    #url(r'signup', views.signup, name='signup'),
]
