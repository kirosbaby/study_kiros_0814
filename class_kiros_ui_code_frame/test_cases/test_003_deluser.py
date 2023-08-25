# -*- coding: utf-8 -*-
"""
@Time:2023/8/25 16:48
@Auth:kirosbaby
@QQ:308902181
"""
import unittest
from page_elemt.main_process_elemt import Process_Elemt as pe
from common_method.com_method import Com_Method as cm
# from test_cases.test_001_login import Test_001_login
# from test_cases.test_002_adduser import Test_002_AddUser

class Test_003_DelUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cm.get_sleep(2)
    @classmethod
    def tearDownClass(cls) -> None:
        cm.get_sleep(5)
        cm.quit()  # 退出浏览器
    @classmethod
    def test_deluser(cls):
        # cm.get_frame(pe.iframe_adduser) # 进入frame框
        cm.get_sleep(1)
        cm.get_click(pe.del_but)
        cm.get_sleep(1)
        cm.get_click(pe.del_enter)




if __name__ == '__main__':
    unittest.main()