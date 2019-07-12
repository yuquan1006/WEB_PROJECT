#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/26 9:07
# @Author  : Yuquan
# @Site    : 
# @File    : 163最新邮件.py
# @Software: PyCharm
from selenium import webdriver
import time

def readEmail():
    driver = webdriver.Chrome()
    driver.get("https://mail.163.com")
    time.sleep(3)
    driver.switch_to.frame(0)
    cur = driver.current_window_handle
    print(cur)
    driver.find_element_by_css_selector("input[name='email']").send_keys('yuquangetpost')
    driver.find_element_by_css_selector("input[name='password']").send_keys("714729yu")
    driver.find_element_by_css_selector("#dologin").click()
    driver.switch_to.default_content()
    driver.switch_to.window(cur)
    time.sleep(3)
    # driver.find_element_by_xpath("//div[text()='未读邮件']").click()
    driver.find_element_by_xpath("//ul[@role='tablist']/li[@title='收件箱']").click()
    time.sleep(200)
    driver.quit()

if __name__ == '__main__':
    readEmail()
