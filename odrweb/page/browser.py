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

try:
    SE = {'se360': webdriver.se360}
    TYPES.update(SE)
except:
    pass


class UnSupportBrowserTypeError(Exception):
    pass


dir = os.path.dirname
home_path = dir(os.path.abspath(dir(__file__)))

REPORT_PATH = os.path.join(home_path, "report")


class Screen(object):
    """这个应该截图功能的装饰器"""

    def __init__(self):
        self.driver = None

    def __call__(self, f):
        def inner(*args):
            try:
                return f(*args)
            except Exception as msg:
                print "EXCEPTION >> {}".format(msg)
                day = time.strftime('%Y%m%d%H', time.localtime(time.time()))
                screenshot_path = os.path.join(REPORT_PATH, 'screenshot_%s' % day)
                if not os.path.exists(screenshot_path):
                    os.makedirs(screenshot_path)

                tm = time.strftime('%H%M%S', time.localtime(time.time()))
                name = "".join([f.__name__, "_", f.__doc__.decode('utf8')])
                file_name = os.path.join(screenshot_path, '%s_%s.png' % (name, tm))
                print "截图为：", file_name
                res = args[0].homepage.driver.save_screenshot(file_name)

                raise

        return inner


class Browser(object):
    def __init__(self, browser_type=None):
        if browser_type:
            self._type = browser_type.lower()
            if self._type in TYPES:
                self.browser = TYPES[self._type]
                self.driver = self.browser()
            else:
                raise UnSupportBrowserTypeError(u'仅支持%s!' % ', '.join(TYPES.keys()))
        else:
            self.driver = None

    def save_screen_shot(self, name='screen_shot'):
        """截图
        """
        day = time.strftime('%Y%m%d%H', time.localtime(time.time()))
        screenshot_path = os.path.join(REPORT_PATH, 'screenshot_%s' % day)
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        file_name = os.path.join(screenshot_path, '%s_%s.png' % (name, tm))
        # screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.png' % (name, tm))
        screenshot = self.driver.save_screenshot(file_name)

        if screenshot:
            print file_name
        else:
            print "screen_shot failed"
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
            self.driver.set_window_size(1849, 1001)
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

    def find_element_by_link_text(self, *args):
        return self.driver.find_element_by_link_text(*args)

    def find_elements_by_xpath(self, *args):
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
    # homepage.baidu()
    # userpage = UserPage(homepage)
    # userpage.sina()
    print homepage.save_screen_shot("dd的")
    #
    # dr = webdriver.Chrome()
    # dr.save_screenshot()


if __name__ == '__main__':
    tt()
    # print REPORT_PATH
