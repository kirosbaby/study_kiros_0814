# -*- coding: utf-8 -*-
"""
@Time:2023/8/24 9:41
@Auth:Dali
@QQ:1334029448
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class Cms_Ui():
    def __init__(self):
        self.driver = webdriver.Chrome()
        url = 'http://www.kiros.love/cms'
        self.driver.get(url)

    def login(self):
        self.driver.find_element(By.XPATH, '//*[@id="userAccount"]').send_keys('admin')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="loginPwd"]').send_keys('123456')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()

    def add_user(self):
        self.driver.find_element(By.XPATH, '//*[@id="menu-user"]/dt/i').click()  # 中心
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="menu-user"]/dd/ul/li[1]/a').click()  # 管理
        time.sleep(1)
        el = self.driver.find_element(By.XPATH, '//*[@id="iframe_box"]/div[2]/iframe')
        self.driver.switch_to.frame(el)  # 切换frame
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/span[1]/a[2]').click()  # 添加用户

        el_1 = self.driver.find_element(By.XPATH, '//*[@id="xubox_iframe1"]')
        self.driver.switch_to.frame(el_1)  # 切换frame  进入添加页面

        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="userName"]').send_keys('kiros')
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, '[value="0"]').click()  # 性别
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="user-tel"]').send_keys('18720705627')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="user-email"]').send_keys('kiros.run@qq.com')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="userAccount"]').send_keys('kiros')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="loginPwd"]').send_keys('kiros1995')
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="confirmPwd"]').send_keys('kiros1995')
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="submitBtn"]').click()  # 点击确定
        self.driver.switch_to.default_content()

    def del_user(self):
        el = self.driver.find_element(By.XPATH, '//*[@id="iframe_box"]/div[2]/iframe')
        self.driver.switch_to.frame(el)  # 切换frame
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="sysUserTab"]/tr[1]/td[9]/a[4]/i').click()  # 删除按钮
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="xubox_layer1"]/div[1]/span[2]/a[1]').click()  # 点击确定删除

    def quit(self):
        time.sleep(2)
        self.driver.refresh()  # 退出框
        self.driver.find_element(By.XPATH, '/html/body/header/span[2]/a').click()
        time.sleep(4)
        self.driver.quit()


if __name__ == '__main__':
    cms_ui = Cms_Ui()
    cms_ui.login()
    cms_ui.add_user()
    cms_ui.del_user()
    cms_ui.quit()
