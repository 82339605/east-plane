from django.conf.urls import url,include
from django.contrib import admin
from .views import *
urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'register',register,name='register'),
    url(r'login',login,name='login'),
    url(r'log',logout,name='logout'),
    url(r'check_repeat',check,name='check'),
    url(r'shopping',shopping,name='shopping')
]