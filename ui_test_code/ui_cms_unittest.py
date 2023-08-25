# -*- coding: utf-8 -*-
"""
@Time:2023/8/24 16:08
@Auth:kirosbaby
@QQ:308902181
"""

# 用unittest框架封装cms

import unittest
import time
import faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from  HTMLTestRunner import HTMLTestRunner

from faker import Faker

fake = faker.Faker()


class Test_Cms(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:  # cls 是类方法
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://www.kiros.love/cms')
        cls.driver.maximize_window()
        cls.newname = fake.name()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        cls.driver.quit()  # 退出浏览器

    def test_001_login(self):
        self.driver.find_element(By.XPATH, '//*[@id="userAccount"]').send_keys('admin')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="loginPwd"]').send_keys('123456')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()  # 登录
        time.sleep(3)
        text = self.driver.find_element(By.XPATH, '/html/body/header/span[2]/span').text  # 获取页面文本元素（超级管理员：admin）
        self.assertIn('admin', text, msg='断言成功！')  # 断言

    def test_002_add_user(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="menu-user"]/dt/i').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="menu-user"]/dd/ul/li[1]/a').click()
        time.sleep(1)

        el = self.driver.find_element(By.XPATH, '//*[@id="iframe_box"]/div[2]/iframe')
        self.driver.switch_to.frame(el)  # 切换frame
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/span[1]/a[2]').click()  # 添加用户

        el_1 = self.driver.find_element(By.XPATH, '//*[@id="xubox_iframe1"]')
        self.driver.switch_to.frame(el_1)  # 切换frame  进入添加页面

        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="userName"]').send_keys(self.newname)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '[value="0"]').click()  # 性别
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="user-tel"]').send_keys('18720705627')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="user-email"]').send_keys('kiros.run@qq.com')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="userAccount"]').send_keys(self.newname)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="loginPwd"]').send_keys('kiros1995')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="confirmPwd"]').send_keys('kiros1995')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="submitBtn"]').click()  # 点击确定
        self.driver.switch_to.default_content()  # 退出框

    def test_003_del_user(self):
        time.sleep(5)
        el = self.driver.find_element(By.XPATH, '//*[@id="iframe_box"]/div[2]/iframe')
        self.driver.switch_to.frame(el)  # 切换frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="sysUserTab"]/tr[1]/td[9]/a[4]/i').click()  # 删除按钮
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="xubox_layer1"]/div[1]/span[2]/a[1]').click()  # 点击确定

    def test_004_quit(self):
        time.sleep(2)
        self.driver.switch_to.default_content()  # 退出框
        self.driver.find_element(By.XPATH, '/html/body/header/span[2]/a').click()  # 退出登录


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    dis = unittest.TestLoader().discover(r'D:\class_project\study_kiros_0814\ui_test_code',pattern='ui_cms_unittest.py') # 加载用例
    with open(fr'D:\class_project\study_kiros_0814\ui_test_code\report-{time.strftime("%y-%m-%d-%H-%M-%S")}.html','wb')as file_wb:   # 写入报告文件地址
        runner = HTMLTestRunner(file_wb,verbosity=2,title='CMS_UI自动化报告',description='内容如下：')  # 写入内容
        runner.run(dis)

