#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
import unittest
from common.browserUtil import BrowserUtil
import time
from page.moiiee.loginPage import LoginPage
from common.logger import LogHandler
import warnings
warnings.simplefilter("ignore", ResourceWarning)
log = LogHandler("test_login")

class TestMoiieeLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserUtil().open_browser()
        cls.login = LoginPage(cls.driver)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()



    def test_login_001(self):
        '''
        测试点：使用正确的用户名和密码登录成功
        检查点：登录成功跳转后页面存在登录用户名
        '''
        self.login.loginBusiness_success()
        result = self.login.verifyLoginSuccess()
        # 推出当前账户登录
        try:
            self.assertEqual(True ,result, "登录断言失败！")
            log.info("- > 正常登录用例验证成功 测试通过！")
            self.login.loginOut(self.login.loc_loginOutButton)

        except:
            self.login.get_Screenshots()
            log.error("- > 正常登录用例验证失败 测试不通过！")
            raise

    def test_login_002(self):
        '''
        测试点：使用空的用户名和密码登录成功
        检查点：获取不到页面存在登录用户名
        '''
        self.login.loginBusiness_02()
        result = self.login.verifyLoginSuccess(lp.loc_verifyLoginSuccess)
        try:
            self.assertEqual(False, result, "登录断言失败！")
            log.info("***********空用户名登录用例验证成功***********测试通过！")
            print("***********空用户名登录用例验证成功***********测试通过！")

        except:
            self.login.get_Screenshots()
            log.error("***********空用户名登录用例验证失败***********测试不通过!")
            log.error("***********空用户名登录用例验证失败***********测试不通过!")
            raise
    def test_login_003(self):
        '''
        测试点：用户名错误
        检查点：获取不到页面存在登录用户名
        '''
        self.login.loginBusiness_03()
        result = self.login.verifyLoginSuccess(lp.loc_verifyLoginSuccess)
        try:
            self.assertEqual(False, result, "登录断言失败！")
            log.info("***********用户名错误登录用例验证成功***********测试通过！")
            print("***********用户名错误登录用例验证成功***********测试通过！")
        except:
            self.login.get_Screenshots()
            log.error("***********用户名错误登录用例验证失败***********测试不通过!")
            print("***********用户名错误登录用例验证失败***********测试不通过!")
            raise
    def test_login_004(self):
        '''
        测试点：密码错误
        检查点：获取不到页面存在登录用户名
        '''
        self.login.loginBusiness_04()
        result = self.login.verifyLoginSuccess(lp.loc_verifyLoginSuccess)
        try:
            self.assertEqual(False, result, "登录断言失败！")
            log.info("***********密码错误登录用例验证成功***********测试通过！")
            print("***********密码错误登录用例验证成功***********测试通过！")
        except:
            self.login.get_Screenshots()
            log.error("***********密码错误登录用例验证失败***********测试不通过!")
            print("***********密码错误登录用例验证失败***********测试不通过!")
            raise
    def test_login_005(self):
        '''
        测试点：密码空
        检查点：获取不到页面存在登录用户名
        '''
        self.login.loginBusiness_05()
        result = self.login.verifyLoginSuccess(lp.loc_verifyLoginSuccess)
        try:
            self.assertEqual(False, result, "登录断言失败！")
            log.info("***********密码空登录用例验证成功***********测试通过！")
            print("***********密码空登录用例验证成功***********测试通过！")
        except:
            self.login.get_Screenshots()
            log.error("***********密码空登录用例验证失败***********测试不通过!")
            print("***********密码空登录用例验证失败***********测试不通过!")
            raise
    def test_megLogin_006(self):
        '''
        测试点：短信登录
        检查点：
        '''
        self.login.megLoginBusiness_01()
        result = self.login.verifyMesLoginSuccess(lp.loc_verifyMessageLogin)
        try:
            self.assertEqual(True, result, "短信登录断言失败！")
            log.info("***********短信登录用例验证成功***********测试通过！")
            print("***********短信登录用例验证成功***********测试通过！")
        except:
            self.login.get_Screenshots()
            log.error("***********短信正常登录用例验证失败***********测试不通过!")
            print("***********短信正常登录用例验证失败***********测试不通过!")
            raise

    def test_megLogin_007(self):
        '''
        测试点：短信登录-空验证码
        检查点：
        '''
        self.login.megLoginBusiness_02()
        result = self.login.verifyLoginSuccess(lp.loc_verifyLoginSuccess)
        try:
            self.assertEqual(False, result, "短信登录断言失败！")
            log.info("***********短信登录用例验证成功***********测试通过！")
            print("***********短信登录用例验证成功***********测试通过！")
        except:
            self.login.get_Screenshots()
            log.error("***********短信正常登录用例验证失败***********测试不通过!")
            print("***********短信正常登录用例验证失败***********测试不通过!")
            raise

    def test_megLogin_008(self):
        '''
        测试点：短信登录
        检查点：
        '''
        self.login.megLoginBusiness_03()
        result = self.login.verifyLoginSuccess(lp.loc_verifyLoginSuccess)
        try:
            self.assertEqual(False, result, "登录断言失败！")
            log.info("***********短信登录用例验证成功***********测试通过！")
            print("***********短信登录用例验证成功***********测试通过！")
        except:
            self.login.get_Screenshots()
            log.error("***********短信正常登录用例验证失败***********测试不通过!")
            print("***********短信正常登录用例验证失败***********测试不通过!")
            raise

    def test_megLogin_009(self):
        '''
        测试点：忘记密码链接
        检查点：跳转忘记密码页面
        '''
        self.login.goToForget()
        result = self.login.verifyForgetPs(lp.loc_verifyForgetPs)
        try:
            self.assertEqual(True, result, "忘记密码链接跳转断言失败！")
            log.info("***********忘记密码链接跳转用例验证成功***********测试通过！")
            print("***********忘记密码链接跳转用例验证成功***********测试通过！")
        except:
            self.login.get_Screenshots()
            log.error("***********忘记密码链接跳转用例验证成功***********测试不通过!")
            print("***********忘记密码链接跳转用例验证成功***********测试不通过!")
            raise
    def test_megLogin_0010(self):
        '''
        测试点：立即注册链接
        检查点：跳转注册页面链接
        '''
        self.login.goToRegister()
        result = self.login.verifyRegister(lp.loc_verifyReg)
        try:
            self.assertEqual(True, result, "立即注册链接跳转断言失败！")
            log.info("***********立即注册链接跳转用例验证成功***********测试通过！")
            print("***********立即注册链接跳转用例验证成功***********测试通过！")
        except:
            self.login.get_Screenshots()
            log.error("***********忘记密码链接跳转用例验证失败***********测试不通过!")
            print("***********忘记密码链接跳转用例验证失败***********测试不通过!")
            raise



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
