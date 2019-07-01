# -*- coding:utf-8 -*-
__auth__ = 'daigd'


class StatusCode:
    success = 200
    failed = 500
    wrong_method = 405
    timeout = 408
    not_found = 404
    bad_request = 400


class RequestMethod:
    get = 'GET'
    post = 'POST'
