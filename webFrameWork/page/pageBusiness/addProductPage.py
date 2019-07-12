#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/28 13:48
# @Author  : Yuquan
# @Site    : 
# @File    : addProductPage.py
# @Software: PyCharm
from webframework.common.base import Base
from selenium.webdriver.common.by import By
from webframework.page.pageBusiness.loginPageBusiness import LoginPage
class AddProduct(Base):
    loc_product = (By.XPATH, "//li[@data-id='product']/a[text()='产品']")
    loc_addproduct= (By.XPATH, "//li[@data-id='create']/a")
    loc_pname = (By.CSS_SELECTOR, "input#name")
    loc_pcode = (By.CSS_SELECTOR, "input#code")
    loc_testman = (By.CSS_SELECTOR, "div#QD_chosen>a")
    loc_t_admin = (By.CSS_SELECTOR, ".active-result.highlighted")
    loc_fbman = (By.CSS_SELECTOR, "div#RD_chosen>a")
    loc_f_admin =(By.CSS_SELECTOR, ".active-result.highlighted")
    iframe = (By.CSS_SELECTOR, "iframe.ke-edit-iframe")
    loc_body = (By.CSS_SELECTOR, "body.article-content")
    loc_submit = (By.CSS_SELECTOR, "#submit")
    loc_p_list = (By.XPATH, ".//*[@id='block10']/div[2]/table/tbody/tr/td[1]")
    loc_p_first = (By.XPATH, ".//*[@id='block10']/div[2]/table/tbody/tr[1]/td[1]")



    def addproduct(self, pname, pcode):
        self.click(self.loc_product)
        self.click(self.loc_addproduct)
        self.send(self.loc_pname, pname)
        self.send(self.loc_pcode, pcode)
        self.click(self.loc_testman)
        self.click(self.loc_t_admin)
        self.click(self.loc_fbman)
        self.click(self.loc_f_admin)
        ele = self.findElement(self.iframe)
        self.driver.switch_to.frame(ele)
        self.send(self.loc_body, "第一个产品")
        self.driver.switch_to.default_content()
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        self.click(self.loc_submit)

    def get_product_list_text(self):
        try:
            self.driver.get("http://127.0.0.1:81/zentao/product")
            eles = self.findElements(self.loc_p_list)
            els = eles[0].text
            return els
        except:
            return ""

    def get_fist_name(self, _text):
        r = self.is_text_in_element(self.loc_p_first, _text=_text)
        return r




if __name__ == '__main__':
    import selenium.webdriver as webdriver
    d = webdriver.Chrome()
    lo = LoginPage(d)
    lo.login()
    a = AddProduct(d)
    a.addproduct("admin07", "007")
    result = a.get_product_list_text()
    print(result)
    assert  result == "admin07"
    print("测试通过！")
    d.quit()


