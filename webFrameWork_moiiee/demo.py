#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/20 13:50
# @Author  : OldFish
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from common.base import Base

driver = webdriver.Chrome()
driver.get(r"C:/Users/A/Desktop/1.html")
a = driver.find_element_by_class_name('article-content')
text = '''[01]：xx\n
    [02]:xxx

'''
a.send_keys(text)
# driver.find_element_by_css_selector('x').parent
# driver = Base(driver)
# driver.openUrl("http://www.baidu.com")
# # driver.find_element_by_id('kw').send_keys(u'中国')
# # driver.find_element_by_name("wd").send_keys(u'中国')
# # driver.find_element_by_class_name("s_ipt").send_keys(u'中国')
# # driver.find_element_by_tag_name("input").send_keys(u'中国')
# # driver.find_element_by_link_text("学术").click()
# # driver.find_element_by_partial_link_text("术").click()
# # driver.find_element_by_xpath(".//*[@id='kw']").send_keys(u'中国')
# driver.send((By.ID,"kw"),"seleniumm")
# ele = (By.CSS_SELECTOR,'.s_ipt')
# driver.keyboard(ele,Keys.BACK_SPACE)
# time.sleep(3)
# driver.quit()


# driver.openUrl("https://mail.126.com/")
# # driver.switch_frame_by_index(0)
# driver.switch_frame(0)
# # driver.switch_frame_by_id()
# driver.sendKeys((By.CLASS_NAME,'j-inputtext'),'1234565')
# time.sleep(3)
# driver.quit()



from selenium.webdriver.support.select import Select
# url = "https://www.baidu.com"
# driver.openUrl(url)
# time.sleep(3)
# mouse = driver.findElement(("link text", "设置"))
# driver.action_move(("link text", "设置"))
# # ActionChains(driver).move_to_element(mouse).perform()
# time.sleep(3)
# # driver.click()
# driver.findElement(("link text", "搜索设置")).click()
# time.sleep(3)
# # 定义元素
# # driver.findElement((By.XPATH,"//select[@id='nr']/option[2]")).click()
# # select模块处理
# # driver.select_by_index((By.ID,'nr'),1)
# print(driver.is_elements_exsit((By.ID,'nr')))
# driver.select_by_value((By.ID,'nr'),'50')
# time.sleep(3)
# driver.click((By.CSS_SELECTOR,'.prefpanelgo'))
# driver.keyboard((By.CSS_SELECTOR,'.prefpanelgo'),Keys.ENTER)
# a = driver.findElement((By.CSS_SELECTOR,'.prefpanelgo'))
# a.click()
# driver.click((By.CSS_SELECTOR,'.prefpaneldgo'))
# time.sleep(2)
# driver.acceptAlert()
# time.sleep(2)


# driver.quit()



# driver.findElement((By.XPATH,'//*[@id="kw"]/../span')).click()
# time.sleep(2)
#
# driver.quit()


errordescription='\n『产品名称』不能为空。'
a = '『产品名称』不能为空。'
print(errordescription)
print(len(a))
