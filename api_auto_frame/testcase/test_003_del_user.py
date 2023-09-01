# -*- coding: utf-8 -*-
"""
@Time:2023/9/1 11:31
@Auth:kirosbaby
@QQ:308902181
"""
from common.request_api import Api as api
from utils.read_excel import Read_Excel
import pytest
from common.read_write_file import Read_Write_File
from db.read_sql_data import Test_MySql
read_e = Read_Excel()
rwf = Read_Write_File('data','userid.txt')
class Test_Del_User():
    @pytest.mark.parametrize('body', read_e.get_body(4))
    def test_del_user(self, body):
        if body[0]['ids'] == '10086':
            # body[0]['ids'] = rwf.read_file()
            body[0]['ids'] = Test_MySql().select_user_id()
            resp = api.post(url=read_e.get_url(4), data=body[0])
            print(resp.json())
if __name__ == '__main__':
    pytest.main(['-vs', r'D:\class_project\study_kiros_0814\api_auto_frame\testcase'])
