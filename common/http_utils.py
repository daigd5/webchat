# -*- coding:utf-8 -*-
import json
from json import JSONDecodeError

from django.http import HttpResponse

from common import exception
from common.constants import RequestMethod

__auth__ = 'daigd'


def http_response(status_code, message, data='', content_type="application/json;charset=UTF-8"):
    if isinstance(data, HttpResponse):
        return data
    res = {"statusCode": status_code, "message": message, "data": data}
    return HttpResponse(content=json.dumps(res, ensure_ascii=False), content_type=content_type)


def assert_para_not_null(**kwargs):
    """
    assert 参数不为None,且不为 '', 且不为 0, **kwargs: key=value
    :param kwargs:
    :return:
    """
    for para in kwargs:
        if not kwargs.get(para):
            raise exception.BadRequest("{}不能为空".format(para))


def get_parameters(request, para_list: list):
    res = list()
    if request.body and "application/json" in request.content_type:
        try:
            para_dict = json.loads(request.body.decode())
        except JSONDecodeError:
            raise exception.BadRequest("参数格式错误")
        for para_name in para_list:
            if para_name not in para_dict:
                raise exception.BadRequest("缺少参数{}".format(para_name))
            res.append(para_dict.get(para_name))
    elif request.method == RequestMethod.get:
        for para_name in para_list:
            para = request.GET.get(para_name)
            if not para:
                raise exception.BadRequest("缺少参数{}".format(para_name))
            res.append(para)
    elif request.method == RequestMethod.post:
        for para_name in para_list:
            para = request.POST.get(para_name)
            if not para:
                raise exception.BadRequest("缺少参数{}".format(para_name))
            res.append(para)
    else:
        raise Exception('未实现的请求方式')
    if not res:
        return None
    return res if len(res) > 1 else res[0]
