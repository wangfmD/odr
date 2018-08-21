# coding=utf-8

import os
import time
import unittest


# from odrweb.core.html.HTMLTestRunner import HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner
# from odrweb.core.generateHtml.HTMLTestRunner import HTMLTestRunner
dir = os.path.dirname
home_path = dir(os.path.abspath(dir(__file__)))



class TestRunner:
    """doc"""

    def __init__(self):
        self.homePath = home_path
        self.test_dir = '.'
        self.discover = unittest.defaultTestLoader.discover(self.test_dir, pattern='*_sta.py')
        # 设置测试报告路径
        self.reportPath = os.path.join(self.homePath, "report")

        if os.path.exists(self.reportPath) is True:
            print " Report Path is {path}".format(path=self.reportPath)
        else:
            print "The report path is not exist,create report directory..."
            os.mkdir(self.reportPath)

    def run(self):

        self.now = time.strftime("%Y-%m-%d%H%H%S")
        restult = 'odr_ui_' + self.now + '_restult.html'
        self.filename = os.path.join(self.reportPath, restult)

        with open(self.filename, 'wb') as fp:
            runner = HTMLTestRunner(
                stream=fp,
                title='ODR_browser_UI',
                description='aa：')
            runner.run(self.discover)


if __name__ == '__main__':
    print(home_path)