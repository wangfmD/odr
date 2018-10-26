# coding: utf-8
import sys
import unittest
from time import sleep

from odrweb.core.initdata import users
from odrweb.core.utils import _funcname_docstring

from odrweb.page.disputepage import DisputePageDjy
from odrweb.page.homepage import HomePage

reload(sys)
sys.setdefaultencoding("utf-8")

t = 1

jf_info_all = {
    "jf_appeal": u"假一赔十",
    "applicant_name": u"a企业或机构名称",  #
    "world_credit_id": "abcde1234567890",
    "applicant": u"钱桂林",
    "applicant_tel": "13160077223",
    "applicant_id": "321023199508166636",
    "applicant_addr": u"1栋2单元303",

    "disputer": u"王发明",
    "disputer_tel": "13913031374",
    "disputer_world_credit_id": "zxcvbnmasdfghjk123",
    "disputer_name": u"b企业或机构名称",
    "disputer_id": "",
    "disputer_addr": u"10栋1单元101",

    "agent_name": u"徐传珠",
    "agent_tel": "15295745648",
    "agent_id": "321281199507077775",

    "agent_b_name": u"段志勇",
    "agent_b_tel": "15895996954",
    "agent_b_id": ""
}


class DjyFunc(unittest.TestCase):
    """机构登记员-基本功能"""

    def setUp(self):
        self.homepage = HomePage()
        print "\n--------------------"

    def tearDown(self):
        self.homepage.driver.quit()

    def test_01(self):
        """机构登记员-首页-登记纠纷保存-申自然人-被自然人"""
        jf_info = {"jf_desc": u"机构登记员-首页-登记纠纷保存-申自然人-被自然人",
                   "applicant_type": u"自然人",  # 自然人 法人 非法人组织
                   "disputer_type": u"自然人",  # 自然人 法人 非法人组织
                   "agent_type": "",  # "" common special,
                   "agent_b_type": "",  # common special,
                   'none_mediator': True,
                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
            disputepage = DisputePageDjy(self.homepage)
            disputepage._goto_dispute_input()
            disputepage.save(**jf_info_all)
            sleep(t)
            res = disputepage.verification_save(**jf_info_all)
            self.assertEqual(True, res)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_02(self):
        """首页-输入查询"""
        try:
            self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
            disputepage = DisputePageDjy(self.homepage)
            disputepage.act_goto_homepage()
            case_id = disputepage.get_search_No()
            disputepage.act_search_by_name_or_id(case_id)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_03(self):
        """纠纷预览-返回列表"""
        try:
            self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
            disputepage = DisputePageDjy(self.homepage)
            disputepage.act_dispute_list_info_back()
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_04(self):
        """纠纷预览-解纷进度"""
        try:
            self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
            disputepage = DisputePageDjy(self.homepage)
            disputepage.act_dispute_list_info_schedule()
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_05(self):
        """纠纷预览-保存"""
        try:
            self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
            disputepage = DisputePageDjy(self.homepage)
            disputepage.act_dispute_list_info_save()
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_06(self):
        """纠纷预览-提交"""
        try:
            self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
            disputepage = DisputePageDjy(self.homepage)
            disputepage.act_dispute_list_info_commit()
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_07(self):
        """机构登记列表-增加纠纷-保存"""
        jf_info = {"jf_desc": u"机构登记列表-增加纠纷-提交",
                   "applicant_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "agent_type": "",  # "" common special,
                   "agent_b_type": "",  # common special,
                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
            disputepage = DisputePageDjy(self.homepage)
            disputepage.act_goto_homepage()
            disputepage.act_list_add_dispute()
            disputepage.save(**jf_info_all)
            sleep(t)
            res = disputepage.verification_save(**jf_info_all)
            self.assertEqual(True, res)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_08(self):
        """构登记列表-删除"""

        try:
            self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
            disputepage = DisputePageDjy(self.homepage)
            disputepage.act_goto_homepage()
            disputepage.act_list_del_dispute()
            print u"登记员删除未提交纠纷成功"
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_09(self):
        """机构登记列表-增加纠纷-提交"""
        jf_info = {"jf_desc": u"机构登记列表-增加纠纷-提交",
                   "applicant_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
                   "agent_type": "",  # "" common special,
                   "agent_b_type": "",  # common special,
                   }
        jf_info_all.update(jf_info)

        try:
            self.homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
            disputepage = DisputePageDjy(self.homepage)
            disputepage.act_goto_homepage()
            disputepage.act_list_add_dispute()
            disputepage.commit(**jf_info_all)
            sleep(t)
            res = disputepage.verification_commit(**jf_info_all)
            self.assertEqual(True, res)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise


if __name__ == '__main__':
    unittest.main()
