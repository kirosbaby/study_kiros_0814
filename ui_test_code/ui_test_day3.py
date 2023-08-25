# -*- coding: utf-8 -*-
"""
@Time:2023/8/24 10:44
@Auth:kirosbaby
@QQ:308902181
"""
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url1 = 'https://www.jd.com'
driver.get(url1)
driver.maximize_window()

'''滚动条'''
# time.sleep(1)
# js_s = 'window.scrollTo(0,2000)'
# driver.execute_script(js_s)  # PX
# time.sleep(2)
# driver.execute_script('window.scrollTo(0,0)')
# time.sleep(3)
# driver.execute_script('window,open("https://www.taobao.com")')  # 打开新的窗口

'''等待'''
# time.sleep(10) # 强制等待---固定等待
driver.implicitly_wait(10) # 隐式等待---全局等待---等待整个页面加载

# 显示等待---等待具体的元素加载
# wait = WebDriverWait(driver, 10)  # 实例化等待的类，拿到对象，并传入等待时间
# wait.until(ec.presence_of_element_located((By.ID, 'key')))  # 直到，某个元素加载出来，就满足条件，往下执行
# driver.find_element(By.ID, 'key').send_keys('公路车')

'''截图---记录执行结果，或者遇到报错截图'''
# js_s = 'window.scrollTo(0,2000)'
# driver.execute_script(js_s)
# time.sleep(2)
# driver.save_screenshot(r'D:\class_project\study_kiros_0814\file_test\jd.png') # 截图
# driver.get_screenshot_as_file(r'D:\class_project\study_kiros_0814\file_test\baidu.png') # 截图

'''keys 键盘操作'''
driver.find_element(By.ID,'key').send_keys('公路自行车')
time.sleep(1)
driver.find_element(By.ID,'key').send_keys((Keys.CONTROL,'a'))
time.sleep(1)
driver.find_element(By.ID,'key').send_keys((Keys.CONTROL,'c'))
time.sleep(1)
driver.find_element(By.ID,'key').clear()
time.sleep(1)
driver.find_element(By.ID,'key').send_keys((Keys.CONTROL,'v'))
time.sleep(1)
driver.find_element(By.ID,'key').send_keys(Keys.BACK_SPACE)
time.sleep(1)
driver.find_element(By.ID,'key').send_keys(Keys.ENTER)


time.sleep(8)
driver.quit()
