# coding: utf-8
import sys
import unittest
from time import sleep

from odrweb.core.initdata import users
from odrweb.page.homepage import HomePage
from odrweb.page.personalpage_one import PersonalPage

reload(sys)
sys.setdefaultencoding("utf-8")

t = 2


class OdrJfInput(unittest.TestCase):
    '''纠纷登记'''

    def setUp(self):
        self.homepage = HomePage()
        print "\n--------------------"

    def tearDown(self):
        pass
        # self.homepage.quit()

    def test_01(self):
        '''登记纠纷提交-申自然人-被自然人'''
        jf_info_all = {"jf_desc": u"登记纠纷提交-申自然人-被自然人",
                       "applicant_type": u"自然人",  # 自然人 法人 非法人组织
                       "disputer_type": u"自然人",  # 自然人 法人 非法人组织
                       "agent_type": "",  # "" common special,
                       "agent_b_type": "",  # common special,

                       "jf_appeal": u"假一赔十",
                       "applicant_name": u"企业或机构名称",  #
                       "world_credit_id": "abcde1234567890",
                       "applicant": u"王发明",
                       "applicant_tel": "13913031374",
                       "applicant_id": "",
                       "applicant_addr": u"1栋2单元303",

                       "disputer": u"徐传珠",
                       "disputer_tel": "15295745648",
                       "disputer_world_credit_id": "zxcvbnmasdfghjk123",
                       "disputer_name": u"企业或机构名称",
                       "disputer_id": "",
                       "disputer_addr": u"10栋1单元101",

                       "agent_name": u"钱桂林",
                       "agent_tel": "13160077223",
                       "agent_id": "321281199507077775",

                       "agent_b_name": u"段志勇",
                       "agent_b_tel": "15895996954",
                       "agent_b_id": ""
                       }

        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        sleep(0.5)
        personalpage = PersonalPage(self.homepage)
        personalpage._input_all(**jf_info_all)

    def test_02(self):
        '''登记纠纷提交-申自然人-被法人'''
        jf_info_all = {"jf_desc": u"登记纠纷提交-申自然人-被法人",
                       "applicant_type": u"自然人",  # 自然人 法人 非法人组织
                       "disputer_type": u"法人",  # 自然人 法人 非法人组织
                       "agent_type": "",  # "" common special,
                       "agent_b_type": "",  # common special,

                       "jf_appeal": u"假一赔十",
                       "applicant_name": u"企业或机构名称",  #
                       "world_credit_id": "abcde1234567890",
                       "applicant": u"王发明",
                       "applicant_tel": "13913031374",
                       "applicant_id": "",
                       "applicant_addr": u"1栋2单元303",

                       "disputer": u"徐传珠",
                       "disputer_tel": "15295745648",
                       "disputer_world_credit_id": "zxcvbnmasdfghjk123",
                       "disputer_name": u"企业或机构名称",
                       "disputer_id": "",
                       "disputer_addr": u"10栋1单元101",

                       "agent_name": u"钱桂林",
                       "agent_tel": "13160077223",
                       "agent_id": "321281199507077775",

                       "agent_b_name": u"段志勇",
                       "agent_b_tel": "15895996954",
                       "agent_b_id": ""
                       }

        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        sleep(0.5)
        personalpage = PersonalPage(self.homepage)
        personalpage._input_all(**jf_info_all)

    def test_03(self):
        '''登记纠纷提交-申自然人-被非法人组织'''
        jf_info_all = {"jf_desc": u"登记纠纷提交-申自然人-被非法人组织",
                           "applicant_type": u"自然人",  # 自然人 法人 非法人组织
                           "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
                           "agent_type": "",  # "" common special,
                           "agent_b_type": "",  # common special,

                           "jf_appeal": u"假一赔十",
                           "applicant_name": u"企业或机构名称",  #
                           "world_credit_id": "abcde1234567890",
                           "applicant": u"王发明",
                           "applicant_tel": "13913031374",
                           "applicant_id": "",
                           "applicant_addr": u"1栋2单元303",

                           "disputer": u"徐传珠",
                           "disputer_tel": "15295745648",
                           "disputer_world_credit_id": "zxcvbnmasdfghjk123",
                           "disputer_name": u"企业或机构名称",
                           "disputer_id": "",
                           "disputer_addr": u"10栋1单元101",

                           "agent_name": u"钱桂林",
                           "agent_tel": "13160077223",
                           "agent_id": "321281199507077775",

                           "agent_b_name": u"段志勇",
                           "agent_b_tel": "15895996954",
                           "agent_b_id": ""
                           }

        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        sleep(0.5)
        personalpage = PersonalPage(self.homepage)
        personalpage._input_all(**jf_info_all)

if __name__ == '__main__':
    unittest.main()
