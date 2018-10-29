# coding: utf-8
import sys
import unittest
from inspect import getdoc, getframeinfo, currentframe
from time import sleep

import datetime

from odrweb.core.initdata import users
from odrweb.core.utils import _funcname_docstring
from odrweb.page.caselistpage import CaseListPage
from odrweb.page.disputepage import DisputePageTjy
from odrweb.page.homepage import HomePage

reload(sys)
sys.setdefaultencoding("utf-8")

t = 1

jf_info_all = {
    "jf_appeal": u"假一赔十",
    "applicant_name": u"企业或机构名称",  #
    "world_credit_id": "abcde1234567890",
    "applicant": u"钱桂林",
    "applicant_tel": "13160077223",
    "applicant_id": "321023199508166636",
    "applicant_addr": u"1栋2单元303",

    "disputer": u"王发明",
    "disputer_tel": "13913031374",
    "disputer_world_credit_id": "zxcvbnmasdfghjk123",
    "disputer_name": u"企业或机构名称",
    "disputer_id": "",
    "disputer_addr": u"10栋1单元101",

    "agent_name": u"徐传珠",
    "agent_tel": "15295745648",
    "agent_id": "321281199507077775",

    "agent_b_name": u"段志勇",
    "agent_b_tel": "15895996954",
    "agent_b_id": ""
}


class DisputeCommit(unittest.TestCase):
    """调解员-纠纷提交"""
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
        """调解员-登记纠纷提交-申自然人-被自然人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申自然人-被自然人",
                   "applicant_type": u"自然人",  # 自然人 法人 非法人组织
                   "disputer_type": u"自然人",  # 自然人 法人 非法人组织
                   "agent_type": "",  # "" common special,
                   "agent_b_type": "",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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
        """调解员-登记纠纷提交-申自然人代理人-被法人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申自然人代理人-被法人",
                   "applicant_type": u"自然人",  # 自然人 法人 非法人组织
                   "disputer_type": u"法人",  # 自然人 法人 非法人组织
                   "agent_type": "common",  # "" common special,
                   "agent_b_type": "",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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
        """案件列表-姓名查询"""

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            search = case_list_page._get_search(type_="name")
            case_list_page.search(search)
            # 获取返回页面纠纷状态
            result = case_list_page.verification_search_name(search)
            self.assertEqual(True, result)
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

    def test_04(self):
        """调解员-登记纠纷提交-申自然人代理人-被非法人组织
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申自然人代理人-被非法人组织",
                   "applicant_type": u"自然人",  # 自然人 法人 非法人组织
                   "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "agent_type": "special",  # "" common special,
                   "agent_b_type": "",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_05(self):
        """调解员-登记纠纷提交-申法人代理人-被自然人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申法人代理人-被自然人",
                   "applicant_type": u"法人",  # 自然人 法人 非法人组织
                   "disputer_type": u"自然人",  # 自然人 法人 非法人组织
                   "agent_type": "special",  # "" common special,
                   "agent_b_type": "",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_06(self):
        """调解员-登记纠纷提交-申法人代理人-被法人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申法人代理人-被法人",
                   "applicant_type": u"法人",  # 自然人 法人 非法人组织
                   "disputer_type": u"法人",  # 自然人 法人 非法人组织
                   "agent_type": "special",  # "" common special,
                   "agent_b_type": "",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_07(self):
        """调解员-登记纠纷提交-申法人代理人-被非法人组织
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申法人代理人-被非法人组织",
                   "applicant_type": u"法人",  # 自然人 法人 非法人组织
                   "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "agent_type": "special",  # "" common special,
                   "agent_b_type": "",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_08(self):
        """调解员-登记纠纷提交-申非法人组织代理人-被自然人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申非法人组织代理人-被自然人",
                   "applicant_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "disputer_type": u"自然人",  # 自然人 法人 非法人组织
                   "agent_type": "special",  # "" common special,
                   "agent_b_type": "",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_09(self):
        """调解员-登记纠纷提交-申非法人组织代理人-被法人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申非法人组织代理人-被法人",
                   "applicant_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "disputer_type": u"法人",  # 自然人 法人 非法人组织
                   "agent_type": "common",  # "" common special,
                   "agent_b_type": "",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_10(self):
        """调解员-登记纠纷提交-申非法人组织代理人-被非法人组织
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申非法人组织代理人-被非法人组织",
                   "applicant_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "agent_type": "special",  # "" common special,
                   "agent_b_type": "",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_11(self):
        """调解员-登记纠纷提交-申自然人代理人-被自然人代理人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申自然人代理人-被自然人代理人",
                   "applicant_type": u"自然人",  # 自然人 法人 非法人组织
                   "disputer_type": u"自然人",  # 自然人 法人 非法人组织
                   "agent_type": "special",  # "" common special,
                   "agent_b_type": "special",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_12(self):
        """调解员-登记纠纷提交-申自然人代理人-被法人代理人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申自然人代理人-被法人代理人",
                   "applicant_type": u"自然人",  # 自然人 法人 非法人组织
                   "disputer_type": u"法人",  # 自然人 法人 非法人组织
                   "agent_type": "common",  # "" common special,
                   "agent_b_type": "common",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_13(self):
        """调解员-登记纠纷提交-申自然人代理人-被非法人组织代理人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申自然人代理人-被非法人组织代理人",
                   "applicant_type": u"自然人",  # 自然人 法人 非法人组织
                   "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "agent_type": "special",  # "" common special,
                   "agent_b_type": "special",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_14(self):
        """调解员-登记纠纷提交-申法人代理人-被自然人代理人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申法人代理人-被自然人代理人",
                   "applicant_type": u"法人",  # 自然人 法人 非法人组织
                   "disputer_type": u"自然人",  # 自然人 法人 非法人组织
                   "agent_type": "special",  # "" common special,
                   "agent_b_type": "common",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_15(self):
        """调解员-登记纠纷提交-申法人代理人-被法人代理人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申法人代理人-被法人代理人",
                   "applicant_type": u"法人",  # 自然人 法人 非法人组织
                   "disputer_type": u"法人",  # 自然人 法人 非法人组织
                   "agent_type": "special",  # "" common special,
                   "agent_b_type": "special",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_16(self):
        """调解员-登记纠纷提交-申法人代理人-被非法人组织代理人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申法人代理人-被非法人组织代理人",
                   "applicant_type": u"法人",  # 自然人 法人 非法人组织
                   "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "agent_type": "special",  # "" common special,
                   "agent_b_type": "special",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_17(self):
        """调解员-登记纠纷提交-申非法人组织代理人-被自然人代理人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申非法人组织代理人-被自然人代理人",
                   "applicant_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "disputer_type": u"自然人",  # 自然人 法人 非法人组织
                   "agent_type": "special",  # "" common special,
                   "agent_b_type": "special",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_18(self):
        """调解员-登记纠纷提交-申非法人组织代理人-被法人代理人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申非法人组织代理人-被法人代理人",
                   "applicant_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "disputer_type": u"法人",  # 自然人 法人 非法人组织
                   "agent_type": "common",  # "" common special,
                   "agent_b_type": "common",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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

    def test_19(self):
        """调解员-登记纠纷提交-申非法人组织代理人-被非法人组织代理人
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-申非法人组织代理人-被非法人组织代理人",
                   "applicant_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "agent_type": "special",  # "" common special,
                   "agent_b_type": "special",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(t)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
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


if __name__ == '__main__':
    unittest.main()
