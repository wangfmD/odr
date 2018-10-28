# -*- coding: utf-8 -*-
import sys
import unittest
from time import sleep

from odrweb.page.homepage import HomePage
from odrweb.page.organizationadmin import MissionCenter

reload(sys)
sys.setdefaultencoding("utf-8")

class OrgCaseOpera(unittest.TestCase):
    """机构管理员"""
    def setUp(self):
        self.homepage = HomePage()

    def tearDown(self):
        self.homepage.quit()

    def test_01(self):
        """任务中心调解类型"""

        org_admin = {
            "机构账号": "17612156739",
            "机构密码": "123456"
        }

        casetime = None

        self.homepage.organization_login(org_admin["机构账号"], org_admin["机构密码"])

        orgpage = MissionCenter(self.homepage)
        orgpage.in_mission_center()
        orgpage.case_time(casetime)
        sleep(5)
