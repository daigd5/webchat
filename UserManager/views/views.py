# Create your views here.
from common import exception
from common.constants import RequestMethod
from common.decorator import inspect
from common.http_utils import get_parameters
from UserManager.service.user_service import UserService

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
