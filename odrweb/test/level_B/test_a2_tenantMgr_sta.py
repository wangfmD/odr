# coding: utf-8
import sys
import unittest
from time import sleep
from selenium import webdriver

from odrWeb.common.model.base_action import login, consult_input

class TenantMgr(unittest.TestCase):
    '''租户管理场景'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(8)
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()

    def test_add_consult(self):
        '''录入纠纷'''
        login(self.driver)
        consult_input(self.driver)

    def test_add_consult1(self):
        '''录入纠纷2'''
        login(self.driver)
        consult_input(self.driver)


if __name__ == '__main__':
    unittest.main()
