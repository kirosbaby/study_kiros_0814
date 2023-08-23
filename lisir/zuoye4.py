# -*- coding: utf-8 -*-
"""
@Time:2023/8/17 13:46
@Auth:Dali
@QQ:1334029448
"""


# read_value = open(r'D:\class_project\class_70\base_code\test.txt', encoding='utf-8')
# values = read_value.readlines()
# print(values)
# split_values = []
# for i in values:
#     split_values.append(i.strip('\n').split(' ')[1])
# print('success:%s  fail:%s'%(split_values.count('success'),split_values.count('fail')))

# value=read_value.read()
# print(value.count('success'))
# print(value.count('fail'))
# print(dir(read_value))
# for i in read_value:
#     print(i)
#     print('*' * 32)

# def user_pwd():
#     read_value = open(r'D:\class_project\class_70\base_code\zuoye\user.txt', 'r', encoding='utf-8')
#     values = read_value.readlines()
#     split_values = {}
#     for i in values:
#         split_values.setdefault(i.strip('\n').split(':')[0], i.strip('\n').split(':')[1])
#     return split_values
# # print(user_pwd())
#
# def login():
#     admin = input('请输入账户\n')
#     passwd = input('请输入密码\n')
#     if admin in user_pwd().keys():
#         if passwd == user_pwd().get(admin):
#             print('登陆成功')
#         else:
#             print('用户名或密码输入错误')
#             login()
#     else:
#         print('用户名或密码输入错误')
#         login()
#
# login()

def get_userdata():
    dict_data = {}
    read_value = open(r'D:\class_project\class_70\base_code\zuoye\user.txt', 'r', encoding='utf-8')
    value = read_value.readlines()
    for i in value:
        a, b = i.strip().split(':')
        dict_data.setdefault(a, b)
    return dict_data


print(get_userdata())


def login():
    data = get_userdata()
    login_user = input('登录用户名：')
    login_pwd = input('登录密码：')
    if login_user in data.keys():
        if login_pwd == data.get(login_user):
            print('登录成功')
        else:
            print('输入有误，请重新登录')
    else:
        print('用户不存在请注册')


login()

# def register():
#     data=get_userdata()
#     regit_user=input('输入注册账号：')
#     regit_pwd=input('输入注册密码')
#     if regit_user not in data.keys():
#         open()
#     else:
#         print('用户名已存在重新注册')
