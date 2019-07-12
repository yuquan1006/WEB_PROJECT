#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
from BeautifulReport import BeautifulReport
import unittest, os
from common.emailUtil import EmailUtil

class RunALL(object):
    def __new__(cls, *args, **kwargs):
        '''单例模式'''
        if not (hasattr(cls, "_instance")):
            orign = super(RunALL, cls)
            cls._instance = orign.__new__(cls, *args, **kwargs)
        return cls._instance



    def all_tests(self,casename="case\zentao", rule="test*.py"):
        curPath = os.path.realpath(__file__)
        parPath = os.path.dirname(curPath)
        rePath = os.path.join(parPath, casename)
        print(rePath)
        discover = unittest.defaultTestLoader.discover(rePath, pattern=rule)
        return discover

    def run(self,discover):
        reportPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),"report")
        if not os.path.exists(reportPath):
            os.mkdir(reportPath)
        # fp = open(report_abspath, "wb")
        runner = BeautifulReport(discover).report(filename='测试报告', description='测试deafult报告', log_path=reportPath)
        reportPath = reportPath+"\测试报告.html"
        # 调用add_case函数返回值
        # runner.run(discover)
        # fp.close()
        print("测试报告生成成功在：%s" % reportPath)
        return reportPath




if __name__ == '__main__':
    r = RunALL()
    discover = r.all_tests()
    r.run(discover)
    # e = EmailUtil(path)
    # e.sendEmail()

