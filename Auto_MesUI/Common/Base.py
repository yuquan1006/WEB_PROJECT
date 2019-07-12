#!/usr/bin/python
# -*- coding: utf-8 -*-
# Version : py3.6
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException,TimeoutException,ElementNotSelectableException
import os,time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import Config.config as gc
from Common.logCmd import LogHandler


log = LogHandler(__name__)
class Base(object):
    '''基于原生的selenium做二次封装'''

    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver
        self.timeout = 10
        self.t = 1

    def findElement(self, locator,types = 'location'):
        '''
        定位元素，参数locator是元祖类型.没定位到，Timeout异常
        :param locator: locator=(By.ID,"XXX")
        :param timeout:
        :return: driver.find_element(locator)
        '''
        if not isinstance(locator, tuple):
            # log.info('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
            log.error('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                '''
                元素在页面的三种状态：
                1.不在dom里，也就是不存在这个元素
                2.在dom里，隐藏元素，也不是不显示is_dispaly ---False
                3.在dom里，显示元素，页面上能看到is_dispaly ---True
                '''

                # 1.presence_of_element_located： 当我们不关心元素是否可见，只关心元素是否存在在页面中。
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
                # 2.visibility_of_element_located： 当我们需要找到元素，并且该元素也可见。
                # ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.visibility_of_element_located(locator))
                # 执行js，使滚动条下滑至a元素位置
                self.js_focus_element(ele)
                log.debug("定位元素信息成功：定位方式->%s, value值->%s"%(locator[0], locator[1]))
                return ele

            except UnexpectedAlertPresentException:
                log.error('定位失败->%s, value值->%s 原因：页面alert弹出来啦'%(locator[0], locator[1]))
                self.get_Screenshots()
                if types == 'location':
                    self.get_Screenshots()
                raise
            except TimeoutException:
                log.error('定位失败->%s, value值->%s 原因：定位元素超时啦'%(locator[0], locator[1]))
                self.get_Screenshots()
                if types == 'location':
                    self.get_Screenshots()
                raise
            except ElementNotSelectableException:
                log.error('定位失败->%s, value值->%s 原因：不是select，不能用select方法'%(locator[0], locator[1]))
                self.get_Screenshots()
                if types == 'location':
                    self.get_Screenshots()
                raise
            except Exception as msg:
                # log.info('定位元素异常 Reason:%s' % msg)
                log.error('定位失败->%s, value值->%s  可能原因 :%s' %(locator[0], locator[1],str(msg).replace("\n","")))
                if types == 'location':
                    self.get_Screenshots()
                raise


    def findElementOld(self, locator):

        if not isinstance(locator, tuple):
            log.error('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
            # log.info('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                # log.info("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))  # *号是把两个参数分开传值
                log.debug("定位元素信息成功：定位方式->%s, value值->%s"%(locator[0], locator[1]))

                return ele
            except Exception as e:
                # log.info("定位元素异常! Reason:%s" % e)
                log.error('element not Found ! Reason:%s' % str(e).replace("\n",""))
                self.get_Screenshots()
                raise


    def findElements(self,locator,types='locator'):
        '''定位一组元素'''
        if not isinstance(locator, tuple):
            log.error('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        try:
            elements = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_all_elements_located(locator))
            # elements = WebDriverWait(self.driver,self.timeout,1).until(EC.visibility_of_any_elements_located(locator))
            log.debug("定位一组元素信息成功：定位方式->%s, value值->%s" % (locator[0], locator[1]))
            return elements
        except Exception as msg:
            # log.info (u'异常原因%s'%msg)
            log.error('elements not Found ! Reason:%s' % str(msg).replace("\n", ""))
            if types == 'locator':
                self.get_Screenshots()
            raise


    def findElementsOld(self, locator):
        if not isinstance(locator, tuple):
            # log.info('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
            log.error('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')

        else:
            try:
                # log.info("正在定位一组元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
                eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
                log.debug("定位一组元素信息成功：定位方式->%s, value值->%s"%(locator[0], locator[1]))

                return eles
            except Exception as e:
                # log.info("定位一组元素异常! Reason:%s" % e)
                log.error('elements not Found ! Reason:%s' % str(e).replace("\n",""))
                self.get_Screenshots()
                raise

    def parent_child_position(self,parent_locator,child_locator):
        '''   父子节点，进行二次定位 '''
        result = self.findElement(parent_locator).findElement(child_locator)
        return result



    def sendKeys(self, locator, text,is_clear=False):
        '''输入内容 is_clear默认为False，不清空输入框'''
        element = self.findElement(locator)
        if is_clear:
            element.clear()
        element.send_keys(text)
        log.info('开始对%s元素 [输入文本]：%s'%(locator,text))

    def click(self, locator):
        '''点击元素'''
        element = self.findElement(locator)
        element.click()
        log.info('开始对%s元素  [点击]'%str(locator))

    #针对一组元素进行的操作
    def clicks(self,locator):
        elements = self.findElements(locator)
        for i in elements:
            i.click()

    def clear(self,locator):
        element = self.findElement(locator)
        element.clear()


    def get_text(self,locator):
        '''获取文本'''
        element = self.findElement(locator)
        return element.text

    def get_attribute(self,locator,name):
        '''获取属性'''
        element = self.find_element(locator)
        return element.get_attribute(name)




     # ********** 浏览器的基本操作
    def openUrl(self, url, title='', timeout=10):
        '''使用get打开URL后，最大化窗口，判断title符合预期'''
        self.driver.get(url)
        self.driver.maximize_window()
        log.info('打开网址：%s '%url)
        # self.driver.implicitly_wait(20)
        # try:
        #     WebDriverWait(self.driver, timeout, 1).until(EC.title_contains(title))
        # except TimeoutException:
        #     log.info('open %s title error' % url)
        # except Exception as msg:
        #     log.info('Error:%s' % msg)


    def clearCookies(self):
        '''清楚cookies'''
        self.driver.delete_all_cookies()
        log.info("清除当前缓存")

    def quit(self):
        '''quit the driver and close all    the windows'''
        self.driver.quit()
        log.info("退出浏览器")

    def close(self):
        '''driver.close()'''
        self.driver.close()
        log.info("关闭当前窗口浏览器")

    def get_title(self):
        '''  获取title'''
        return self.driver.title

    def getUrl(self):
        return self.driver.current_url

    def implicitlyWait(self,secs):
        self.driver.implicitly_wait(secs)

    def refresh(self):
        '''刷新当前页面'''
        self.driver.refresh()

    def back(self):
        ''' 返回上一页 '''
        self.driver.back()

    def maximizeWindow(self):
        '''窗口最大化'''
        self.driver.maximize_window()

    def set_windows_size(self, width, height):
        ''' 设置浏览器大小 '''
        self.driver.set_window_size(width, height)

    def get_Screenshots(self):
        ''' 屏幕截图 '''
        try:
            self.driver.get_screenshot_as_file(gc.screenName)
            log.info("屏幕截图成功！文件为:%s" % gc.screenName)
            # log.info("屏幕截图成功！文件为:%s" % gc.screenName)
        except BaseException as e:
            log.info(gc.screenName)
            log.error("屏幕截图失败！Reason:%s" % e)
            # log.info("屏幕截图失败！Reason:%s" % e)




    # ********** JS 处理
    def js_execute(self, js):
        '''执行js'''
        self.driver.execute_script(js)

    def js_focus_element(self, ele):
        '''聚焦元素 直接让想要定位的元素出现在屏幕最上面 '''
        # target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        # log.info('聚焦元素成功')


    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTop(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''
        滚动到底部  scrollTo方法第一个参数是横向坐标（左右），0代表起点， 第二个参数纵向坐标（上下），0代表起点，10000是终点
        :return:
        '''
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def js_scroll_choose(self,x=0, y=0):
        js = "window.scrollTo(0,1000)"
        self.driver.execute_script(js)



    # ******* Swtich——to
    def swith_first_handle(self):
        try:
            handles = self.driver.window_handles
            fist_handles = handles[0]
            self.driver.switch_to.window(fist_handles)
        except Exception as e:
            log.info(" 切换至第一个handles异常! Reason：%s" % e)

    def swith_new_handle(self):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != self.driver.current_window_handle:
                # self.driver.close()
                self.driver.switch_to.window(handle)

    def switch_frame(self, locator):
        ''' locator可以为id/索引定位 也可以元素定位的元祖 '''
        try:
            # frame_to_be_available_and_switch_to_it 来判断iframe是否存在并切换进去
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.frame_to_be_available_and_switch_to_it(locator))
            log.info('成切换到iframe框架中')
            return result
        except Exception as e:
            log.info("切换iframe异常! Reason:%s" % e)
            self.get_Screenshots()
            raise

    def switch_to_defaultFrame(self):
        '''跳出所有frame,回到主界面'''
        self.driver.switch_to.default_content()
        log.info('跳出所有frame,回到主界面')
    def switch_to_parentFrame(self):
        '''返回上一级iframe'''
        self.driver.switch_to.parent_frame()
        log.info(' 返回上一级iframe')



    # 下拉框  locator 是下拉框的元素定位
    def select_by_index(self,locator,index):
        '''通过索引，index是索引的第几个，从0开始'''
        element = self.findElement(locator)
        Select(element).select_by_index(index)


    def select_by_value(self,locator,value):
        '''通过value属性进行选择下拉框选项'''
        element = self.findElement(locator)
        Select(element).select_by_value(value)


    def select_by_text(self,locator,text):
        '''通过文本值定位'''
        element = self.findElement(locator)
        Select(element).select_by_visible_text(text)

    # alert
    def acceptAlert(self):
        '''点击确定'''
        self.driver.switch_to.alert.accept()
        # log.info('Base - >点击系统弹框的确定按钮')
        # log.info('Click the ok button in the system popup box')


    def dismissAlert(self):
        '''取消'''
        self.driver.switch_to.alert.dismiss()
        log.info('点击系统弹框的取消按钮')
        # log.info('Click the cancel button in the system popup box')

    def getAlertText(self):
        '''获取弹出框文本'''
        text = self.driver.switch_to.alert.text
        log.info(' 开始获取系统弹出框文本：%s'%text)
        return text

    def send_Alert(self, _text):
        '''输入值'''
        self.driver.switch_to.alert.send_keys(_text)


    # ********** 鼠标键盘事件
    def action_move(self, locator):
        ''' 鼠标移动/悬停 '''
        try:
            element = self.findElement(locator)
            ActionChains(self.driver).move_to_element(element).perform()
        except BaseException as e:
            log.info("鼠标移动/悬停异常！ Reason:%s" % e)

    def action_slide(self,locator,offset=500):
        '''鼠标滑动'''
        try:
            element = self.findElement(locator)
            a = ActionChains(self.driver)
            a.click_and_hold(element)
            a.move_by_offset(offset, 0)
            a.release().perform()
            log.info("页面进行滑动")
        except BaseException as e:
            log.info("鼠标滑动异常！ Reason:%s" %e)



    def action_click(self, locator):
        ''' 鼠标右击 '''
        try:
            element = self.findElement(locator)
            ActionChains(self.driver).context_click(element).perform()
        except BaseException as e:
            log.info("鼠标右击异常！ Reason:%s" % e)

    def action_double_click(self, locator):
        ''' 鼠标双击 '''
        try:
            element = self.findElement(locator)
            ActionChains(self.driver).context_click(element).perform()
        except BaseException as e:
            log.info("鼠标双击异常！ Reason:%s" % e)

    def action_drag_and_drop(self, locator1, locator2):
        ''' 鼠标拖动 '''
        try:
            element1 = self.findElement(locator1)
            element2 = self.findElement(locator2)
            actions = ActionChains(self.driver).drag_and_drop(element1, element2).perform()
        except BaseException as e:
            log.info("鼠标拖动异常！ Reason:%s" % e)

    def keyboard(self, locator, operation=Keys.ENTER):
        ''' 键盘事件，operation=模拟的键盘值 Keys. '''
        try:
            elememt = self.findElement(locator)
            self.sendKeys(locator, *operation)
        except BaseException as e:
            log.info("键盘事件异常！ Reason:%s" % e)



    # ****** 判断类方法：等待（WDwait）与判断（ec）结合，循环判断成功返回True，失败会抛超时异常。所以根据是否用异常来判断

    def find(self, locator):
        '''
        定位元素，参数locator是元祖类型.没定位到超时异常
        '''
        if not isinstance(locator, tuple):
            # log.info('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
            log.error('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        else:
            try:
                # log.info("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
                # 1.presence_of_element_located： 当我们不关心元素是否可见，只关心元素是否存在在页面中。
                ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
                # 2.visibility_of_element_located： 当我们需要找到元素，并且该元素也可见。
                # ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.visibility_of_element_located(locator))
                log.info("正在定位元素信息：定位方式->%s, value值->%s"%(locator[0], locator[1]))
                return ele
            except Exception as msg:
                # log.info('定位元素未找到！ Reason:%s' % msg)
                log.error('element not Found ! Reason:%s' % str(msg).replace("\n",""))

    def is_element_exsit(self, locator):
        '''查找元素是否存在 返回bool值'''
        try:
            element = self.findElement(locator,types='judge')
            return True
        except:
            return False

    def is_elements_exsit(self, locator):
        '''查找一组元素是否存在 返回bool值  复数定位elements，定位不到就返回空list，不会抛异常'''
        element = self.findElements(locator,types="judge")
        count = len(element)
        if count == 0:
            return  False
        elif count == 1:
            return True
        else:
            log.info("元素个数：%s" % count)
            return True

    def is_title(self,_title):
        ''' 判断title完全等于 返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False



    def is_title_contains(self, _title):
        '''判断title包含 返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, _text):
        '''判断文本是否在元素里 返回bool值'''
        if not isinstance(locator, tuple):
            log.info('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False


    def is_value_in_element(self, locator, _value=''):
        '''判断元素value值  返回bool值, value为空字符串，返回Fasle'''
        if not isinstance(locator, tuple):
            log.info('locator参数类型错误，必须传元祖类型：loc = ("id", "value1")')
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, _value))
            return result
        except:
            return False

    def is_alert_parsent(self, timeout=3):
        '''当前是否有alert弹出框 有返回alert(注意这里是返回alert,不是True)  没有返回False'''
        try:
            result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def is_selected(self, locator):
        ''' 判断元素是否选中，一般用于下拉列表'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.element_located_to_be_selected(locator))
            return result
        except:
            return False

    def is_selected_be(self,locator,selected=True,timeout=10):
        '''判断元素的状态，selected是期望参数true或者false返回布尔值'''
        if not isinstance(selected, bool):
            log.info("selected参数类型错误，必须传bool类型：selected=True")
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(
                EC.element_located_selection_state_to_be(locator, selected))
            return result
        except:
            return False

    def is_visibility(self,locator,timeout=10):
        '''判断页面元素存在且可见返回元素，不可见返回False'''
        try:
            result = WebDriverWait(self.driver,timeout,1).until(EC.visibility_of_element_located(locator))
            return result
        except:
            return False

    def is_located(self,locator,timeout=10):
        '''
        判断元素有没有在dom中(并不意味着可见)，定位到返回element,没有定位到返回False
        :param locator:
        :param timeout:
        :return:
        '''
        try:
            result = WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))
            return result
        except:
            return False

    def is_invisibility(self,locator,timeout=10):
        '''判断页面元素不存在或不可见返回元素，可见返回False'''
        try:
            result = WebDriverWait(self.driver,timeout,1).until(EC.invisibility_of_element_located(locator))
            return result
        except:
            return False


    def is_clicked(self, locator):
        ''' 判断元素是可以点击的，可以返回ele，不可以返回False'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.element_to_be_clickable(locator))
            return result
        except:
            return False

    def is_links(self, _url):
        '''判断Url是否相等'''
        try:
            self.swith_new_handle()
            result = self.getUrl()
            log.info(_url)
            log.info(result)
            assert result==_url, 'URl不相等'
            self.swith_new_handle()
            return True
        except:
            log.info(_url)
            return False






if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:81/zentao/user-moiiee-L3plbnRhby8=.html")
    zentao = Base(driver)
    # loc1 = (By.ID, "account")
    # loc2 = (By.CSS_SELECTOR, "[name='password']")
    # loc3 = (By.XPATH, "//*[@id='submit']")

    loc1 = ("id", "account")
    loc2 = ("css selector", "[name='password']")
    loc3 = ("xpath", "//*[@id='submit']")
    zentao.send(loc1, "admin")
    zentao.send(loc2, "123456")
    zentao.click(loc3)

    # zentao.move_to_element()




    # zentao.sendKeys(loc1, "admin")
    # zentao.sendKeys(loc2, "123456")

    # log.info(11111111111)
    #
    # r = zentao.is_alert()
    # log.info(r)
    # log.info(2222222222222)


