# coding: utf-8
import datetime
import sys
import unittest
from inspect import getdoc, getframeinfo, currentframe
from time import sleep

from odrweb.core.initdata import users
from odrweb.core.utils import _funcname_docstring
from odrweb.page.caselistpage import CaseListPage
from odrweb.page.disputepage import DisputePageTjy
from odrweb.page.homepage import HomePage

reload(sys)
sys.setdefaultencoding("utf-8")


jf_info = {
    "jf_desc": u"调解员-登记纠纷提交-申法人代理人-被非法人组织代理人",
    "applicant_type": u"自然人",  # 自然人 法人 非法人组织
    "disputer_type": u"非法人组织",  # 自然人 法人 非法人组织
    "agent_type": "special",  # "" common special,
    "agent_b_type": "special",  # common special,


    "jf_appeal": u"假一赔十",
    "applicant_name": u"企业或机构名称",  #
    "world_credit_id": "abcde1234567890",
    "applicant": u"钱桂林",
    "applicant_tel": "13160077223",
    "applicant_id": "321023199508166636",
    "applicant_addr": u"1栋2单元303",

    "disputer": u"顾乐",
    "disputer_tel": "18362983886",
    "disputer_world_credit_id": "zxcvbnmasdfghjk123",
    "disputer_name": u"企业或机构名称",
    "disputer_id": "321283199503266424",
    "disputer_addr": u"10栋1单元101",

    "agent_name": u"徐传珠",
    "agent_tel": "15295745648",
    "agent_id": "321281199507077775",

    "agent_b_name": u"陈瑶玮",
    "agent_b_tel": "17625908729",
    "agent_b_id": "320102199107292810"
}


class TjyFuncJudicialList(unittest.TestCase):
    """调解员-司法确认申请列表"""

    homepage = None
    case_id = ''

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
        self.homepage.quit()

    def test_01(self):
        """等待调解-调解成功
        """

        try:
            self.homepage.self.homepage.mediator_login()
            case_list_page = CaseListPage(self.homepage)
            case_list_page.mediate_success()
            # 获取返回页面纠纷状态
            dispute_status = case_list_page.get_detail_dispute_status()
            result = case_list_page.verification_dispute_status(dispute_status, u"调解成功")
            self.assertEqual(True, result)
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

