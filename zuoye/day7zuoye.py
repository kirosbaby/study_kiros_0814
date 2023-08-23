# -*- coding: utf-8 -*-
"""
@Time:2023/8/18 18:09
@Auth:kirosbaby
@QQ:308902181
"""
import json


# 1、分析以下数字的规律， 1 1 2 3 5 8 13 21 34用Python语言编程实现输出
# 斐波那契数列

# def fibonacci1(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#         print(a)
#
#
# fibonacci1(15)

# 2、使用os模块写一个递归调用打印出某个目录下的所有文件名的绝对路径（例如e:\\home下的所有文件名的绝对路径）？
# import os
#
# '''
# 递归函数：函数内部调用函数本身
# '''
import os


# def path_dir(a):
#     dir_file = os.listdir(a)  # 找到该路径下的文件
#     for i in dir_file:  #
#         file_path = os.path.join(a, i)
#         if os.path.isfile(file_path):
#             print(file_path)
#         else:
#             path_dir(file_path)
#
#
# path_dir(r'D:\class_project\study_kiros_0814\file_test')


# 3\登录和注册
# 要求如下：
# 1、调用本地文件（user.txt)完成登录，如果存在则调用本地文件中用户
# 和对应的密码进行登录，用户在本地文件中的格式如下（用户名：密码）
# admin:123456
# xiao:123123
# 2、登录用户不存在则调注册函数，将注册好的用户写入本地user.txt文件中，写入不能覆盖已有用户。
# 3、用户名的长度大于等于6位，小于等于8位，用户密码大于等于6位小于等于8位。

def get_userdata():
    dict_1 = {}
    txt_1 = open(r'D:\class_project\study_kiros_0814\file_test\user.txt', 'r', encoding='utf-8')
    get_user = txt_1.readlines()
    for i in get_user:
        a, b = i.strip().split(':')
        dict_1.setdefault(a, b)
    return dict_1

def login():
    data = get_userdata()
    global login_user
    login_user = input('请输入用户名：')
    global login_pwd
    login_pwd = input('请输入密码：')
    if login_user in data.keys():
        if login_pwd == data.get(login_user):
            print('恭喜登录成功！')
        else:
            print('输入有误，请重新输入')
            login()
    else:
        print('用户不存在，请注册！')
        zhuce()

def zhuce():
    with open(r'D:\class_project\study_kiros_0814\file_test\user.txt', 'a', encoding='utf-8') as dict_file:
        dict_file.write(f'\n{login_user}:{login_pwd}')
        print('注册成功！')

login()
