#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 9:35
# @Author  : Yuquan
# @Site    : 
# @File    : debug.py
# @Software: PyCharm
from selenium import webdriver
from common.base import Base
from page.pageElements.loginPageElement import *
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver = Base(driver)
driver.openUrl("http://www.moiiee.com/#/user-sign/sign-in")
driver.send(loc_userBox, UserName)
driver.send(loc_passwdBox, PassWord)
driver.click(loc_loginButton)
a = ('xpath', ("//a[text()='男装']"))
driver.click(a)
b = (By.CSS_SELECTOR, ".home-image")
driver.action_move(b)
loc_manFirstLeimu = (By.XPATH, "//li[@class='active-li']/div/span[@class='active-children']")    # 男装下毛衫
# driver.js_focus_element(loc_manFirstLeimu)
driver.click(loc_manFirstLeimu)


# driver.close()

# if __name__ == '__main__':
# #     js = '$x(\'//*[text()="男装"]\')[0].click()'
# #     print(js)