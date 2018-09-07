# coding: utf-8
import sys
import unittest

from odrweb.core.initdata import users
# from odrweb.page.disputepage import DisputePage
from odrweb.page.homepage import HomePage
from odrweb.page.personalpage_one import PersonalPage_one

reload(sys)
sys.setdefaultencoding("utf-8")

jf_consult = {"jf_type": u"消费维权",
              "jf_desc": u"假冒商品",
              "jf_appeal": u"假一赔十",
              "jf_applyName": u"徐传珠",
              "jf_applyTel": '15295745648',
              "jf_applyNumber": '321281199507077775',
              "jf_appliedName": u"钱桂林",
              "jf_appliedTel": '13160077223',
              "jf_agentName": u"段志勇",
              "jf_agentTel":' 15895996954 ',
              "jf_organization": u"北明测试",
              "jf_societyNumber": '123456789123456789'}

class DifferentUserJfInput(unittest.TestCase):
    '''不同用户身份登记纠纷'''
    def setUp(self):
        self.homepage = HomePage()
        print "\n--------------------"

    def tearDown(self):
        self.homepage.quit()


    def test_01(self):
        '''申请人自然人，被申请人自然人'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage_one = PersonalPage_one(self.homepage)
        personalpage_one.user_sqr_natural_natural(personalpage_one)
        personalpage_one.verification_apply_uatural_mediate(jf_consult["jf_desc"])


    def test_02(self):
        '''申请人为自然人，被申请人为法人'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage_one = PersonalPage_one(self.homepage)
        personalpage_one.user_sqr_natural_logel(personalpage_one)
        personalpage_one.verification_apply_uatural_mediate(jf_consult["jf_desc"])


    def test_03(self):
        '''申请人为自然人，被申请人为非法人组织'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage_one = PersonalPage_one(self.homepage)
        personalpage_one.user_sqr_natural_organization()
        personalpage_one.verification_apply_uatural_mediate(jf_consult["jf_desc"])



    def test_04(self):
        '''申请人为法人，被申请人为自然人'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage_one = PersonalPage_one(self.homepage)
        personalpage_one.user_sqr_logel_natural()
        personalpage_one.verification_apply_organization_mediate(jf_consult["jf_organization"])


    def test_05(self):
        '''申请人为法人，被申请人为法人'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage_one = PersonalPage_one(self.homepage)
        personalpage_one.user_sqr_logel_logel(personalpage_one)
        personalpage_one.verification_apply_organization_mediate(jf_consult["jf_organization"])


    def test_06(self,**kwargs):
        '''申请人为法人，被申请人为法人组织'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage_one = PersonalPage_one(self.homepage)
        personalpage_one.user_sqr_logel_organization(personalpage_one)
        personalpage_one.verification_apply_organization_mediate(jf_consult["jf_organization"])


    def test_07(self):
        '''申请人为非法人组织，被申请人为自然人'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage_one = PersonalPage_one(self.homepage)
        personalpage_one.user_sqr_organization_natural(personalpage_one)
        personalpage_one.verification_apply_organization_mediate(jf_consult["jf_organization"])


    def test_08(self):
        '''申请人为非法人组织，被申请人为法人'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage_one = PersonalPage_one(self.homepage)
        personalpage_one.user_sqr_organization_logel(personalpage_one)
        personalpage_one.verification_apply_organization_mediate(jf_consult["jf_organization"])




    def test_09(self):
        '''申请人为非法人组织，被申请人非法人组织'''
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage_one = PersonalPage_one(self.homepage)
        personalpage_one.user_sqr_organization_logel(personalpage_one)
        personalpage_one.verification_apply_organization_mediate(jf_consult["jf_organization"])


if __name__ == '__main__':
    unittest.main()





