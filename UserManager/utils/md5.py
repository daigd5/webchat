# -*- coding:utf-8 -*-
import hashlib
__auth__ = 'daigd'


def to_md5(text: str):
    m = hashlib.md5()
    m.update(text.encode())
    return m.hexdigest()
