# -*- coding:utf-8 -*-
from functools import wraps

from common.constants import StatusCode
from common.exception import BadRequest
from common.log import logger
from common.http_utils import http_response
import json
import traceback

__auth__ = 'daigd'


def inspect(method=None):
    """
    请求前的请求方式检查
    请求后的异常捕捉
    :param method:
    :return:
    """
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            assert len(args) > 0, "请传request参数"
            request = args[0]
            user = ""
            if method and request.method != method:
                logger.error(f"用户{user}访问{request.path}时，请求方式错误！")
                return http_response(StatusCode.wrong_method, '请求方式错误！')
            try:
                res = func(*args, **kwargs)
                logger.info(f"用户{user}访问{request.path}成功")
                return res
            except BadRequest as msg:
                logger.error(f"用户{user}访问{request.path}时，请求参数不正确：{str(msg)}")
                return http_response(StatusCode.bad_request, str(msg))
            except Exception as err:
                logger.error(f'用户{user}访问{request.path}时，发生异常：{str(err)}'
                             f'\n请求参数为{json.loads(request.body)},\n{traceback.format_exc()}')
                return http_response(StatusCode.failed, f'发生异常：{str(err)}')
        return wrapper
    return inner
