#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 16:33
# @Author  : Yuquan
# @Site    : 
# @File    : addbugPage.py
# @Software: PyCharm
from common.base import Base
import time

from selenium.webdriver.common.by import By
class AddBugPage(Base):
    #
    ele_main_TestButton = (By.XPATH,'//*[@data-id="qa"]/a[text()="测试"]') #首页测试页面入口按钮
    ele_test_bugButton = (By.XPATH, '//li[@data-id="bug"]/a[text()="Bug"]') #测试页面bug按钮
    ele_bug_addbugButton = (By.XPATH, '//div[@id="createActionMenu"]/a[text()="提Bug"]') # bug页面提bug按钮
    ele_swtichproductButton = (By.CSS_SELECTOR, '#currentItem')  # 提bug页面切换产品
    ele_swtichproduct_select = (By.CSS_SELECTOR, 'a[href="/zentao/bug-browse-1.html"]')  # 提bug页面选择admin产品
    ele_addbug_affversionBox = (By.CSS_SELECTOR, '#openedBuild_chosen>ul') # 影响版本
    ele_addbug_affversionSelect = (By.CSS_SELECTOR, 'div#openedBuild_chosen>div>ul.chosen-results>li.active-result') # 影响版本
    ele_addbug_osSelect = (By.CSS_SELECTOR, '#os')
    ele_addbug_browserSelect = (By.CSS_SELECTOR, '#browser')
    ele_addbug_bugtitleBox = (By.XPATH, '//*[text()="Bug标题"]/../td/div/div/div/input')
    ele_addbug_stepiframe = (By.CSS_SELECTOR, 'iframe.ke-edit-iframe')
    ele_addbug_stepBox = (By.CSS_SELECTOR,'body.article-content')
    ele_addbug_copytoBOX = (By.CSS_SELECTOR, '#mailto_chosen>ul')
    ele_addbug_copytoSelect = (By.CSS_SELECTOR, '#contactListGroup>div>div>ul>li')
    ele_addbug_keywordBox = (By.CSS_SELECTOR,'#keywords')
    ele_addbug_uploadButton = (By.CSS_SELECTOR,'input.fileControl')
    ele_addbug_saveButton = (By.XPATH, '//button[text()="保存"]')
    # 断言
    ele_verifyaddbug = (By.XPATH, '//table[@id="bugList"]/tbody/tr[1]/td[4]/a') # bug表格中第一条bugtitle




    def addbug_success(self,bugtitle='title%s'%time.time()):
        '''正常添加bug'''
        self.click(self.ele_main_TestButton)
        self.click(self.ele_test_bugButton)
        self.click(self.ele_bug_addbugButton)
        self.click(self.ele_swtichproductButton)
        self.click(self.ele_swtichproduct_select)
        self.click(self.ele_bug_addbugButton)
        self.click(self.ele_addbug_affversionBox)
        self.click(self.ele_addbug_affversionSelect)
        self.select_by_value(self.ele_addbug_osSelect,"all")
        self.select_by_value(self.ele_addbug_browserSelect,"chrome")
        self.sendKeys(self.ele_addbug_bugtitleBox,bugtitle)
        self.switch_frame(self.ele_addbug_stepiframe)
        body = '[步骤]:test\n[结果]:fail\n[期望]:pass'
        self.sendKeys(self.ele_addbug_stepBox,body)
        self.switch_to_defaultFrame()
        self.click(self.ele_addbug_copytoBOX)
        self.click(self.ele_addbug_copytoSelect)
        self.sendKeys(self.ele_addbug_keywordBox,'Risk')
        self.sendKeys(self.ele_addbug_uploadButton,r"C:\Users\A\Desktop\s.png")
        self.click(self.ele_addbug_saveButton)
        print("AddbugPage - > 添加bug事件完成")

    def veriryaddbug_success(self,bugtitle):
        try:
            result = self.get_text(self.ele_verifyaddbug)
            # print(result)
            assert result == bugtitle
            return True
        except:
            return False

    def verifyrepeatTitle(self,text='已有相同标题的Bug'):
        '''验证重复title'''
        try:
            self.is_alert_parsent()
            result = self.getAlertText()
            result =result.strip()
            assert text == result
            self.acceptAlert()
            return True
        except:
            return False



if __name__ == '__main__':
    from page.zentao.loginPage import LoginPage
    from selenium import webdriver
    import random
    d = webdriver.Chrome()
    l = LoginPage(d)
    l.login_succes()
    a = AddBugPage(d)
    title = 'title%s'%time.time()
    a.addbug_success(bugtitle="01")
    result = a.verifyrepeatTitle()
    print(result)

