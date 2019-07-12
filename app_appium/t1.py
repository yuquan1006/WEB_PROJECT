#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 15:39
# @Author  : Yuquan
# @Site    : 
# @File    : t1.py
# @Software: PyCharm

# coding=utf-8

from appium import webdriver
import time
# 初始化
desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="5.1.1"
desired_caps["deviceName"]="Vivoy20"
desired_caps["appPackage"]="com.android.bbkcalculator"
desired_caps["appActivity"]="com.android.bbkcalculator.Calculator"
desired_caps["noReset"] = 'true' # 不要在会话前重置应用状态。默认值false
# desired_caps["app"] = ""  # app .apk文件路径  比如/abs/path/to/my.apk或http://myapp.com/app.ipa

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 定位方法
#  1.通过id定位元素  resrouce-id属性是id
# driver.find_element_by_id("com.android.bbkcalculator:id/mul").click()

# 通过ClassName定位元素 class属性是classname
# driver.find_element_by_class_name("android.widget.ImageButton")
# driver.find_element_by_name("")   # .通过name定位元素 text属性是name
# driver.find_element_by_xpath("//*[@class='android.widget.LinearLayout']/ImageButton[@]").click()  # Appium对于xpath定位执行效率是比较低的，一般情况下尽量不用这个定位方式。
# driver.find_element_by_css_selector("xx") # 通过css_selector定位（webview） 只适用于webview的html页面，继承自webdriver，与pc版本的UI测试一致
# driver.find_element_by_accessibility_id("")  # 5.通过AccessibilityId定位元素 content-desc的值
# driver.find_element_by_link_text("xx")  # 通过link_text定位（webview）只适用于webview容器中的html页面，继承自webdriver，与pc版本的UI测试一致
# 层级定位

# 通过AndroidUiAutomator定位元素 AndroidUIAutomator是一个强有力的元素定位方式，它是通过Android UIAutomator类库去找元素，可以选择id、name、className作为传入的字符串
# driver.find_element_by_android_uiautomator("new UiSelector().text('空')") # 见下一py文件

# 定位混合应用元素 混合应用是原生APP+webview组成的，可以简单的理解为一个原生app的外壳，内部全是html页面。在处理这样的app的定位的时候 需要先定位原生APP上的按钮或者链接，然后点击按钮或者链接，然后经过appium提供的方法，进入webview页面，通过之前介绍的定位工具和方法进行元素定位了。如果说你的android版本小于4.4，那么你需要使用Selendroid模式来作为测试引擎，在测试初始化的时候需要设置该capability。如果你的android版本大于等于4.4，那么Appium作为测试引擎，然后通过chromedriver来处理webview。如果你使用的是APPIUM测试引擎，调试WebView需要满足安卓系统版本为Android 4.4+已上，并且需要在你的APP内配置相应的代码，在WebView类中调用静态方法setWebContentsDebuggingEnabled，如下：


time.sleep(2)

driver.quit()
