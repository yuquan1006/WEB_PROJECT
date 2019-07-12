#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/24 22:01
# @Author  : OldFish
# @Site    : 
# @File    : test_login.py
# @Software: PyCharm
import unittest
from common.browserUtil import BrowserUtil
from page.zentao.loginPage import LoginPage
from common.logger import LogHandler
log = LogHandler()
class Test_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserUtil().open_browser()
        cls.login = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print('Testcase - > Start Next Testcase Now\n')

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    # @unittest.skipIf(1==1,'暂时测试通过')
    def test_login_success(self):
        '''正常登录'''
        try:
            self.login.login_succes()
            log.info('Testcase - > 开始检验检查点')
            result = self.login.verifyLogin()
            self.assertTrue(result)
            log.info('Testcase - > Test PASS !')
        except:
            log.error('Testcase - > Test FAIL !')
            raise

    def test_login_userNull(self):
        '''空用户名登录'''
        try:
            self.login.login_succes(user='')
            print('Testcase - > 开始检验检查点')
            result = self.login.verifyLoginFail()
            self.assertTrue(result)
            print('Testcase - >  Test PASS !')
        except:
            print('Testcase - >  Test FAIL !')
            raise

    def test_login_userwrong(self):
        '''错误的用户名登录'''
        try:
            self.login.login_succes(user='admins')
            result = self.login.verifyLoginFail()
            print('Testcase - >  开始检验检查点')
            self.assertTrue(result)
            print('Testcase - >  Test PASS !')
        except:
            print('Testcase - >  Test FAIL !')
            raise

    def test_login_passwdNull(self):
        '''空密码登录'''
        try:
            self.login.login_succes(passwd='')
            print('Testcase - > 开始检验检查点')
            result = self.login.verifyLoginFail()
            self.assertTrue(result)
            print('Testcase - >  Test PASS !')
        except:
            print('Testcase - >  Test FAIL !')
            raise

    def test_login_passwdwrong(self):
        '''错误的密码登录'''
        try:
            self.login.login_succes(passwd='123456aaa')
            result = self.login.verifyLoginFail()
            print('Testcase - >  开始检验检查点')
            self.assertTrue(result)
            print('Testcase - >  Test PASS !')
        except:
            print('Testcase - >  Test FAIL !')
            raise

    # @unittest.skip('暂时测试通过')
    def test_forgetpasswd(self):
        try:
            self.login.forgetPassWord()
            print('Testcase - >  开始检验检查点')
            result = self.login.verifyforgetPassWord()
            self.assertTrue(result)
            print('Testcase - >  Test PASS !')
        except:
            print('Testcase - >  Test FAIL !')
            raise

if __name__ == '__main__':
    unittest.main()