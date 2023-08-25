# -*- coding: utf-8 -*-
"""
@Time:2023/8/25 10:41
@Auth:kirosbaby
@QQ:308902181
"""
import os

'''获取路径---拼接项目路径'''
base_path = os.path.dirname(os.path.dirname(__file__))


def get_path(*args):
    return os.path.join(base_path, *args)


if __name__ == '__main__':
    print(base_path)
    print(get_path('data','Data.xlsx'))
