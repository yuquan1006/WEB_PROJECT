#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
import configparser,os
from selenium import webdriver
import Config.config as gc
from Common.logCmd import LogHandler
log = LogHandler(__name__)

class BrowserUtil(object):
    '''浏览器类'''
    def open_browser(self):
        '''创建对应浏览器Driver'''
        con = configparser.ConfigParser()
        con.read(gc.bsConfing, encoding="utf-8")
        browserName = con.get("browserType", "browserName")
        switch = con.get("guiStartType", "switch")

        if browserName == "Chrome":
            if switch == "off":
                option = webdriver.ChromeOptions()
                option.add_argument('headless')  # 静默模式
                self.driver = webdriver.Chrome(options=option)
                log.debug("Starting Chrome browser")
                self.driver.maximize_window()
                log.debug("Maximize the current window")
            else:
                self.driver = webdriver.Chrome()
                log.debug("Starting Chrome browser")
                self.driver.maximize_window()
                log.debug("Maximize the current window")


        elif browserName == "Firefox":
            self.driver = webdriver.Firefox()
            log.debug("Starting Firefox browser")
            self.driver.maximize_window()
            log.debug("Maximize the current window")

        return self.driver

if __name__ == '__main__':
    A = BrowserUtil()
    a = A.open_browser()
    a.get("http://127.0.0.1:81/zentao/user-login.html")
    print(a.title)
    a.quit()



