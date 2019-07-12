#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
from common.base import Base
# from webframework.page.pageElements.login_Element import *
from common.logger import Logger
log = Logger("LoginPageOperation")
class LoginPageOperation(Base):


    # 打开登录页面
    def openLoginUrl(self, loc_loginUrl):
        self.openUrl(loc_loginUrl)
        log.debug("< 打开登录页面 %s>" % loc_loginUrl)
        # print("打开登录页面 %s" % loc_loginUrl)
    # 输入用户名
    def inputUserName(self, loc_userBox, name):
        self.send(loc_userBox, name)
        log.debug("< 输入登录用户名:%s >" % name)
        # print("<输入用户名>:%s" % name)

    # 输入密码
    def inputPassWord(self, loc_passwdBox, password):
        self.send(loc_passwdBox, password)
        # print("密码:%s" % password)
        log.debug("< 输入登录密码:%s >" % password)


    #点击登录按钮
    def clickLoginButton(self, loc_loginButton):
        self.click(loc_loginButton)
        # print("点击登录按钮")
        log.debug("< 点击登录按钮 >")

    #点击保持登录按钮
    def clickKeepButton(self, loc_keepRedio):
        self.click(loc_keepRedio)
        # print("点击保持登录按钮")
        log.debug("< 点击保持登录按钮 >")

    # 点击忘记按钮
    def clickForgetButton(self, loc_forgetButton):
        self.click(loc_forgetButton)
        log.debug("< 点击忘记密码按钮 >")
        # print("点击忘记密码按钮")

    # 登录断言
    def verifyUserName(self, loc_verifyUserName):
        result = self.is_element_exsit(loc_verifyUserName)
        # print("获取首页用户名元素是否存在：%s" % result)
        log.debug("< 登录断言结果：%s >" % result)
        return result

    # 获取提示弹框信息
    def getPromptInformation(self):
        text = self.getAlertText()
       # print("< 登录页面弹框文本信息:%s >" % text)
        log.debug("< 登录页面弹框文本信息:%s >" % text)
        return text

    # 关闭弹框
    def closePromptInformation(self):
        alert = self.driver.switch_to.alert
        alert.accept()
       # print("关闭登录页面弹框")
        log.debug("< 关闭登录页面弹框 >")
if __name__ == '__main__':
    from webframework.page.pageElements.loginPageElement import *
    from selenium import webdriver
    driver = webdriver.Chrome()
    a = LoginPageOperation(driver)
    a.openLoginUrl(LoginUrl)
    a.inputUserName(loc_userBox, "admin")
    a.inputPassWord(loc_passwdBox, "123456")
    a.clickKeepButton(loc_keepRedio)
    a.clickLoginButton(loc_loginButton)
    b = a.verifyUserName(loc_verifyUserName)
    print(b)
    # c = a.getPromptInformation()
    # print(c)
    # a.closePromptInformation()
