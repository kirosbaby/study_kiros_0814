# -*- coding: utf-8 -*-
"""
@Time:2023/8/15 9:57
@Auth:Dali
@QQ:1334029448
"""
'''写一个程序判断一个数字是不是回文数，回文数的概念：如12321，倒过来还是12321'''

# a=input('输入:')
# if a==a[::-1] and len(a)>=2:
#     print('是回文数')
# else:
#     print('不是回文数')

# import random  #导入random模块
# pass_num = random.randint(1, 100)
#
# cishu=1
# while cishu<=10:
#     pass_1=int(input('猜数字:'))
#     if pass_1>0 and pass_1<100:
#         if pass_1>pass_num:
#             print('太大了','剩余机会：',10-cishu)
#             cishu +=1
#         elif pass_1<pass_num:
#             print('太小了','剩余机会：',10-cishu)
#             cishu += 1
#         else:
#             print('中奖了')
#             break


# import random  # 导入random模块
# pass_num = random.randint(1, 100)
#
# i = 10
# while i > 0:
#     input11 = int(input())
#     if input11 == pass_num:
#         print("恭喜你猜对了！")
#         break
#     elif input11 < pass_num:
#         print(f"太小了！你还有{i}次机会")
#     elif input11 >pass_num:
#         print(f"太大了！你还有{i}次机会")
#     i -= 1
# print(pass_num)


'''# 3、# 有一个url："https://baidu.com?username=admin&password=123456&sex=GG&from=China"，
# 将url中所有参数值取出并装在一个列表中，如['admin', '123456', 'GG', 'China']'''
# urls = 'https://baidu.com?username=admin&password=123456&sex=GG&from=China'
# urls_params= urls.split('?')[1].split('&')
# print(urls_params)
# params = []
# for i in urls_params:
#     index=i.index('=')
#     print(index)
#     params.append(i[index+1:])
# print(params)
#
# str_1 ="https://baidu.com?username=admin&password=123456&sex=GG&from=China"
# list_55 =[]
# url_1 = str_1.split('?')[1].split('&')
# print(url_1)
# for i in url_1:
#     print(i.split('='))
#     list_55.append(i.split('=')[1])
# print(list_55)

# list_9=['aaab', 'W', 'aaab','XiaohuE','W', 'aaaa', 'TY', 'XIO','W','aaaa']
#
# list_1 = [1, 1, 2, 3, 4, 3, 2, 5]
# list_2 = list(set(list_1))
# print(list_2)


# 6、有一个列表：['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'rongqi', 'niuba']，
# 将其中所有姓名以'z'开头的添加到另一个列表中，并将其全部大写
# a=['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'rongqi', 'niuba']
# b=[]
# for i in a:
#      if i[0] in 'z':
#          b.append(i.upper())
# print(b)
