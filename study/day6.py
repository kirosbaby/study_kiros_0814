# -*- coding: utf-8 -*-
"""
@Time:2023/8/17 15:37
@Auth:kirosbaby
@QQ:308902181
"""
import json
import os
import re
import string
import time
import random
import hashlib
import faker
import xlrd
import copy

# from time import *
# from time import localtime, ctime, asctime
# from zdy import test_model
# import zdy as z
# z.test_model()

# print(T.ctime())
# print(T.localtime())
# print(T.asctime())
#

# print(localtime())
# print(ctime())
# print(asctime())

'''time'''
# print(time.time())
# print(time.ctime())
# time.sleep(5)
# print(time.strftime('%Y%m%d'))  # 格式化输出时间
# print(time.strftime('%Y%m%d %H%M%S'))
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

'''random---随机模块'''
# print(random.randint(1, 11))
# print(random.random())  # 随机输出浮点数
# print(random.randrange(1, 9))  # 随机输出整数
# print(random.randrange(1, 9, 3))
# print(random.uniform(1, 9))  # 返回指定范围浮点

# list_1 = ('admin', 'xiaoli', 'xiaohe', 'chen', 'jack')
# list_2 = ['admin', 'xiaoli', 'xiaohe', 'chen', 'jack']
# print(random.choice(list_1))  # 随机取序列里面的值
# random.shuffle(list_2)  # 打乱 -- 洗牌 -- 乱序
# print(list_2)
# print(random.sample(list_2, 2)) # 随机取值

# 随机生成136开头的手机号码
# print('136'+ str(random.randint(10000000,99999999)))
#
# num = '136'
# for i in range(8):
#     num += random.choice('1234567890')
# print(num)
#
# num1 = '136'
# value = list('1234567890')
# for i in range(8):
#     num1 += random.choice(value)
# print(num1)
#
# value=list('1234567890')
# list_num=['136']
# for i in range(8):
#     list_num.append(random.choice(value))
# print(''.join(list_num))
#
# print('136'+str(random.random())[2:10])

'''json模块---序列化模块---json串'''
# dict_1 = {"user": "ysq", "age": 30, "data": {"pwd": "123456", "code": 200, "times": "2013"}}
# print(type(dict_1))
# json_1 = json.dumps((dict_1)) # 序列化处理---把python对象转为json对象
# print(type(json_1),json_1)
#
# dict_2 = json.loads(json_1) # 反序列化处理---json对象转为python对象
# print(type(dict_2),dict_2)

# json_1 = json.dumps((dict_1)) # 序列化处理---把python对象转为json对象
# print(type(json_1),json_1)
# with open(r'D:\class_project\pythonProject\test_json.json','w') as test_file:
#     test_file.write(json_1)


# with open(r'D:\class_project\pythonProject\test_json.json', 'r') as test_r:
#     dict1 = test_r.read()
#     dict2 = json.loads(dict1)
#     print(dict2['data']['times'])

# 针对文件的序列化和反序列化处理
# with open(r'D:\class_project\pythonProject\test_json.json', 'r') as test_r:
#     value = json.load(test_r) #反序列化处理--文件
#     print(value['data']['times'])

# with open(r'D:\class_project\pythonProject\test_json.json', 'w') as test_w:
#     json.dump(dict_1, test_w)  # 序列化处理---文件

'''hashlib---md5'''

# MD5 = hashlib.md5(b'@#$%')  # 创建MD5对象---b'@#$%'加盐
# MD5.update('123456'.encode('utf-8'))  # 对内容加密
# print(MD5.hexdigest())  # 以16进制输出

'''os---系统模块'''
# os.chdir(r'D:\class_project\pythonProject\study')  # 进入--cd
# print(os.listdir())  # --ls--
# print(os.getcwd())  # 获取当前位置
# os.mkdir('ui89') # 创建目录
# os.rmdir('ui89') # 删除目录
# os.rmdir('wewwe') # 删除不存在的目录--会报错
# os.rename('../iu.jpg','IUIU.png') # 改名
# os.remove('./user.txt') #删除文件

# print(os.path.exists('IUIU.png')) # 判断文件或者目录是否存在
# print(os.path.exists('zuoye'))

# print(os.path.isfile('test.txt')) # 判断当前路径的文件是否存在
# print(os.path.isfile('day6.py'))
# print(os.path.isfile('day3zuoye.py'))

