# -*- coding: utf-8 -*-
"""
@Time:2023/8/24 14:11
@Auth:kirosbaby
@QQ:308902181
"""
import unittest

'''
unittest----
1.有很多类，TestCase
2.继承TestCase,批量执行用
3.方法名为test开头
4.执行顺序根据ascii
'''


class Test_unit_70(unittest.TestCase):
    def test_001_70(self):
        print('这是test 001_70')

    def test_003_70(self):
        print('这是test 003_70')

    def test_002_70(self):
        print('这是test 002_70')

    def test_aa_70(self):
        print('这是te aa_70')


if __name__ == '__main__':
    unittest.main(verbosity=2)
