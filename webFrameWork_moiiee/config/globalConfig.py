#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
import os,time

curPath = os.path.realpath(__file__)
parPath = os.path.dirname(curPath)
projectPath = os.path.dirname(parPath)

# 截图保存路径
screenPath = os.path.join(projectPath, "screenshots")
if not os.path.exists(screenPath):
    os.mkdir(screenPath)
nowtime = time.strftime("%Y%m%d_%H_%M_%S", time.localtime())
screenName = os.path.join(screenPath, "%s.png" % nowtime)


# borwser.ini文件路径
bsConfing = os.path.join(projectPath, "config", "browser.ini")


# email参数
sender = '1251523660@qq.com'
passwd = "ykbpqkpfxsdxgbjg"
host = "smtp.qq.com"
port = 465
receiver = ["1251523660@qq.com", "1311766437@qq.com"]
cc = "985687042@qq.com"
subject = "邮件主题"
contents = "UI自动化测试报告邮件已发送，详情请查看附件。"
# attachments = r'%s' % reportPath
reportPath = os.path.join(projectPath, "report", "result.html")
off = 1  # 发送开关



# logger参数
logPath = os.path.join(projectPath, "report","log")
if not os.path.exists(logPath):
    os.mkdir(logPath)
logName = os.path.join(logPath,"out.log")

# excek文件路径
login_testdata = os.path.join(projectPath, "data")
if not os.path.exists(login_testdata):
    os.mkdir(login_testdata)
login_testdata =os.path.join(login_testdata, "login_testdata.xls")
login_sheet = "Sheet1"



if __name__ == '__main__':
    # print(logName)
    # print(login_testdata)
    import time

    nowtime = time.strftime("%Y%m%d_%H_%M_%S", time.localtime())
    print(screenName)