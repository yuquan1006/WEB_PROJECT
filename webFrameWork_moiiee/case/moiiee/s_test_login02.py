#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
# 知识点：封装函数调用

from webframework.page.pageBusiness.loginPageBusiness import LoginPage
import unittest
from selenium import webdriver
import time

class ChanDAOLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.Login = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_loginsuccess(self):
        '''
        测试点：使用正确的用户名和密码登录成功
        检查点：登录成功跳转后页面存在登录用户名
        '''
        result = self.Login.login()
        self.assertTrue(result)
        print("登录成功用例——测试通过")

    def test_loginfail(self):
        '''
        测试点：使用错误的用户名和密码登录失败
        检查点：登录失败弹出登录失败弹框
        '''
        result = self.Login.login(user='addd', passwd='123456')

        self.assertFalse(result)
        self.is_alert_exist()
        print("登录失败用例-测试通过")

    @unittest.skip # 无条件跳过该用例
    def test_skip01(self):
        pass

    @unittest.skipIf(1 > 0, "表达式成立跳过")  # 表达式成立跳过
    def test_skip02(self):
        pass

    @unittest.skipUnless(1, "除非为真跳过")  # 除非为真跳过
    def test_skip03(self):
        pass


    def is_alert_exist(self):
        '''判断alert是不是在'''
        try:
            time.sleep(2)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept() # 用alert 点alert
            return text
        except:
            return ""
if __name__=='__man__':
    unittest.main()

