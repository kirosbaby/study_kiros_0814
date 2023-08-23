# -*- coding: utf-8 -*-
"""
@Time:2023/8/18 9:38
@Auth:kirosbaby
@QQ:308902181
"""

'''面向对象'''
'''类--class--类名首字母大写'''

'''
class Test_House():
#     def __init__(self):
#         print('构造函数--初始化函数')
#
#     def level(self):
#         print('三层小洋房')
#
#
# if __name__ == '__main__':
#     test_house = Test_House()  # 实例化--把类实例化成为一个对象
#     test_house.level()

# class FushiK():
#     def __init__(self, color, xh, cpu, memory, chicun):  # 初始化存放实例对象属性---实例化之后
#         self.color = color
#         self.cpu = cpu
#         self.memory = memory
#         self.chicun = chicun
#         self.XH = xh
#
#     def call(self, name):  # self---指向对象本身--把对象作为参数传入
#         print(
#             f'{name}用{self.XH}{self.color}{self.cpu}核心{self.memory}G内存{self.chicun}屏幕在跟ta打电话，还可以放外音')
#
#     def game(self, name):
#         self.name = name
#         print(f'用{self.color}和{name}打游戏')
#
#     def video(self,action):
#         print(f'{self.cpu}和{self.name}看视频{action}')
#
#
# if __name__ == '__main__':
#     iphone11 = FushiK('土豪金', 'IPHONE11', 8, 64, 8.9)  # 实例化对象
#     iphone11.call('八戒')
#     iphone11.game('沙僧')
#     iphone11.video('有点卡')
#
#     iphone15 = FushiK('樱花粉', 'IPHONE15', 16, 128, 6.7)
#     iphone15.call('悟空')
#     iphone15.game('唐僧')
#     iphone15.video('不卡的')
'''

'''# class Test_Cms():
#     def __init__(self):
#         print('这是初始化方法')
#
#     def test1(self):
#         print('这是实例方法')
#
#     @classmethod  # 装饰器
#     def test2(cls):  # 被装饰的方法
#         print('这是类方法')
#
#     @staticmethod
#     def test3():  # 一个函数
#         print('这是静态方法')
#
#     def __test4(self):
#         print('这是私有方法')
#
#     def test5(self):
#         self.__test4()


# if __name__ == '__main__':
#     cms = Test_Cms()
# cms.test1()  # 实例对象能调用实例方法
# cms.test2()  # 实例对象能调用类方法
# cms.test3()  # 实例对象能调用静态方法

# Test_Cms.test1(cms)  # 类不能直接调用实例方法
# Test_Cms.test2() # 类能调用类方法
# Test_Cms.test3() # 类能调用静态方法

# cms.__test4()  # 实例对象无法在外面调用私有方法
# cms.test5() # 触发私有方法
# def di():
#     print('找对象')
# aa1 = di # 引用
# aa1()
'''

'''三大特性---封装'''
'''
import requests


class Test_Cms_Api():
    def __init__(self):
        self.url = 'http://192.168.31.44:8080/'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        self.login_body = {
            'userAccount': 'admin',
            'loginPwd': '123456'
        }

    def login(self):
        resp = requests.post(url=self.url + 'cms/manage/loginJump.do', data=self.login_body, headers=self.header)
        print(resp.json())
        self.cookie = resp.cookies  # 获取cookie

    def query(self):
        resp = requests.post(url=self.url + 'cms/manage/queryUserList.do', data=self.login_body, headers=self.header,cookies=self.cookie)
        print(resp.json())


if __name__ == '__main__':
    cms = Test_Cms_Api()
    cms.login()
    cms.query()'''

'''
继承
父类（基类-超类）---子类（派生类）
object---是所有类的父类
'''

'''
class Father_Lw():
    def Smoke(self):
        print('抽华子')

    def Run(self):
        print('跑马拉松')


class Mother_Wt(Father_Lw):
    def __init__(self,name1):
        self.name1 = name1

    def Square_danc(self):
        print('每天晚上六点半，楼下广场舞')

    def Shop(self, xmb):
        print(f'买买买---{xmb}--买买买')

    def Smoke(self,brand):
        print(f'{self.name1}{brand}电子烟')


class Son_Xw(Mother_Wt):  # 继承父类---单继承--多继承
    def __init__(self, name,name1):
        self.name = name
        super().__init__(name1)  # 重新调用父类的构造函数

    def Game(self):
        print(f'{self.name}最近收购了EDM')

    def Smoke(self,brand):  # 子类和父类方法一样的时候---重写父类方法（用子类方法）
        print(f'{self.name}抽雪茄---老烟枪---水烟')
        Father_Lw.Smoke(self)  # 重新调用父类方法
        super().Smoke(brand)  # 重新调用父类方法---最近


if __name__ == '__main__':
    sonxw = Son_Xw('小王','王太太爱抽')
    sonxw.Game()
    sonxw.Smoke('悦刻')  # 按照继承顺序取值
    sonxw.Run()
    sonxw.Shop('买大炮')
    sonxw.Square_danc()
'''

'''多态---不同对象，调用同一个方法，有不同结果或行为让代码调用更加灵活'''

'''
class Animal():
    def call(self):
        print('发出声音')


class Dog(Animal):
    def call(self):
        print('旺旺旺')


class Cat(Animal):
    def call(self):
        print('喵喵喵')


class Sheep(Animal):
    def call(self):
        print('咩咩咩')


def jiao(obj):
    obj().call()
    # obj.call()



if __name__ == '__main__':
    jiao(Dog)
    jiao(Cat)
# jiao(Cat())
'''

'''
try:
    with open('D:\class_0814\study', 'r') as file_r:
        vlaue = file_r.read()
        print(vlaue)

# except OSError:  # 抛出指定异常
#     print('运行遇到麻烦')
# except FileNotFoundError:
#     print('文件不存在')
# except ValueError:
#     print('文件不存在')

except Exception as e:   # 任意捕获异常
    print(e)
print('关闭文件')
'''

