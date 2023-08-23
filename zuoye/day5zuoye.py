# -*- coding: utf-8 -*-
"""
@Time:2023/8/16 19:05
@Auth:kirosbaby
@QQ:308902181
"""

# 1、随机生成6位数验证码，包含大小写英文字母和数字
import random


# 2、登录和注册
# # 要求如下：
# # 1、调用本地文件（user.txt)完成登录，如果存在则调用本地文件中用户
# # 和对应的密码进行登录，用户在本地文件中的格式如下（用户名：密码）
# admin:123456
# xiao:123123


# txt1 = open(r'D:\class_project\pythonProject\study\user.txt', 'r', encoding='utf-8')
# file_1 = txt1.readline()
# file_2 = txt1.readline()
#
# def login():
#     if file_1 not in '' and file_2 not in '':
#         name = input('name:')
#         password = input('password:')
#         user1 = file_1.strip('\n').split(':')
#         user2 = file_2.strip('\n').split(':')
#         if name == user1[0] and password == user1[1]:
#             print('恭喜登录成功！')
#         elif name == user2[0] and password == user2[1]:
#             print('恭喜登录成功！')
#         else:
#             print('系统中没有对应的账号或者密码！！')
#     else:
#         print('系统中没有账号信息,请完善信息后登录！！')
# login()


def get_userdata():
    dict_1 = {}
    txt_1 = open(r'D:\class_project\pythonProject\study\user.txt', 'r', encoding='utf-8')
    get_user = txt_1.readlines()
    for i in get_user:
        a, b = i.strip().split(':')
        dict_1.setdefault(a, b)
    return dict_1

def login():
    data = get_userdata()
    login_user = input('请输入用户名：')
    login_pwd = input('请输入密码：')
    if login_user in data.keys():
        if login_pwd == data.get(login_user):
            print('恭喜登录成功！')
        else:
            print('输入有误，请重新输入')
            login()
    else:
        print('用户不存在，请注册！')

def zhuce ():
    pass



# 2、存在一个文件, 文件名test.txt
# 内容如下：
# 01 success
# 02 fail
# 03 fail
# 04 success
# ....请使用Python语言编写程序实现统计该文件中
# 有多少个success，多少个fail

# def count_1():
#     txt1 = open(r'D:\class_project\pythonProject\testysq.txt', 'r', encoding='utf-8')
#     file_1 = txt1.readlines()
#     list_1 = []
#     dict_1 = {}
#     for i in file_1:
#         list_1.append(i.split(' ')[1].strip('\n'))    # 分割和清空
#     for i in list_1:
#         dict_1.setdefault(i, list_1.count(i))
#     return dict_1
# print(count_1())
#
