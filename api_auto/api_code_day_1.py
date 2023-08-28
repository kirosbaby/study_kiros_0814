# -*- coding: utf-8 -*-
"""
@Time:2023/8/28 11:45
@Auth:kirosbaby
@QQ:308902181
"""
import time

import requests
import json
import re
import random
from pprint import pprint
from faker import Faker

'''
# post
# 一个http--url--请求方法--请求头--请求体--响应头--响应体--响应协议状态码
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
login_url = 'http://kiros.love/cms/manage/loginJump.do'
login_body = {'userAccount': 'admin', 'loginPwd': '123456'}

resp = requests.post(url=login_url, data=login_body, headers=head)


# print(type(resp.json()),resp.json()) # 反序列化处理---json对象转为python
# print(resp.json()['msg'])
# print(type(resp.text),resp.text) # json串
#
# print(resp.status_code) # 协议状态码
# print(resp.cookies)
# print(resp.url)
# print(resp.content)
'''

''' get '''
'''
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
login_url1 = 'http://kiros.love/cms/manage/loginJump.do?userAccount=admin&loginPwd=123456'
login_url = 'http://kiros.love/cms/manage/loginJump.do'
login_body = {'userAccount': 'admin', 'loginPwd': '123456'}

resp = requests.post(url=login_url,params= login_body,headers=head)
print(resp.json())
'''

'''手动获取cookie'''

# class Test_Cms():
#     def __init__(self):
#         self.hread = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
#         self.login_url = 'http://kiros.love/cms/manage/loginJump.do'
#         self.login_body = {'userAccount': 'admin', 'loginPwd': '123456'}
#         self.adduser_url = 'http://kiros.love/cms/manage/saveSysUser.do'
#         self.adduser_body = {'id': '',
#                              'userName': 'kir',
#                              'userSex': 0,
#                              'userMobile': 18720705627,
#                              'userEmail': '',
#                              'userAccount': 'kir',
#                              'loginPwd': '!*4TqQ7L(z',
#                              'confirmPwd': '!*4TqQ7L(z]'}
#         self.query_url = 'http://kiros.love/cms/manage/queryUserList.do'
#         # self.query_body  = 'startCreateDate=&endCreateDate=&searchValue=&page=1'
#         self.query_body = {'startCreateDate':'','endCreateDate':'','searchValue':'','page':1}
#         self.del_url = 'http://kiros.love/cms/manage/deleteByIds.do'
#         self.del_body = {'ids':160}
#     def test_login(self):
#         resp = requests.post(url=self.login_url, data=self.login_body, headers=self.hread)
#         print(resp.json())
#         self.cookie = resp.cookies
#
#     def test_adduser(self):
#         resp = requests.post(url=self.adduser_url, data=self.adduser_body, headers=self.hread,cookies=self.cookie)
#         print(resp.json())
#
#     def test_query(self):
#         resp = requests.get(url=self.query_url,data=self.query_body,headers=self.hread,cookies=self.cookie)
#         print(resp.json())
#
#     def test_deluser(self):
#         resp = requests.post(url=self.del_url, data=self.del_body, headers=self.hread, cookies=self.cookie)
#         print(resp.json())
#
#
# if __name__ == '__main__':
#     testcmes = Test_Cms()
#     # testcmes.test_login()
#     # # testcmes.test_adduser()
#     # testcmes.test_query()
#     # testcmes.test_deluser()

'''通过session(会话)'获取cookie'''

