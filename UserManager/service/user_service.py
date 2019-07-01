# -*- coding:utf-8 -*-

from common.constants import StatusCode
from common.http_utils import http_response
from UserManager.dao.user import UserDAO
from common.log import logger

__auth__ = 'daigd'

status_code = StatusCode()


class UserService:
    user_dao = UserDAO()

    def user_login(self, request, username, password):
        user = self.user_dao.get_user(username=username, password=password)
        if user:
            self.update_user_login_status(user.id)
            logger.info(f"更新用户{user.username}的登录状态成功")
            self.save_session(request, username)
            logger.info(f"用户{username}登录成功")
            return http_response(status_code.success, '登录成功')
        else:
            logger.info(f"用户{username}登录密码或用户名错误")
            return http_response(status_code.failed, '用户名或密码错误')

    @staticmethod
    def save_session(request, username):
        request.session[username] = username
        # 默认半个小时
        request.session.set_expiry(30*60)
        logger.info(f"保存用户{username}的session成功")

    def update_user_login_status(self, id):
        self.user_dao.update_user_status(id)

    def user_register(self, username, password, password2, email):
        if password != password2:
            return http_response(status_code.bad_request, "两次密码输入不一致")
        user = self.user_dao.get_user(username=username)
        if user:
            logger.info(f"用户名{username}已存在")
            return http_response(status_code.failed, "用户名已存在")
        self.user_dao.create_user(username, password, email)
        logger.info(f"用户{username}注册成功")
        return http_response(status_code.success, "注册成功")





