# -*- coding: utf-8 -*-
"""
@Time:2023/8/25 15:27
@Auth:kirosbaby
@QQ:308902181
"""

import unittest, time
import faker
from page_elemt.main_process_elemt import Process_Elemt as pe
from common_method.com_method import Com_Method as cm
from test_cases.test_001_login import Test_001_login

fake = faker.Faker()
fake_name = fake.name()
fake_pwd = fake.password()


class Test_002_AddUser(unittest.TestCase):
    @classmethod
    def test_adduser(cls):
        cm.get_click(pe.user_center)
        cm.get_click(pe.user_manage)
        cm.get_frame(pe.iframe_add_user)  # 进入添加页面大框
        cm.get_click(pe.add_user_but)
        cm.get_frame(pe.iframe_adduser)  # 进入添加用户小框

        cm.get_send(pe.add_name, fake_name)
        cm.get_click(pe.add_sex)  # 选择性别
        cm.get_send(pe.add_phone, 18720705627)
        cm.get_send(pe.add_email, fake.safe_email())
        cm.get_send(pe.add_login_account, fake_name)
        cm.get_send(pe.add_pws_01, fake_pwd)
        cm.get_send(pe.add_pws_02, fake_pwd)
        cm.get_click(pe.add_user_enter_but)  # 确定按钮

        cm.get_sleep(1)
        cm.out_frame() # 退出框


if __name__ == '__main__':
    unittest.main()
