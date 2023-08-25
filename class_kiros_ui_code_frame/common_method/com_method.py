# -*- coding: utf-8 -*-
"""
@Time:2023/8/25 14:28
@Auth:kirosbaby
@QQ:308902181
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()

class Com_Method():
    @classmethod
    def get_driver(cls, driver):  # 获取浏览器驱动
        cls.driver = driver

    @classmethod
    def find_elemt(cls, elemt):
        a, b = elemt
        return cls.driver.find_element(a, b)

    @classmethod
    def get_click(cls, elemt):
        cls.find_elemt(elemt).click()

    @classmethod
    def get_send(cls, elemt, text):
        cls.find_elemt(elemt).send_keys(text)

    @classmethod
    def get_text(cls, elemt):
        return cls.find_elemt(elemt).text

    @classmethod
    def get_frame(cls,elemt):
        cls.driver.switch_to.frame(cls.find_elemt(elemt))  # 进入ifram框
    @classmethod
    def out_frame(cls):
        # cls.driver.switch_to.default_content()  # 退出框
        cls.driver.switch_to.parent_frame() # 返回上一级框内
    @classmethod
    def get_sleep(cls,sco):
        return time.sleep(sco)
    @classmethod
    def refresh(cls):            # 刷新页面
        cls.driver.refresh()
    @classmethod
    def quit(cls):   # 退出浏览器
        cls.driver.quit()
