# -*- coding: utf-8 -*-
"""
@Time:2023/8/30 18:09
@Auth:kirosbaby
@QQ:308902181
"""
from common.request_api import Api as api
from utils.read_excel import Read_Excel
import pytest
read_e = Read_Excel(0,'data', 'Data.xlsx')
class Test_login():
    @pytest.mark.parametrize('body',read_e.get_body(1))
    def test_login(self,body):
        resp = api.post(url=read_e.get_url(1),data=body[0])
        print(resp.json())
if __name__ == '__main__':
    pytest.main(['-vs',r'D:\class_project\study_kiros_0814\api_auto_frame\testcase\test_001_login.py'])