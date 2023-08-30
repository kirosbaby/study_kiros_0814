# -*- coding: utf-8 -*-
"""
@Time:2023/8/30 13:55
@Auth:kirosbaby
@QQ:308902181
"""
import json

import pytest
import requests
import yaml


# class Test_Pramas():
    # list_1 =  [12,3,45,23,2,3,12,34]
    # @pytest.mark.parametrize('num',list_1)
    # def test_num1(self,num):
    #     print(num)

    # list_1 = [(12, 3, 45), (23, 2, 3), (55,12, 34)]
    #
    # @pytest.mark.parametrize('num', list_1)  # 参数化
    # def test_num2(self, num):
    #     print(num)

    # list_1 = [(12, 3, 45), (1, 2, 3), (55, 12, 34)]
    #
    # @pytest.mark.parametrize('a,b,num', list_1)
    # def test_num3(self, a, b, num):
    #     print(a, '+', b, '=', num)
    #     assert a +b == num  # 断言


# 参数化
# class Test_Cms():
#     login_body = [{'userAccount': 'null', 'loginPwd': '123456'}, {'userAccount': 'admin', 'loginPwd': ''},
#         {'userAaccount': 'admin1123', 'loginPwd': '123456'}, {'userAccount': 'admin', 'loginPwd': '123456'}]
#     def setup_class(self):
#         self.url = 'http://kiros.love/cms/manage/loginJump.do'
#         self.hread = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
#
#     def teardown(self):
#         pass
#     @pytest.mark.parametrize('login_body',login_body)
#     def test_login(self,login_body):
#         resp = requests.post(url=self.url, data=login_body, headers=self.hread)
#         print(resp.json())
#         assert '登录成功!' == resp.json()['msg']

# json文件参数化
# class Test_Cms():
#     with open(r'D:\class_project\study_kiros_0814\api_auto\login_json.json','r',encoding='utf-8') as json_r:
#         value = json.load(json_r)
#     @pytest.mark.parametrize('pramas',value)
#     def test_login(self,pramas):
#         resp = requests.post(url=pramas['request']['url'], data=pramas['request']['body'], headers=pramas['request']['header'])
#         print(resp.json())
#         print('*' * 100)
#         assert pramas['response']['code'] == resp.json()['code']  # 断言


# yaml文件参数化
class Test_Cms():
    with open(r'D:\class_project\study_kiros_0814\api_auto\login_yaml.yaml','r',encoding='utf-8') as yaml_r:
        value = list(yaml.safe_load_all(yaml_r))
        print(value[0]['url'])
        print(value[0]['body'])
        print(value[0]['header'])
        print(value[0]['response']['msg'])
    @pytest.mark.parametrize('pramas',value)
    def test_login(self,pramas):
        resp = requests.post(url=pramas['url'], data=pramas['body'], headers=pramas['header'])
        print(resp.json())
        print('*' * 100)
        assert pramas['response']['msg'] == resp.json()['msg']  # 断言

if __name__ == '__main__':
    pytest.main(['-vs', r'D:\class_project\study_kiros_0814\api_auto\test_adi_code_day_3_params.py'])
