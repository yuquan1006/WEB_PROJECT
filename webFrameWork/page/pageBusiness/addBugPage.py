#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
from webframework.common.base import Base
from selenium.webdriver.common.by import By
from webframework.page.pageBusiness.loginPageBusiness import LoginPage
import time


class AddBug(Base):
    loc_test = (By.XPATH, "//a[text()='测试']")
    loc_bug = (By.XPATH, "//*[@data-id='bug']/a")
    loc_tibug = (By.CSS_SELECTOR, ".btn.btn-bug-create")
    loc_product = (By.XPATH, ".//*[@id='product_chosen']/a/span")
    loc_amdin = (By.XPATH, ".//*[@id='product_chosen']/div/ul/li[11]")
    loc_yxbb = (By.CSS_SELECTOR, "div#openedBuild_chosen>ul")
    loc_trunk = (By.CSS_SELECTOR, "li.active-result")
    loc_title = (By.CSS_SELECTOR, "#title")
    iframe = (By.CSS_SELECTOR, "iframe.ke-edit-iframe")
    loc_body = (By.CSS_SELECTOR, ".article-content")
    loc_tijiao = (By.CSS_SELECTOR, "#submit")

    loc_product_choose = (By.CSS_SELECTOR, 'a#currentItem')
    loc_admin_p = (By.CSS_SELECTOR, "//*[href='/zentao/bug-browse-1.html']")
    loc_buglist = (By.XPATH, "//*[@id='bugList']/tbody/tr/td[4]/a")
    loc_bug_first = ("xpath", ".//*[@id='bugList']/tbody/tr[1]/td[4]/a")


    def addBug(self, timestr):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_tibug)
        # self.driver.maximize_window()
        # self.click(self.loc_product)
        # self.click(self.loc_amdin)
        self.click(self.loc_yxbb)
        self.click(self.loc_trunk)
        self.send(self.loc_title, timestr)
        self.driver.switch_to.frame(self.findElement(self.iframe))
        self.send(self.loc_body, "aa")
        self.driver.switch_to.default_content()
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        self.click(self.loc_tijiao)
        # if self.is_success(timestr):
        #     return 1
        # else:
        #     return 0


    def bug_list_title(self):
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:81/zentao/bug-browse-11.html")

        time.sleep(2)
        try:
            # self.click(self.loc_product_choose)
            # self.click(self.loc_admin_p)
            ele = self.findElements(self.loc_buglist)
            print(ele)
            t1 = ele[0].text
            print(t1)
            return t1
        except:
            return ''

    def new_get_text(self, _text):
        self.driver.maximize_window()
        r = self.is_text_in_element(self.loc_bug_first, _text=_text)
        return r


if __name__ == '__main__':
    import selenium.webdriver as webdriver
    driver = webdriver.Chrome()
    lo = LoginPage(driver)
    lo.login()
    add = AddBug(driver)
    timestr = str(time.time())
    print(timestr)
    add.addBug(timestr)
    r1 = add.new_get_text(timestr)
    print("新方法的结果： %s"% r1)
    assert r1 == timestr
    driver.quit()