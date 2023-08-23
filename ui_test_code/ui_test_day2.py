# -*- coding: utf-8 -*-
"""
@Time:2023/8/23 10:10
@Auth:kirosbaby
@QQ:308902181
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url1 = 'https://www.baidu.com/'
url2 = 'file:///C:/Users/Administrator/Documents/tencent%20files/308902181/filerecv/alert.html'
url3 = 'file:///C:/Users/Administrator/Documents/tencent%20files/308902181/filerecv/alert3.html'
url4 = 'https://mail.163.com/'
driver.get(url4)
time.sleep(1)
# driver.refresh()  # 刷新页面
time.sleep(1)
'''获取文本'''
# vlaue = driver.find_elements(By.XPATH,'//*[@class="title-content-title"]')[5].text
# print(vlaue)
# vlaue = driver.find_element(By.ID,'hotsearch-content-wrapper').text  # 获取文本
# print(vlaue)

'''鼠标悬停'''

# elemt = driver.find_element(By.LINK_TEXT,'更多')
# action = ActionChains(driver)
# action.move_to_element(elemt).perform()
# driver.find_element(By.XPATH,'//*[@id="s-top-more"]/div[3]/a[3]/img').click()

'''弹框处理'''
# time.sleep(2)
# driver.switch_to.alert.dismiss() # 弹窗取消操作
# time.sleep(1)
# driver.switch_to.alert.accept() # 弹窗同意操作

# driver.find_element(By.ID,'prompt').click()
# print(driver.switch_to.alert.text)
# time.sleep(1)
# driver.switch_to.alert.send_keys('你好')
# time.sleep(1)
# driver.switch_to.alert.accept()

'''frame框的操作'''
elemt = driver.find_element(By.XPATH,'//*[@id="loginDiv"]/iframe')
driver.switch_to.frame(elemt)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'[name="email"]').send_keys('12345678')
driver.find_element(By.CSS_SELECTOR,'[name="password"]').send_keys('234234325')
driver.find_element(By.CSS_SELECTOR,'[id="dologin"]').click()
driver.switch_to.default_content() # 退出框





time.sleep(5)
driver.quit()

