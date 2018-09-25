# -*- coding: utf-8 -*-
import unittest
from time import sleep
import sys
from odrweb.page.homepage import HomePage
from odrweb.page.OrganizationAdmin import OrganizationAdmin

reload(sys)
sys.setdefaultencoding("utf-8")

class OrganizationCaseOperation(unittest.TestCase):
    '''复数申请人'''
    def setUp(self):
        self.homepage = HomePage()

    def tearDown(self):
        self.homepage.quit()

    def test_01(self):
        '''机构管理员处理案件'''

        self.homepage.organization_login("5958234274", "123456")

