# -*- coding: utf-8 -*-
"""
@Time:2023/8/24 14:11
@Auth:kirosbaby
@QQ:308902181
"""
import unittest

'''
unittest----
1.有很多类，TestCase,TestLoader
2.继承TestCase,批量执行用
3.方法名为test开头
4.执行顺序根据ascii
5.用例级别的初始化结束方法setUp/tearDown
6.类级别的初始化和结束方法setUpClass/tearDownClass
'''

'''
class Test_unit(unittest.TestCase):
    # def setUp(self) -> None:
    #     print('打开浏览器')
    #
    # def tearDown(self) -> None:
    #     print('关闭浏览器')
    @classmethod
    def setUpClass(cls) -> None:
        print('打开浏览器')

    @classmethod
    def tearDownClass(cls) -> None:
        print('关闭浏览器')

    def test_001(self):
        print('这是test 001')
        # self.assertEqual('admin', 'admin', msg='断言失败，内容不相等')  # 断言内容相等

    def test_003(self):
        print('这是test 003')
        # self.assertIn('admin1', 'admin', msg='断言失败，内容不存在包含关系')

    def test_002(self):
        print('这是test 002')
        self.assertNotIn('admin1', 'admin', msg='断言失败,内容存在包含关系')  # 判断内容不存在包含关系

    def test_aa(self):
        print('这是te aa')
        # self.assertNotEqual('admin', 'admin', msg='断言失败，内容相等')  # 判断内容不相等


class Test_te01(unittest.TestCase):
    def test_ysq(self):
        print('这是 ysq')


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 一般用来调试
    # testload = unittest.TestLoader()  # 加载用例
    # value = testload.discover(r'D:\class_project\study_kiros_0814\ui_test_code', pattern='ui_test_day3_*.py')
    # runner = unittest.TextTestRunner(verbosity=2)  # 实例化执行用例的类
    # runner.run(value)
'''


