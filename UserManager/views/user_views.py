# Create your views here.
import json

from UserManager.service.user_service import UserService
from common import exception
from common.constants import RequestMethod
from common.decorator import inspect
from common.http_utils import get_parameters

method = RequestMethod()
user_service = UserService()


@inspect(method=method.post)
def login(request):
    username, password = get_parameters(request, ['username', 'password'])
    if not username or not password:
        raise exception.BadRequest('参数不能为空！')
    response = user_service.user_login(request, username, password)
    return response


@inspect(method=method.post)
def register(request):
    username, password, password2, email = get_parameters(request, ['username', 'password', 'password2', 'email'])
    if not username or not password or not password2:
        raise exception.BadRequest('参数不能为空！')
    response = user_service.user_register(username, password, password2, email)
    return response


@inspect(method=method.post)
def update_user(request):
    body = json.loads(request.body)
    user_id = body.get('userId')
    username = body.get('username')
    password = body.get('password')
    password2 = body.get('password2')
    email = body.get('userId')
    if not user_id:
        raise exception.BadRequest('参数userId不能为空！')
    if not username or not password or not password2 or not email:
        raise exception.BadRequest('没有任何更改！')
    response = user_service.update_user_info(user_id, username, password, password2, email)
    return response
