# -*- coding:utf-8 -*-
import datetime


__auth__ = 'daigd'

FORMAT = "%Y-%m-%d %H:%M:%S"


def date2str(date):
    return datetime.datetime.strftime(date, FORMAT)


