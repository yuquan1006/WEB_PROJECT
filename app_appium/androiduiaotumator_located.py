#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 10:45
# @Author  : Yuquan
# @Site    : 
# @File    : androiduiaotumator_located.py
# @Software: PyCharm
from appium import webdriver
import time
desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="5.1.1"
desired_caps["deviceName"]="VivoX7——c0ecfa65"
desired_caps["appPackage"]="com.aiwuyu.awy"
desired_caps["appActivity"]="com.aiwuyu.awy.business.modules.splash.FFSplashActivity"
desired_caps["appWaitDuration"] = 30
desired_caps["noReset"] = 'true' # 不要在会话前重置应用状态。默认值false
# desired_caps["app"] = ""  # app .apk文件路径  比如/abs/path/to/my.apk或http://myapp.com/app.ipa

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(2)
# driver.find_element_by_id("com.aiwuyu.awy:id/tab_home_personal").click()
# 通过AndroidUiAutomator定位元素

# 0.通过text定位
# driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
# 如果文本比较长，可以用textContains模糊匹配
# driver.find_element_by_android_uiautomator('new UiSelector().textContains("我的")').click()
# 用textStartsWith是以某个文本开头来匹配
driver.find_element_by_android_uiautomator('new UiSelector().textStartsWith("我")').click()

# 1.通过resourceId_id
# driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.aiwuyu.awy:id/tab_home_personal")').click()

# 2.通过classname定位
# driver.find_elements_by_android_uiautomator('new UiSelector().className("android.widget.TextView")')[2]  # 页面上的class属性一般不唯一，多半用在复数定位时候。此时定位相应下标

# 3..description也是用contenet-des属性定位
# driver.find_element_by_android_uiautomator('new UiSelector().description("contenet-des属性")')

# 4.组合定位
# 点击注册/登录按钮
driver.find_element_by_android_uiautomator('text("注册/登录").resourceId("com.aiwuyu.awy:id/tv_auth_or_user")').click()
# driver.find_element_by_android_uiautomator('resourceId("com.aiwuyu.awy:id/tv_auth_or_user").text("注册/登录")').click()
# driver.find_element_by_android_uiautomator('className("android.widget.TextView").text("图书")')


# 5.关系定位
# 5.1 父子定位childSelector
# driver.find_element_by_android_uiautomator('resourceId("com.aiwuyu.awy:id/bottom_tabs").childSelector(text("我的"))')
# 5.2 兄弟定位
# driver.find_element_by_android_uiautomator('resourceId("com.aiwuyu.awy:id/tab_home_main").fromParent(text("我的"))').click()
# driver.find_element_by_android_uiautomator('')


# 点击qq登录
# time.sleep(2)
driver.find_element_by_android_uiautomator('resourceId("com.aiwuyu.awy:id/lyt_3rd_qq").childSelector(className("android.widget.ImageView"))').click()
# e1 = e1.find_element_by_class_name('android.widget.ImageView').click()
# qq登录界面点击授权
driver.find_element_by_android_uiautomator('resourceId("com.tencent.mobileqq:id/name").text("授权并登录")').click()
time.sleep(2)
driver.quit()
