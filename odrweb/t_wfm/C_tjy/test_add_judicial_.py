# coding: utf-8
import datetime
import sys
import unittest
from inspect import getdoc, getframeinfo, currentframe

from odrweb.core.utils import _funcname_docstring
from odrweb.page.disputepage import JudicialInputPage
from odrweb.page.homepage import HomePage

reload(sys)
sys.setdefaultencoding("utf-8")

T1 = 'https://train.odrcloud.cn:8443'
# T1 = 'https://uatodr.odrcloud.net'
tjy = '13913031374'
pwd = '000000'

jf_info_all = {
    "jf_appeal": u"假一赔十",
    "applicant_name": u"申请企业或机构名称一",  #
    "world_credit_id": "abcde1234567890",
    "applicant": u"钱桂林",
    "applicant_tel": "13160077223",
    "applicant_id": "321023199508166636",
    "applicant_addr": u"1栋2单元303",

    "disputer": u"顾乐",
    "disputer_tel": "18362983886",
    "disputer_world_credit_id": "zxcvbnmasdfghjk123",
    "disputer_name": u"申请企业或机构名称二",
    "disputer_id": "321283199503266424",
    "disputer_addr": u"10栋1单元101",

    "agent_name": u"徐传珠",
    "agent_tel": "15295745648",
    "agent_id": "321281199507077775",

    "agent_b_name": u"陈瑶玮",
    "agent_b_tel": "17625908729",
    "agent_b_id": "320102199107292810"
}


