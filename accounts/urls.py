from django.urls import path
from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^home/$',views.Home,name="home"),
    url(r'^login/$',views.loginView, name="login"),
    url(r'^register/$',views.registerView,name="register"),
    url(r'^logout/$',views.logoutView,name='logout'),

]