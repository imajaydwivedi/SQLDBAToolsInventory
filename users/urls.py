from django.conf.urls import url
from django.urls import path, re_path
from users import views

# TEMPLATE URLS!
app_name = 'users'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'signup', views.signup, name='signup'),
    url(r'^register/$', views.user_register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    # url(r'^logout/$', views.user_logout, name = 'user_logout'),
    # url(r'special/', views.special, name = 'special'),
    #url(r'signup', views.signup, name='signup'),
]
