# -*- coding: utf-8 -*-
"""
@Time:2023/8/25 11:49
@Auth:kirosbaby
@QQ:308902181
"""
from utils.read_excel import Read_Excel


class Login_Data():
    read_e = Read_Excel(0, 'data', 'Data.xlsx')

    @classmethod
    def url(cls):
        return cls.read_e.read_data(1, 0)

    @classmethod
    def username(cls):
        return cls.read_e.read_data(1,1)

    @classmethod
    def password(cls):
        return int(cls.read_e.read_data(1,2))


if __name__ == '__main__':
    print(Login_Data.username())
    print(Login_Data.url())
    print(Login_Data.password())
