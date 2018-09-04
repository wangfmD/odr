# coding: utf-8
import sys
import unittest
from time import sleep

from odrweb.core.initdata import users
from odrweb.page.disputepage import DisputePageDjy, DisputePageTjy
from odrweb.page.homepage import HomePage

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
        self.homepage.quit()

    # def test_01(self):
        # '''机构登记员登记纠纷提交-申(被)请人自然人'''
        # jf_info_all = {"jf_desc": u"机构登记员登记纠纷提交-申(被)请人自然人",
        #                "applicant_type": u"自然人",  # 自然人 法人 非法人组织
        #                "disputer_type": u"自然人",  # 自然人 法人 非法人组织
        #                "agent_type": "",  # "" common special,
        #                "agent_b_type": "",  # common special,
        #
        #                "jf_appeal": u"假一赔十",
        #
        #                "applicant_name": u"企业或机构名称",  #
        #                "world_credit_id": "abcde1234567890",
        #                "applicant": u"王发明",
        #                "applicant_tel": "13013031374",
        #                "applicant_id": "320830198309064815",
        #                "applicant_addr": u"addr",
        #
        #                "disputer": u"徐传珠",
        #                "disputer_tel": "13800010001",
        #
        #                "agent_name": u"钱桂林",
        #                "agent_tel": "13160077111",
        #                "agent_id": "321023199508166636",
        #
        #                "agent_b_name": u"段志勇",
        #                "agent_b_tel": "15895996111",
        #                "agent_b_id": ""
        #                }
        # self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
        # disputepage = DisputePageDjy(self.homepage)
        # disputepage.commit(**jf_info_all)
        # sleep(t)
        # res = disputepage.verification_commit(**jf_info_all)
        # self.assertEqual(True, res)

    def test_02(self):
        '''调解员登记纠纷提交-申(被)请人自然人'''
        jf_info_all = {"jf_desc": u"机构登记员登记纠纷提交-申(被)请人自然人",
                       "applicant_type": u"自然人",  # 自然人 法人 非法人组织
                       "disputer_type": u"自然人",  # 自然人 法人 非法人组织
                       "agent_type": "",  # "" common special,
                       "agent_b_type": "",  # common special,

                       "jf_appeal": u"假一赔十",

                       "applicant_name": u"企业或机构名称",  #
                       "world_credit_id": "abcde1234567890",
                       "applicant": u"王发明",
                       "applicant_tel": "13013031374",
                       "applicant_id": "320830198309064815",
                       "applicant_addr": u"addr",

                       "disputer": u"徐传珠",
                       "disputer_tel": "13800010001",

                       "agent_name": u"钱桂林",
                       "agent_tel": "13160077111",
                       "agent_id": "321023199508166636",

                       "agent_b_name": u"段志勇",
                       "agent_b_tel": "15895996111",
                       "agent_b_id": ""
                       }
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        disputepage = DisputePageTjy(self.homepage)
        disputepage.commit(**jf_info_all)
        sleep(t)
        res = disputepage.verification_commit(**jf_info_all)
        self.assertEqual(True, res)

if __name__ == '__main__':
    unittest.main()
