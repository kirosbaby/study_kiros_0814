# -*- coding: utf-8 -*-
"""
@Time:2023/8/14 9:50
@Auth:goalkeeping
@QQ:3295908828
"""
'''
list_2 = ["admin","xiaoli","dalia","xiaohe","diaowu","xiaochen"]
list_3 = []
for i in list_2:
    print(i)
    if "xiao" in i:
        list_3.append(i)
print(list_3)
'''
'''
list_2 = ["admin", "xiaoli", "daliaxiao", "xiaohe", "diaowu", "wuaochen"]
list_3 = []
i = 0
while i < len(list_2):
    if list_2[i][0:3] == "xia" or "wu" in list_2[i]:
        list_3.append(list_2[i])
    i += 1
print(list_3)

list_2 = ["admin", "xiaoli", "daliaxiao", "xiaohe", "diaowu", "wuaochen"]
list_3 = []
i = 0
while i < len(list_2):
    if list_2[i][0:3] == "xia":
        list_3.append(list_2[i])
    elif "wu" in list_2[i]:
        list_3.append(list_2[i])
    i += 1
print(list_3)
'''
'''
list_2 = ["admin", "xiaoli", "daliaxiao", "xiaohe", "diaowu", "wuaochen"]
list_2.reverse()
list_3=list_2
print(list_3)

print(list_2[::-1])

list_4 =[]
i = len(list_2)-1
while i>=0:
    list_4.append(list_2[i])
    i -=1
print(list_4)
'''
'''str_1 = "kjflakdsjflakDSF"
value = str_1.upper()  # 转大写
print(value)
str_2 = value.lower()  # 转小写
print(str_2)
str_3 = str_2.capitalize()  # 首字母大写
print(str_3)
print("sdfasd".islower())  # 判断是否小写
str_4 = "lkjsfljdsflSDF"
print(str_4.isupper())  # 判断是否大写
print(str_4.startswith("lk"))  # 以某元素开头
print(str_4.endswith("DF"))  # 以某元素结尾
print(str_4.index("f"))  # 查看元素索引位置
print(str_4.index("f", 5, 10))
print(str_4.count("s"))  # 统计元素个数
'''

str_2 = "hellohangzooohou"
list_1 = []
# str_2.index("o")

i = 0
'''
print(len(str_2))
while i < len(str_2):
    if str_2[i] == "o":
        list_1.append(str_2.index(str_2[i],i))
    i +=1
print(list_1)
'''
# for i in str_2:
#     if i == "o":
#         list_1.append(str_2.index(i))
# print(list_1)
'''
# 制表符：\t     换行符：\n
str_4 = "s\thanghai\thangzhou\tbeijing\nchengd\nu"
print(str_4)
str_5 = '\n\t   hello shanghai   \t\n'
print(str_5.strip())
str_6 = 'aaadfjslkdjfldksaaa'
print(str_6.strip('asd'))  # 清空左右两边的指定内容

str_7 = 'https://invest-stage.finexasia.com/my-account/statistics'
print(str_7.split("/"))  # 切割字符串--返回列表格式
str_8 = 'hellohangzhou'
print('_'.join(str_8))  # 拼接字符串
list_2 = ['https:', '', 'invest-stage.finexasia.com', 'my-account', 'statistics']
print('_'.join(list_2))  # 拼接字符串
'''

# str_9 = 'hellohangzhou'
# value = str_9.replace('h','H')
# value = str_9.replace('h','H',2) #替换元素
# print(value)
# value = str_9.find('h',1) # 查找元素的索引位置
# print(value)
# print(str_9.isalpha()) # 判断字符串是否由字母或者文字组成。
# print('水杭州dfds'.isalpha())
# print('34523'.isdigit()) # 判断字符串的字符是否为纯数字。
# print("sdfdsSDF".isdigit())
#
# str_10 = '杭州sdfdsf'
# v = str_10.encode('utf-8')
# print(v)
# print(b'\xe6\x9d\xad'.decode())

