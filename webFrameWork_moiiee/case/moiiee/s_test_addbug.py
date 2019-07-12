#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 13:18
# @Author  : Yuquan
# @Site    : 
# @File    : s_test_addbug.py
# @Software: PyCharm
import unittest,time
from webframework.page.pageBusiness.addBugPage import AddBug
from webframework.page.pageBusiness.loginPageBusiness import LoginPage
from selenium import webdriver


class TestAddBug(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login = LoginPage(self.driver)
        self.add = AddBug(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_o1(self):
        '''提交bug'''
        result = self.login.login()
        self.assertTrue(result)
        timestr = str(time.time())
        self.add.addBug(timestr)
        result = self.add.new_get_text(timestr)
        # print('a', result)
        # print("b", timestr)
        self.assertTrue(result)

    def test_02(self):
        '''提交重复bug'''
        result = self.login.login()
        self.assertTrue(result)
        oldtitle = "add"
        self.add.addBug(oldtitle)
        time.sleep(2)
        alert = self.add.is_alert()
        result = alert.text
        time.sleep(3)
        alert.accept()
        self.assertTrue(result == "已有相同标题的Bug")


if __name__ == '__main__':
    unittest.main()
