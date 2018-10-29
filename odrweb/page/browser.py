# -*- coding: utf-8 -*-
import datetime
import os
import sys
import time

from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

from odrweb.core.initdata import init

# chrome =webdriver.Chrome()
# chrome.save_screenshot()

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
            start = datetime.datetime.now()
            print("###start:{}".format(start))
            try:
                return f(*args)
            except Exception as msg:
                print "EXCEPTION >> {}".format(msg)

                day = time.strftime('%Y%m%d%H', time.localtime(time.time()))
                screenshot_path = os.path.join(REPORT_PATH, 'screenshot_%s' % day)
                if not os.path.exists(screenshot_path):
                    os.makedirs(screenshot_path)

                tm = time.strftime('%H%M%S', time.localtime(time.time()))
                # 去换行，去空格
                docstr = f.__doc__.replace('\n', '').replace('\r', '').strip()

                if isinstance(docstr, str):
                    docstr = docstr.decode('utf8')
                name = "".join([f.__name__, "_", docstr])
                file_name = os.path.join(screenshot_path, '%s_%s.png' % (name, tm))
                print "截图为：", file_name
                print "\n"
                res = args[0].homepage.driver.save_screenshot(file_name)

                raise
            finally:
                end = datetime.datetime.now()
                duration = (end - start).seconds
                print "###  end:{}, case duration: {}s ###".format(end, duration)

        inner.__doc__ = f.__doc__
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

        try:
            screenshot = self.driver.save_screenshot(file_name)
        except UnexpectedAlertPresentException as msg:
            # alert_ = self.driver.switch_to_alert()
            self.driver.switch_to.alert.accept()
            # alert_.accept()
            screenshot = self.driver.save_screenshot(file_name)
        except Exception as msg:
            print "###{}###".format(msg)
            raise

        print "###截图为：{}".format(file_name)
        if not screenshot:
            print "###screen_shot failed###"
        print "\n"
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

        self.driver.implicitly_wait(2)

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
