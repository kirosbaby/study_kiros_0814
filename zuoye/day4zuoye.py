# -*- coding: utf-8 -*-
"""
@Time:2023/8/15 17:53
@Auth:gongkewei
@QQ:3295908828
"""


# 1.输入三个整数 a, b,c 分别作为三角形的三边边长。通过程序判定所构成的三角形的类型，
# 当此三角形为一般三角形，等腰三角形，等边三角型，直角三角形时，分别做打印操作，其他情况下输出错误提示。
# 判断三角形类型
def sj(a, b, c):
    ls = sorted([a, b, c])
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            print("这是一个等边三角形")
        elif a == b or b == c or a == c:
            print("这是一个等腰三角形")
        elif ls[0] ** 2 + ls[1] ** 2 == ls[-1] ** 2:
            print("这是一个直角三角形")
        else:
            print("这是一个一般三角形")
    else:
        print("这不是一个有效的三角形")


sj(1, 3, 34)

# 2# 有一个url："https://baidu.com?username=admin&password=123456&sex=GG&from=China"，
# 将url中所有参数值取出并装在字典里，如{'username':'admin', 'password':'123456', 'sex':'GG', 'from':'China'}

url = "https://baidu.com?username=admin&password=123456&sex=GG&from=China"
dict_url = {}
url_1 = url.split("?")[1].split('&')
for i in url_1:
    dict_url.setdefault(i.split('=')[0], i.split('=')[1])
print(dict_url)


# 3、# 冒泡排序list_1=[34,4,2,45,6,9,11](百度了解冒泡排序,然后结合for循环编写)#选做
# list_1 = [34, 4, 2, 45, 6, 9, 11]
# print(len(list_1))
# for i in range(len(list_1)):  # 根据列表元素设置循环次数
#     print(i)
#     for j in range(len(list_1)-1):
#         print(j)
#         if j > i:
#             print(j)

# 4、一个球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第4次落地时，这个期间共经过多少米？第4次反弹多高？


# 5、定义函数 输入参数，判断这个数可以整除3并且自身为偶数。
def nb(num_1):
    if num_1 % 3 == 0 and num_1 % 2 == 0:
        # str_1 = '我可以整除3，并且是偶数！
        print('可以整除3,且是偶数')
    else:
        print('不能整除')


nb(96)

# 6、了解ascii gbk,utf-8（https://blog.csdn.net/longwen_zhi/article/details/79704687）
