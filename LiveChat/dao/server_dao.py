# -*- coding:utf-8 -*-
from LiveChat.models import Server

__auth__ = "daigd"


class ServerDao:

    def __init__(self):
        pass

    @staticmethod
    def save(ip, port):
        Server.objects.create(host=ip, port=port)
