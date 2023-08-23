# -*- coding: utf-8 -*-
"""
@Time:2023/8/14 17:59
@Auth:gongkewei
@QQ:3295908828
"""
# 1、写一个程序判断一个数字是不是回文数，回文数的概念：如12321，倒过来还是12321
# aaa = str(input())
# bbb ='12321'
# aaa = bbb[::-1]
# print(aaa)
# if aaa == aaa[::-1] and len(aaa) >= 2:
#     print("是回文数！")
# else:
#     print("不是回文数！")

# 3、写一个猜谜游戏，先定义好一个数，程序开始运行后总共有十次机会猜，猜对了则提示中奖了并结束程序，猜错了则提示太大了或太小了并给出剩余次数
# 生成随机数的方法：比如1~100随机
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

# 3、# 有一个url："https://baidu.com?username=admin&password=123456&sex=GG&from=China"，
# 将url中所有参数值取出并装在一个列表中，如['admin', '123456', 'GG', 'China']
str_1 ="https://baidu.com?username=admin&password=123456&sex=GG&from=China"
list_55 =[]
url_1 = str_1.split('?')[1].split('&')
print(url_1)
for i in url_1:
    list_55.append(i.split('=')[1])
print(list_55)


# 4、 删除该列表重复的元素
# list_9=['aaab', 'W', 'aaab','XiaohuE','W', 'aaaa', 'TY', 'XIO','W','aaaa']


# 4、 列表去重
'''
list_1 = [1, 1, 2, 3, 4, 3, 2, 5]
list_2 = set(list_1)
list_3 = []
print(list_2)

for i in list_1:
    if i not in list_3:
        list_3.append(i)
print(list_3)
'''

# 5、有一个列表：['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'rongqi', 'niuba']，
# 将其中所有姓名以'z'开头的添加到另一个列表中，并将其全部大写
#
# list_22 =['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'rongqi', 'niuba']
# list_33 =[]
# for i in list_22:
#     if i[0] == 'z':
#         list_33.append(i.capitalize())
# print(list_33)
