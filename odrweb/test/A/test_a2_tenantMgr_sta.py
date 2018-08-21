# coding: utf-8
import unittest

import sys

from odrweb.core.model.homepage import HomePage
from odrweb.core.initdata import users

reload(sys)
sys.setdefaultencoding("utf-8")

class TenantMgr(unittest.TestCase):
    '''租户管理场景'''

    def setUp(self):
        self.homepage = HomePage()

    def tearDown(self):
        self.homepage.quit()

    def test_01_user_login(self):
        u'''普通用户登录'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_login_verification()

    def test_02_user_login_quit(self):
        u'''普通用户登出'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_login_quit()
        result = self.homepage.user_login_quit_verification()
        self.assertEqual(result,True)

    def test_03_mediator_login_tiaojy(self):
        '''调解员登录'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        result = self.homepage.mediator_login_verification()
        self.assertEqual(result, True)

    def test_04_mediator_quit_tiaojy(self):
        '''调解员登出'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        self.homepage.mediator_quit()
        result = self.homepage.mediator_login_quit_sverification()
        self.assertEqual(result, True)
    #
    def test_05_mediator_login_banafg(self):
        '''办案法官登录'''
        self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
        result = self.homepage.mediator_bafg_login_verification()
        self.assertEqual(result, True)

    def test_06_mediator_quit_banafg(self):
        '''办案法官登出'''
        self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
        self.homepage.mediator_quit_bafg()
        result = self.homepage.mediator_login_quit_sverification()
        self.assertEqual(result, True)

    def test_07_organization_user_login(self):
        '''机构登记员登录'''
        self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
        result = self.homepage.organization_user_login_verification()
        self.assertEqual(result, True)

    def test_08_organization_user_quit(self):
        '''机构登记员登出'''
        self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
        self.homepage.organization_user_login_quit()
        result = self.homepage.organization_user_login_quit_verification()
        self.assertEqual(result, True)

    def test_09_organization_login(self):
        '''机构登录北明心理咨询'''
        self.homepage.organization_login(users.user_bmxlzxysxxjg['username'], users.user_bmxlzxysxxjg['pwd'])
        result = self.homepage.organization_login_verification()
        self.assertEqual(result, True)

    def test_10_organization_quit(self):
        '''机构登出北明心理咨询'''
        self.homepage.organization_login(users.user_bmxlzxysxxjg['username'], users.user_bmxlzxysxxjg['pwd'])
        self.homepage.organization_login_quit()
        result = self.homepage.organization_login_quit_verfication()
        self.assertEqual(result, True)

    def test_11_customer_login(self):
        '''客服登录'''
        self.homepage.customer_login(users.user_kf['username'], users.user_kf['pwd'])
        result = self.homepage.customer_login_verification()
        self.assertEqual(result, True)

    def test_12_customer_quit(self):
        '''客服登出'''
        self.homepage.customer_login(users.user_kf['username'], users.user_kf['pwd'])
        self.homepage.customer_login_quit()
        result = self.homepage.customer_login_quit_verification()
        self.assertEqual(result, True)

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

    def test_15_organization_login_shenadmin(self):
        '''省级账号登录'''
        self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
        result = self.homepage.organization_login_verification()
        self.assertEqual(result, True)

    def test_16_organization_quit_shenadmin(self):
        '''省级账号登出'''
        self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
        self.homepage.organization_login_quit()
        result = self.homepage.organization_login_quit_verfication()
        self.assertEqual(result, True)

    def test_17_organization_login_shinadmin(self):
        '''市级账号登录'''
        self.homepage.organization_login(users.user_quadmin['username'], users.user_quadmin['pwd'])
        result = self.homepage.organization_login_verification()
        self.assertEqual(result, True)

    def test_18_organization_quit_shinadmin(self):
        '''市级账号登出'''
        self.homepage.organization_login(users.user_quadmin['username'], users.user_quadmin['pwd'])
        self.homepage.organization_login_quit()
        result = self.homepage.organization_login_quit_verfication()
        self.assertEqual(result, True)

    def test_19_organization_login_quadmin(self):
        '''西湖区级账号登录'''
        self.homepage.organization_login(users.user_quadmin['username'], users.user_quadmin['pwd'])
        result = self.homepage.organization_login_verification()
        self.assertEqual(result, True)

    def test_20_organization_quit_quadmin(self):
        '''西湖区级账号登出'''
        self.homepage.organization_login(users.user_quadmin['username'], users.user_quadmin['pwd'])
        self.homepage.organization_login_quit()
        result = self.homepage.organization_login_quit_verfication()
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
