#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 14:47
# @Author  : Yuquan
# @Site    : 
# @File    : test_addproduct.py
# @Software: PyCharm
import unittest,time,random
from common.browserUtil import BrowserUtil
from page.zentao.loginPage import LoginPage
from page.zentao.addproductPage import AddProductPage
class Test_AddProduct(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserUtil().open_browser()
        cls.login = LoginPage(cls.driver)
        cls.addprooduct = AddProductPage(cls.driver)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print('Testcase - > Start Next Testcase Now\n')

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()


    def test_addproduct_success(self):
        '''正常添加产品'''
        try:
            self.login.login_succes()
            result = self.login.verifyLogin()
            self.assertTrue(result)
            productName = "product_"+ str(random.random())
            productCode = "code_" + str(random.random())
            productDescription = "test_%s" %time.time()
            self.addprooduct.addproduct_success(productName,productCode,productDescription)
            print('Testcase - >  开始检验检查点')
            result = self.addprooduct.verifyaddproduct_success(productName)
            self.assertTrue(result)
            print('Testcase - >  Test PASS !')

        except:
            print('Testcase - >  Test FAIL !')
            raise


    def test_addproduct_pNameNull(self):
        '''空产品名——添加产品'''
        try:
            self.login.login_succes()
            result = self.login.verifyLogin()
            self.assertTrue(result)
            productName = ""
            productCode = "code_" + str(random.random())
            productDescription = "test_%s" % time.time()
            self.addprooduct.addproduct_success(productName,productCode,productDescription)
            print('Testcase - >  开始检验检查点')
            result = self.addprooduct.verifyaddproduct_Fail(errordescription='『产品名称』不能为空。')
            self.assertTrue(result)
            print('Testcase - >  Test PASS !')

        except:
            print('Testcase - >  Test FAIL !')
            raise

    def test_addproduct_pCodeNull(self):
        '''空产品代号——添加产品'''
        try:
            self.login.login_succes()
            result = self.login.verifyLogin()
            self.assertTrue(result)
            productName = "product_" + str(random.random())
            productCode = ""
            productDescription = "test_%s" % time.time()
            self.addprooduct.addproduct_success(productName,productCode,productDescription)
            print('Testcase - >  开始检验检查点')
            result = self.addprooduct.verifyaddproduct_Fail(errordescription='『产品代号』不能为空。')
            self.assertTrue(result)
            print('Testcase - >  Test PASS !')

        except:
            print('Testcase - >  Test FAIL !')
            raise



if __name__ == '__main__':
    unittest.main()










