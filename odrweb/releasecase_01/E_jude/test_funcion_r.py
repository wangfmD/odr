# -*- coding: utf-8 -*-
import sys
import unittest

from odrweb.core.initdata import users
from odrweb.core.utils import _funcname_docstring

from odrweb.page.homepage import HomePage
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
        self.homepage.driver.quit()

    def test_01(self):
        """选择查询-待确认"""
        select_status = u'待确认'

        try:
            self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
            judgepage = JudgePage(self.homepage)
            judgepage.act_search_select(select_status)
            result = judgepage.verfc_act_search_select(select_status)
            self.assertEqual(result, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_02(self):
        """选择查询-确认有效"""
        select_status = u'确认有效'

        try:
            self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
            judgepage = JudgePage(self.homepage)
            judgepage.act_search_select(select_status)
            result = judgepage.verfc_act_search_select(select_status)
            self.assertEqual(result, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_03(self):
        """选择查询-驳回申请"""

        select_status = u'驳回申请'

        try:
            self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
            judgepage = JudgePage(self.homepage)
            judgepage.act_search_select(select_status)
            result = judgepage.verfc_act_search_select(select_status)
            self.assertEqual(result, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_04(self):
        """输入查询-案件编号全匹配"""

        try:
            self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
            judgepage = JudgePage(self.homepage)
            # 拿测试数据-查询案件id
            search_ctx = judgepage._get_case_id()
            judgepage.act_seacrh_input(search_ctx)
            result = judgepage.verfc_act_seacrh_input(search_ctx)
            self.assertEqual(result, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_05(self):
        """进入案件详情"""
        try:
            self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
            judgepage = JudgePage(self.homepage)
            judgepage.act_goto_case_detail()
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_06(self):
        """案件详情-返回列表"""

        try:
            self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
            judgepage = JudgePage(self.homepage)
            judgepage.act_goto_case_detail_back()
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_07(self):
        """法官个人信息修改"""

        try:
            self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
            judgepage = JudgePage(self.homepage)
            judgepage.act_account_save()
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise