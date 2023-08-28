# -*- coding: utf-8 -*-
"""
@Time ： 2021/6/17 8:37
@Auth ： Dali
@QQ ：1334029448
@WeChat ：A13420113351T
"""
import logging,time
from conf.config import get_path
#日志存放的路径
# print(get_path('log',f'{time.strftime("%Y_%m_%d")}_test.log'))

class Logger():
    def __init__(self):
        #写入的日志文件的路径
        self.log=get_path('log',f'{time.strftime("%Y_%m_%d")}_test.log')
        self.format = '%(asctime)s-%(levelname)s-%(module)s-%(message)s'

    def logger(self):
        #设置日志输出格式
        formatter = logging.Formatter(self.format)
        #设置控制台日志
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        #设置文件日志
        file_handler = logging.FileHandler(filename=self.log, encoding='utf-8')
        file_handler.setFormatter(formatter)
        # file_handler.setLevel(logging.INFO)
        loggers=logging.getLogger()
        loggers.addHandler(console)
        loggers.addHandler(file_handler)

        loggers.setLevel("INFO")
        return loggers

log = Logger().logger()

def trace_log(func):
    def wrapper(*args):
        log.info(f'Function:{func.__name__}, args:{args}')
        result = func(*args)
        log.info('Function:{}, Result: {}'.format(func.__name__, result))
        return result
    return wrapper


if __name__ =='__main__':
    # """调试代码"""
    @trace_log
    def add1(a, b):
        return a + b
    add1(12, 10)


    # def waibu(func):
    #     def neibu(*args):
    #         print(*args)
    #         value=func(*args)
    #         print(value)
    #     return neibu
    #
    #
    # @waibu
    # def add(a, b):
    #     return a+b
    # add(1, 10)
    #
    #
    # @waibu
    # def add1(a, b):
    #     return a + b
    # add1(12111, 10)