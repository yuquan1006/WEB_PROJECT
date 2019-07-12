#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 15:19
# @Author  : Yuquan
# @Site    : 
# @File    : emailUtil.py
# @Software: PyCharm
import yagmail
import config.globalConfig as gc
class EmailUtil(object):

    def __init__(self, reportPath = gc.reportPath):
        self.sender = gc.sender
        self.passwd = gc.passwd
        self.host = gc.host
        self.port = gc.port
        self.receiver = gc.receiver
        self.cc = gc.cc
        self.subject = gc.subject
        self.contents = gc.contents
        self.attachments = r'%s' % reportPath
        self.off = gc.off        # 发送开关
    def sendEmail(self):
        if self.off == 1:
            try:
                yag = yagmail.SMTP(self.sender, self.passwd, self.host, self.port)
                yag.send(to=self.receiver, subject=self.subject, contents=self.contents, cc=self.cc, attachments=self.attachments)
                yag.close()
                print("发送邮件成功！")
            except BaseException as e:
                print("发送邮件失败！可能出现错误的原因：%s" % e)
        else:
            print("当前选择不发送邮件！")
if __name__ == '__main__':
    a = EmailUtil()
    a.sendEmail()
