#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
import logging
import os,time
import config.globalConfig as gc
from logging.handlers import TimedRotatingFileHandler

class Logger:
    '''
    配置loggin
    '''
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        log_file_path = gc.logName
        #日志保留十天时间，一天保存一个日志
        self.handler1 = TimedRotatingFileHandler(log_file_path,"d",1,10)

        self.handler1 = logging.FileHandler(log_file_path, mode="a", encoding="utf-8") # 打印到文件
        self.handler2 = logging.StreamHandler() # 打印到终端

        self.formmater1=logging.Formatter('%(asctime)s - %(name)s - 【%(levelname)s】 -%(module)s:  %(message)s', datefmt='%Y-%m-%d %H:%M:%S %p',)
        self.formmater2=logging.Formatter('%(asctime)s - 【%(levelname)s】 -%(module)s:  %(message)s', datefmt='%Y-%m-%d %H:%M:%S %p',)

        self.handler1.setFormatter(self.formmater1)
        self.handler2.setFormatter(self.formmater2)

        self.logger.addHandler(self.handler1)
        self.logger.addHandler(self.handler2)
        self.logger.setLevel(10)

    def info(self, msg=None):
        self.logger.info(msg)

    def debug(self, msg=None):
        self.logger.debug(msg)

    def error(self, msg=None):
        self.logger.error(msg)

    def fatal(self, msg=None):
        self.logger.fatal(msg)

    def warn(self, msg=None):
        self.logger.warning(msg)

if __name__ == '__main__':
    log = Logger("main")
    log.info("测试通过")
    log.warn("测试通过")