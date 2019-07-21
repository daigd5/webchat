# -*- coding:utf-8 -*-
import abc
import socket
import threading

from LiveChat.dao.server_dao import ServerDao

__auth__ = "daigd"


class BaseServer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def bind(self):
        pass

    @abc.abstractmethod
    def accept(self):
        pass


server_dao = ServerDao()


class ChatServer(BaseServer):

    def __init__(self):
        self.socket = socket.socket()
        self.room = {}
        self.start_port = 8000
        self.limit_conn = 10

    def __get_an_available_addr(self):
        ip = self.__get_local_ip()
        addr = None
        while True:
            try:
                s = socket.socket()
                s.connect((ip, self.start_port))
            except ConnectionRefusedError:
                addr = ip, self.start_port
                break
            else:
                self.start_port += 1
                continue
        return addr

    def __get_local_ip(self):
        return socket.gethostbyname(socket.getfqdn(socket.gethostname()))

    def __bind(self):
        ip, port = self.__get_an_available_addr()
        server_dao.save(ip, port)
        self.socket.bind((ip, port))
        self.socket.listen(self.limit_conn)

    def __message_hub(self, sok: socket.socket):
        while True:
            msg = sok.recv(1024)
            if msg:
                for sk in self.room:
                    if sk != id(sok):
                        self.room.get(sk).send(msg)


    def __save_message(self, msg):
        pass

    def __accept(self):
        sok, raddr = self.socket.accept()
        self.room[id(sok)] = sok
        threading.Thread(target=self.__message_hub, args=(sok), name="chatroom").start()

    def connect(self):
        while True:
            threading.Thread(target=self.__accept, name="conn").start()
