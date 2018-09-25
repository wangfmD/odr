# -*- coding: utf-8 -*-
import unittest
from time import sleep
import sys
from odrweb.page.homepage import HomePage
from odrweb.page.OrganizationAdmin import OrganizationAdmin


reload(sys)
sys.setdefaultencoding("utf-8")

class OrganizationCaseOperation(unittest.TestCase):
    '''复数申请人'''
    def setUp(self):
        self.homepage = HomePage()

    def tearDown(self):
        self.homepage.quit()

    def test_01(self):
        '''机构管理员处理案件'''

        orgadmin = {
            "机构账号":"5958234274",
            "机构密码":"123456"
        }

        self.homepage.organization_login(orgadmin["机构账号"], orgadmin["机构密码"])

        orgpage = OrganizationAdmin(self.homepage)
        orgpage.in_mission_center()

        caseoptioninfo = {
            "编号/姓名/案号":"1661014720F65",
            "分配调解员姓名":u"陈"
        }
        orgpage.search_case_by_id_or_name(**caseoptioninfo)
        orgpage.case_acceptance()
        orgpage.tip_agree()   # 重要提示 确定
        orgpage.info_agree()  # 信息 确定
        sleep(1)
        orgpage.case_select_mediator()
        orgpage.case_mediator_choose(**caseoptioninfo)



