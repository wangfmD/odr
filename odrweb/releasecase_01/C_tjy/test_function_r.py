# coding: utf-8
import datetime
import sys
import unittest
from inspect import getdoc, getframeinfo, currentframe
from time import sleep

from odrweb.core.initdata import users
from odrweb.core.utils import _funcname_docstring
from odrweb.page.caselistpage import CaseListPage
from odrweb.page.disputepage import DisputePageTjy
from odrweb.page.homepage import HomePage

reload(sys)
sys.setdefaultencoding("utf-8")

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


class TjyFuncCaseList(unittest.TestCase):
    """调解员-纠纷调解案件列表"""

    homepage = None
    case_id = ''

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

    def test_01(self):
        """等待调解-调解成功
        """

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.mediate_success()
            # 获取返回页面纠纷状态
            dispute_status = case_list_page.get_detail_dispute_status()
            result = case_list_page.verification_dispute_status(dispute_status, u"调解成功")
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

    def test_02(self):
        """等待调解-调解失败"""

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.mediate_failed()
            # 获取返回页面纠纷状态
            dispute_status = case_list_page.get_detail_dispute_status()
            result = case_list_page.verification_dispute_status(dispute_status, u"调解失败")
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

    def test_03(self):
        """等待调解-调解终止"""
        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.mediate_stop()
            # 获取返回页面纠纷状态
            dispute_status = case_list_page.get_detail_dispute_status()
            result = case_list_page.verification_dispute_status(dispute_status, u"终止调解")
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
        """等待调解-调解撤回"""
        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.mediate_revocation()
            # 获取返回页面纠纷状态
            dispute_status = case_list_page.get_detail_dispute_status()
            result = case_list_page.verification_dispute_status(dispute_status, u"撤回调解")
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

    def test_05(self):
        """等待调解-调解重新分配"""

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.mediate_redistribution()
            # 获取返回页面纠纷状态
            # dispute_status = case_list_page.get_detail_dispute_status()
            # result = case_list_page.verification_dispute_status(dispute_status, u"调解撤回")
            # self.assertEqual(True, result)
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
        """正在调解-调解成功"""

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.mediate_success(dispute_status=u'正在调解')
            # 获取返回页面纠纷状态
            dispute_status = case_list_page.get_detail_dispute_status()
            result = case_list_page.verification_dispute_status(dispute_status, u"调解成功")
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

    def test_07(self):
        """正在调解-调解失败"""

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.mediate_failed()
            # 获取返回页面纠纷状态
            dispute_status = case_list_page.get_detail_dispute_status()
            result = case_list_page.verification_dispute_status(dispute_status, u"调解失败")
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

    def test_08(self):
        """正在调解-调解终止"""

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.mediate_stop(dispute_status=u'正在调解')
            # 获取返回页面纠纷状态
            dispute_status = case_list_page.get_detail_dispute_status()
            result = case_list_page.verification_dispute_status(dispute_status, u"终止调解")
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

    def test_09(self):
        """正在调解-调解撤回"""
        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.mediate_revocation(dispute_status=u'正在调解')
            # 获取返回页面纠纷状态
            dispute_status = case_list_page.get_detail_dispute_status()
            result = case_list_page.verification_dispute_status(dispute_status, u"撤回调解")
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

    # def test_10(self):
    #     """正在调解-预约调解"""
    #     try:
    #         self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #         case_list_page = CaseListPage(self.homepage)
    #         case_list_page.mediate_video_create(dispute_status=u'正在调解')
    #         # 获取返回页面纠纷状态
    #         conference_title = case_list_page.get_conference_title()
    #         result = case_list_page.verification_dispute_status(conference_title, "conference_title")
    #         self.assertEqual(True, result)
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
    def test_11(self):
        """正在调解-调解重新分配"""

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.mediate_redistribution(dispute_status=u'正在调解')
            # 获取返回页面纠纷状态
            # dispute_status = case_list_page.get_detail_dispute_status()
            # result = case_list_page.verification_dispute_status(dispute_status, u"调解撤回")
            # self.assertEqual(True, result)
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
        """案件列表-纠纷编号查询"""

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            search = case_list_page._get_search()
            case_list_page.search(search)
            # 获取返回页面纠纷状态
            result = case_list_page.verification_search_No(search)
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

    # 没有测试数据，放置在添加纠纷场景中测试
    # def test_14(self):
    #     """案件列表-姓名查询"""
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     search = case_list_page._get_search(type_="name")
    #     case_list_page.search(search)
    #     # 获取返回页面纠纷状态
    #     result = case_list_page.verification_search_name(search)
    #     self.assertEqual(True, result)

    def test_13(self):
        """案件列表-状态筛选-等待调解"""
        try:
            dispute_status = u'等待调解'
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.select_dispute_status(dispute_status=dispute_status)
            # 获取返回页面纠纷状态
            result = case_list_page.verification_select_status(dispute_status)
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

    def test_14(self):
        """案件列表-状态筛选-正在调解"""
        dispute_status = u'正在调解'

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.select_dispute_status(dispute_status=dispute_status)
            # 获取返回页面纠纷状态
            result = case_list_page.verification_select_status(dispute_status)
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

    def test_15(self):
        """案件列表-状态筛选-调解成功"""

        dispute_status = u'调解成功'

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.select_dispute_status(dispute_status=dispute_status)
            # 获取返回页面纠纷状态
            result = case_list_page.verification_select_status(dispute_status)
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

    def test_16(self):
        """案件列表-状态筛选-调解失败"""

        dispute_status = u'调解失败'

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.select_dispute_status(dispute_status=dispute_status)
            # 获取返回页面纠纷状态
            result = case_list_page.verification_select_status(dispute_status)
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

    def test_17(self):
        """案件列表-状态筛选-撤回调解"""

        dispute_status = u'撤回调解'

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.select_dispute_status(dispute_status=dispute_status)
            # 获取返回页面纠纷状态
            result = case_list_page.verification_select_status(dispute_status)
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

    def test_18(self):
        """案件列表-状态筛选-调解终止"""

        dispute_status = u'终止调解'

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.select_dispute_status(dispute_status=dispute_status)
            # 获取返回页面纠纷状态
            result = case_list_page.verification_select_status(dispute_status)
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

    def test_19(self):
        """调解员-登记纠纷提交-非法人组织-非法人组织
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-非法人组织-非法人组织",
                   "applicant_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "agent_type": "",  # "" common special,
                   "agent_b_type": "",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(1)
            res, TjyFuncCaseList.case_id = disputepage.verification_commit(**jf_info_all)
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

    def test_20(self):
        """案件列表-等待调解-修改保存"""

        dispute_status = u'等待调解'

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.case_modification_save(search=self.case_id, dispute_status=dispute_status)
            # 获取返回页面纠纷状态
            result = case_list_page.verification_dispute_modification()
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

    def test_21(self):
        """等待调解-预约调解"""

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.mediate_video_create(search=self.case_id)
            # 获取返回页面纠纷状态
            conference_title = case_list_page.get_conference_title()
            result = case_list_page.verification_dispute_status(conference_title, "conference_title")
            self.assertEqual(True, result)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_22(self):
        """正在调解-预约调解"""
        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.mediate_video_create(search=self.case_id, dispute_status=u'正在调解')
            # 获取返回页面纠纷状态
            conference_title = case_list_page.get_conference_title()
            result = case_list_page.verification_dispute_status(conference_title, "conference_title")
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

    def test_23(self):
        """案件列表-正在调解-修改保存"""

        dispute_status = u'正在调解'

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.case_modification_save(search=self.case_id, dispute_status=dispute_status)
            # 获取返回页面纠纷状态
            result = case_list_page.verification_dispute_modification()
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
