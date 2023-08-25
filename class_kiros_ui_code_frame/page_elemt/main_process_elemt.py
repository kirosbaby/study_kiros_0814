# -*- coding: utf-8 -*-
"""
@Time:2023/8/25 14:01
@Auth:kirosbaby
@QQ:308902181
"""
from selenium.webdriver.common.by import By


class Process_Elemt():
    user_name = (By.XPATH, '//*[@id="userAccount"]')
    pwd = (By.XPATH, '//*[@id="loginPwd"]')
    login_but = (By.XPATH, '//*[@id="loginBtn"]')

    user_center = (By.XPATH, '//*[@id="menu-user"]/dt/i')
    user_manage = (By.XPATH, '//*[@id="menu-user"]/dd/ul/li[1]/a')
    iframe_add_user = (By.XPATH, '//*[@id="iframe_box"]/div[2]/iframe') # 进入添加用户的iframe框
    add_user_but = (By.XPATH, '/html/body/div/div[2]/span[1]/a[2]')
    iframe_adduser = (By.XPATH, '//*[@id="xubox_iframe1"]')  # 添加用户切换iframe进行输入

    add_name = (By.XPATH, '//*[@id="userName"]')
    add_sex  =(By.CSS_SELECTOR, '[value="0"]')
    add_phone = (By.XPATH, '//*[@id="user-tel"]')
    add_email = (By.XPATH, '//*[@id="user-email"]')
    add_login_account = (By.XPATH, '//*[@id="userAccount"]')
    add_pws_01 = (By.XPATH, '//*[@id="loginPwd"]')
    add_pws_02 = (By.XPATH, '//*[@id="confirmPwd"]')
    add_user_enter_but = (By.XPATH, '//*[@id="submitBtn"]')

    #DEL
    # (By.XPATH, '//*[@id="iframe_box"]/div[2]/iframe') # frame框
    del_but = (By.XPATH, '//*[@id="sysUserTab"]/tr[1]/td[9]/a[4]/i') # 删除按钮
    del_enter = (By.XPATH, '//*[@id="xubox_layer1"]/div[1]/span[2]/a[1]') # 确认按钮