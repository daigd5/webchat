# -*- coding:utf-8 -*-
from django.conf.urls import url

from UserManager.views import views

__auth__ = 'daigd'

urlpatterns = [
    url(r'login', views.login),
    url(r'register', views.register),
]