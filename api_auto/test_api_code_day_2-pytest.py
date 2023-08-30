# -*- coding: utf-8 -*-
"""
@Time:2023/8/29 16:02
@Auth:kirosbaby
@QQ:308902181
"""
import pytest

'''pytest单元测试框架--第三方
1、有丰富的执行指令
2、执行顺序根据用例的先后
3、类名Test  函数名test 方法名test 模块名test  开头
4、pytest可以执行unittest
5、：：冒号代表层级关系
6、方法(用例)级别的初始化和结束方法setup/teardown
7、类级别的初始化和结束方法setup_class/teardown_class
8、函数级别的初始化和结束方法setup_function/teardown_function
9、模块级别的初始化和结束方法setup_module/teardown_module
'''

def setup_module():
    print('模块级别---打开浏览器')
def teardown_module():
    print('模块级别---关闭浏览器')
# def setup_function():
#     print('函数级别---打开浏览器')
# def teardown_function():
#     print('函数级别---关闭浏览器')
@pytest.mark.p0
def test_open_func1():
    print('这是函数test_open_func1')
@pytest.mark.p0
def test_close_func2():
    print('这是函数test_close_func2')

class Test_lei1():
    # def setup(self):
    #     print('用例级别---打开浏览器')
    # def teardown(self):
    #     print('用例级别---关闭浏览器')
    def setup_class(self):
        print('类级别---打开浏览器')
    def teardown_class(self):
        print('类级别---关闭浏览器')
    @pytest.mark.p0
    @pytest.mark.flaky(reruns=3,reruns_delay=2) # reruns -- 重跑次数
    def test_login_003(self):
        print('这是方法test_login_003')
        assert 1 == 1
    @pytest.mark.p1
    def test_login_add_001(self):
        print('这是方法test_login_add_001')
    @pytest.mark.p1
    def test_add_002(self):
        print('这是方法test_add_002')

class Test_lei2():
    @pytest.mark.p0
    def test_open_001(self):
        print('这是方法test_open_001')

if __name__ == '__main__':
    # pytest.main(['-v',r'D:\class_project\study_kiros_0814\api_auto\test_api_code_day_2-pytest.py::test_func1'])
    # -s 详细打印输出---在控制台
    # pytest.main(['-vs',r'D:\class_project\study_kiros_0814\api_auto\test_api_code_day_2-pytest.py'])
    # -k 指定用例名称
    # pytest.main(['-vsk','login and add or open',r'D:\class_project\study_kiros_0814\api_auto\test_api_code_day_2-pytest.py'])
    # -m 通过装饰器标记执行用例
    # pytest.main(['-vsm','p1',r'D:\class_project\study_kiros_0814\api_auto\test_api_code_day_2-pytest.py'])
    # -x 遇到错误时停止测试
    # pytest.main(['-vsx',r'D:\class_project\study_kiros_0814\api_auto\test_api_code_day_2-pytest.py'])
    # pytest.main(['-vsx','--maxfail=3',r'D:\class_project\study_kiros_0814\api_auto\test_api_code_day_2-pytest.py'])

    # @pytest.mark.flaky 失败重跑
    pytest.main(['-vsx',r'D:\class_project\study_kiros_0814\api_auto\test_api_code_day_2-pytest.py'])
