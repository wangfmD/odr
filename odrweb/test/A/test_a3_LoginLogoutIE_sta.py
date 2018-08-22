# coding: utf-8
import unittest

import sys

from odrweb.core.model.homepage_IE11 import HomePage
from odrweb.core.initdata import users

reload(sys)
sys.setdefaultencoding("utf-8")

class TenantMgr(unittest.TestCase):
    '''租户管理场景'''

    def setUp(self):
        self.homepage = HomePage()

    def tearDown(self):
        self.homepage.quit()


    def test_13_login_yun(self):
        '''云解中心登录'''
        self.homepage.login_yun(users.user_wfm['username'], users.user_wfm['pwd'])
        result = self.homepage.login_yun_verification()
        self.assertEqual(result, True)

    def test_14_login_yun_quit(self):
        '''云解中心账号登出'''
        self.homepage.login_yun(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.login_yun_quit()
        result = self.homepage.login_yun_quit_verification()
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
