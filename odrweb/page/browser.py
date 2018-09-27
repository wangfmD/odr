# -*- coding: utf-8 -*-
import os
import sys
import time

from selenium import webdriver
from odrweb.core.initdata import init

TYPES = {'firefox': webdriver.Firefox,
         'chrome': webdriver.Chrome,
         'ie': webdriver.Ie,
         'phantomjs': webdriver.PhantomJS}


class UnSupportBrowserTypeError(Exception):
    pass




dir = os.path.dirname
home_path = dir(dir(os.path.abspath(dir(__file__))))

REPORT_PATH = os.path.join(home_path, "report")


class Browser(object):
    def __init__(self, browser_type=None):
        if browser_type:
            self._type = browser_type.lower()
            if self._type in TYPES:
                self.browser = TYPES[self._type]
                self.driver = self.browser()


                print "Browser:", browser_type
            else:
                raise UnSupportBrowserTypeError(u'仅支持%s!' % ', '.join(TYPES.keys()))
        else:
            self.driver = None

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = REPORT_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()


class Page(Browser):

    def __init__(self, page=None, browser_type=init.browser):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__(browser_type=browser_type)

        self.driver.implicitly_wait(5)

        if sys.platform == 'darwin':
            self.driver.set_window_size(1849,1001)
        else:
            try:
                self.driver.maximize_window()
            except:
                print("Window has be maxsize")

    def get_driver(self):
        return self.driver
    #
    # def find_element(self, *args):
    #     return self.driver.find_element(*args)
    #
    # def find_elements(self, *args):
    #     return self.driver.find_elements(*args)

    def find_element_by_xpath(self, *args):
        try:
            el = self.driver.find_element_by_xpath(*args)
        except:
            time.sleep(0.5)
            try:
                el = self.driver.find_element_by_xpath(*args)
            except:
                time.sleep(0.5)
                try:
                    el = self.driver.find_element_by_xpath(*args)
                except:
                    time.sleep(0.5)
                    try:
                        el = self.driver.find_element_by_xpath(*args)
                    except:
                        time.sleep(0.5)
                        el = self.driver.find_element_by_xpath(*args)
        return el

    def find_element_by_css_selector(self, *args):
        return self.driver.find_element_by_css_selector(*args)

    def find_element_by_link_text(self,*args):
        return self.driver.find_element_by_link_text(*args)

    def find_elements_by_xpath(self,*args):
        return self.driver.find_elements_by_xpath(*args)






class HomePage(Page):

    def baidu(self):
        self.driver.get("http://www.baidu.com")
        time.sleep(10)


class UserPage(Page):

    def sina(self):
        self.driver.get("http://www.sina.com")
        time.sleep(10)


def tt():
    homepage = HomePage()
    homepage.baidu()
    userpage = UserPage(homepage)
    userpage.sina()



if __name__ == '__main__':
    # tt()
    print TYPES