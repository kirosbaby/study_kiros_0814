# -*- coding: utf-8 -*-
"""
@Time:2023/8/14 9:50
@Auth:kiros
@QQ:3295908828
"""

# dict_1 = {'admin':'ysq','pwd':'123456'}
# print(dir(dict_1))
# dict_1.clear() # 清空
# print(dict_1.items()) #拆包
# print(dict_1.fromkeys('2', 'a67'))
# print(dict_1)
#
# tup1 = (123,222,234,211,456,123,123)
# print(tup1.index(123))  # 取索引位置
# print(tup1.count(123)) # 统计元素出现的次数

# set1 = {123,123,456,234,123,432}
# print(dir(set1))

# num =101
# while num > 0:
#     num -= 1
#     if num%3 == 0 or '3' in str(num):
#         continue
#     print(num)




# for i in range(100,0,-1):
#     if i%7==0 or '7' in str(i):
#         # continue
#         print('过')
#     else:
#         print(i)

# class Atest():
#     def __init__(self,name):
#         self.name = name #实例属性——实例变量
#     def test_1(self):
#         print(self.name,'test方法')
# if __name__ == '__main__':
#     test70 = Atest('小李') # 实例化类--实例对象
#     test70.test_1()
#     test70 = Atest('小杨')  # 实例化类--实例对象
#     test70.test_1()

# def wai(name):
#     def aa(func):
#         def inner(num):
#             print('闭包1',name)
#             func(num)
#             print('闭包2',name)
#         return inner
#     return aa
# @wai('xiaoyang')
# def func_1(num):
#     print('打印结果')
# func_1('12345')
#
# f = lambda x,y:x*y
# print(f(3,9))
# f1 = lambda x,y:[i for i in range(x,y)]
# print(f1(1,77))

# list_11 = [12,3,23,4,2]
# value = list(map(lambda x:x*2,list_11))
# print(value)
#
# list_12 = [234,321,21,32,3,123,1231,32]
# list_13 = [22,34,323,12,23,23,123,321]
# value = list(map(lambda x,y:x+y,list_12,list_13))
# print(value)
#
# tuple_1 = (223,23,4,3132,1223,123,2)
# value=sorted(tuple_1)
# print(value)

# tuple_2 = ((223,23,4),(3132,1223,123),(2,45,23))
# value = sorted(tuple_2,key=lambda x:x[1])
# print(value)

list_13 = [1,23,4,5,6,8,9,19,654,3,2,66]
value = list((filter(lambda x:x%2 == 0,list_13)))
print(value)