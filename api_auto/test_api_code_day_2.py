# -*- coding: utf-8 -*-
"""
@Time:2023/8/29 10:42
@Auth:kirosbaby
@QQ:308902181
"""
import json

import requests

'''参数化'''
import unittest
from ddt import ddt, data, file_data, unpack

#
# @ddt
# class Test_Ddt(unittest.TestCase):
#     # @data(1, 1, 324, 23, 32, 2, 1, 221, 3, 12, 2)
#     # def test_num1(self, num1):
#     #     print(num1)
#
#     # @data([1, 1], [324, 23], [32, 2], [1, 221], [3, 12])
#     # @unpack
#     # def test_num2(self, num2,num3):
#     #     print(num2,'X',num3)
#
#     # @data(*[{'useraccount':'null','loginpwd':'123456'},{'useraccount':'admin','loginpwd':''},
#     #        {'useraccount':'admin1123','loginpwd':'123456'},{'useraccount':'admin','loginpwd':'123456'}])
#     # def test_num3(self,body):
#     #     print(body)
#     @classmethod
#     def setUpClass(cls) -> None:
#         cls.url = 'http://kiros.love/cms/manage/loginJump.do'
#         cls.hread = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         pass
#
#     body = ([{'userAccount': 'null', 'loginPwd': '123456'}, {'userAccount': 'admin', 'loginPwd': ''},
#              {'userAaccount': 'admin1123', 'loginPwd': '123456'}, {'userAccount': 'admin', 'loginPwd': '123456'}])
#
#     @data(*body)
#     def test_login(self, bodys):
#         print(bodys)
#         resp = requests.post(url=self.url, data=bodys, headers=self.hread)
#         print(resp.json())
#
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)


@ddt
class Test_Ddt(unittest.TestCase):
    with open(r'D:\class_project\study_kiros_0814\api_auto\login_json.json', 'r', encoding='utf-8') as json_file:
        value = json.load(json_file)
    @data(*value)
    def test_login(self, values):
        url = values['request']['url']
        body = values['request']['body']
        heade = values['request']['header']
        resp = requests.post(url=url, data=body, headers=heade)
        print(resp.json())
        self.assertEqual(values['response']['msg'],resp.json()['msg'])
if __name__ == '__main__':
    unittest.main(verbosity=2)

