import os
from django.db import models

# Create your models here.


from webchat.settings import BASE_DIR

headimg_path = os.path.join(BASE_DIR, 'UserManager', 'media', 'headImg')
default_headimg = os.path.join(headimg_path, 'defaultAvatar.jpg')


class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to=headimg_path, default=default_headimg)
    email = models.EmailField()
    is_admin = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    last_login = models.DateTimeField(default=None, null=True)
    mtime = models.DateTimeField(auto_now_add=True)
    ctime = models.DateTimeField(auto_now=True)


class Group(models.Model):
    group_name = models.CharField(max_length=64)
    description = models.CharField(max_length=254)
    mtime = models.DateTimeField(auto_now_add=True)
    ctime = models.DateTimeField(auto_now=True)


class GroupMember(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    mtime = models.DateTimeField(auto_now_add=True)
    ctime = models.DateTimeField(auto_now=True)

