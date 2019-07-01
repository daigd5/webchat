# -*- coding:utf-8 -*-
from django.db.models.functions import datetime

from UserManager.models import User
from UserManager.utils.md5 import to_md5

__auth__ = 'daigd'


class UserDAO:
    @staticmethod
    def get_user(id=None, username=None, password=None):
        if id:
            # 通过id查询用户
            return User.objects.get(id=id)
        if username and password:
            # 通过用户名和密码
            return User.objects.filter(username=username, password=to_md5(password)).first()
        if username and not password:
            # 通过用户名
            return User.objects.filter(username=username).first()

    @staticmethod
    def update_user_status(id):
        user = User.objects.get(id=id)
        user.last_login = datetime.datetime.now()
        user.is_online = True
        user.save()

    @staticmethod
    def create_user(username, password, email):
        User.objects.create(username=username, password=to_md5(password), email=email)



