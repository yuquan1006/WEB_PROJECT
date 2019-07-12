#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
from selenium.webdriver.common.by import By
from common.base import  Base
import page.pageElements.loginPageElement as lp
from page.PageOperation.login_PageOperation import LoginPageOperation

class LoginPageBusiness(LoginPageOperation):
    # loc_user = (By.CSS_SELECTOR, "#account")
    # loc_passwd = (By.CSS_SELECTOR, "[name='password']")
    # loc_login = (By.CSS_SELECTOR, "#submit")
    # log_admin = (By.CSS_SELECTOR, "div#userMenu>a")

    # def __init__(self,driver):
        # self.driver = driver
        # self.b = Base(self.driver)
    # ddt驱动
    def loginBusiness(self, user, passwd):
        self.openUrl(lp.LoginUrl)
        self.inputUserName(lp.loc_userBox, user)
        self.inputPassWord(lp.loc_passwdBox, passwd)
        self.clickKeepButton(lp.loc_keepRedio)
        self.clickLoginButton(lp.loc_loginButton)


    # 正常登录
    def loginBusiness_01(self):
        self.openUrl(lp.LoginUrl)
        self.inputUserName(lp.loc_userBox, lp.UserName)
        self.inputPassWord(lp.loc_passwdBox, lp.PassWord)
        self.clickKeepButton(lp.loc_keepRedio)
        self.clickLoginButton(lp.loc_loginButton)


    # 用户名为空
    def loginBusiness_02(self):
        self.openUrl(lp.LoginUrl)
        self.inputUserName(lp.loc_userBox, lp.UserNameBlank)
        self.inputPassWord(lp.loc_passwdBox, lp.PassWord)
        self.clickKeepButton(lp.loc_keepRedio)
        self.clickLoginButton(lp.loc_loginButton)

    # 用户名错误
    def LoginBusiness_03(self):
        self.openUrl(lp.LoginUrl)
        self.inputUserName(lp.loc_userBox, lp.UserNameWrong)
        self.inputPassWord(lp.loc_passwdBox, lp.PassWord)
        self.clickKeepButton(lp.loc_keepRedio)
        self.clickLoginButton(lp.loc_loginButton)


    # 密码错误
    def loginBusiness_04(self):
        self.openUrl(lp.LoginUrl)
        self.inputUserName(lp.loc_userBox, lp.UserName)
        self.inputPassWord(lp.loc_passwdBox, lp.PassWordWrong)
        self.clickKeepButton(lp.loc_keepRedio)
        self.clickLoginButton(lp.loc_loginButton)

    # 密码为空
    def loginBusiness_05(self):
        self.openUrl(lp.LoginUrl)
        self.inputUserName(lp.loc_userBox, lp.UserName)
        self.inputPassWord(lp.loc_passwdBox, lp.PassWordBlank)
        self.clickKeepButton(lp.loc_keepRedio)
        self.clickLoginButton(lp.loc_loginButton)


if __name__ == '__main__':
    from selenium import webdriver
    d = webdriver.Chrome()
    login = LoginPageBusiness(d)
    login.loginBusiness_01()
    rs = login.verifyUserName(lp.loc_verifyUserName)
    print(rs)


    # print(text)
    # login.closePromptInformation()
    loc_about = ("xpath", "//a[text()='关于']")
    id = "modalIframe11"
    loc_g = ("xpath", "//*[@id='official']")
    login.click(loc_about)
    # d.switch_to.frame(id)
    login.switch_frame(id)
    login.click(loc_g)

