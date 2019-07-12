#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
from selenium.webdriver.common.by import By

# url
LoginUrl = "http://127.0.0.1:81/zentao/user-login.html"
# 登录页面元素
loc_userBox = (By.CSS_SELECTOR, "#account")
loc_passwdBox = (By.CSS_SELECTOR, "[name='password']")
loc_keepRedio = (By.CSS_SELECTOR, "input#keepLoginon")
loc_loginButton = (By.CSS_SELECTOR, "#submit")
loc_forgetButton = (By.LINK_TEXT, "忘记密码")
   # 验证首页用户名
# 登录页面数据
UserName = "admin"
UserNameBlank = ' '                                                                         #用户名为空
UserNameWrong = 'yang@emotibot.com'                                                         #用户名错误
PassWord = '123456'                                                                       #密码
PassWordBlank = ' '                                                                         #密码为空
PassWordWrong = '341234123'                                                                 #密码错误
loc_verifyUserName = (By.CSS_SELECTOR, "div#userMenu>a")                                    #验证登录用户名是否正确
PromptInformation = "登录失败，请检查您的用户名或密码是否填写正确。"                               #账号密码错误提示信息：
UserNameBlankAssert = (By.XPATH,".//*[@id='log']/ul/li[1]/span/b")                          #账号为空提示信息
ClosePromptInformation = (By.CLASS_NAME, 'ivu-btn')                                          #关闭提示信息框，点击【确定】按钮
PassWordBlankAssert = (By.XPATH,".//*[@id='log']/ul/li[2]/span/b")                          #密码为空提示信息


