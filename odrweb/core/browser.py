# -*- coding:utf-8 -*-
from initdata import init
from selenium import webdriver
from logger import logger


class SingleTon(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingleTon, cls).__new__(cls, *args, **kwargs)
            logger.info("init webdriver browser")
        else:
            logger.info("already existed browser")
        return cls._instance


class Browser(SingleTon):
    if init.execEnv['execType'] == 'local':
        driver = webdriver.Chrome()
        driver.implicitly_wait(4)
        verificationErrors = []
        accept_next_alert = True
        logger.info("local webdriver...")
    else:
        browser = webdriver.DesiredCapabilities.CHROME
        driver = webdriver.Remote(
            command_executor=init.execEnv['remoteUrl'],
            desired_capabilities=browser)
        driver.implicitly_wait(4)
        verificationErrors = []
        accept_next_alert = True
        logger.info(" remote webdriver...")


if __name__ == '__main__':
    b1 = Browser()
    chrome = b1.driver
    print "vist baidu"
    chrome.get('http://www.baidu.com')
    import time
    time.sleep(4)
    b2 = Browser()
    chrome2 = b2.driver
    print "vist sina"
    chrome2.get('http://www.sina.com.cn')
