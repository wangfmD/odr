# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver

TYPES = {'firefox': webdriver.Firefox,
         'chrome': webdriver.Chrome,
         'ie': webdriver.Ie,
         'phantomjs': webdriver.PhantomJS}

class UnSupportBrowserTypeError(Exception):
    pass

dir = os.path.dirname
home_path = dir(dir(os.path.abspath(dir(__file__))))

REPORT_PATH= os.path.join(home_path, "report")

class Browser(object):
    def __init__(self, browser_type='firefox'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError(u'仅支持%s!' % ', '.join(TYPES.keys()))
        self.driver = None

    def get(self, url, maximize_window=True, implicitly_wait=30):
        self.driver = self.browser()
        self.driver.get(url)
        if maximize_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

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

if __name__ == '__main__':
    print(REPORT_PATH)