# print(os.path.isdir('sdf')) # 判断当前路径目录是否存在
#
# print(os.path.split(r'D:\class_project\pythonProject\study\day5.py'))
# print(os.path.split(r'D:\class_project\pythonProject\study'))
# print(os.path.split(r'D:\class_project\pythonProject'))
#
#
# name = 'jsontest.json'
# print(os.path.join('D:\class_project','pythonProject','study',f'{name}'))
#

'''re---正则表达式'''
# str_1 = 'num18720705627phone1378987324518720705627电话0571-99988877，0571-32453321 手机18890987654'
# print(re.findall('18720705627', str_1))  # 列表
# print(re.findall('\d', str_1))  # 匹配数字
# print(re.findall('\D', str_1))  # 非数字
# print(re.findall('\d+', str_1))  # 匹配+号前面一次或多次
# print(re.findall('\d*', str_1))  # 匹配+号前面0次或者多次

# print(re.findall('\d.', str_1))  # 任意匹配字符
# print(re.findall('\d?', str_1))  # 匹配前面的0次或一次
# print(re.findall('\d{11}', str_1))  # 匹配指定次数
# print(re.findall('\d{8,11}', str_1))  # 匹配指定范围
# print(re.findall('\d{4}-\d{8}|\d{11}',str_1))

# value = re.match('\d+', str_1) # 从第一个字符开始匹配，如果第一个字符不是要匹配的类型，则匹配失败并报错
# print(value.group())

# value_1 = re.search('\d+',str_1) # 从第一个字符开始查找，找到全部相关匹配为止，找不到返回一个列表[]
# print(value_1.group())

# value_2 = re.compile('\d{11}')
# print(re.findall(value_2,str_1))

# with open(r'D:\class_project\study_kiros_0814\file_test\test_xml.xml','r',encoding='utf-8') as file_xml:
# value_3 = file_xml.read()
# print(re.findall('<string>(.+)</string>',value_3))  # 括号是分组
#     for i in file_xml:
#         print(re.findall('<string>(\D{2,5})</string>',i))

'''string---字符串模块'''
# print(string.digits) # 数字字符串
# print(string.ascii_lowercase) # 小写英文字母字符串
# print(string.ascii_uppercase) # 大写英文字母字符串
# print(string.ascii_letters) # 大小写英文字母字符串

# 随机生成6位数的验证码（包含数字和英文字符）

# str_1 = string.ascii_letters + string.digits     # 生成字符串大小写字母和数字
# yzm_1 = ''
# for i in range(6):   # 循环6次
#     yzm_1 += random.choice(str_1)     # 随机取一位并且拼接成6位验证码
# print(yzm_1)

'''faker'''
# faker_1 = faker.Faker('zh_CN')
# print(faker_1.name())  # 姓名
# print(faker_1.password())  # 密码
# print(faker_1.address())  # 地址
# print(faker_1.ssn())  # 身份证号码
# print(faker_1.phone_number())  # 手机号码
# print(faker_1.credit_card_number())  # 银行卡号
# print(faker_1.company())  # 公司名

'''xlrd'''
work = xlrd.open_workbook(r'D:\class_project\study_kiros_0814\file_test\data.csv')
value_sheet = work.sheet_by_index(0)  # 获取sheet页
print(value_sheet.cell_value(1, 0))  # 先按行找，再按列找

'''is 内存地址   ==变量值'''
# 浅拷贝---拷贝内最外层（父级）的内容，里面的层级共用内存地址----可变类型
# 不可变类型---浅拷贝--各个层级共用内存地址
# list_1 = ['xiaoli','dalo',['wewe','tuoni','ssd'],'xiaow1w']
# list_2 = list_1.copy()
# print(list_2 is list_1)
# print(list_2[1] is list_1[1])
# list_2[2].append('aaaaddd')
# print(list_2,list_1)

# list_3 = copy.copy(list_1)
# list_1[2].append('dddd')
# print(list_1 is list_3)
# print(list_1[2] is list_3[2])
# print(list_1,list_3)

#不可变类型
# tup_1 = ('xiaoli','dalo',['wewe','tuoni','ssd'],'xiaow1w')
# tup_2 = copy.copy(tup_1)
# print(tup_2 is tup_1)
# print(tup_2[2] is tup_1[2])

# list2 = list_1 = ['xiaoli','dalo',['wewe','tuoni','ssd'],'xiaow1w']
# print(list2 is list_1)
# print(list2[2] is list_1[2])

#深拷贝---完全拷贝--开辟新的内存地址存放--可变

# list2 = list_1 = ['xiaoli','dalo',['wewe','tuoni','ssd'],'xiaow1w']
# list_3 = copy.deepcopy(list2)
# print(list_3 is list2)
# print(list_3[2] is list2[2])

