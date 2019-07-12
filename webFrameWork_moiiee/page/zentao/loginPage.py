#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 21:07
# @Author  : OldFish
# @Site    : 
# @File    : loginPage.py
# @Software: PyCharm
from common.base import Base
from selenium.webdriver.common.by import By
class LoginPage(Base):
    # url
    # ele_loginUrl = "http://192.168.124.20:81/zentao/user-login-L3plbnRhby8=.html"
    ele_loginUrl = "http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html"
    ele_userNameBox = (By.CSS_SELECTOR, '#account')
    ele_passWordBox = (By.CSS_SELECTOR, '[name="password"]')
    ele_loginButton = (By.XPATH, '//*[text()="登录"]')
    ele_forgetPassWord = (By.XPATH, '//*[text()="忘记密码"]')
    ele_keepLoginRadio = (By.CSS_SELECTOR, '#keepLoginon')

    # 断言页面元素
    ele_verifyforgetPassWord = (By.XPATH,'//strong[text()="忘记密码"]')
    ele_verifyLogin = (By.CSS_SELECTOR, 'div#userMenu>a')


    def login_succes(self,user='admin',passwd='Admin@123'):
        '''正常登录'''
        self.openUrl(self.ele_loginUrl)
        self.sendKeys(self.ele_userNameBox,user)
        self.sendKeys(self.ele_passWordBox,passwd)
        self.click(self.ele_loginButton)
        print('Page - > 登录事件完成')

    def verifyLogin(self,user='admin'):
        '''登录验证'''
        result = self.is_text_in_element(self.ele_verifyLogin, user)
        return result

    def forgetPassWord(self):
        '''忘记密码'''
        self.openUrl(self.ele_loginUrl)
        self.click(self.ele_forgetPassWord)

    def verifyforgetPassWord(self):
        '''验证忘记密码'''
        result = self.is_element_exsit(self.ele_forgetPassWord)
        return result

    def verifyLoginFail(self):
        '''验证登录失败'''
        try:
            result = self.is_alert_parsent()
            if result:
                text = self.getAlertText()
                assert text == '登录失败，请检查您的用户名或密码是否填写正确。'
                self.acceptAlert()
                return True
            return result
        except:
            return False

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    l = LoginPage(driver)
    l.login_succes(user='',passwd='123456')
    result = l.verifyLoginFail()
    print(result)

