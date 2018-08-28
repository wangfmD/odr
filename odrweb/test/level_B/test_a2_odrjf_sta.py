# coding: utf-8
import sys
import unittest
from time import sleep

from odrweb.core.initdata import users
from odrweb.core.page.disputepage import DisputePage
from odrweb.core.page.homepage import HomePage

reload(sys)
sys.setdefaultencoding("utf-8")

jf_info = {"jf_desc": u"假冒商品",
           "jf_appeal": u"假一赔十",
           "applicant": u"徐传珠",
           "applicant_tel": "15295745648",
           "applicant_id": "321281199507077775",
           "applicant_addr": u"addr",
           "disputer": u"钱桂林",
           "disputer_tel": "13160077223"
           }


class OdrJfInput(unittest.TestCase):
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

    def test_03_tjy_commit(self):
        '''调解员登记纠纷'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        disputepage = DisputePage(self.homepage)
        disputepage.dispute_tjy_commit(**jf_info)
        res = disputepage.verification_dispute_tjy_commit(jf_info['jf_desc'])
        self.assertEqual(True, res)

    def test_04_tjy_save(self):
        '''调解员登记纠纷保存'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        disputepage = DisputePage(self.homepage)
        disputepage.dispute_tjy_save(**jf_info)
        res = disputepage.verification_dispute_tjy_save(jf_info['jf_desc'])
        self.assertEqual(True, res)

    def test_05_tjy_to_save(self):
        '''调解员登记纠纷保存'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        disputepage = DisputePage(self.homepage)
        disputepage.dispute_tjy_save(**jf_info)
        disputepage.dispute_tjy_save_commit()
        res = disputepage.verification_dispute_tjy_commit(jf_info['jf_desc'])
        self.assertEqual(True, res)

    def test_06_user_to_commit(self):
        '''用户登记纠纷'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        from odrweb.core.page.personalpage import PersonalPage
        personalpage = PersonalPage(self.homepage)
        personalpage.apply_mediate()
        personalpage.verification_apply_mediate("test")



if __name__ == '__main__':
    unittest.main()
