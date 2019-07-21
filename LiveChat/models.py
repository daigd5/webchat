from django.db import models

# Create your models here.
from UserManager.models import User


class Room(models.Model):
    id = models.AutoField()
    room_name = models.CharField(max_length=32, null=False)
    description = models.CharField(max_length=255, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    ctime = models.DateTimeField(auto_now_add=True)
    socket = models.IntegerField(null=True)
    mtime = models.DateTimeField(auto_now=True)


class RoomMember(models.Model):
    id = models.AutoField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ChatRecord(models.Model):
    id = models.AutoField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.CharField(max_length=255, null=False)
    ctime = models.DateTimeField(auto_now_add=True)


class Server(models.Model):
    id = models.AutoField()
    host = models.IPAddressField()
    port = models.SmallIntegerField()
    ctime = models.DateTimeField(auto_now_add=True)
