# -*- coding: utf-8 -*-
import unittest

from odrweb.core.initdata import users
from odrweb.page.homepage import HomePage

class OdrLoginAndQuit(unittest.TestCase):
    '''用户登录登出'''

    def setUp(self):
        self.homepage = HomePage()

    def tearDown(self):
        self.homepage.quit()

    def test_01(self):
        '''普通用户登录'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_login_verification()

    def test_02(self):
        '''普通用户登出'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_login_quit()
        result = self.homepage.user_login_quit_verification()
        self.assertEqual(result,True)

    def test_03(self):
        '''调解员登录'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        result = self.homepage.mediator_login_verification()
        self.assertEqual(result, True)

    def test_04(self):
        '''调解员登出'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        self.homepage.mediator_quit()
        result = self.homepage.mediator_login_quit_sverification()
        self.assertEqual(result, True)
    #
    def test_05(self):
        '''办案法官登录'''
        self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
        result = self.homepage.mediator_bafg_login_verification()
        self.assertEqual(result, True)

    def test_06(self):
        '''办案法官登出'''
        self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
        self.homepage.mediator_quit_bafg()
        result = self.homepage.mediator_login_quit_sverification()
        self.assertEqual(result, True)

    def test_07(self):
        '''机构登记员登录'''
        self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
        result = self.homepage.organization_user_login_verification()
        self.assertEqual(result, True)

    def test_08(self):
        '''机构登记员登出'''
        self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
        self.homepage.organization_user_login_quit()
        result = self.homepage.organization_user_login_quit_verification()
        self.assertEqual(result, True)

    def test_09(self):
        '''机构登录北明心理咨询'''
        self.homepage.organization_login(users.user_bmxlzxysxxjg['username'], users.user_bmxlzxysxxjg['pwd'])
        result = self.homepage.organization_login_verification()
        self.assertEqual(result, True)

    def test_10(self):
        '''机构登出北明心理咨询'''
        self.homepage.organization_login(users.user_bmxlzxysxxjg['username'], users.user_bmxlzxysxxjg['pwd'])
        self.homepage.organization_login_quit()
        result = self.homepage.organization_login_quit_verfication()
        self.assertEqual(result, True)

    def test_11(self):
        '''客服登录'''
        self.homepage.customer_login(users.user_kf['username'], users.user_kf['pwd'])
        result = self.homepage.customer_login_verification()
        self.assertEqual(result, True)

    def test_12(self):
        '''客服登出'''
        self.homepage.customer_login(users.user_kf['username'], users.user_kf['pwd'])
        self.homepage.customer_login_quit()
        result = self.homepage.customer_login_quit_verification()
        self.assertEqual(result, True)

    def test_13(self):
        '''云解中心登录'''
        self.homepage.login_yun(users.user_wfm['username'], users.user_wfm['pwd'])
        result = self.homepage.login_yun_verification()
        self.assertEqual(result, True)

    def test_14(self):
        '''云解中心账号登出'''
        self.homepage.login_yun(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.login_yun_quit()
        result = self.homepage.login_yun_quit_verification()
        self.assertEqual(result, True)

    def test_15(self):
        '''省级账号登录'''
        self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
        result = self.homepage.organization_login_verification()
        self.assertEqual(result, True)

    def test_16(self):
        '''省级账号登出'''
        self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
        self.homepage.organization_login_quit()
        result = self.homepage.organization_login_quit_verfication()
        self.assertEqual(result, True)

    def test_17(self):
        '''市级账号登录'''
        self.homepage.organization_login(users.user_quadmin['username'], users.user_quadmin['pwd'])
        result = self.homepage.organization_login_verification()
        self.assertEqual(result, True)

    def test_18(self):
        '''市级账号登出'''
        self.homepage.organization_login(users.user_quadmin['username'], users.user_quadmin['pwd'])
        self.homepage.organization_login_quit()
        result = self.homepage.organization_login_quit_verfication()
        self.assertEqual(result, True)

    def test_19(self):
        '''西湖区级账号登录'''
        self.homepage.organization_login(users.user_quadmin['username'], users.user_quadmin['pwd'])
        result = self.homepage.organization_login_verification()
        self.assertEqual(result, True)

    def test_20(self):
        '''西湖区级账号登出'''
        self.homepage.organization_login(users.user_quadmin['username'], users.user_quadmin['pwd'])
        self.homepage.organization_login_quit()
        result = self.homepage.organization_login_quit_verfication()
        self.assertEqual(result, True)

    def test_21(self):
        '''咨询师登录'''
        self.homepage.counselor_login(users.user_zxs['username'], users.user_zxs['pwd'])
        self.homepage.counselor_login_verification()

    def test_22(self):
        '''咨询师登出'''
        self.homepage.counselor_login(users.user_zxs['username'], users.user_zxs['pwd'])
        self.homepage.counselor_quit()
        self.homepage.counselor_quit_verification()

    def test_23(self):
        '''普通用户头部登录'''
        self.homepage.user_head_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_login_verification()

    def test_24(self):
        '''普通用户头部登出'''
        self.homepage.user_head_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_head_login_quit()
        result = self.homepage.user_login_quit_verification()
        self.assertEqual(result,True)



if __name__ == '__main__':
    unittest.main()
