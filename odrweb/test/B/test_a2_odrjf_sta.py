# coding: utf-8
import sys
import unittest

from odrweb.core.initdata import users
# from odrweb.page.disputepage import DisputePage
from odrweb.page.homepage import HomePage
from odrweb.page.personalpage import PersonalPage

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
    '''纠纷登记'''

    def setUp(self):
        self.homepage = HomePage()
        print "\n--------------------"

    def tearDown(self):
        self.homepage.quit()

    # def test_01(self):
    #     '''登记员保存纠纷并提交'''
    #     self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
    #     disputepage = DisputePage(self.homepage)
    #     disputepage.dispute_djy_save(**jf_info)
    #     res = disputepage.dispute_djy_commit_verification(jf_info['jf_desc'])
    #     self.assertEqual(True, res)

    # def test_02(self):
    #     '''登记员登记纠纷'''
    #     self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
    #     disputepage = DisputePage(self.homepage)
    #     disputepage.dispute_djy_commit(**jf_info)
    #     res = disputepage.dispute_djy_commit_verification(jf_info['jf_desc'])
    #     self.assertEqual(True, res)

    # def test_03(self):
    #     '''调解员登记纠纷'''
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     disputepage = DisputePage(self.homepage)
    #     disputepage.dispute_tjy_commit(**jf_info)
    #     res = disputepage.verification_dispute_tjy_commit(jf_info['jf_desc'])
    #     self.assertEqual(True, res)

    # def test_04(self):
    #     '''调解员登记纠纷保存'''
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     disputepage = DisputePage(self.homepage)
    #     disputepage.dispute_tjy_save(**jf_info)
    #     res = disputepage.verification_dispute_tjy_save(jf_info['jf_desc'])
    #     self.assertEqual(True, res)

    # def test_05(self):
    #     '''调解员登记纠纷保存'''
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     disputepage = DisputePage(self.homepage)
    #     disputepage.dispute_tjy_save(**jf_info)
    #     disputepage.dispute_tjy_save_commit()
    #     res = disputepage.verification_dispute_tjy_save(jf_info['jf_desc'])
    #     self.assertEqual(True, res)

    def test_01(self):
        ''' 用户-我要调解'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.apply_mediate()
        personalpage.verification_apply_mediate("test")

    def test_02(self):
        '''用户-我要评估'''
        # 测试数据
        jf_consult = {"jf_type": u"消费维权",
                      "jf_desc": u"假冒商品",
                      "jf_appeal": u"假一赔十"}
        # 执行
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()

        personalpage = PersonalPage(self.homepage)
        personalpage.evaluate(**jf_consult)
        # 验证
        result = personalpage.verification_evaluate(jf_consult["jf_desc"])
        self.assertEqual(True,result)


    def test_03(self):
        '''用户-我要咨询'''
        jf_consult = {"jf_type": u"消费维权",
                      "jf_desc": u"假冒商品",
                      "jf_appeal": u"假一赔十"}
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.consult(**jf_consult)
        self.homepage.user_personal_center()
        personalpage.verification_consult(jf_consult['jf_desc'])


if __name__ == '__main__':
    unittest.main()
