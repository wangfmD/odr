# -*- coding: utf-8 -*-
import sys
import unittest
from time import sleep

from odrweb.page.homepage import HomePage
from odrweb.page.orgregpage import OrgRegCase

reload(sys)
sys.setdefaultencoding("utf-8")

class OrgCaseOpera(unittest.TestCase):
    """机构登记员登记案件"""
    def setUp(self):
        self.homepage = HomePage()
        userinfo={
            "UserName": "1805130007",
            "PassWord": "123456"} #登录用户配置
        self.homepage.organization_user_login(userinfo["UserName"], userinfo["PassWord"])
        sleep(3)

    def tearDown(self):
        self.homepage.quit()
        print('=====================================================================')

    def test_01(self):
        """申请人：自然人、法人、非法人组织/被申请人:自然人、法人、非法人组织3v3"""
        org_reg_page = OrgRegCase(self.homepage)



