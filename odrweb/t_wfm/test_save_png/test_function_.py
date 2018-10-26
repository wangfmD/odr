# coding: utf-8
import sys
import traceback
import unittest

from odrweb.core.initdata import users
from odrweb.core.utils import _funcname_docstring

from odrweb.page.caselistpage import CaseListPage
from odrweb.page.homepage import HomePage

reload(sys)
sys.setdefaultencoding("utf-8")


class TjyFuncCaseList(unittest.TestCase):
    """调解员-纠纷调解案件列表"""

    def setUp(self):
        self.homepage = HomePage()
        print "\n--------------------"

    def tearDown(self):
        self.homepage.driver.quit()

    def test_11(self):
        """正在调解-预约调解"""
        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.mediate_video_create(dispute_status=u'正在调解')
            # 获取返回页面纠纷状态
            conference_title = case_list_page.get_conference_title()
            result = case_list_page.verification_dispute_status(conference_title, "conference_title")
            self.assertEqual(True, result)
        except Exception as msg:
            print "exception: {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_19(self):
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
            print "exception: {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_20(self):
        """案件列表-等待调解-修改保存"""
        dispute_status = u'等待调解'
        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.case_modification_save(dispute_status=dispute_status)
            # 获取返回页面纠纷状态
            result = case_list_page.verification_dispute_modification()
            self.assertEqual(True, result)
        except Exception as msg:
            print "exception: {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_21(self):
        """案件列表-正在调解-修改保存"""
        dispute_status = u'正在调解'
        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = CaseListPage(self.homepage)
            case_list_page.case_modification_save(dispute_status=dispute_status)
            # 获取返回页面纠纷状态
            result = case_list_page.verification_dispute_modification()
            self.assertEqual(True, result)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise


if __name__ == '__main__':
    unittest.main()
