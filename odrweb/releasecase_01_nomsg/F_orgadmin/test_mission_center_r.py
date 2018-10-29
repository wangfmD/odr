# -*- coding: utf-8 -*-
import sys
import unittest
from inspect import getdoc, getframeinfo, currentframe
from time import sleep

from odrweb.core.utils import _funcname_docstring
from odrweb.page.homepage import HomePage
from odrweb.page.organizationadmin import MissionCenter

reload(sys)
sys.setdefaultencoding("utf-8")


class OrgCaseOpera(unittest.TestCase):
    """机构管理员"""
    homepage = None

    @classmethod
    def setUpClass(cls):
        cls.homepage = HomePage()

    @classmethod
    def tearDownClass(cls):
        cls.homepage.driver.quit()

    def setUp(self):
        print "Browser type: {}".format(self.homepage._type)
        print "\n--------------------"

    def tearDown(self):
        self.homepage.quit()

    def test_01(self):
        """任务中心调解类型"""

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }

        casetype = None  # 设定调解类型，默认值为全部

        try:
            self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

            orgpage = MissionCenter(self.homepage)
            orgpage.in_mission_center()
            result = orgpage.case_type(casetype)
            self.assertEquals(result, True, msg='任务中心调解类型选择失败')
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_02(self):
        """任务中心调解状态"""

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }

        casestatus = None  # 设定调解状态，默认值为全部

        try:
            self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

            orgpage = MissionCenter(self.homepage)
            orgpage.in_mission_center()
            result = orgpage.case_status(casestatus)
            self.assertEquals(result, True, msg='任务中心调解状态选择失败')
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_03(self):
        """任务中心登记时间"""

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }

        casetime = None  # 设定登记时间，默认值为全部

        try:
            self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

            orgpage = MissionCenter(self.homepage)
            orgpage.in_mission_center()
            result = orgpage.case_time(casetime)  # 如传入自定义时间 需要追加两位参数：起始时间，格式YYYY-MM-DD
            self.assertEquals(result, True, msg='任务中心登记时间选择失败')
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_04(self):
        """机构管理员查看临期案件"""

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }

        try:
            self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

            orgpage = MissionCenter(self.homepage)
            orgpage.in_mission_center()
            result = orgpage.case_uptodate_check()
            self.assertEquals(result, True, msg='只看到期案件点选失败')
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_05(self):
        """案件总量"""

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }

        try:
            self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

            orgpage = MissionCenter(self.homepage)
            orgpage.in_mission_center()
            total_casenumber = orgpage.get_total_case_num()
            result = orgpage.verfc_total_case_number_visitable(total_casenumber)
            self.assertEquals(result, True, msg='案件总量显示不为数字')
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_06(self):
        """案件编号精确搜索"""

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }
        case_optioninfo = {
            "编号/姓名/案号": "166575BAC9777",
        }

        try:
            self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

            orgpage = MissionCenter(self.homepage)
            orgpage.in_mission_center()
            orgpage.case_time()
            orgpage.search_case_by_id_or_name(**case_optioninfo)  # 检索纠纷
            total_casenumber = orgpage.get_total_case_num()
            result = orgpage.verfc_case_search_successful(total_casenumber)
            self.assertEquals(result, True, msg='案件编号精确搜索结果唯一性校验失败')
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_07(self):
        """案件搜索重置"""

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }
        case_optioninfo = {
            "编号/姓名/案号": "166575BAC9777",
        }

        try:
            self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

            orgpage = MissionCenter(self.homepage)
            orgpage.in_mission_center()
            orgpage.case_time()
            sleep(1)
            total_casenumber1 = orgpage.get_total_case_num()

            orgpage.search_case_by_id_or_name(**case_optioninfo)  # 检索纠纷
            total_casenumber2 = orgpage.get_total_case_num()
            orgpage.clear_search_case_area()
            sleep(1)
            total_casenumber3 = orgpage.get_total_case_num()
            result = orgpage.verfc_case_search_clear_successful(total_casenumber1, total_casenumber2, total_casenumber3)
            self.assertEquals(result, True, msg='搜索重置功能校验失败')
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_08(self):
        """批量受理按钮"""

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }

        try:
            self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

            orgpage = MissionCenter(self.homepage)
            orgpage.in_mission_center()
            result = orgpage.click_batch_process()
            self.assertEquals(result, True, msg='批量受理按钮点击失败')
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_09(self):
        """机构管理员查看纠纷详情"""

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }
        case_optioninfo = {
            "编号/姓名/案号": "166575BAC9777",
        }

        try:
            self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

            orgpage = MissionCenter(self.homepage)
            orgpage.in_mission_center()
            orgpage.case_time()

            orgpage.search_case_by_id_or_name(**case_optioninfo)  # 检索纠纷
            result = orgpage.case_detail()  # 点击查看详情
            self.assertEquals(result, True, msg='切换纠纷详情页面失败')
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_10(self):
        """机构管理员受理纠纷"""

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }

        try:
            self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

            orgpage = MissionCenter(self.homepage)
            orgpage.in_mission_center()
            orgpage.case_time()
            casenumber = orgpage.get_an_unaccept_case()  # 获取一个未受理纠纷编号
            case_optioninfo = {
                "编号/姓名/案号": casenumber
            }

            print(case_optioninfo["编号/姓名/案号"])
            orgpage.search_case_by_id_or_name(**case_optioninfo)  # 检索纠纷
            orgpage.case_acceptance()  # 点击受理
            orgpage.tip_agree()  # 重要提示 确定
            orgpage.info_agree()  # 信息 确定
            sleep(1)
            result = orgpage.verfc_case_acceptable(casenumber)
            self.assertEquals(result, True, msg='案件受理失败')
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_11(self):
        """机构管理员不受理纠纷"""

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }

        try:
            self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

            orgpage = MissionCenter(self.homepage)
            orgpage.in_mission_center()
            orgpage.case_time()
            casenumber = orgpage.get_an_unaccept_case()  # 获取一个未受理纠纷编号
            case_optioninfo = {
                "编号/姓名/案号": casenumber
            }
            orgpage.search_case_by_id_or_name(**case_optioninfo)  # 检索纠纷
            orgpage.case_refuse()  # 点击不受理
            orgpage.tip_agree()  # 重要提示 确定
            sleep(1)
            orgpage.click_refuse_type()
            orgpage.input_refuse_detail(u'111')
            orgpage.click_commit_refuse()
            sleep(2)
            result = orgpage.verfc_case_unacceptable(casenumber)
            self.assertEquals(result, True, msg='案件不受理失败')
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_12(self):
        """机构管理员受理纠纷、分配调解员"""

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }

        try:
            self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

            orgpage = MissionCenter(self.homepage)
            orgpage.in_mission_center()
            orgpage.case_time()
            casenumber = orgpage.get_an_unaccept_case()  # 获取一个未受理纠纷编号

            case_optioninfo = {
                "编号/姓名/案号": casenumber,
                "分配调解员姓名": u"TS(宋红波）"
            }

            print(case_optioninfo["编号/姓名/案号"])
            orgpage.search_case_by_id_or_name(**case_optioninfo)  # 检索纠纷
            orgpage.case_acceptance()  # 点击受理
            orgpage.tip_agree()  # 重要提示 确定
            orgpage.info_agree()  # 信息 确定
            sleep(1)
            orgpage.case_select_mediator()
            orgpage.case_mediator_choose(**case_optioninfo)
            result = orgpage.verfc_case_assignable(casenumber)
            self.assertEquals(result, True, msg='案件分配调解员失败')
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_13(self):
        """机构管理员重新分配机构"""

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }

        try:
            self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

            orgpage = MissionCenter(self.homepage)
            orgpage.in_mission_center()
            orgpage.case_time()
            casenumber = orgpage.get_an_unaccept_case()  # 获取一个未受理纠纷编号
            case_optioninfo = {
                "编号/姓名/案号": casenumber
            }
            orgpage.search_case_by_id_or_name(**case_optioninfo)  # 检索纠纷
            orgpage.case_change_organization()
            orgpage.input_change_reason(u'111')
            orgpage.choose_change_organization(u'浙江省宁波市宁海县道路交通事故人民调解委员会')  # 转移的的调解机构
            result = orgpage.verfc_change_organization(casenumber)
            self.assertEquals(result, True, msg='调解机构转移失败')
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_14(self):
        """机构管理员查看进度"""

        org_admin = {
            "机构账号": "5958234274",
            "机构密码": "123456"
        }
        case_optioninfo = {
            "编号/姓名/案号": "1661014720F65",
        }

        try:
            self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

            orgpage = MissionCenter(self.homepage)
            orgpage.in_mission_center()
            orgpage.case_time()

            orgpage.search_case_by_id_or_name(**case_optioninfo)  # 检索纠纷
            result = orgpage.case_progress()  # 点击查看进度
            self.assertEquals(result, True, msg='查看进度失败')
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

            # def xtest_006(self):
            #     """机构管理员重新分配案件"""
            #
            #     org_admin = {
            #         "机构账号": "17612156739",
            #         "机构密码": "123456"
            #     }
            #
            #     self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])
            #
            #     orgpage = MissionCenter(self.homepage)
            #     orgpage.in_mission_center()
            #
            #     case_optioninfo = {
            #         "编号/姓名/案号": "1661FB5842888",
            #         "分配调解员姓名": u"徐传珠"
            #
            #     }
            #     orgpage.search_case_by_id_or_name(**case_optioninfo)  # 检索纠纷
            #     orgpage.case_select_mediator()  # 点击重新分配
            #     orgpage.case_mediator_choose(**case_optioninfo)
            #     orgpage.tip_agree()   # 重要提示 确定
            #     orgpage.info_agree()  # 信息 确定
            #     sleep(1)
