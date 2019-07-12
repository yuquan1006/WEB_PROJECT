#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 20:35
# @Author  : OldFish
# @Site    : 
# @File    : loginPage.py
# @Software: PyCharm
from common.base import Base
from selenium.webdriver.common.by import By
from common.logger import Logger
log = Logger()

class LoginPage(Base):
    # url
    LoginUrl = "http://www.moiiee.com/#/user-sign/sign-in"
    # 登录页面元素
    loc_userBox = (By.CSS_SELECTOR, "input[placeholder='请输入手机号']")
    loc_passwdBox = (By.CSS_SELECTOR, "input[placeholder='请输入密码']")
    loc_loginButton = (By.CSS_SELECTOR, ".confirm-login")
    loc_loginOutButton = (By.XPATH, "//*[@name='nickName']/span[contains(text(), '[退出]')]")
    loc_forgetButton = (By.XPATH, "//a[text()='忘记密码']")

    loc_messageLoginEntry = (By.XPATH, "//*[text()='短信验证登录']")
    loc_messageuserBox = (By.CSS_SELECTOR, "input.login-tel-left-item-input")
    loc_messageCodeButton = (By.CSS_SELECTOR, ".count-down")
    loc_messageCodeBox = (By.CSS_SELECTOR, "input[placeholder=\"请输入验证码\"]")
    loc_messageLoginButton = (By.CSS_SELECTOR, ".confirm-login-tel")

    loc_registerEntry = (By.CSS_SELECTOR, "a.register")
    loc_LoginEntry = (By.XPATH, "//*[text()='直接登录']")

    # 登录成功调转断言：
    loc_verifyLoginSuccess = (By.XPATH, "//*[@name='nickName']/span")
    # 忘记密码跳转断言
    loc_verifyForgetPs = (By.XPATH, "//*[@placeholder='请重复输入新密码']")
    # 注册页面调转断言
    loc_verifyReg = (By.XPATH, "//div[text()='注册']")
    # 短信登录断言
    loc_verifyMessageLogin = (By.CSS_SELECTOR, '.ivu-btn.ivu-btn-primary.ivu-btn-large')

    # 验证首页用户名
    # 登录页面数据
    UserName = "18973019192"
    UserNameBlank = ''  # 用户名为空
    UserNameWrong = 'yang@emotibot.com'  # 用户名错误
    PassWord = 'yu1234'  # 密码
    PassWordBlank = ''  # 密码为空
    PassWordWrong = '341234123'  # 密码错误
    CodeBlank = ""
    CodeWrong = '123455'


    # 登录后点击退出按钮
    def loginOut(self, loc_loginOutButton):
        self.click(loc_loginOutButton)
        log.debug("< 点击退出登录按钮 >")

# ***********************************操作

    def loginBusiness(self, user, passwd):
        self.openUrl(self.LoginUrl)
        self.sendKeys(self.loc_userBox,user)
        self.sendKeys(self.loc_passwdBox, passwd)
        self.click(self.loc_loginButton)

    # 正常登录
    def loginBusiness_success(self):
        self.openUrl(self.LoginUrl)
        self.sendKeys(self.loc_userBox,self.UserName)
        self.sendKeys(self.loc_passwdBox, self.PassWord)
        self.click(self.loc_loginButton)

    # 用户名为空
    def loginBusiness_userNull(self):
        self.openUrl(self.LoginUrl)
        self.sendKeys(self.loc_userBox,self.UserNameBlank)
        self.sendKeys(self.loc_passwdBox, self.PassWord)
        self.click(self.loc_loginButton)

    # 用户名错误
    def loginBusiness_userwrong(self):
        self.openUrl(self.LoginUrl)
        self.sendKeys(self.loc_userBox,self.UserNameWrong)
        self.sendKeys(self.loc_passwdBox, self.PassWord)
        self.click(self.loc_loginButton)


    # 密码错误
    def loginBusiness_passwrong(self):
        self.openUrl(self.LoginUrl)
        self.sendKeys(self.loc_userBox,self.UserName)
        self.sendKeys(self.loc_passwdBox, self.PassWordWrong)
        self.click(self.loc_loginButton)

    # 密码为空
    def loginBusiness_passNull(self):
        self.openUrl(self.LoginUrl)
        self.sendKeys(self.loc_userBox,self.UserName)
        self.sendKeys(self.loc_passwdBox, self.PassWordBlank)
        self.click(self.loc_loginButton)

    # 短信验证登录
    def megLoginBusiness_success(self):
        self.openUrl(self.LoginUrl)
        self.click(self.loc_messageLoginEntry)
        self.sendKeys(self.loc_messageuserBox, self.UserName)
        self.click(self.loc_messageCodeButton)

    # 短信验证登录-空验证码
    def megLoginBusiness_null(self):
        self.openUrl(self.LoginUrl)
        self.click(self.loc_messageLoginEntry)
        self.sendKeys(self.loc_messageuserBox, self.UserName)
        self.sendKeys(self.loc_messageCodeBox, self.CodeBlank)
        self.click(self.loc_messageLoginButton)


    # 短信验证登录-错误验证码
    def megLoginBusiness_03(self):
        self.openUrl(self.LoginUrl)
        self.click(self.loc_messageLoginEntry)
        self.sendKeys(self.loc_messageuserBox, self.UserName)
        self.sendKeys(self.loc_messageCodeBox, self.CodeWrong)
        self.click(self.loc_messageLoginButton)

    # 跳转立即注册页面
    def goToRegister(self):
        self.openUrl(self.LoginUrl)
        self.click(self.loc_registerEntry)

    # 跳转忘记密码页面
    def goToForget(self):
        self.openUrl(self.LoginUrl)
        self.click(self.loc_forgetButton)

        # **************断言方法
        # 登录成功断言

    def verifyLoginSuccess(self):
        result = self.is_element_exsit(self.loc_verifyLoginSuccess)
        # print("获取首页用户名元素是否存在：%s" % result)
        log.debug("< 登录断言结果：%s >" % result)
        return result

    def verifyMesLoginSuccess(self, loc_verifyMessageLogin):
        result = self.is_element_exsit(loc_verifyMessageLogin)
        log.debug("< 短信登录断言结果：%s >" % result)
        return result

        # 忘记密码连接断言

    def verifyForgetPs(self, loc_verifyForgetPs):
        result = self.is_element_exsit(loc_verifyForgetPs)
        # print("< 登录页面弹框文本信息:%s >" % text)
        log.debug("< 忘记密码跳转页面断言结果:%s >" % result)
        return result

        # 注册页面调转断言

    def verifyRegister(self, loc_verifyReg):
        result = self.is_element_exsit(loc_verifyReg)
        # print("< 登录页面弹框文本信息:%s >" % text)
        log.debug("< 注册页面跳转页面断言结果:%s >" % result)
        return result

if __name__ == '__main__':
    import selenium.webdriver as webdriver
    driver = webdriver.Chrome()
    l = LoginPage(driver)
    l.loginBusiness(l.UserName,l.PassWord)
    l.verifyLoginSuccess()




