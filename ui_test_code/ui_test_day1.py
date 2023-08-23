# -*- coding: utf-8 -*-
"""
@Time:2023/8/22 11:38
@Auth:kirosbaby
@QQ:308902181
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()  # 实例化
url1 = 'https://www.baidu.com'
url2 = 'file:///C:/Users/Administrator/Documents/Tencent%20Files/308902181/FileRecv/study.html'
url3 = 'https://jd.com'
driver.get(url3)

'''id定位'''
# driver.find_element_by_id('kw').send_keys('牛郎织女千里来相会')  # send_keys--输入内容
# driver.find_element_by_id('su').click()  # 点击
#
# driver.find_element(By.ID,'kw').send_keys('你好')
# driver.find_element(By.ID,'su').click()
'''name和class定位'''
# driver.find_element(By.NAME,'wd').send_keys('出名要趁早')
# driver.find_element(By.CLASS_NAME,'s_btn').click()

'''xpath定位'''
# 相对路径
# driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('黄埔军校，保定军校')
# driver.find_element(By.XPATH,'//input[@class="bg s_btn"]').click()
# driver.find_element(By.XPATH,'//*[@id="form"]/span[1]/input').send_keys('戴雨农')
# driver.find_element(By.XPATH,'//*[@id="form"]/span[2]/input').click()

# 绝对路径
# driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input').send_keys('七夕舔狗经济学')
# driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/div/form/span[2]/input').click()

'''css定位'''
# driver.find_element(By.CSS_SELECTOR,'[name="wd"]').send_keys('吴川年例')
# driver.find_element(By.CSS_SELECTOR,'[value="百度一下"]').click()

'''tag标签定位，需要标签是唯一的才能定位'''
'''link链接定位'''
# driver.find_element(By.XPATH,'//*[@id="s-top-left"]/a[2]').click()
# driver.find_element(By.LINK_TEXT,'hao123').click()
# driver.find_element(By.PARTIAL_LINK_TEXT,'123').click()

'''单选按钮'''

# driver.find_element(By.CSS_SELECTOR,'[id="girl"]').click()
# value = driver.find_elements(By.CSS_SELECTOR,'[type="checkbox"]')
# for i in value:
#     i.click()
#     time.sleep(1)
# for i in value:
#     i.click()
#     time.sleep(1)
'''下拉框'''
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="file_number"]').send_keys(r'C:\Users\Administrator\Desktop\原桌面\class.txt')
# time.sleep(3)
# elemt = driver.find_element(By.XPATH,'/html/body/form/table/tbody/tr[7]/td[2]/select')
# select=Select(elemt)
# select.select_by_index(1)

'''上传文件'''
# driver.find_element(By.ID,'file_number').send_keys(r'C:\Users\Administrator\Documents\Tencent Files\308902181\FileRecv\data.csv')

'''窗口切换'''
# driver.find_element(By.LINK_TEXT,'新闻').click()
# handles = driver.window_handles # 获取所有句柄
# print(handles)
# driver.switch_to.window(handles[1])
# time.sleep(2)
# driver.find_element(By.LINK_TEXT,'星火成炬 | 陪伴是最长情的告白').click()

'''前进，后退，获取title，最大化'''
driver.find_element(By.CLASS_NAME, 'link-login').click()
time.sleep(2)
driver.back()  # 返回
time.sleep(2)
driver.forward()  # 前进
time.sleep(2)
# driver.set_window_size(width=700,height=500)# 设置浏览器窗口大小
time.sleep(2)
driver.maximize_window()  # 最大化浏览器
time.sleep(2)
print(driver.get_window_size())  # 获取窗口大小
print(driver.title)  # 获取title







time.sleep(8)
# driver.quit()# 关闭浏览器
