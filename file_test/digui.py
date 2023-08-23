# -*- coding: utf-8 -*-
"""
@Time:2023/8/19 10:17
@Auth:kirosbaby
@QQ:308902181
"""

import sys,time
sys.setrecursionlimit(100000)

def digui(num=0):
    num+=1
    time.sleep(0.00001)
    print('我是朱晓明',num)
    digui(num)
digui()
