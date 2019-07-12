#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 16:07
# @Author  : Yuquan
# @Site    : 
# @File    : Base.py
# @Software: PyCharm

from appium import webdriver.webdriver

class Base(object):
    def __init__(self, driver:webdriver.webdriver):
        self.driver = driver


    def findelement(self):
        pass

    def findelements(self):
        pass

    def getSize(self):
        '''获取屏幕尺寸'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipeLeft(self,times=1):
        '''向左滑动'''
        for i in range(times):
            l = self.getSize()
            x1 = l[0]*0.9
            y1 = l[-1]*0.5
            x2 = l[0]*0.1
            self.driver.swipe(x1, y1, x2, y1)

        print('向左滑动%d次' % times)




if __name__ == '__main__':
    import time
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
    b = Base(driver)
    b.swipeLeft(times=3)
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.haimai.baletu:id/btn_skip")').click()
    time.sleep(4)
    driver.find_element_by_android_uiautomator('resourceId("com.haimai.baletu:id/tv_hot_city_name").text("上海市")').click()
    driver.quit()
