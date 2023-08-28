# -*- coding: utf-8 -*-
"""
@Time:2023/8/28 10:15
@Auth:kirosbaby
@QQ:308902181
"""

import logging

logger = logging.getLogger()  # 获取日志--日志记录器
file_hand = logging.FileHandler(r'D:\class_project\study_kiros_0814\class_kiros_ui_code_frame\log\test.log', 'a',
                                encoding='utf-8')
stream_hand = logging.StreamHandler()
formtter = logging.Formatter('%(asctime)s-%(filename)s-[line:%(lineno)d]-%(levelname)s-%(module)s-%(message)s')  # 格式化输出

# logger.setLevel(10) # 设置日志等级
logger.setLevel('ERROR')

file_hand.setFormatter(formtter)  # 写入的日志--设置格式
logger.addHandler(file_hand)  # 把日志写入的文件位置，添加到记录器

stream_hand.setFormatter(formtter)  # 绑定格式化输出
logger.addHandler(stream_hand)

logging.debug('调用日志')  # 级别10
logging.info('正常消息日志')  # 20
logging.warning('警告--日志')  # 30
logging.error('错误xxx日志')  # 40
logging.critical('严重---错误')  # 50
