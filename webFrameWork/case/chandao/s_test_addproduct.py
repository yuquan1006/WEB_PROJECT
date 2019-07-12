#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 16:28
# @Author  : Yuquan
# @Site    : 
# @File    : s_test_addproduct.py
# @Software: PyCharm
import unittest,time
from webframework.page.pageBusiness.addProductPage import AddProduct
from webframework.page.pageBusiness.loginPageBusiness import LoginPage
from selenium import webdriver


class TestAddProduct(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login = LoginPage(self.driver)
        self.add = AddProduct(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_o1(self):
        '''新增产品'''
        result = self.login.login()
        self.assertTrue(result)
        p_name = str(time.time())
        p_code = str(time.time())
        self.add.addproduct(p_name, p_code)
        result = self.add.get_product_list_text()
        self.assertTrue(result == p_name)

    def test_02(self):
        '''新增重复产品'''
        result = self.login.login()
        self.assertTrue(result)
        p_name = str("admin02")
        p_code = str(time.time())
        self.add.addproduct(p_name, p_code)
        result = self.add.get_product_list_text()
        a = self.add.is_alert()
        result = a.text
        print(result)
        a.accept()
        self.assertFalse(result == "『产品名称』已经有『%s』这条记录了。如果您确定该记录已删除，请到后台管理-回收站还原。。"%p_name)

if __name__ == '__main__':
    unittest.main()