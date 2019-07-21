# -*- coding:utf-8 -*-
import json

from UserManager.services.group_service import GroupService
from common import exception
from common.constants import RequestMethod
from common.decorator import inspect
from common.exception import BadRequest
from common.http_utils import get_parameters

__auth__ = 'daigd'

group_service = GroupService()


@inspect(method=RequestMethod.post)
def add_group(request):
    group_name, desc = get_parameters(request, ['groupName', 'description'])
    response = group_service.add_group(group_name, desc)
    return response


@inspect(method=RequestMethod.post)
def update_group(request):
    body = json.loads(request.body)
    group_id = body.get('groupId')
    group_name = body.get('groupName')
    desc = body.get('description')
    if not group_id:
        raise exception.BadRequest('缺少参数groupId!')
    if not group_name or not desc:
        raise exception.BadRequest('没有任何更改！')
    response = group_service.update_group(group_id, group_name, desc)
    return response


@inspect(method=RequestMethod.get)
def delete_group(request):
    group_id = get_parameters(request, ['groupId'])
    response = group_service.delete_group(group_id)
    return response


@inspect(method=RequestMethod.post)
def delete_groups(request):
    group_id_list = get_parameters(request, ['groupIdList'])
    if not isinstance(group_id_list, list):
        raise BadRequest('参数groupIdList应为数组')
    response = group_service.delete_groups(group_id_list)
    return response


@inspect(method=RequestMethod.get)
def load_groups(request):
    session_id = request.COOKIES.get('sessionId')
    username = request.session.get(session_id)
    assert username, "未正确获取username"
    response = group_service.load_groups(username)
    return response
