# coding: utf-8
import datetime
import sys
import unittest
from inspect import getdoc, getframeinfo, currentframe
from time import sleep

from odrweb.core.initdata import users
from odrweb.core.utils import _funcname_docstring
from odrweb.page.homepage import HomePage
from odrweb.page.jfpersonalpage import PersonalPage


reload(sys)
sys.setdefaultencoding("utf-8")

t = 2


class UserApply(unittest.TestCase):
    """用户纠纷登记-申请人"""
    dispute_info = {
        "jf_appeal": u"假一赔十",
        "applicant_name": u"申企业或机构名称",  #
        "world_credit_id": "abcde1234567890",
        "applicant": u"王发明",
        "applicant_pwd": "11111111",
        "applicant_tel": "13913031374",
        "applicant_id": "",
        "applicant_addr": u"1栋2单元303",

        "disputer": u"徐传珠",
        "disputer_tel": "15295745648",
        "disputer_world_credit_id": "zxcvbnmasdfghjk123",
        "disputer_name": u"被申企业或机构名称",
        "disputer_id": "",
        "disputer_addr": u"10栋1单元101",

        "agent_name": u"钱桂林",
        "agent_tel": "13160077223",
        "agent_id": "321023199508166636",

        "agent_b_name": u"段志勇",
        "agent_b_tel": "15895996954",
        "agent_b_id": ""
    }
    case_id = ''
    homepage = None

    @classmethod
    def setUpClass(cls):
        cls.homepage = HomePage()

    @classmethod
    def tearDownClass(cls):
        cls.homepage.driver.quit()

    def setUp(self):
        self.start = datetime.datetime.now()
        print "Browser type: {}".format(self.homepage._type)
        print "\n--------------------"

    def tearDown(self):
        self.homepage.quit()

    def test_01(self):
        """用户-登记纠纷-申自然人-被自然人"""
        jf_info_all = {"jf_desc": u"用户-登记纠纷-申自然人-被自然人",
                       "applicant_type": u"自然人",  # 自然人 法人 非法人组织
                       "disputer_type": u"自然人",  # 自然人 法人 非法人组织
                       "agent_type": "",  # "" common special,
                       "agent_b_type": ""  # common special,
                       }
        jf_info_all.update(self.dispute_info)

        try:
            self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
            self.homepage.user_personal_center()
            sleep(0.5)
            personalpage = PersonalPage(self.homepage)
            personalpage._input_all(**jf_info_all)
            sleep(t)
            res, UserApply.case_id = personalpage.verfication_commit_dlr(**jf_info_all)
            self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)

    def test_02(self):
        """用户撤回案件"""
        try:
            self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
            self.homepage.user_personal_center()
            sleep(0.5)
            from odrweb.page.personalpage import PersonalPage
            personalpage = PersonalPage(self.homepage)
            page = PersonalPage(personalpage)
            page.act_dispute_search(UserApply.case_id)
            page.act_case_revocation()
            # 查询撤回纠纷，验证
            page.driver.refresh()
            page.act_dispute_search(UserApply.case_id)
            res = page.verfc_case_revocation()
            self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)

    def test_03(self):
        """用户-登记纠纷-申自然人特殊代理人-被自然人特殊代理人"""
        jf_info_all = {"jf_desc": u"用户-登记纠纷-申自然人特殊代理人-被自然人特殊代理人",
                       "applicant_type": u"自然人",  # 自然人 法人 非法人组织
                       "disputer_type": u"自然人",  # 自然人 法人 非法人组织
                       "agent_type": "special",  # "" common special,
                       "agent_b_type": "special"  # common special,

                       }
        jf_info_all.update(self.dispute_info)

        try:
            self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
            self.homepage.user_personal_center()
            sleep(0.5)
            personalpage = PersonalPage(self.homepage)
            personalpage._input_all(**jf_info_all)
            sleep(t)
            res, _ = personalpage.verfication_commit_dlr(**jf_info_all)
            self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)

            # def test_03(self):
            #     """用户-登记纠纷-申法人-被非法人组织"""
            #     jf_info_all = {"jf_desc": u"用户-登记纠纷-申法人-被非法人组织",
            #                    "applicant_type": u"自然人",  # 自然人 法人 非法人组织
            #                    "disputer_type": u"法人",  # 自然人 法人 非法人组织
            #                    "agent_type": "",  # "" common special,
            #                    "agent_b_type": ""  # common special,
            #
            #                    }
            #     jf_info_all.update(self.dispute_info)
            #
            #     try:
            #         self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
            #         self.homepage.user_personal_center()
            #         sleep(0.5)
            #         personalpage = PersonalPage(self.homepage)
            #         personalpage._input_all(**jf_info_all)
            #         sleep(t)
            #         personalpage.verfication_commit_dlr(**jf_info_all)
            #     except Exception as msg:
            #         print "EXCEPTION >> {}".format(msg)
            #         # class function name_class docstring
            #         docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            #         name = _funcname_docstring(self, docstr.decode('utf8'))
            #         # 截图
            #         self.homepage.save_screen_shot(name)
            #         raise
            #     finally:
            #         self.end = datetime.datetime.now()
            #         duration = (self.end - self.start).seconds
            #         print "###case duration: {}###".format(duration)
            #
            # def test_04(self):
            #     """用户-登记纠纷-申非法人组织特殊代理人-被法人代理人"""
            #     jf_info_all = {"jf_desc": u"用户-登记纠纷-申非法人组织特殊代理人-被法人代理人",
            #                    "applicant_type": u"非法人组织",  # 自然人 法人 非法人组织
            #                    "disputer_type": u"法人",  # 自然人 法人 非法人组织
            #                    "agent_type": "special",  # "" common special,
            #                    "agent_b_type": "special",  # common special,
            #                    # "mode": "agent",
            #                    }
            #     jf_info_all.update(self.dispute_info)
            #
            #     try:
            #         self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
            #         self.homepage.user_personal_center()
            #         sleep(0.5)
            #         personalpage = PersonalPage(self.homepage)
            #         personalpage._input_all(**jf_info_all)
            #         sleep(t)
            #         personalpage.verfication_commit_dlr(**jf_info_all)
            #     except Exception as msg:
            #         print "EXCEPTION >> {}".format(msg)
            #         # class function name_class docstring
            #         docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            #         name = _funcname_docstring(self, docstr.decode('utf8'))
            #         # 截图
            #         self.homepage.save_screen_shot(name)
            #         raise
            #     finally:
            #         self.end = datetime.datetime.now()
            #         duration = (self.end - self.start).seconds
    #         #         print "###case duration: {}###".format(duration)


if __name__ == '__main__':
    unittest.main()
