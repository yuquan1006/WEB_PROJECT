#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 18:19
# @Author  : Yuquan
# @Site    : 
# @File    : test_addbug.py
# @Software: PyCharm
from common.browserUtil import BrowserUtil
from page.zentao.loginPage import LoginPage
from page.zentao.addbugPage import AddBugPage
import unittest,time

class Test_addbug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserUtil().open_browser()
        cls.login = LoginPage(cls.driver)
        cls.addbug = AddBugPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print('Testcase - > Start Next Testcase Now\n')

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test_addbug_success(self):
        try:
            self.login.login_succes()
            result = self.login.verifyLogin()
            self.assertTrue(result)
            title = "title%s" % time.time()
            self.addbug.addbug_success(title)
            print('Testcase - > 开始检验检查点')
            result = self.addbug.veriryaddbug_success(title)
            self.assertTrue(result)
            print('Testcase - > Test PASS !')

        except:
            print('Testcase - > Test FAIL !')
            raise

    def test_addbug_repeatTitle(self):
        '''重复title'''
        try:
            self.login.login_succes()
            result = self.login.verifyLogin()
            self.assertTrue(result)
            title = '01'
            self.addbug.addbug_success(bugtitle=title)
            print('Testcase - > 开始检验检查点')
            result = self.addbug.verifyrepeatTitle()
            self.assertTrue(result)
            print('Testcase - > Test PASS !')

        except:
            print('Testcase - > Test FAIL !')
            raise


if __name__ == '__main__':
    unittest.main()