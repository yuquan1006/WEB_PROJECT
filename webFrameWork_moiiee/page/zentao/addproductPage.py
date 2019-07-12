#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/25 11:32
# @Author  : Yuquan
# @Site    :
# @File    : addproductPage.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
from common.base import Base
import time

class AddProductPage(Base):
    # 元素
    ele_main_ProductButton = (By.XPATH, "//nav[@id='mainmenu']/ul/li/a[text()='产品']") # 首页产品按钮
    ele_product_addproductButton = (By.CSS_SELECTOR, 'a[href="/zentao/product-create.html"]')  # 产品页添加产品按钮
    ele_addproduct_productNameBox = (By.CSS_SELECTOR,'input#name')  # 新增产品页——产品名称
    ele_addproduct_productCodeBox = (By.CSS_SELECTOR,'input#code')  # 新增产品页——
    ele_addproduct_productLeaderBox = (By.CSS_SELECTOR,'div#PO_chosen>.chosen-single>div')  # 新增产品页——
    ele_addproduct_productLeaderResultButton  = (By.CSS_SELECTOR, 'div#PO_chosen>div>ul.chosen-results>li.active-result')    # 新增产品页——
    ele_addproduct_TestLeaderBox = (By.CSS_SELECTOR, 'div#QD_chosen>.chosen-single>div')  # 新增产品页——
    ele_addproduct_TestLeaderResultButton  = (By.CSS_SELECTOR, 'div#QD_chosen>div>ul.chosen-results>li.active-result')    # 新增产品页——
    ele_addproduct_ReleaseLeaderBox = (By.CSS_SELECTOR,'div#RD_chosen>.chosen-single>div')
    ele_addproduct_ReleaseLeaderResultButton = (By.CSS_SELECTOR, 'div#RD_chosen>div>ul.chosen-results>li.active-result')
    ele_addproduct_productDescriptionIframe = (By.CSS_SELECTOR,'iframe.ke-edit-iframe')
    ele_addproduct_productDescriptionTextBox = (By.CSS_SELECTOR,'body.article-content')
    ele_addproduct_SaveButton = (By.CSS_SELECTOR,'#submit')
    # 断言元素
    ele_verify_addproduct_top = (By.XPATH, '//*[@id="productList"]/tbody/tr[1]/td[2]/a') # 全部产品页面第一行产品名称


    def addproduct_success(self,productName,productCode,productDescription):
        '''添加产品'''
        self.click((self.ele_main_ProductButton))
        self.click(self.ele_product_addproductButton)
        self.sendKeys(self.ele_addproduct_productNameBox,productName)
        self.sendKeys(self.ele_addproduct_productCodeBox,productCode)
        self.click(self.ele_addproduct_productLeaderBox)
        self.click(self.ele_addproduct_productLeaderResultButton)
        self.click(self.ele_addproduct_TestLeaderBox)
        self.click(self.ele_addproduct_TestLeaderResultButton)
        self.click(self.ele_addproduct_ReleaseLeaderBox)
        self.click(self.ele_addproduct_ReleaseLeaderResultButton)
        self.switch_frame(self.ele_addproduct_productDescriptionIframe)
        self.sendKeys(self.ele_addproduct_productDescriptionTextBox,productDescription)
        self.switch_to_defaultFrame()
        self.click(self.ele_addproduct_SaveButton)
        print('addproductPage - > 新增产品事件完成')



    def verifyaddproduct_success(self,productName):
        '''验证添加产品'''
        try:
            self.openUrl("http://127.0.0.1:81/zentao/product-all-13.html")  #打开全部产品页面
            result = self.get_text(self.ele_verify_addproduct_top)
            assert result == productName
            print(result)
            return True
        except:
            return False

    def verifyaddproduct_Fail(self,errordescription='『产品名称』不能为空。'):
        '''验证新增失败'''
        try:
            self.is_alert_parsent()
            result = self.getAlertText()
            result=result.strip()
            assert errordescription == result,"%s！=%s"%(result,errordescription)
            self.acceptAlert()
            return True
        except:
            raise



if __name__ == '__main__':
    from page.zentao.loginPage import LoginPage
    from selenium import webdriver
    import random
    d = webdriver.Chrome()
    l = LoginPage(d)
    l.login_succes()
    a = AddProductPage(d)
    # a.addproduct_success("p_01","c_01","test%s"%time.time())
    # a.verifyaddproduct_success("p_01")

    productName = "product_"+ str(random.random())
    productCode = ""
    productDescription = "test_%s" % time.time()
    a.addproduct_success(productName, productCode, productDescription)
    result = a.verifyaddproduct_Fail(errordescription='『产品代号』不能为空。')
    print(result)