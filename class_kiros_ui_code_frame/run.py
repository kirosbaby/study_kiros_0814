# -*- coding: utf-8 -*-
"""
@Time:2023/8/25 10:27
@Auth:kirosbaby
@QQ:308902181
"""
import unittest, time
from conf.config import get_path
from utils.HTMLTestRunner import HTMLTestRunner
from utils.email_new import Test_Email

# if __name__ == '__main__':

dis = unittest.TestLoader().discover(get_path('test_cases'), pattern='test_0*.py')  # 加载用例
report_path = get_path('report', f'{time.strftime("%y%m%d-%H%M%S")}report.html')
with open(report_path, 'wb') as file_wb:  # 写入报告文件地址
    runner = HTMLTestRunner(file_wb, verbosity=2, title='CMS_UI自动化报告', description='内容如下：')  # 写入内容
    runner.run(dis)
valaue = Test_Email(report_path)  # 实例化发邮件的类
valaue.send_email()  # 调用方法发送邮件
