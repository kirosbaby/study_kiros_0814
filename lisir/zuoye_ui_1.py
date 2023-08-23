# -*- coding: utf-8 -*-
"""
@Time:2023/8/23 19:03
@Auth:Dali
@QQ:1334029448
"""
import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
url_1 = 'https://www.ctrip.com/'
url_2 = 'http://www.kiros.love/cms'
driver.get(url_2)
driver.maximize_window()
time.sleep(1)

# driver.find_element(By.CSS_SELECTOR,'[class="hs_show-hightlight_CWkCV"]').clear()
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR,'[class="hs_show-hightlight_CWkCV"]').send_keys('杭州')
# time.sleep(1)
# elemt = driver.find_element(By.CSS_SELECTOR,'[class="hs_show-hightlight_CWkCV"]')
# elemt.send_keys(Keys.TAB)
#
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="checkIn"]').click()
# time.sleep(6)
# # driver.find_element(By.XPATH,'//*[@id="kakxi"]/li[2]/div[2]/div/div[1]/div[1]/div/ul[5]/li[4]/span').click()
# # time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="kakxi"]/li[2]/div[2]/div/div[1]/div[1]/div/ul[5]/li[4]/span').click()
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="kakxi"]/li[2]/div[2]/div/div[1]/div[2]/div/ul[4]/li[3]/span').click()
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="kakxi"]/li[3]/div/div[1]/p').click()  # 房间以及住客
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="kakxi"]/li[3]/div/div[2]/div[1]/div[1]/div[2]/span[3]').click()
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="kakxi"]/li[3]/div/div[2]/div[2]/div/span').click()
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="kakxi"]/li[4]/div/div[1]').click() # 酒店级别
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="kakxi"]/li[4]/div/div[2]/div[4]').click()
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="kakxi"]/li[4]/div/div[2]/div[5]/span[2]').click() # 确定按钮
# time.sleep(1)
# driver.find_element(By.XPATH,'//*[@id="kakxi"]/li[6]/div/span').click() # 搜索
#
# time.sleep(5)
# driver.quit()


driver.find_element(By.XPATH, '//*[@id="userAccount"]').send_keys('admin')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="loginPwd"]').send_keys('123456')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()  # 登录

time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="menu-user"]/dt/i').click()#中心
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="menu-user"]/dd/ul/li[1]/a').click()#管理
time.sleep(1)

el = driver.find_element(By.XPATH, '//*[@id="iframe_box"]/div[2]/iframe')
driver.switch_to.frame(el)  # 切换frame
driver.find_element(By.XPATH, '/html/body/div/div[2]/span[1]/a[2]').click()  # 添加用户

el_1 = driver.find_element(By.XPATH, '//*[@id="xubox_iframe1"]')
driver.switch_to.frame(el_1)  # 切换frame  进入添加页面

time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="userName"]').send_keys('kiros')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '[value="0"]').click()  # 性别
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="user-tel"]').send_keys('18720705627')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="user-email"]').send_keys('kiros.run@qq.com')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="userAccount"]').send_keys('kiros')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="loginPwd"]').send_keys('kiros1995')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="confirmPwd"]').send_keys('kiros1995')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="submitBtn"]').click()  # 点击确定
driver.switch_to.default_content()  # 退出框
time.sleep(2)
el = driver.find_element(By.XPATH, '//*[@id="iframe_box"]/div[2]/iframe')
driver.switch_to.frame(el)  # 切换frame
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="sysUserTab"]/tr[1]/td[9]/a[4]/i').click() # 删除按钮
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="xubox_layer1"]/div[1]/span[2]/a[1]').click()  # 点击确定删除

time.sleep(2)
driver.switch_to.default_content()  # 退出框
driver.find_element(By.XPATH, '/html/body/header/span[2]/a').click()  # 退出登录

time.sleep(5)
driver.quit() # 退出浏览器