class JudicialInputCommit(unittest.TestCase):
    '''调解员-司法确认提交'''

    homepage = None

    @classmethod
    def setUpClass(cls):
        cls.homepage = HomePage()

    @classmethod
    def tearDownClass(cls):
        cls.homepage.driver.quit()

    def setUp(self):
        self.start = datetime.datetime.now()
        print "\n--------------------"

    def tearDown(self):
        self.homepage.quit()

    # def test_01(self):
    #     """调解员-司法确认-自然人-自然人
    #     """
    #     jf_info = {
    #         "jf_desc": u"调解员-司法确认-自然人-自然人",
    #         "applicant_type": u"自然人",  # 自然人 法人 非法人组织
    #         "disputer_type": u"自然人",  # 自然人 法人 非法人组织
    #         "agent_type": "",  # "" common special,
    #         "agent_b_type": "",  # common special,
    #     }
    #     jf_info_all.update(jf_info)
    #
    #     self.homepage.mediator_login('13913031374', '000000', url=T1)
    #     page = JudicialInputPage(self.homepage)
    #     page.act_judicial_commit(**jf_info_all)
    #     res = page.verification_judicial_commit(jf_info_all['jf_desc'])
    #     self.assertEqual(res, True)
    #
    # def test_02(self):
    #     """调解员-司法确认-法人-法人
    #     """
    #     jf_info = {
    #         "jf_desc": u"调解员-司法确认-法人-法人",
    #         "applicant_type": u"法人",  # 自然人 法人 非法人组织
    #         "disputer_type": u"法人",  # 自然人 法人 非法人组织
    #         "agent_type": "",  # "" common special,
    #         "agent_b_type": "",  # common special,
    #     }
    #     jf_info_all.update(jf_info)
    #
    #     self.homepage.mediator_login('13913031374', '000000', url=T1)
    #     page = JudicialInputPage(self.homepage)
    #     page.act_judicial_commit(**jf_info_all)
    #     res = page.verification_judicial_commit(jf_info_all['jf_desc'])
    #     self.assertEqual(res, True)
    #
    # def test_03(self):
    #     """调解员-司法确认-非法人组织-非法人组织
    #     """
    #     jf_info = {
    #         "jf_desc": u"调解员-司法确认-非法人组织-非法人组织",
    #         "applicant_type": u"非法人组织",  # 自然人 法人 非法人组织
    #         "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
    #         "agent_type": "",  # "" common special,
    #         "agent_b_type": "",  # common special,
    #     }
    #     jf_info_all.update(jf_info)
    #
    #     self.homepage.mediator_login('13913031374', '000000', url=T1)
    #     page = JudicialInputPage(self.homepage)
    #     page.act_judicial_commit(**jf_info_all)
    #     res = page.verification_judicial_commit(jf_info_all['jf_desc'])
    #     self.assertEqual(res, True)
    #
    # def test_04(self):
    #     """调解员-司法确认-自然人-代-非法人组织-代
    #     """
    #     jf_info = {
    #         "jf_desc": u"调解员-司法确认-自然人-代-非法人组织-代",
    #         "applicant_type": u"自然人",  # 自然人 法人 非法人组织
    #         "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
    #         "agent_type": "special",  # "" common special,
    #         "agent_b_type": "special",  # common special,
    #     }
    #     jf_info_all.update(jf_info)
    #
    #     self.homepage.mediator_login('13913031374', '000000', url=T1)
    #     page = JudicialInputPage(self.homepage)
    #     page.act_judicial_commit(**jf_info_all)
    #     res = page.verification_judicial_commit(jf_info_all['jf_desc'])
    #     self.assertEqual(res, True)
    #
    # def test_05(self):
    #     """调解员-司法确认-法人-代-非法人组织
    #     """
    #     jf_info = {
    #         "jf_desc": u"调解员-司法确认-法人-代-非法人组织",
    #         "applicant_type": u"自然人",  # 自然人 法人 非法人组织
    #         "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
    #         "agent_type": "special",  # "" common special,
    #         "agent_b_type": "",  # common special,
    #     }
    #     jf_info_all.update(jf_info)
    #
    #     self.homepage.mediator_login('13913031374', '000000', url=T1)
    #     page = JudicialInputPage(self.homepage)
    #     page.act_judicial_commit(**jf_info_all)
    #     res = page.verification_judicial_commit(jf_info_all['jf_desc'])
    #     self.assertEqual(res, True)

    # def test_01(self):
    #     """调解员-司法确认-法人-非法人组织-代
    #     """
    #     jf_info = {
    #         "jf_desc": u"调解员-司法确认-法人-非法人组织-代",
    #         "applicant_type": u"法人",  # 自然人 法人 非法人组织
    #         "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
    #         "agent_type": "",  # "" common special,
    #         "agent_b_type": "special",  # common special,
    #     }
    #     jf_info_all.update(jf_info)
    #
    #     try:
    #         self.homepage.mediator_login(tjy, pwd, url=T1)
    #         page = JudicialInputPage(self.homepage)
    #         page.act_judicial_commit(**jf_info_all)
    #         res = page.verification_judicial_commit(jf_info_all['jf_desc'])
    #         self.assertEqual(res, True)
    #     except Exception as msg:
    #         print "EXCEPTION >> {}".format(msg)
    #         # class function name_class docstring
    #         docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
    #         print type(docstr)
    #         print docstr
    #         name = _funcname_docstring(self, docstr.decode('utf8'))
    #         # 截图
    #         self.homepage.save_screen_shot(name)
    #
    #         raise
    #     finally:
    #         self.end = datetime.datetime.now()
    #         duration = (self.end - self.start).seconds
    #         print "###case duration: {}###".format(duration)

    def test_02(self):
        """调解员-申请司法确认列表-编号查询
        """
        case_id = '166BEBC2B5673'
        try:
            self.homepage.mediator_login(tjy, pwd, url=T1)
            page = JudicialInputPage(self.homepage)
            page.act_search_apply_judicial_list(case_id)
            res = page.verfc_act_search_apply_judicial_search_content(case_id)
            self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            print type(docstr)
            print docstr
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)

            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)

    # def test_03(self):
    #     """调解员-申请司法确认列表-案件状态查询-登记成功
    #     """
    #     case_status = u'登记成功'
    #     try:
    #         self.homepage.mediator_login(tjy, pwd, url=T1)
    #         page = JudicialInputPage(self.homepage)
    #         page.act_search_apply_judicial_list(select_status=case_status)
    #         res = page.verfc_act_search_apply_judicial_status(case_status)
    #         self.assertEqual(res, True)
    #     except Exception as msg:
    #         print "EXCEPTION >> {}".format(msg)
    #         # class function name_class docstring
    #         docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
    #         print type(docstr)
    #         print docstr
    #         name = _funcname_docstring(self, docstr.decode('utf8'))
    #         # 截图
    #         self.homepage.save_screen_shot(name)
    #
    #         raise
    #     finally:
    #         self.end = datetime.datetime.now()
    #         duration = (self.end - self.start).seconds
    #         print "###case duration: {}###".format(duration)

    def test_04(self):
        """调解员-申请司法确认列表-案件状态查询-待分配
        """
        case_status = u'待分配'
        try:
            self.homepage.mediator_login(tjy, pwd, url=T1)
            page = JudicialInputPage(self.homepage)
            page.act_search_apply_judicial_list(select_status=case_status)
            res = page.verfc_act_search_apply_judicial_status(case_status)
            self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            print type(docstr)
            print docstr
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)

            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)

    def test_05(self):
        """调解员-申请司法确认列表-案件状态查询-法院退回
        """
        case_status = u'法院退回'
        try:
            self.homepage.mediator_login(tjy, pwd, url=T1)
            page = JudicialInputPage(self.homepage)
            page.act_search_apply_judicial_list(select_status=case_status)
            # res = page.verfc_act_search_apply_judicial_status(case_status)
            # self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            print type(docstr)
            print docstr
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)

            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)

    def test_06(self):
        """调解员-申请司法确认列表-案件状态查询-不受理
        """
        case_status = u'不受理'
        try:
            self.homepage.mediator_login(tjy, pwd, url=T1)
            page = JudicialInputPage(self.homepage)
            page.act_search_apply_judicial_list(select_status=case_status)
            res = page.verfc_act_search_apply_judicial_status(u'不予受理')
            self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            print type(docstr)
            print docstr
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)

            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)


    def test_07(self):
        """调解员-申请司法确认列表-案件状态查询-待确认
        """
        case_status = u'待确认'
        try:
            self.homepage.mediator_login(tjy, pwd, url=T1)
            page = JudicialInputPage(self.homepage)
            page.act_search_apply_judicial_list(select_status=case_status)
            res = page.verfc_act_search_apply_judicial_status(case_status)
            self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            print type(docstr)
            print docstr
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)

            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)


    def test_08(self):
        """调解员-申请司法确认列表-案件状态查询-确认有效
        """
        case_status = u'确认有效'
        try:
            self.homepage.mediator_login(tjy, pwd, url=T1)
            page = JudicialInputPage(self.homepage)
            page.act_search_apply_judicial_list(select_status=case_status)
            res = page.verfc_act_search_apply_judicial_status(case_status)
            self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            print type(docstr)
            print docstr
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)

            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)

    def test_09(self):
        """调解员-申请司法确认列表-案件状态查询-驳回申请
        """
        case_status = u'驳回申请'
        try:
            self.homepage.mediator_login(tjy, pwd, url=T1)
            page = JudicialInputPage(self.homepage)
            page.act_search_apply_judicial_list(select_status=case_status)
            res = page.verfc_act_search_apply_judicial_status(case_status)
            self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            print type(docstr)
            print docstr
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)

            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)