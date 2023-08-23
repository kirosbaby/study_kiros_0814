# -*- coding: utf-8 -*-
"""
@Time:2023/8/16 9:51
@Auth:Dali
@QQ:1334029448
"""
# 1.输入三个整数 a, b,c 分别作为三角形的三边边长。通过程序判定所构成的三角形的类型，
# 当此三角形为一般三角形，等腰三角形，等边三角型，直角三角形时，分别做打印操作，其他情况下输出错误提示。
# 判断三角形类型
# def sj(a, b, c):
#     ls = sorted([a, b, c])
#     if a + b > c and a + c > b and b + c > a:
#         if a == b and b == c:
#             print("这是一个等边三角形")
#         elif a == b or b == c or a == c:
#             print("这是一个等腰三角形")
#         elif ls[0] ** 2 + ls[1] ** 2 == ls[-1] ** 2:
#             print("这是一个直角三角形")
#         else:
#             print("这是一个一般三角形")
#     else:
#         print("这不是一个有效的三角形")
# sj(1, 3, 34)


# a = int(input('第一条'))
# b = int(input('第二条'))
# c = int(input('第三条'))
# if a==b==c:
#     print('三角形为等边三角形')
# elif a==b or a==c or b==c:
#     print('三角形为等腰三角形')
# elif a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2:
#     print('三角形为直角三角形')
# else:
#     print('三角形为一般三角形')



# a=int (input('请输入第1个数字：'))
# b=int (input('请输入第2个数字：'))
# c=int (input('请输入第3个数字：'))
# if (a<=0 or b<=0 or c<=0):
#     print('三角形的边必须大于0')
# elif a==b==c:
#     print('这是个等边三角形')
# elif a==b or b==c or c==a:
#     print('这是个等腰三角形')
# elif a**2+b**2==c**2:
#     print('这个是直角三角形')
# elif a + b > c and b + c > a and c + a > b:
#     print('这是普通三角形')
# else:
#     print('这是个数无法组成三角形')


# 2# 有一个url："https://baidu.com?username=admin&password=123456&sex=GG&from=China"，
# # 将url中所有参数值取出并装在字典里，如{'username':'admin', 'password':'123456', 'sex':'GG', 'from':'China'}

from urllib.parse import urlparse, parse_qs
url_1="https://baidu.com?username=admin&password=123456&sex=GG&from=China"
parsed_url_1= urlparse(url_1)
# print(parsed_url_1)
params = parse_qs(parsed_url_1.query)
print(params)
params_dict = {key: value[0] for key, value in params.items()}
print(params_dict)

url = "https://baidu.com?username=admin&password=123456&sex=GG&from=China"
dict_url = {}
url_1 = url.split("?")[1].split('&')
print(url_1)
for i in url_1:
    dict_url.setdefault(i.split('=')[0], i.split('=')[1])
print(dict_url)


# 3、# 冒泡排序list_1=[34,4,2,45,6,9,11](百度了解冒泡排序,然后结合for循环编写)#选做
list_1=[9,34,4,45,6,2,11]
# n=len(list_1)
# for i in range(n):
#     for j in range(n-i-1):
#         if list_1[j]>list_1[j+1]:
#             list_1[j],list_1[j+1]=list_1[j+1],list_1[j]
# print(list_1)

# for i in range(len(list_1)-1):
#     for j in range(len(list_1)-1-i):
#         if list_1[j]>list_1[j+1]:
#             list_1[j],list_1[j+1]=list_1[j+1],list_1[j]
# print(list_1)


#4、一个球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第4次落地时，这个期间共经过多少米？第4次反弹多高？
gaodu=100
ftgd=gaodu/2
for i in range(2,5):
    gaodu=gaodu+2*ftgd
    ftgd=ftgd/2
print('第4次落地共进过：',gaodu,'米')
print('第4次反弹',ftgd,'米高')


# h=100
# sumh=0
# i=1
# while i<=4:
#     if i==1:
#         sumh+=h
#     else:
#         h=h/2
#         sumh+=2*h
#     i+=1
# print('%f,%f'%(sumh,h/2))


print(chr(97))
print(chr(122))
print(ord('a'))
print(ord('A'))