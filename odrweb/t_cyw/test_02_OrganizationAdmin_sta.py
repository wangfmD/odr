# -*- coding: utf-8 -*-
import unittest
from time import sleep
import sys
from odrweb.page.homepage import HomePage
from odrweb.page.OrganizationAdmin import OrganizationAdmin


reload(sys)
sys.setdefaultencoding("utf-8")

class OrgCaseOpera(unittest.TestCase):
    '''机构管理员'''
    def setUp(self):
        self.homepage = HomePage()

    def tearDown(self):
        self.homepage.quit()


    def test_01(self):
        '''机构管理员查看纠纷详情'''

        org_admin = {
            "机构账号": "5958234274",
            "机构密码": "123456"
        }

        self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

        orgpage = OrganizationAdmin(self.homepage)
        orgpage.in_mission_center()

        case_optioninfo = {
            "编号/姓名/案号": "1661014720F65",
        }
        orgpage.search_case_by_id_or_name(**case_optioninfo) # 检索纠纷
        orgpage.case_detail()  # 点击查看详情

    def test_02(self):
        '''案件搜索重置'''

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }

        self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

        orgpage = OrganizationAdmin(self.homepage)
        orgpage.in_mission_center()

        case_optioninfo = {
            "编号/姓名/案号": "1661FB5842888",
        }
        orgpage.search_case_by_id_or_name(**case_optioninfo)  # 检索纠纷

        orgpage.clear_search_case_area()


    def test_03(self):
        '''机构管理员查看临期案件'''

        org_admin = {
            "机构账号": "5958234274",
            "机构密码": "123456"
        }

        self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

        orgpage = OrganizationAdmin(self.homepage)
        orgpage.in_mission_center()
        orgpage.case_uptodate_check()


    def test_04(self):
        '''机构管理员受理、分配纠纷'''

        org_admin = {
            "机构账号": "5958234274",
            "机构密码": "123456"
        }

        self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

        orgpage = OrganizationAdmin(self.homepage)
        orgpage.in_mission_center()

        case_optioninfo = {
            "编号/姓名/案号": "1661014720F65",
            "分配调解员姓名": u"陈"
        }
        orgpage.search_case_by_id_or_name(**case_optioninfo) # 检索纠纷
        orgpage.case_acceptance()  # 点击受理
        orgpage.tip_agree()   # 重要提示 确定
        orgpage.info_agree()  # 信息 确定
        sleep(1)
        orgpage.case_select_mediator()
        orgpage.case_mediator_choose(**case_optioninfo)

    def test_05(self):
        '''机构管理员不受理纠纷'''

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }

        self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

        orgpage = OrganizationAdmin(self.homepage)
        orgpage.in_mission_center()

        case_optioninfo = {
            "编号/姓名/案号": "1635962AD0C24"
        }
        orgpage.search_case_by_id_or_name(**case_optioninfo) # 检索纠纷
        orgpage.case_refuse()  # 点击不受理
        orgpage.tip_agree()   # 重要提示 确定
        orgpage.info_agree()  # 信息 确定
        sleep(1)

    def test_06(self):
        '''机构管理员重新分配案件'''

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }

        self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

        orgpage = OrganizationAdmin(self.homepage)
        orgpage.in_mission_center()

        case_optioninfo = {
            "编号/姓名/案号": "1661FB5842888",
            "分配调解员姓名": u"徐传珠"

        }
        orgpage.search_case_by_id_or_name(**case_optioninfo) # 检索纠纷
        orgpage.case_select_mediator()  # 点击重新分配
        orgpage.case_mediator_choose(**case_optioninfo)
        orgpage.tip_agree()   # 重要提示 确定
        orgpage.info_agree()  # 信息 确定
        sleep(1)

    def test_07(self):
        '''机构管理员查看进度'''

        org_admin = {
            "机构账号": "5958234274",
            "机构密码": "123456"
        }

        self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

        orgpage = OrganizationAdmin(self.homepage)
        orgpage.in_mission_center()

        case_optioninfo = {
            "编号/姓名/案号": "1661014720F65",
        }
        orgpage.search_case_by_id_or_name(**case_optioninfo) # 检索纠纷
        orgpage.case_progress()  # 点击查看进度



