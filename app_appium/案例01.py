#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 9:15
# @Author  : Yuquan
# @Site    : 
# @File    : 案例01.py
# @Software: PyCharm
# baletu
from appium import webdriver
import time
from app_appium.common.Base import Base
# 初始化
def login():
    '''不使用缓存登录'''

    desired_cpas = {}
    desired_cpas["platformName"] = "Android"
    desired_cpas["platformVersion"] = "5.1.1"
    desired_cpas["deviceName"] = "test_BLT"
    desired_cpas["appPackage"] = "com.haimai.baletu"
    desired_cpas["appActivity"] = "com.haimai.main.activity.SplashActivity"
    desired_cpas["noReset"] = "false"
    desired_cpas["unicodeKeyboard"] = "false"
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cpas)
    time.sleep(5)
    driver = Base(driver)
    driver.swipeLeft(times=3)
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.haimai.baletu:id/btn_skip")').click()
    time.sleep(4)
    driver.find_element_by_android_uiautomator('resourceId("com.haimai.baletu:id/tv_hot_city_name").text("上海市")').click()
    driver.quit()
    # 点击我的
    driver.find_elements_by_android_uiautomator('resourceId("com.haimai.baletu:id/rg_main_tab").childSelector(className("android.widget.RadioButton"))')[1].click()
    # 点击账户登录
    driver.find_element_by_android_uiautomator('resourceId("com.haimai.baletu:id/rbLogin_nor").text("账号登录")').click()
    time.sleep(1)
    # 输入手机号
    driver.find_element_by_android_uiautomator('resourceId("com.haimai.baletu:id/login_phone").text("手机号")').send_keys(
        name)
    # 输入密码
    driver.find_element_by_android_uiautomator(
        'new UiSelector().resourceId("com.haimai.baletu:id/login_smsCode_et")').send_keys("123456")
    # 点击登录
    driver.find_element_by_android_uiautomator('resourceId("com.haimai.baletu:id/login_btn").text("登录")').click()
    # 点击我的，查看登录是否成功
    driver.find_element_by_android_uiautomator('resourceId("com.haimai.baletu:id/rb_wode").text("我的")').click()

    try:
        e = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.haimai.baletu:id/mine_phone")')
        # print(e.text)
        print('登录验证定位成功！')

    except BaseException as e:
        print('登录验证定位失败！')
    driver.quit()

def login2():
    '''使用缓存登录'''
    desired_cpas = {}
    desired_cpas["platformName"] = "Android"
    desired_cpas["platformVersion"] = "5.1.1"
    desired_cpas["deviceName"] = "test_BLT"
    desired_cpas["appPackage"] = "com.haimai.baletu"
    desired_cpas["appActivity"] = "com.haimai.main.activity.SplashActivity"
    desired_cpas["noReset"] = "true"
    desired_cpas["unicodeKeyboard"] = "false"

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cpas)
    time.sleep(5)
    name = "18973019192"
    wd = "123456"
    # 点击首页我的按钮
    # driver.find_element_by_android_uiautomator('resourceId("com.haimai.baletu:id/rb_wode").text("我的")').click()
    # driver.find_element_by_id("com.haimai.baletu:id/rg_main_tab").find_elements_by_class_name("android.widget.RadioButton")[3].click()
    driver.find_elements_by_android_uiautomator('resourceId("com.haimai.baletu:id/rg_main_tab").childSelector(className("android.widget.RadioButton"))')[1].click()
    time.sleep(1)
    # 点击账户登录
    driver.find_element_by_android_uiautomator('resourceId("com.haimai.baletu:id/rbLogin_nor").text("账号登录")').click()
    time.sleep(1)
    # 输入手机号
    driver.find_element_by_android_uiautomator('resourceId("com.haimai.baletu:id/login_phone").text("手机号")').send_keys(name)
    # 输入密码
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.haimai.baletu:id/login_smsCode_et")').send_keys("123456")
    # 点击登录
    driver.find_element_by_android_uiautomator('resourceId("com.haimai.baletu:id/login_btn").text("登录")').click()
    # 点击我的，查看登录是否成功
    driver.find_element_by_android_uiautomator('resourceId("com.haimai.baletu:id/rb_wode").text("我的")').click()

    try:
        e = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.haimai.baletu:id/mine_phone")')
        # print(e.text)
        print('登录验证定位成功！')

    except BaseException as e:
        print('登录验证定位失败！')

    # 退出登录
    # 点击账户设置
    driver.find_element_by_android_uiautomator('resourceId("com.haimai.baletu:id/account_setting_ll").className("android.widget.RelativeLayout")').click()
    time.sleep(3)

    # 点击退出登录
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.haimai.baletu:id/mine_exit")').click()
    time.sleep(3)
    driver.quit()
if __name__ == '__main__':
    login()