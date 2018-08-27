# coding: utf-8
import unittest

import sys

from odrweb.core.page.homepage import HomePage
from odrweb.core.initdata import users
from odrweb.core.page.disputepage import DisputePage

reload(sys)
sys.setdefaultencoding("utf-8")

jf_info = {"jf_desc": u"假冒商品",
           "jf_appeal": u"假一赔十",
           "applicant": u"徐传珠",
           "applicant_tel": "15295745648",
           "applicant_id": "321281199507077775",
           "applicant_addr": u"addr",
           "Disputer": u"钱桂林",
           "disputer_tel": "13160077223"
           }


class OdrLoginAndQuit(unittest.TestCase):
    '''平台用户登录登出'''

    def setUp(self):
        self.homepage = HomePage()

    def tearDown(self):
        self.homepage.quit()

    def test_01_djy_save_commit(self):
        '''登记员保存纠纷并提交'''
        self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
        disputepage = DisputePage(self.homepage)
        disputepage.dispute_djy_save(**jf_info)
        res = disputepage.dispute_djy_commit_verification(jf_info['jf_desc'])
        self.assertEqual(True, res)

    def test_02_djy_commit(self):
        '''登记员登记纠纷'''
        self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
        disputepage = DisputePage(self.homepage)
        disputepage.dispute_djy_commit(**jf_info)
        res = disputepage.dispute_djy_commit_verification(jf_info['jf_desc'])
        self.assertEqual(True, res)

if __name__ == '__main__':
    unittest.main()
