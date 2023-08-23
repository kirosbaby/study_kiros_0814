# -*- coding: utf-8 -*-
"""
@Time:2023/8/19 9:55
@Auth:Dali
@QQ:1334029448
"""
# 斐波那契数列
'''1 1 2 3 5 8 13 21 34'''
# list_1 = []
# for i in range(10):
#     if i == 0 or i ==1:
#         list_1.append(1)
#     else:
#         list_1.append(list_1[i-1] + list_1[i - 2])
# print(list_1)
#
# def fibonacci1(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#         print(a,end=' ')
# fibonacci1(15)

import os
def path_dir(a):
    dir_file = os.listdir(a)  # 找到该路径下的文件
    for i in dir_file:  #
        file_path = os.path.join(a, i)
        if os.path.isfile(file_path):
            print(file_path)
        else:
            path_dir(file_path)


# path_dir(r'D:\class_project\class_70\base_code')

import os


def get_filename(path):
    o = os.listdir(path)
    for i in o:
        new_path = os.path.join(path, i)
        if os.path.isfile(new_path):
            print(new_path)
        else:
            get_filename(new_path)
# get_filename(r'D:\class_project\class_70\base_code')
# 2、使用os模块写一个递归调用打印出某个目录下的所有文件名的绝对路径（例如e:\\home下的所有文件名的绝对路径）？
# import os
#
# '''
# 递归函数：函数内部调用函数本身
# '''

# import os
# def get_filename(path):
#     o=os.listdir(path)
#     for i in o:
#         new_path=os.path.join(path,i)
#         if os.path.isfile(new_path):
#             print(new_path)
#         else:
#             get_filename(new_path)
# get_filename(r'D:\class_project\class_70\base_code')

# import sys,time
# sys.setrecursionlimit(10000)
# def digui(num=0):
#     num+=1
#     print('你好靓仔',num)
#     time.sleep(0.0001)
#     digui(num)
# digui()


# 3\登录和注册
# 要求如下：
# 1、调用本地文件（user.txt)完成登录，如果存在则调用本地文件中用户
# 和对应的密码进行登录，用户在本地文件中的格式如下（用户名：密码）
# admin:123456
# xiao:123123
# 2、登录用户不存在则调注册函数，将注册好的用户写入本地user.txt文件中，写入不能覆盖已有用户。
# 3、用户名的长度大于等于6位，小于等于8位，用户密码大于等于6位小于等于8位。
# def get_userdata():
#     dict_1 = {}
#     txt_1 = open(r'D:\class_project\class_70\base_code\zuoye\user.txt', 'r', encoding='utf-8')
#     get_user = txt_1.readlines()
#     for i in get_user:
#         a, b = i.strip().split(':')
#         dict_1.setdefault(a, b)
#     return dict_1
#
# def login():
#     data = get_userdata()
#     global login_user
#     login_user = input('请输入用户名：')
#     global login_pwd
#     login_pwd = input('请输入密码：')
#     if login_user in data.keys():
#         if login_pwd == data.get(login_user):
#             print('恭喜登录成功！')
#         else:
#             print('输入有误，请重新输入')
#             login()
#     else:
#         print('用户不存在，请注册！')
#         zhuce()
#
# def zhuce ():
#     with open(r'D:\class_project\class_70\base_code\zuoye\user.txt', 'a', encoding='utf-8') as dict_file:
#         dict_file.write(f'\n{login_user}:{login_pwd}')
#         print('注册成功！')
# login()


user_path=r'D:\class_project\class_70\base_code\zuoye\user.txt'
def get_user_pwd():
    read_value = open(user_path, 'r', encoding='utf-8')
    values = read_value.readlines()
    split_values = {}
    for i in values:
        split_values.setdefault(i.strip('\n').split(':')[0], i.strip('\n').split(':')[1])
    return split_values


def register():
    a_value = open(user_path, 'a', encoding='utf-8')
    admin = input('请输入账户\n')
    passwd = input('请输入密码\n')
    if admin not in get_user_pwd().keys():
        a_value.write('\n%s:%s' % (admin, passwd))
        a_value.close()
        print('注册成功')
        login()
    else:
        print('用户已存在，请重新注册')
        register()

def login():
    user_pwd = get_user_pwd()
    admin = input('请输入账户\n')
    passwd = input('请输入密码\n')
    if admin in user_pwd.keys():
        if passwd == user_pwd.get(admin):
            print('登录成功')
        else:
            print('用户名或密码输入错误')
            login()
    else:
        print('请注册')
        register()
login()


''''while循环'''
# def get_userdata():
#     dict_data={}
#     read_value = open(r'D:\class_project\class_70\base_code\zuoye\user.txt', 'r', encoding='utf-8')
#     value=read_value.readlines()
#     for i in value:
#         a,b=i.strip().split(':')
#         dict_data.setdefault(a,b)
#     return dict_data
#
# print(get_userdata())
#
# def login():
#     while True:
#         data=get_userdata()
#         login_user=input('登录用户名：')
#         login_pwd = input('登录密码：')
#         if login_user in data.keys():
#             if login_pwd==data.get(login_user):
#                 print('登录成功')
#                 break
#             else:
#                 print('输入有误，请重新登录')
#         else:
#             print('用户不存在请注册')
#             register()
#
# def register():
#     while True:
#         data=get_userdata()
#         regit_user=input('输入注册账号：')
#         regit_pwd=input('输入注册密码')
#         if regit_user not in data.keys():
#             with open(r'D:\class_project\class_70\base_code\zuoye\user.txt','a')as file_a:
#                 file_a.write(f'\n{regit_user}:{regit_pwd}')
#                 print('注册成功')
#                 break
#         else:
#             print('用户名已存在重新注册')
# login()


''''函数之间调用'''

def get_userdata():
    dict_data={}
    read_value = open(r'D:\class_project\class_70\base_code\zuoye\user.txt', 'r', encoding='utf-8')
    value=read_value.readlines()
    for i in value:
        a,b=i.strip().split(':')
        dict_data.setdefault(a,b)
    return dict_data

print(get_userdata())

def login():
    data=get_userdata()
    login_user=input('登录用户名：')
    login_pwd = input('登录密码：')
    if login_user in data.keys():
        if login_pwd==data.get(login_user):
            print('登录成功')
        else:
            print('输入有误，请重新登录')
            login()
    else:
        print('用户不存在请注册')
        register()
        login()




def register():
    data=get_userdata()
    regit_user=input('输入注册账号：')
    regit_pwd=input('输入注册密码')
    if regit_user not in data.keys():
        with open(r'D:\class_project\class_70\base_code\zuoye\user.txt','a')as file_a:
            file_a.write(f'\n{regit_user}:{regit_pwd}')
            print('注册成功')

    else:
        print('用户名已存在重新注册')
        register()
login()