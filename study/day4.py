# -*- coding: utf-8 -*-
"""
@Time:2023/8/15 9:47
@Auth:gongkewei
@QQ:3295908828
"""
# list_1 = [23, 231, 21, 32, 434, 34, 2, 31, 2, 42, 324, 3242432, 34]
# tuple_1 = (23, 434, 23, 123, 3543, 243, 1342, 132132, 213)
# tuple_2 = (2, 3, 45, 32232, 12311111, 233)
# print(tuple_2 + tuple_1)  # 两个元组拼接
# print('2' in tuple_2)  # '2'是字符串所以结果是false
# print(2 in tuple_2)
# print(len(tuple_2))  # 长度
# print(min(tuple_2))  # 最小值
# print(max(tuple_1))  # 最大值
#
# list_2 = []
# for i in range(1, 101):
#     list_2.append(i)
# print(sum(list_2))  # 求和

'''字典--dict---键值对：键是唯一的,值可以重复可以为空，可变可修改可遍历'''
# dict_1 = dict()
# print(type(dict_1), dict_1)
# dict_2 = {'name': 'xiaoli', 'age': 20, 'classs': '70', 'name': 'dali'}
# print(dict_2)

'''查--- 获取'''
# print(dict_2.get('name'))  # 获取键对应的值
# print(dict_2.get('aaa'))  # 键不存在返回none
# # print(dict_2['aaa']) # 键不存在报错---key error
# print(dict_2.keys())  # 获取所有的键
# print(dict_2.values())  # 获取所有的值

'''添加'''
# dict_2['hobby'] = '爬山'
# print(dict_2)
# dict_2['hobby'] = ['学习', '游泳', '足球']
# print(dict_2)
# dict_2.setdefault('date', '2023-08-15')  # 添加键值对---如果键存在了，不能写入
# dict_2.setdefault('name','xiaoli')
# dict_2.setdefault('addr')  # 只有键，值为none
# dict_2.setdefault('data',{'num':'18720705627','code':'200','userlist':['xiaoli','dada','ysq']})
# print(dict_2)

# 一道题
# dict_4 = {'name':'xiaoli','age':30,'classs':'70','data':{'num':'18813913812','code':'200','userlist':['xiaoli','admin']}}
# print(dict_4['data']['userlist'][1])

'''删除'''
# print(dict_2.pop('name')) # 有返回值
# print(dict_2)
# dict_2.clear() #清空字典
# print(dict_2)
# del dict_2 # 删除字典
# print(dict_2)
# print(dict_2.popitem()) # 默认删除最后一个键值对---元组
# print(dict_2)


# print(dict_2.items()) # 可迭代对象
# for  i in dict_2.items():
#     print(i)
#
# for i ,j in dict_2.items():
#     print(i ,'=', j)
#
# for i in dict_2.keys():
#     print(i)
#
# for i in dict_2.values():
#     print(i)

# 变量的转换
# a = 100
# b = 10
# t = a
# a = b
# b = t
# print(a)
# print(b)
#
# A =99
# B = 30
# A,B = B ,A
# print(A)
# print(B)

'''拆包--元组--列表--元素和变量一致'''
# list_1 = ['dali','xiaoli','laoli']
# a,b,c = tuple_1 = ('zhangsan','lisi','wangwu')
# A,B,C = list_1
# print(A,C,B)
# print(c,b,a)

dict_3 = {'admin':'12345','xiaoli':'123456'}
# input去登录，判断用户名，密码正确---如果错误重新输入
# print(dict_3.keys())
# print(dict_3.values())
# while True:
#     a = input('请输入用户名：')
#     b = input("请输入密码：")
#     if a in dict_3.keys() and b == dict_3.get(a) :
#         print("登录成功！")
#         break
#     else:
#         print('请重新输入！')

# while True:
#     a = input('请输入用户名：')
#     b = input('请输入密码：')
#     if a in dict_3.keys():
#         if b == dict_3[a]:
#             print('登录成功！')
#             break
#         else:
#             continue
#     break
#     else:
#         continue

'''set---集合---无序---可修改---元素唯一'''
# set_1 = set()
# print(type(set_1),set_1)
# set_2 = {'admin','xiaohu','xiaoli','xiaohe','xiaochen','daadmin',23,2323,23,2321,'xiaoli','admin'}
# print(set_2)
#
# set_2.add('classs70')
# print(set_2)
# set_2.update({'74','34'})
# print(set_2)
# print(set_2.pop()) #删除   ---无序，所有没法指定删除
# set_2.clear() # 清空
# print(set_2)

# set_4 = {'admin','xiaohu','xiaoli','xiaohe','xiaochen','daadmin',23,2323,23,2321,'xiaoli','admin'}
# set_5 = {'xiaohe','xiaochen','daadmin',23,999,'ysq','qwe'}
# print(set_4&set_5) # 交集
# print(set_4|set_5) # 并集
# print(set_4-set_5) # 差集
# print(set_5-set_4) # 差集
# print(set_4^set_5) # 补集

# 用字典的形式统计字符串中元素出现的次数
# str_1 = 'fjldsfjlwejlkdfjl3k4j32k4jk324lkjfdsfls234321412'
# dict_6 = {}
# for i in str_1:
#     dict_6.setdefault(i,str_1.count(i))
# print(dict_6)


# 数据类型的分类总结：

#有序：列表，字符串，元组
#无序：字典，集合

# 可变：列表，字典，集合
# 不可变：元组，字符串，数字

'''函数---python自带函数---第三方库---自定义'''
# def xunhuan():
#     print('你好')
# xunhuan()
#
# def num1():
#     for i in range(1,11):
#         print(i)
# num1()
# num1()
# num1()

# def xun(num1): # num1---形式参数--形参
#     for i in range(num1,10):
#         print(i)
# xun(5) # 实际参数---实参
#
# def xun1(num1,num2): # num1，num2---形式参数--形参
#     for i in range(num1,num2):
#         print(i)
# xun1(10,101) # 实际参数--实参

# def xun2(num1,num2):
#     for i in range(num1,num2):
#         print(i)
# xun2(num2=1111,num1=234) # 指定位置参数
#
# def xun3(num1,num2=99):  # num1默认参数---有入参会覆盖默认参数
#     for i in range(num1,num2):
#         print(i)
# xun3(56,80)
#
# def xun4(num1,num2,name):
#     for i in range(num1,num2):
#         print('%s中奖%s次'%(name,i))
# xun4(1,101,'ysq')
#
# def xun4(num1,num2,name):
#     for i in range(num1,num2):
#         print('%s中奖%s次'%(name,i))
# xun4(1,101,['ysq','小元','小钟'])  #列表
#
# def xun4(num1,num2,name):
#     for i in range(num1,num2):
#         print('%s中奖%s次'%(name,i))
# xun4(1,101,('ysq','小元','小钟'))  #元组
#
# def xun4(num1,num2,name):
#     for i in range(num1,num2):
#         print('%s中奖%s次'%(name,i))
# xun4(1,101,{'ysq','小元','小钟'}) # 集合

def xun4(num1,num2,*args): # 可变长参数 ---元组型
    for i in range(num1,num2):
        print('%s中奖%s次'%(args,i))
xun4(1,101,'ysq','小元','小钟')

def xun4(num1,num2,**kwargs): # 可变长参数 ---字典型
    for i in range(num1,num2):
        print('%s中奖%s次'%(kwargs,i))
xun4(1,101,name1='ysq',name2='小元',name3='小钟')