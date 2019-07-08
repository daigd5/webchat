# -*- coding:utf-8 -*-
from django.conf.urls import url

from UserManager.views import user_views

__auth__ = 'daigd'

urlpatterns = [
    url(r'login', user_views.login),
    url(r'register', user_views.register),
    url(r'update', user_views.update_user),
]