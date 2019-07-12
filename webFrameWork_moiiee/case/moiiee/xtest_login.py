#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
# 知识点：unittest 和ddt 数据驱动
import unittest
from selenium import webdriver
import time
from common.browserUtil import BrowserUtil
from page.pageBusiness.loginPageBusiness import LoginPageBusiness
import page.pageElements.loginPageElement as lp
import ddt
from common.logger import Logger
log = Logger("test_login")
from common.excelUtil import ExcelUtil
data = ExcelUtil().get_data()
# data = [
#     {"username":"admin", "password": 123456, "expect":True},
#     {"username":"", "password": 123456, "expect": False},
#     {"username":"admin2", "password": 123456, "expect": False}
# ]
@ddt.ddt
class ChanDAOLogin(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
    # def tearDown(self):
    #     self.driver.quit()
    #
    # @classmethod
    # def setUpClass(cls):
    #     pass
    #
    # @classmethod
    # def tearDownClass(cls):
    #     pass

    def setUp(self):
        self.driver = BrowserUtil().open_browser()
        self.login = LoginPageBusiness(self.driver)


    def tearDown(self):

        self.driver.close()  # 清楚cookies 相当于退出登录



    @ddt.data(*data)
    def test_login(self, testdata):
        '''
        '''
        expect = bool(testdata["expect"])
        user = testdata['username']
        passwd = testdata['password']
        print(user, passwd, expect)

        self.login.loginBusiness(user, passwd)
        actual = self.login.verifyUserName(lp.loc_verifyUserName)
        print(actual)
        expect = bool(testdata["expect"])
        print(expect)
        try:
            self.assertEqual(actual, expect, "期望结果和实际结果不相符！")
            log.info("***********登录断言成功***********测试通过！")

        except:
            log.error("***********登录断言失败***********测试不通过！")


if __name__=='__man__':
    unittest.main()
