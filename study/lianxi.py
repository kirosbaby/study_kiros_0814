# -*- coding: utf-8 -*-
"""
@Time:2023/8/16 14:16
@Auth:gongkewei
@QQ:3295908828
"""
# 先定义一个字典来存放用户名和密码如dic = {'admin': '123456', 'class09': '654321'}
# 1、定义login函数，从字典中获取用户完成登入，登入时判断用户是否存在存在直接登入
# 2、如果输入的登入用户判断不存在字典，则调用 注册（register）函数 ，完成该用户的注册，注册成功后写入字典

# dic_1 = {'admin': '123456', 'class09': '654321'}
# def login(name,password):
#     if name in dic_1.keys() and password in dic_1.get(name) :
#         print('登录成功')
#     else:
#         print('账号密码不存在，现在帮您注册！')
#         return name,password
# # login('class09','654321')
# def register(name1,password1):
#     if name1 not in dic_1.keys() and password1 not in dic_1.values():
#         dic_1.setdefault(name1,password1)
#         print('注册成功！','最新字典为:',dic_1)
#     else:
#         print('账号密码已存在！')
#
# reg_1 = login('admin34','132423456')
# register(reg_1[0],reg_1[1])


# dic_1 = {'admin': '123456', 'class09': '654321'}
# def login():
#     global name
#     name = input('输入您的账号:')
#     global password
#     password = input('偷偷输入密码:')
#     if name != '' and password != '':
#         if name in dic_1.keys() and password in dic_1.get(name):
#             print('登录成功啦！')
#         else:
#             print('账号不存在,现在为您注册一下！')
#             register()
#     else:
#         print('请认真的输入！')
#
# def register():
#      if name not in dic_1.keys() and password not in dic_1.values():
#          dic_1.setdefault(name,password)
#          print('注册成功！','您的新注册的账号是',dic_1)
#          login()
#      else:
#         print('注册失败！')
# login()