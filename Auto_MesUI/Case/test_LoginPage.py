import unittest
from Common.browserUtil import BrowserUtil
from Page.LoginPage import LoginPage
from Common.logCmd import LogHandler
log = LogHandler(__name__)

class Test_LoginPage(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = BrowserUtil().open_browser()
    #     cls.login = LoginPage(cls.driver)
    #
    def setUp(self):
        self.driver = BrowserUtil().open_browser()
        self.login = LoginPage(self.driver)

    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.quit()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    def test_loginBusiness(self):
        '''登录操作测试用例'''
        try:
            self.login.loginpage_loginBusiness()
            log.info('Testcase - > 开始检验检查点')
            result = self.login.loginpage_verifylogin('yu@qq.com')
            self.assertTrue(result)
            log.info('Testcase - > Test PASS !')
        except BaseException as e:
            log.info('Testcase - > Test FAIL !')
            log.error("断言失败，可能原因：%s"%e)
            raise

    def test_loginpage_registerBusigness(self):
        '''立即注册链接测试用例'''
        try:
            self.login.loginpage_registerBusigness()
            log.info('Testcase - > 开始检验检查点')
            result = self.login.loginpage_verifyregister()
            self.assertTrue(result)
            log.info('Testcase - > Test PASS !')
        except:
            log.info('Testcase - > Test FAIL !')
            raise

    def test_loginpage_forgetpwd(self):
        '''忘记密码测试用例'''
        try:
            self.login.loginpage_forgetpwd()
            log.info('Testcase - > 开始检验检查点')
            result = self.login.loginpage_verifyforgetpwd()
            self.assertTrue(result)
            log.info('Testcase - > Test PASS !')
        except:
            log.info('Testcase - > Test FAIL !')
            raise

    def test_loginpage_returnmain(self):
        try:
            self.login.loginpage_returnmain()
            log.info('Testcase - > 开始检验检查点')
            result = self.login.loginpage_verifyreturnmain()
            self.assertTrue(result)
            log.info('Testcase - > Test PASS !')
        except:
            log.info('Testcase - > Test FAIL !')
            raise

    def test_loginpage_gokjsd(self):
        try:
            self.login.loginpage_gokjsd()
            log.info('Testcase - > 开始检验检查点')
            result = self.login.loginpage_verifygokjsd()
            self.assertTrue(result)
            log.info('Testcase - > Test PASS !')
        except:
            log.info('Testcase - > Test FAIL !')
            raise

    def test_loginpage_gokjsk(self):
        try:
            self.login.loginpage_gokjsk()
            log.info('Testcase - > 开始检验检查点')
            result = self.login.loginpage_verifygokjsk()
            self.assertTrue(result)
            log.info('Testcase - > Test PASS !')
        except:
            log.info('Testcase - > Test FAIL !')
            raise

    def test_loginpage_gogylkj(self):
        try:
            self.login.loginpage_gogylkj()
            log.info('Testcase - > 开始检验检查点')
            result = self.login.loginpage_verifygogylkj()
            self.assertTrue(result)
            log.info('Testcase - > Test PASS !')
        except:
            log.info('Testcase - > Test FAIL !')
            raise

    def test_loginpage_goaboutwe(self):
        try:
            self.login.loginpage_goaboutwe()
            log.info('Testcase - > 开始检验检查点')
            result = self.login.loginpage_verifygoaboutwe()
            self.assertTrue(result)
            log.info('Testcase - > Test PASS !')
        except:
            log.info('Testcase - > Test FAIL !')
            raise
    def test_loginpage_gotouchwe(self):
        try:
            self.login.loginpage_gotouchwe()
            log.info('Testcase - > 开始检验检查点')
            result = self.login.loginpage_verifygotouchwe()
            self.assertTrue(result)
            log.info('Testcase - > Test PASS !')
        except:
            log.info('Testcase - > Test FAIL !')
            raise
if __name__ == '__main__':
    unittest.main()