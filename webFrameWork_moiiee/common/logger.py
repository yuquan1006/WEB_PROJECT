#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 15:50
# @Author  : Yuquan
# @Site    :
# @File    : logUtil.py
# @Software: PyCharm
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
import logging
import os,time
from logging.handlers import TimedRotatingFileHandler

# 日志级别
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0


# 日志路径
curPath = os.path.realpath(__file__)
projectPath = os.path.dirname(os.path.dirname(curPath))
logPath = os.path.join(projectPath, "report","log")
if not os.path.exists(logPath):
    os.mkdir(logPath)


class LogHandler(logging.Logger):
    '''
    配置loggin
    '''
    def __init__(self,name='main',level=INFO, stream=True, file=True):
        self.name = name
        self.level = level
        logging.Logger.__init__(self, self.name, level=level)
        if stream:
            self.set_stream_handler()
        if file:
            self.set_file_handler()

    def set_file_handler(self,lever=None):
        file_name = os.path.join(logPath,'{name}.log'.format(name=self.name))
        # 设置日志回滚, 保存在log目录, 一天保存一个文件, 保留15天
        self.file_handler = TimedRotatingFileHandler(filename=file_name, when='D', interval=1,backupCount=15, encoding='utf-8')
        if not lever:
            self.file_handler.setLevel(self.level)
        else:
            self.file_handler.setLevel(lever)
        # 设置日志格式
        formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        self.file_handler.setFormatter(formatter)

        #
        self.addHandler(self.file_handler)

    def set_stream_handler(self,lever=None):
        self.stream_handle = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
        self.stream_handle.setFormatter(formatter)
        if not lever:
            self.stream_handle.setLevel(self.level)
        else:
            self.stream_handle.setLevel(lever)
        self.addHandler(self.stream_handle)



if __name__ == '__main__':
    logger = LogHandler('logUtil',10)
    logger.info("ddd")



