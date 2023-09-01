# -*- coding: utf-8 -*-
"""
@Time:2023/8/30 16:29
@Auth:kirosbaby
@QQ:308902181
"""
import pytest
from conf.config_path import get_path
from utils.email_new import Test_Email
import time,os
def run():
    # report_path = get_path("report",f"case{time.strftime('%y%m%d%H%M%S')}report.html")
    # pytest.main(['-vs',get_path('testcase'),f'--html={report_path}','--self-contained-html'])
    # Test_Email(report_path).send_email()
    pytest.main(['-vs',f'{get_path("testcase")}', '--alluredir', './report/result'])
    os.system('allure serve ./report/result')

if __name__ == '__main__':
    run()