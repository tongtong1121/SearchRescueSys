# 此模块放置一下供其他app调用的接口方法
from django.contrib.auth.models import User
# TODO:[*] 20-02-04 使用此处方式会出错？？
from .models import AuthUserDir,CaseInfo
# 尝试引入类型约束
from typing import List


def check_case_name(user_id: str, case_name: str) -> bool:
    '''
        根据指定user_id判断指定user_id是否已经创建了指定case_name
    :param user_id:
    :param case_name:
    :return:
    '''
    # TODO:[*] 20-02-04 引发了一个错误，暂时去掉
    users = User.objects.filter(id=user_id)
    if len(users) > 0:
        # 获取该用户的全部的case
        rela_user_case: List[AuthUserDir] = AuthUserDir.objects.filter(uid=users[0].id)
        case_names: List[str] = []
        if len(rela_user_case) > 0:
            # 获取所有的CaseInfo
            case_names = [CaseInfo.objects.filter(id=temp.did.id)[0].case_name for temp in rela_user_case]
        # 判断传入的case_name 是否存在在user的关系中
        if case_name in case_names:
            return True
        return False
    pass

