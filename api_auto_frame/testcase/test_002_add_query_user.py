# -*- coding: utf-8 -*-
"""
@Time:2023/9/1 10:16
@Auth:kirosbaby
@QQ:308902181
"""
import faker

from common.request_api import Api as api
from utils.read_excel import Read_Excel
import pytest,pprint,logging
from common.read_write_file import Read_Write_File
from faker import Faker
read_e = Read_Excel()
name = faker.Faker().name()
rwf = Read_Write_File('data','userid.txt')

class Test_add_query_user():
    @pytest.mark.parametrize('body',read_e.get_body(2))
    def test_add_user(self,body):
        if body[0]['userAccount'] == 'None':
            body[0]['userAccount'] = name
            body[0]['userName'] = name

        resp = api.post(url=read_e.get_url(2),data=body[0])
        logging.info(resp.json())
        assert body[1]['code'] == resp.json()['code']

    @pytest.mark.parametrize('body',read_e.get_body(3))
    def test_query_user(self,body):
        resp = api.post(url=read_e.get_url(3),data=body[0])
        if resp.json()['model']['userList']:
            rwf.write_file(str(resp.json()['model']['userList'][0]['id']))


if __name__ == '__main__':
    pytest.main(['-vs',r'D:\class_project\study_kiros_0814\api_auto_frame\testcase'])