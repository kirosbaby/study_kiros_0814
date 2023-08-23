# -*- coding: utf-8 -*-
"""
@Time:2023/8/16 9:47
@Auth:gongkewei
@QQ:3295908828
"""

'''作用域'''
# score = 100  # 变量--全局变量
#
#
# def get_score():
#     global score  # 把局部变量设置成全局变量
#     score = 88  # 局部变量 --- 函数内部使用
#     print('数学成绩', score)
#
#
# def get_score1():
#     print('英语成绩', score)
#
#
# get_score1()
# get_score()
# get_score1()

'''return'''


# 1、有return则return值，没有return则返回none
# 2、调用函数把return的返回值给到调用结果
# 3、函数执行到return，代表程序结束
# 4、通过return返回参数传递给下游函数

# def test_2(a, b):
#     return a + b
#     print(a * b)  # 函数程序结束了，这个不执行了
#
#
# def test_3(a, b):
#     print(a + b)
#
#
# print(test_2(10, 3))
# print(test_3(4, 4))


# def score(nu1, nu2):
#     return (nu1 + nu2) / 2
#

# def student(socre_num):
#     if socre_num > 70:
#         print('三好学生')
#     else:
#         print('一好学生')
#
#
# # print((score(56, 43)))
# value = score(88, 90)
# print(value)
# student(value)
# print(student(score(4,5)))


# def score(nu1, nu2):
#     return (nu1 + nu2) / 2
#
# def student(nu1,nu2):
#     socre_num = score(nu1,nu2)
#     if socre_num > 70:
#         print('三好学生')
#     else:
#         print('一好学生')
#
# student(95,91)

'''格式化输出函数formant'''
name = 'lisir1'
age = '50'
# print('姓名:%s,年龄:%s'%s(name,age))
# print('姓名：{},年龄：{}'.format(name,age))
# print('姓名：{}，年龄：{}'.format(age,name))

# print('姓名：{1}，年龄：{0}'.format(age,name))
# user = 'lidali'
# pwd = '123456'
# print('账号：{a},密码{b}'.format(b=user,a=pwd))

# list_1 = ['xiaoli','xiaohu','xiaohe','xiaochen']
# tup_1 = ['dali','dahe','dajiang','dachen']
# print('报道名字如下：{0[1]}{0[2]}{0[3]}'.format(list_1))
# print('报道人数如下：{0[0]}{1[1]}{1[2]}'.format(list_1,tup_1))

# num1 = 3.1415926
# print('圆周率{}'.format(num1))
# print('圆周率{:.2f}'.format(num1))
# print('圆周率{:.3}'.format(num1))
# print('圆周率{:.3f}'.format(num1))
# print('圆周率{:%}'.format(num1))
# print('圆周率{:.2%}'.format(num1))
# print('圆周率{:.2%}'.format(0.031415926))
#
#
'''open --- 打开文件---读、写、追加'''
# raw -- r 防止转义
#以读的方式打开文件
#read_value = open(r'D:\class_project\pythonProject\testysq.txt','r',encoding='utf-8')
# value = read_value.read() #读取里面所有内容---字符串格式返回
# print(value)

# num1 = read_value.readline() #读取行
# print(num1)
# print(read_value.readline())
# print(read_value.readline())
#
# read_list = read_value.readlines() #列表方式读取内容
# print(read_list)

# 写的方式打开文件 W --- 覆盖写入
# write_value = open(r'D:\class_project\pythonProject\testysq.txt','w',encoding='utf-8')
# write_value.write('十年生死两茫茫，不思量，自难忘\n直教人生死相许！')

#追加--a
# write_value = open(r'D:\class_project\pythonProject\testysq.txt','a',encoding='utf-8')
# write_value.write('十年生死两茫茫，不思量，自难忘\n直教人生死相许！')

# import time
# with open(r'D:\class_project\pythonProject\testysq.txt','a',encoding='utf-8') as file_a:
#     file_a.write('今天有雨，记得带伞！')
#     file_a.flush() #冲刷
#     time.sleep(5)  #休眠

# with open(r'D:\class_project\pythonProject\testysq.txt','r',encoding='utf-8') as file_r:
#     # vlaue = file_r.read()
#     # print(vlaue)
#     for i in file_r: # 可循环--可迭代
#         print(i)

# with open(r'D:\QQ图片20210616141157.jpg','rb') as file_rb :
#     vlaue_rb = file_rb.read()
#     print(vlaue_rb)
#
# with open(r'D:\class_project\pythonProject\iu.jpg','wb') as file_wb :
#     file_wb.write(vlaue_rb)
#
with open(r'D:\class_project\pythonProject\testysq.txt','r',encoding='utf-8') as flie_txt:
    vlaue_1 = flie_txt.read()
    print(vlaue_1)

with open(r'D:\class_project\pythonProject\zuoye\ysq.txt','w',encoding='utf-8') as flie_1:
    flie_1.write(vlaue_1)