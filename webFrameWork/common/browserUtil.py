#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
import configparser,os
from selenium import webdriver
import config.globalConfig as gc
from common.logger import Logger
log = Logger("browserUtil")

class BrowserUtil(object):
    def open_browser(self):
        con = configparser.ConfigParser()
        con.read(gc.bsConfing, encoding="utf-8")
        browserName = con.get("browserType", "browserName")
        browserPath = con.get("browserType", "browserPath")
        print(browserPath)
        switch = con.get("guiStartType", "switch")
        if browserName == "Chrome":
            if switch == "off":
                option = webdriver.ChromeOptions()
                option.add_argument('headless')  # 静默模式
                self.driver = webdriver.Chrome(browserPath, chrome_options=option)
                # print("Starting Chrome browser")
                log.debug("Starting Chrome browser")
                self.driver.maximize_window()
                # print("Maximize the current window")
                log.debug("Maximize the current window")
                self.driver.implicitly_wait(10)
                # print("Set imlipcitly wait 10 second.")
                log.debug("Set imlipcitly wait 10 second.")
            else:
                self.driver = webdriver.Chrome(browserPath)
                # print("Starting Chrome browser")
                log.debug("Starting Chrome browser")
                self.driver.maximize_window()
                # print("Maximize the current window")
                log.debug("Maximize the current window")
                self.driver.implicitly_wait(10)
                # print("Set imlipcitly wait 10 second.")
                log.debug("Set imlipcitly wait 10 second.")


        elif browserName == "Firefox":
            self.driver = webdriver.Firefox()
            # print("Starting Firefox browser")
            log.debug("Starting Firefox browser")
            self.driver.maximize_window()
            # print("Maximize the current window")
            log.debug("Maximize the current window")
            self.driver.implicitly_wait(10)
            # print("Set imlipcitly wait 10 second.")
            log.debug("Set imlipcitly wait 10 second.")

        # self.driver.get("http://127.0.0.1:81/zentao/user-login.html")
        return self.driver

if __name__ == '__main__':
    A = BrowserUtil()
    a = A.open_browser()
    a.get("http://127.0.0.1:81/zentao/user-login.html")
    print(a.title)
    a.quit()



