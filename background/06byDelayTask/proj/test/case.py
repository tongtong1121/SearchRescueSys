#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 16:24
# @Author  : evaseemefly
# @Desc    :
# @Site    : 
# @File    : case.py
# @Software: PyCharm
from datetime import datetime

from core.job import coverage_current_job, coverage_wind_job, init_product
from util.tools import exe_run_time

from conf.settings import _MYSQL
from core.db import DbFile

def case_test_coveragedownload():
    '''
        20-04-07 + 测试下载 current 栅格数据(date)
    :return:
    '''
    current = datetime.now()
    init_product(current)
    coverage_current_job()
    # TODO:[-] 20-04-14 增加风场下载 by caiwb
    coverage_wind_job()


# err:TypeError: exe_run_time() takes 0 positional arguments but 1 was given
# err:TypeError: 'NoneType' object is not callable
@exe_run_time()
def case_test_wrap():
    '''
        20-04-10 + 测试计时器
    :return:
    '''
    print('测试')


def main():
    case_test_coveragedownload()
    # case_test_wrap()

    # file_name = 'bhs_cur_20200413.nc'
    # target_dir = r'd:\data\SearchRescueSys\data\download\COMMON\DAILY\2020\4\13'
    # db_file = DbFile(_MYSQL.get('HOST'), _MYSQL.get('DB_NAME'), _MYSQL.get('USER'), _MYSQL.get('PASSWORD'))
    # db_file.record_state(file_name, target_dir)
    pass


if __name__ == '__main__':
    main()
    pass
