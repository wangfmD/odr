# coding: utf-8
import sys
import unittest
from inspect import currentframe, getframeinfo, getdoc

from odrweb.core.initdata import users
from odrweb.core.utils import _funcname_docstring
from odrweb.page.caselistpage import InputCaseListPage
from odrweb.page.homepage import HomePage

reload(sys)
sys.setdefaultencoding("utf-8")


class TjyFunc(unittest.TestCase):
    """调解员-案件登记列表"""

    homepage = None

    @classmethod
    def setUpClass(cls):
        cls.homepage = HomePage()

    @classmethod
    def tearDownClass(cls):
        cls.homepage.driver.quit()

    def setUp(self):
        print "\n--------------------"

    def tearDown(self):
        self.homepage.quit()

    def test_1(self):
        """纠纷登记列表-添加纠纷-保存"""
        desc = u"纠纷登记列表-添加纠纷-保存"

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = InputCaseListPage(self.homepage)
            case_list_page.dispute_add_save(desc)
            # 获取返回页面纠纷状态
            result = case_list_page.verification_add_save(desc)
            self.assertEqual(True, result)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_2(self):
        """纠纷登记列表-添加纠纷-提交"""
        # 1，纠纷登记列表-已提交-添加纠纷
        # 2，修改纠纷描述
        # 3，-提交
        desc = u"纠纷登记列表-添加纠纷-提交"

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = InputCaseListPage(self.homepage)
            case_list_page.dispute_add_commit(desc)
            # 获取返回页面纠纷状态
            result = case_list_page.verification_add_commit(desc)
            self.assertEqual(True, result)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_3(self):
        """纠纷登记列表-纠纷预览-保存"""

        # 1，纠纷登记列表-已提交-纠纷预览
        # 2，修改纠纷描述、诉求
        # 3，保存

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = InputCaseListPage(self.homepage)
            case_list_page.case_modification_save()
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

    def test_4(self):
        """纠纷登记列表-删除"""

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = InputCaseListPage(self.homepage)
            case_list_page.dispute_delete()
            # 获取返回页面纠纷状态
            # result = case_list_page.verification_dispute_modification()
            # self.assertEqual(True, result)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_5(self):
        """纠纷登记列表-查询-纠纷编号"""
        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            case_list_page = InputCaseListPage(self.homepage)
            case_list_page._into_input_case_list()
            dis_id = case_list_page.get_search_No()
            #
            case_list_page.search(dis_id)
            #
            result = case_list_page.verification_search_No(dis_id)
            self.assertEqual(True, result)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise


if __name__ == '__main__':
    unittest.main()
