# coding=utf-8

import json
import os
import shutil
import socket
import time
import unittest

import requests

from utils import sendReportWithAtt
from generateHtml.file_os import HTMLFileRunner
from generateHtml.HTMLTestRunner import HTMLTestRunner
from logger import logger
from tools import cfg

# from HTMLTestRunner import HTMLTestRunner
home_path = cfg.home_path


class TestRunner:
    """doc"""

    def __init__(self, generateHtmlType="no", email=None):
        if email is None:
            from webmgr.common.initdata import init
            self.receiver = init.email
        else:
            self.receiver = email
        logger.info("report email receivers : {}".format(self.receiver))
        self.generateHtmlType = generateHtmlType
        self.homePath = home_path

        self.test_dir = '.'
        self.discover = unittest.defaultTestLoader.discover(
            self.test_dir, pattern='*_sta.py')
        # 设置测试报告路径
        self.reportPath = os.path.join(self.homePath, "report")

        if os.path.exists(self.reportPath) is True:
            print " Report Path is {path}".format(path=self.reportPath)
        else:
            print "The report path is not exist,create report directory..."
            os.mkdir(self.reportPath)

    def run(self):

        version = ""
        sql_Add = ""
        from webmgr.common.initdata import init
        try:
            try:
                # 获取init.db_conf[]
                sql_Add = init.db_conf["hostadd"]
                strs = requests.get(
                    "http://" + sql_Add + "/middleclient/version", timeout=5)
                # print sql_Add
                s = json.loads(strs.text)
                version = 'middleclient_' + s['version']
            except AttributeError:
                sql_Add = "init.db_conf Configuration is not read"
                # 获取init.db_conf[]
        except:
            version = "version Timeout!"

        self.now = time.strftime("%Y-%m-%d%H%H%S")
        restult = 'web_' + self.now + '_restult.html'
        self.filename = os.path.join(self.reportPath, restult)

        with open(self.filename, 'wb') as fp:
            runner = HTMLTestRunner(
                stream=fp,
                title=u'管理平台功能测试',
                description=u'用例执行情况：',
                sqlAdd=sql_Add,
                version_add=version)
            # runner = HTMLTestRunner(
            #     stream=fp,
            #     title='测试报告',
            #     description='用例执行情况：')
            runner.run(self.discover)
            sendReportWithAtt(self.filename, self.receiver)

        if self.generateHtmlType == 'is':
            folderPath = "Z:\\reports\\"
            if os.path.exists(folderPath):
                hostname = socket.gethostname()
                mkdirFolder = folderPath + socket.gethostbyname(
                    hostname) + "report\\"
                if not os.path.exists(mkdirFolder):
                    os.mkdir(mkdirFolder)
                shutil.copy(self.filename, mkdirFolder)
                HTMLFileRunner(
                    title='测试报告 ', description='用例执行情况：').generatr(folderPath)
            else:
                print "没有挂在nas到本地请挂在！"


if __name__ == '__main__':
    # runner = TestRunner('dev_wf_57', 'is', '')
    # print runner.reportPath
    # runner.run()
    from webmgr.common.initdata import init
    print init.email