# str_12 = "jlkdsajflkdsajflkkkwqernvv"  # 统计每个元素出现的次数
# list_13 = []
# i = 0
# while i < len(str_12):
#     print(str_12[i])
#     if '%s:%s'%(str_12[i],str_12.count(str_12[i])) not in list_13:
#         list_13.append('%s:%s'%(str_12[i],str_12.count(str_12[i])))
#     i +=1
# print(list_13)

# for i in str_12:
#     print(str_12.count(i))

'''for 循环---有自增'''
'''
str_13 = "hello_hangzhou"
for i in str_13:
    print(i, end='\t')

for i in range(1, 100):
    print(i)
for i in range(50, 9, -1):
    print(i)
'''
'''
# 奇数求和，偶数求积
ou = 1
ji = 0
for i in range(1, 101):
    if i % 2 == 0:
        ou *= i
    else:
        ji += 1
print(ji, ou)
'''
'''
for i in range(2,101,2):
    if i == 80:
        break
    print(i)

for i in range(2,101,2):
    if i == 80:
        continue
    print(i)
'''
# 2、list_irc28=["王安宝","邱昌豪","戴林林","徐婷","丁鼎立","靳涛","李清尘","曹立军","李嘉明","张德伟"]
# 初始化一个列表并录入班级所有同学的姓名
# 1.打印班级所有姓“王邱李”的同学姓名
# 2.随后删除班级所有姓“王邱李”的同学

list_28 = ["王安宝", "邱昌豪", "戴林林", "徐婷", "丁鼎立", "靳涛", "李清尘", "曹立军", "李嘉明", "张德伟"]
list_new28 = []
list_del28 = []
# 第一种写法
# for i in list_28:
#     if i[0] in '王邱李':
#         list_new28.append(i)
# for i in list_28:
#     if i not in list_new28:
#         list_del28.append(i)
# print(list_del28)

# 第二种写法
# for i in list_28[::-1]:
#     if i[0] in "王邱李":
#         print(i)
#         list_28.remove(i)
# print(list_28)

# # 第三种写法
# for i in range(len(list_28) -1, -1, -1):
#     if list_28[i][0] in '王邱李':
#         list_28.remove(list_28[i])
# print(list_28)

# '''元组---可遍历--不能修改（不可变）---小括号'''
# value = tuple('sdfkjdslkjf')
# print(type(value),value)
# tuple_1 = ('admin','xiali',234,['lista','listb'],'admin','dfhju','dahe','test1')
# print(type(tuple_1),tuple_1)
# print(tuple_1.count('admin'))
# print(tuple_1.index('admin'))
# print(tuple_1.index('admin',3))
# tuple_1[3].append('listc')
# print(tuple_1)
# # 经典面试题
# a = ('1')
# b =(1)
# c = ('1',)
# print(type(a))
# print(type(b))
# print(type(c))

# 数据类型转换
list_14 = ['xiaoli', 'xiaohu']
tuple_11 = ('dali', 'dahu')
str_11 = 'sdfsadfsadfdsaf'
# tup_list_11 = tuple(list_14) # 列表转元组
# print(type(tup_list_11),tuple(list_14))
# tup_str_11 = tuple(str_11) # 字符串转元组
# print(type(tup_str_11),tup_str_11)
#
# lis_tuple_11 = list(tuple_11) # 元组转列表
# print(type(lis_tuple_11),lis_tuple_11)
# lis_str_11 = list(str_11) # 字符串转列表
# print(type(lis_str_11),lis_str_11)

str_list_11 = str(list_14)
print(type(str_list_11), str_list_11)
str_tuple_11 = str(tuple_11)
print(type(str_tuple_11), str_tuple_11)

value = ''.join(list_14)
print(type(value), value)
value1 = ''.join(tuple_11)
print(type(value1), value1)

