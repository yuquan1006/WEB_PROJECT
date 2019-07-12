#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
import common.HTMLTestRunnerCN as HTMLTestRunner
import unittest, os
from common.emailUtil import EmailUtil

def all_tests(casename = "case" ,rule="test*.py"):
    curPath = os.path.realpath(__file__)
    parPath = os.path.dirname(curPath)
    rePath = os.path.join(parPath,casename)
    print(rePath)
    discover = unittest.defaultTestLoader.discover(rePath, pattern=rule)
    return discover

def run(discover):
    reportPath = os.path.join(os.path.dirname(os.path.realpath(__file__)),"report")
    if not os.path.exists(reportPath):
        os.mkdir(reportPath)
    report_abspath = os.path.join(reportPath,"result.html")

    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                              verbosity=2,
                                              title=u'自动化测试报告,测试结果如下：',
                                              description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(discover)
    fp.close()
    print("测试报告生成成功在：%s" % report_abspath)
    return report_abspath




if __name__ == '__main__':
    a = all_tests()
    print(a)
    path = run(a)
    # e = EmailUtil(path)
    # e.sendEmail()

