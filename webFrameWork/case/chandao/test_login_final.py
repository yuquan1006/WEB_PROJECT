#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
import unittest
from common.browserUtil import BrowserUtil
import time
from page.pageBusiness import loginPageBusiness
import page.pageElements.loginPageElement as lp
from common.logger import Logger
log = Logger("test_login")

class ChanDAOLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserUtil().open_browser()
        cls.login = loginPageBusiness.LoginPageBusiness(cls.driver)

    def tearDown(self):
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_001(self):
        '''
        测试点：使用正确的用户名和密码登录成功
        检查点：登录成功跳转后页面存在登录用户名
        '''
        self.login.loginBusiness_01()
        result = self.login.verifyUserName(lp.loc_verifyUserName)
        if result:
            result = self.login.get_text(lp.loc_verifyUserName)
            try:
                self.assertEqual(result, lp.UserName ,"获取用户名和登录用户名不相同")
                log.info("***********正常登录用例验证成功***********测试通过！")


            except:
                # 失败截图
                self.login.get_Screenshots()
                log.error("***********正常登录用例验证失败***********测试不通过!")
        else:
            log.error("***********正常登录用例验证失败***********测试不通过!")

        # self.assertTrue(result)
        # print("断言成功！测试通过")

    def test_login_002(self):
        '''
        测试点：使用空的用户名和密码登录成功
        检查点：登录失败弹框文本
        '''
        self.login.loginBusiness_02()
        result = self.login.getPromptInformation()
        try:
            self.assertEqual(result, lp.PromptInformation ,"用户名为空断言失败!")
            log.info("***********空用户名登录验证成功***********测试通过")
        except:
            # 失败截图
            self.login.get_Screenshots()
            log.info("***********空用户名登录验证失败***********测试不通过")

        self.login.closePromptInformation()

    @unittest.skip # 无条件跳过该用例
    def test_skip01(self):
        pass

    @unittest.skipIf(1 > 0, "表达式成立跳过")  # 表达式成立跳过
    def test_skip02(self):
        pass

    @unittest.skipUnless(0, "除非为真跳过")  # 除非为真跳过
    def test_skip03(self):
        pass


if __name__=='__man__':
    unittest.main()
