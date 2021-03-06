# -*- coding: utf-8 -*-
import datetime
import sys
import unittest
from inspect import getdoc, getframeinfo, currentframe

from odrweb.core.initdata import users
from odrweb.core.utils import _funcname_docstring
from odrweb.page.homepage import HomePage
from odrweb.page.judgepage import JudgePage

reload(sys)
sys.setdefaultencoding("utf-8")


class JugeFunc(unittest.TestCase):
    """办案法官-基本功能
    """
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
        """进入案件详情"""
        try:
            self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
            judgepage = JudgePage(self.homepage)
            judgepage.act_goto_case_detail()
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
        """案件详情-返回列表"""

        try:
            self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
            judgepage = JudgePage(self.homepage)
            judgepage.act_goto_case_detail_back()
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
        """法官个人信息修改"""

        try:
            self.homepage.mediator_login(users.user_bafg['username'], users.user_bafg['pwd'])
            judgepage = JudgePage(self.homepage)
            judgepage.act_account_save()
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
