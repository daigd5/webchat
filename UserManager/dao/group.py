# -*- coding:utf-8 -*-
from UserManager.models import Group

__auth__ = 'daigd'


class GroupDAO:

    @staticmethod
    def create_group(group_name, desc):
        return Group.objects.create(group_name=group_name, description=desc)

    @staticmethod
    def is_group_name_exist(group_name):
        return Group.objects.filter(group_name=group_name).exists()

    @staticmethod
    def update_group(group_id, group_name, desc):
        group = Group.objects.get(id=group_id)
        if group_name:
            group.group_name = group_name
        if desc:
            group.description = desc
        group.save()

    @staticmethod
    def delete_group(group_id):
        Group.objects.get(id=group_id).delete()

    @staticmethod
    def delete_groups(group_id_list):
        Group.objects.filter(id__in=group_id_list).delete()

    @staticmethod
    def query_groups_by_username(username):
        return Group.objects.filter(creator__username=username)
