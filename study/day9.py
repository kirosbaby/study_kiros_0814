# -*- coding: utf-8 -*-
"""
@Time:2023/8/21 14:09
@Auth:kirosbaby
@QQ:308902181
"""
import time

# def func1(msg):
#     print(msg, '这是func1')
# # func1()
# aa = func1  # 函数的引用---把函数作为变量赋值
# aa('函数1')

# def func2():
#     print('这是func2')
# def func3(msg): # 把函数作为参数传入
#     msg()
#     print('这是func3')
# func3(func2)

# def func2(msgg):
#     print(msgg,'这是func2')
# def func3(msg,data,data3): # 把函数作为参数传入
#     msg(data)
#     print('这是func3',data3)
# func3(func2,'函数2的数据','函数3')


# 嵌套函数
# def func4(msg1,msg2): # 外部函数
#     print(msg1,'这是func4')
#     def func5(msg2): # 内部函数
#         print(msg1,msg2,'这是func5')
#     return func5(msg2) # 外部函数返回内部函数的调用
# func4('4的参数','5的参数')


'''闭包：在一个外函数中定义了一个内函数，内函数里运用了外函数的变量
并且外函数的返回值是内函数的引用，这样就构成了一个闭包。
'''
#
# def func6(msg1):
#     print(msg1,'外部函数')
#     def func7(msg2):
#         print(msg1,msg2,'内部函数')
#     return func7 # 外部函数返回内部函数的引用
# # value = func6() # 外部函数---拿到返回的内部函数
# # value() # 调用内部函数
# func6('函数6')('函数7')

# def xunh():
#     start = time.perf_counter()
#     for i in range(1,1000000):
#         print(f'你好啊，靓仔{i}')
#     end = time.perf_counter()
#     print(end - start)
# xunh()

'''
def xunh(num1,num2):
    for i in range(num1,num2):
        print(f'你好啊，靓仔{i}')

def external(func):
    def inner(num1,num2):
        start = time.perf_counter()
        func(num1,num2)
        end = time.perf_counter()
        print(f'耗时{end-start}')
    return inner
external(xunh)(1,1000000)
'''
'''装饰器---一个函数，运用了闭包的原理进行操作，不影响原有函数的功能，还能添加新的功能'''

'''
def external(func): # 装饰器函数
    def inner(num1,num2):
        start = time.perf_counter()
        func(num1,num2)
        end = time.perf_counter()
        print(f'耗时{end-start}')
    return inner


@external # 添加装饰器--把被装饰函数作为参数传入装饰器函数  external()
def xunh(num1,num2): # 被装饰函数
    for i in range(num1,num2):
        print(f'你好啊，靓仔{i}')
xunh(1,12345)

'''

'''lambda---匿名函数   左边是入参：右边是出参'''
# def test1(x,y):
#     return x*y
# print(test1(11,8))

# f = lambda x,y:x*y
# print(f(9,5))


# x = 11
# if x%2 == 0:
#     print('even')
# else:
#     print('odd')
#
# value = 'even' if x%2==0 else 'odd'
# print(value)
#
# f = lambda  x: 'even' if x%2==0 else 'odd'
# print(f(110))

# f = lambda x, y: [i for i in range(x, y)]
# print(f(23, 324))

# list_1 = [(3, 52), (9, 23), (2, 17), (9, 110), (32, 88)]
# def test_p(x):
#     return x[1]
# list_1.sort(key=test_p)
# print(list_1)
# list_1.sort(key= lambda  x:x[1])  # 匿名函数的方法
# print(list_1)

#
# a = [1, 2, 14, 6, 7, 8]
# aa = [1, 21, 4, 4, 17, 38]
# b = []
# for i in a:
#     b.append(i ** 2)
# print(b)
#
# a_1 = list(map(lambda x: x * 2, a))
# print(a_1)
#
# a_11 = list(map(lambda x, y: x * 2 + y, a, aa))
# print(a_11)

'''
# 练习
a = [1, 2, 14, 6, 7, 8]
b = []
for i in range(len(a) - 1):
    b.append(a[i] * a[i + 1])
print(b)

a = [1, 2, 14, 6, 7, 8]
a_12 = list(map(lambda x,y: x*y , a[1:],a[:len(a)-1]))
a_12.sort()
print(a_12)
'''

'''sorted排序'''
# list_1 = [(23,'dsfdsf'),(32,'ewrwerqwe'),(123,'we'),(435,'dfsewqqqq'),(2,'lkjsdasew2323')]
# value = sorted(list_1,key=lambda x:x[0])   # 按照数字大小排序
# print(value)
# value = sorted(list_1,key=lambda x : len(x[1])) # 按照字符串长度排序，从少到多
# print(value)
# value = sorted(list_1,key=lambda x:len(x[1]),reverse=True) # 按照字符串长度排序，从多到少
# print(value)


# 练习
# 找到class对应的值来排序
# list_9=[{'name':'xiaoli','sex':'boy','class':18},{'name':'xiaoliu','sex':'girl','class':17},
#         {'name':'xiaochen','sex':'boy','class':11},{'name':'xiaowu','sex':'boy','class':10}]
# value = sorted(list_9,key=lambda x: x.get('class'))
# print(value)

'''过滤---filter'''
# a = [1, 2, 14, 6, 7, 8]
# value = list(filter(lambda x: x % 2 == 0, a))
# print(value)
#
# value = list(filter(lambda x:x%3 == 0 and x%2==0,range(1,100)))
# print(value)

# 练习
list_11 = [1,2,'xiaochen',45 ,'45',34,'admin',True,14]
value = list(filter(lambda x : type(x)==int and x%2 == 0,list_11))
print(value)