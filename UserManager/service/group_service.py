# -*- coding:utf-8 -*-
from UserManager.dao.group import GroupDAO
from UserManager.models import Group
from UserManager.utils.date_utils import date2str
from common.constants import StatusCode
from common.http_utils import http_response
from common.log import logger

__auth__ = 'daigd'

status_code = StatusCode()


class GroupService:
    group_dao = GroupDAO()

    def add_group(self, group_name, desc):
        if self.is_group_exists(group_name):
            logger.info(f"组名{group_name}已存在")
            return http_response(StatusCode.failed, '组名已存在！')
        group = self.group_dao.create_group(group_name, desc)
        logger.info(f"创建组{group_name}成功")
        return http_response(status_code.success, "创建成功", data={"groupId": group.id})

    def is_group_exists(self, group_name):
        return self.group_dao.is_group_name_exist(group_name)

    def update_group(self, group_id, group_name, desc):
        self.group_dao.update_group(group_id, group_name, desc)
        logger.info(f"更改id={group_id}组名为{group_name}，描述为{desc}")
        return http_response(status_code.success, "修改成功")

    def delete_group(self, group_id):
        self.delete_group(group_id)
        logger.info(f'删除组id={group_id}成功')
        return http_response(status_code.success, '删除成功')

    def delete_groups(self, group_id_list: list):
        self.group_dao.delete_groups(group_id_list)
        logger.info(f'删除组id in{str(group_id_list)}成功')
        return http_response(status_code.success, "删除成功")

    def load_groups(self, username):
        group_objs = self.group_dao.query_groups_by_username(username)
        result = list()
        for group in group_objs:
            result.append(self.group2json(group))
        logger.info(f"用户{username}查询组列表成功")
        return http_response(status_code.success, "获取成功", data=result)

    @staticmethod
    def group2json(group: Group):
        return {"groupId": group.id, "groupName": group.group_name, "description": group.description,
                "creator": group.creator.username, "modifyTime": date2str(group.mtime),
                "createTime": date2str(group.ctime)}
