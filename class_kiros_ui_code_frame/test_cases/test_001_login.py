# -*- coding: utf-8 -*-
"""
@Time:2023/8/25 14:39
@Auth:kirosbaby
@QQ:308902181
"""
from selenium import webdriver
import unittest, time
from page_elemt.main_process_elemt import Process_Elemt as pe
from common_method.com_method import Com_Method as cm
from conf.login_data import Login_Data as ld
from utils.logger import trace_log


class Test_001_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get(ld.url())
        cm.get_driver(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @trace_log
    def test_login(self):
        cm.get_send(pe.user_name, ld.username())
        cm.get_send(pe.pwd, ld.password())
        cm.get_click(pe.login_but)
        time.sleep(2)
        text = cm.get_text(pe.user_text)
        print(text)
        self.assertIn('admin',text)
        return text


if __name__ == '__main__':
    unittest.main()
