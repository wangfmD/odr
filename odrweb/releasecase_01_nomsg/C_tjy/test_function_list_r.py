# coding: utf-8
import datetime
import sys
import unittest
from inspect import currentframe, getframeinfo, getdoc
from time import sleep

from odrweb.core.initdata import users
from odrweb.core.utils import _funcname_docstring
from odrweb.page.caselistpage import InputCaseListPage
from odrweb.page.disputepage import DisputePageTjy
from odrweb.page.homepage import HomePage

reload(sys)
sys.setdefaultencoding("utf-8")

jf_info_all = {
    "jf_appeal": u"假一赔十",
    "applicant_name": u"企业或机构名称",  #
    "world_credit_id": "abcde1234567890",
    "applicant": u"钱桂林",
    "applicant_tel": "13160077223",
    "applicant_id": "321023199508166636",
    "applicant_addr": u"1栋2单元303",

    "disputer": u"王发明",
    "disputer_tel": "13913031374",
    "disputer_world_credit_id": "zxcvbnmasdfghjk123",
    "disputer_name": u"企业或机构名称",
    "disputer_id": "",
    "disputer_addr": u"10栋1单元101",

    "agent_name": u"徐传珠",
    "agent_tel": "15295745648",
    "agent_id": "321281199507077775",

    "agent_b_name": u"段志勇",
    "agent_b_tel": "15895996954",
    "agent_b_id": ""
}


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
        self.start = datetime.datetime.now()
        print "\n--------------------"

    def tearDown(self):
        self.end = datetime.datetime.now()
        duration = (self.end - self.start).seconds
        print "###case duration: {}###".format(duration)
        self.homepage.quit()




    def test_01(self):
        """调解员-登记纠纷提交-非法人组织-非法人组织
        """
        jf_info = {"jf_desc": u"调解员-登记纠纷提交-非法人组织-非法人组织",
                   "applicant_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "agent_type": "",  # "" common special,
                   "agent_b_type": "",  # common special,

                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
            disputepage = DisputePageTjy(self.homepage)
            disputepage.commit(**jf_info_all)
            sleep(1)
            res, _= disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            name = _funcname_docstring(self, docstr.decode('utf8'))
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_02(self):
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

    def test_03(self):
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

    def test_04(self):
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

    def test_05(self):
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

    def test_06(self):
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