'''
class Test_Cms():
    def __init__(self):
        # 实例化会话的类，自动获取cookie，使上下游接口保持会话状态
        self.seesion = requests.Session()
        fake = Faker()
        self.name = fake.name()
        self.hread = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
        self.login_url = 'http://kiros.love/cms/manage/loginJump.do'
        self.login_body = {'userAccount': 'admin', 'loginPwd': '123456'}
        self.adduser_url = 'http://kiros.love/cms/manage/saveSysUser.do'
        self.adduser_body = {'id': '',
                             'userName': self.name,
                             'userSex': 0,
                             'userMobile': 18720705627,
                             'userEmail': '',
                             'userAccount': self.name,
                             'loginPwd': '!*4TqQ7L(z',
                             'confirmPwd': '!*4TqQ7L(z]'}
        self.query_url = 'http://kiros.love/cms/manage/queryUserList.do'
        # self.query_body  = 'startCreateDate=&endCreateDate=&searchValue=&page=1'
        self.query_body = {'startCreateDate':'','endCreateDate':'','searchValue':'','page':1}
        self.del_url = 'http://kiros.love/cms/manage/deleteByIds.do'
        # self.del_body = {'ids':160}
    def test_login(self):
        resp = self.seesion.post(url=self.login_url, data=self.login_body, headers=self.hread)
        pprint(resp.json())
        self.cookie = resp.cookies

    def test_adduser(self):

        resp = self.seesion.post(url=self.adduser_url, data=self.adduser_body, headers=self.hread)
        pprint(resp.json())

    def test_query(self):
        resp = self.seesion.get(url=self.query_url,data=self.query_body,headers=self.hread)
        self.userid = resp.json()['model']['userList'][0]['id'] #获取ID值
        self.userid1 = resp.json()['model']['userList'][1]['id']  # 获取ID值
        print(self.userid)

    def test_deluser(self):
        self.del_body = {'ids':{self.userid,self.userid1}} # 根据查询id删除
        resp = self.seesion.post(url=self.del_url, data=self.del_body, headers=self.hread)
        pprint(resp.json())


if __name__ == '__main__':
    testcmes = Test_Cms()
    testcmes.test_login()
    testcmes.test_adduser()
    # testcmes.test_query()
    # testcmes.test_deluser()

'''

'''练习 ---响应结果为xml格式'''

'''
class Province():
    def __init__(self):
        self.url_province = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getSupportProvince'
        self.url_city = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getSupportCity'

    def get_prov(self):
        resp = requests.post(self.url_province)
        city  = re.findall('<string>(.+)</string>', resp.text) # 正则匹配
        self.city1 = random.choice(city) # 随机取一个值
        print(self.city1)


    def get_city(self):
        body = {'byProvinceName': self.city1}
        resp = requests.get(url=self.url_city, params=body)
        print(resp.text)


if __name__ == '__main__':
    province = Province()
    province.get_prov()
    province.get_city()
'''

# '''json格式'''
#
# hread = {'Content-Type': 'application/json'}
# url_login = '/user/init'
# body_login = {"username": "admin", "password": "123456"}
#
# # value_body = json.dumps(body_login) # json模块把字典转化为json串   入参
# # url = 'http://192.168.31.240:5000/user/login'
# # resp = requests.post(url=url, data=value_body, headers=hread)
# # print(resp.json())
#
# url = 'http://192.168.31.240:5000/user/login'
# resp = requests.post(url=url, json=body_login, headers=hread)  # json把字典转为json传入
# print(resp.json())
#
# '''
# :params---get请求，传入参数
# data---psot--请求为表单格式的时候传参
# json---post---请求json格式时候传参
# file---上传文件
#
# 怎么理解json---是一种文件传输格式，不是字典，是js里面的子集，用来数据传输，理解为json串
# '''

class Test_Cms():
    def __init__(self):
        self.url_init = 'http://192.168.31.240:5000/user/init'
        self.hread = {'Content-Type': 'application/json'}
        self.url_login = 'http://192.168.31.240:5000/user/login'
        self.body_login = {"username": "admin", "password": "123456"}
        self.url_query = 'http://192.168.31.240:5000/user/query'
        self.url_delete = 'http://192.168.31.240:5000/user/delete'
    def test_login(self):
        self.seesion = requests.Session()
        resp = self.seesion.post(url=self.url_login, json=self.body_login, headers=self.hread)
        print(resp.json()['token'])
        self.token = resp.json()['token']
    def test_init(self):
        self.token_boby = {"token": self.token}
        resp = self.seesion.post(url=self.url_init, json=self.token_boby, headers=self.hread)
        print(resp.json())
    def test_query(self):
        resp = self.seesion.post(url=self.url_query, json=self.token_boby, headers=self.hread)
        print(resp.json())
    def test_delete(self):
        self.body_delete = {"token": self.token, "username": "user16"}
        resp = self.seesion.post(url=self.url_delete, json=self.body_delete, headers=self.hread)
        print(resp.json())

if __name__ == '__main__':
    testcms = Test_Cms()
    testcms.test_login()
    testcms.test_init()
    testcms.test_query()
    testcms.test_delete()


