# -*- coding: utf-8 -*-
import unittest
import sys
import unittest

from odrweb.page.homepage import HomePage
from odrweb.core.initdata import users
from odrweb.page.judgepage import JudgePage

reload(sys)
sys.setdefaultencoding("utf-8")

class JugeFunc(unittest.TestCase):
    """办案法官-基本功能
    """

    def setUp(self):
        self.homepage = HomePage()
        print "\n--------------------"

    def tearDown(self):
        pass
        self.homepage.quit()

    def test_01(self):
        '''选择查询-待确认'''
        select_status = u'待确认'
        self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
        judgepage = JudgePage(self.homepage)
        judgepage.act_search_select(select_status)
        result = judgepage.verfc_act_search_select(select_status)
        self.assertEqual(result, True)

    def test_02(self):
        '''选择查询-确认有效'''
        select_status = u'确认有效'
        self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
        judgepage = JudgePage(self.homepage)
        judgepage.act_search_select(select_status)
        result = judgepage.verfc_act_search_select(select_status)
        self.assertEqual(result, True)

    def test_03(self):
        '''选择查询-驳回申请'''
        select_status = u'驳回申请'
        self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
        judgepage = JudgePage(self.homepage)
        judgepage.act_search_select(select_status)
        result = judgepage.verfc_act_search_select(select_status)
        self.assertEqual(result, True)


