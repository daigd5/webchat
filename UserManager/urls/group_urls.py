# -*- coding:utf-8 -*-
from django.conf.urls import url

from UserManager.views import group_views

__auth__ = 'daigd'

urlpatterns = [
    url(r'addGroup', group_views.add_group),
    url(r'deleteGroup', group_views.delete_group),
    url(r'deleteGroups', group_views.delete_groups),
    url(r'updateGroup', group_views.update_group),
]