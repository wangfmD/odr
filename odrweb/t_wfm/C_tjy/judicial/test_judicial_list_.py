# coding: utf-8
import datetime
import sys
import unittest
from inspect import getdoc, getframeinfo, currentframe

from odrweb.core.utils import _funcname_docstring
from odrweb.page.disputepage import TjyJudicialPage, TjyJudicialInfoPage
from odrweb.page.homepage import HomePage

reload(sys)
sys.setdefaultencoding("utf-8")

T1 = 'https://train.odrcloud.cn:8443'
# T1 = 'https://uatodr.odrcloud.net'
tjy = '13913031374'
pwd = '000000'


class JudicialList(unittest.TestCase):
    '''调解员-申请司法确认列表'''

    homepage = None
    case_id = ''  # 存储司法确认案件编号

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

    # def test_01(self):
    #     """在线司法确认列表-选择查询-待确认
    #     """
    #     select_status = u'待确认'
    #     try:
    #         self.homepage.mediator_login(tjy, pwd, url=T1)
    #         page = JudicialInputPage(self.homepage)
    #         page.act_search_judicial_list(select_status=select_status)
    #         res, _ = page.verfc_act_search_judicial_list_status(select_status)
    #         self.assertEqual(res, True)
    #     except Exception as msg:
    #         print "EXCEPTION >> {}".format(msg)
    #         # class function name_class docstring
    #         docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
    #         name = _funcname_docstring(self, docstr.decode('utf8'))
    #         # 截图
    #         self.homepage.save_screen_shot(name)
    #
    #         raise
    #     finally:
    #         self.end = datetime.datetime.now()
    #         duration = (self.end - self.start).seconds
    #         print "###case duration: {}###".format(duration)
    #
    # def test_02(self):
    #     """在线司法确认列表-选择查询-确认有效
    #     """
    #     select_status = u'确认有效'
    #     try:
    #         self.homepage.mediator_login(tjy, pwd, url=T1)
    #         page = JudicialInputPage(self.homepage)
    #         page.act_search_judicial_list(select_status=select_status)
    #         res, _ = page.verfc_act_search_judicial_list_status(select_status)
    #         self.assertEqual(res, True)
    #     except Exception as msg:
    #         print "EXCEPTION >> {}".format(msg)
    #         # class function name_class docstring
    #         docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
    #         name = _funcname_docstring(self, docstr.decode('utf8'))
    #         # 截图
    #         self.homepage.save_screen_shot(name)
    #
    #         raise
    #     finally:
    #         self.end = datetime.datetime.now()
    #         duration = (self.end - self.start).seconds
    #         print "###case duration: {}###".format(duration)
    #
    # def test_03(self):
    #     """在线司法确认列表-选择查询-驳回申请
    #     """
    #     select_status = u'驳回申请'
    #     try:
    #         self.homepage.mediator_login(tjy, pwd, url=T1)
    #         page = JudicialInputPage(self.homepage)
    #         page.act_search_judicial_list(select_status=select_status)
    #         res, JudicialList.case_id = page.verfc_act_search_judicial_list_status(select_status)
    #         self.assertEqual(res, True)
    #     except Exception as msg:
    #         print "EXCEPTION >> {}".format(msg)
    #         # class function name_class docstring
    #         docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
    #         name = _funcname_docstring(self, docstr.decode('utf8'))
    #         # 截图
    #         self.homepage.save_screen_shot(name)
    #
    #         raise
    #     finally:
    #         self.end = datetime.datetime.now()
    #         duration = (self.end - self.start).seconds
    #         print "###case duration: {}###".format(duration)
    #
    # def test_04(self):
    #     """在线司法确认列表-查询-案件编号
    #     """
    #     try:
    #         self.homepage.mediator_login(tjy, pwd, url=T1)
    #         page = JudicialInputPage(self.homepage)
    #         page.act_search_judicial_list(search_content=JudicialList.case_id)
    #         res= page.verfc_act_search_judicial_list_search_content(JudicialList.case_id)
    #         self.assertEqual(res, True)
    #     except Exception as msg:
    #         print "EXCEPTION >> {}".format(msg)
    #         # class function name_class docstring
    #         docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
    #         # name= _funcname_docstring(self, docstr.decode('utf8'))
    #         name = _funcname_docstring(self, docstr)
    #         # 截图
    #         self.homepage.save_screen_shot(name)
    #
    #         raise
    #     finally:
    #         self.end = datetime.datetime.now()
    #         duration = (self.end - self.start).seconds
    #         print "###case duration: {}###".format(duration)

    def test_05(self):
        """在线司法确认列表-案件详情-材料选择-文书类
        """
        select_type = u"文书类"
        try:
            self.homepage.mediator_login(tjy, pwd, url=T1)
            page = TjyJudicialInfoPage(self.homepage)
            page.act_goto_jidicial_info()
            page.act_case_material_select(select_type)

            res= page.verfc_act_case_material_select(select_type)
            self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            # name= _funcname_docstring(self, docstr.decode('utf8'))
            name = _funcname_docstring(self, docstr)
            # 截图
            self.homepage.save_screen_shot(name)

            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)

    def test_06(self):
        """在线司法确认列表-案件详情-材料选择-申请类
        """
        select_type = u"申请类"
        try:
            self.homepage.mediator_login(tjy, pwd, url=T1)
            page = TjyJudicialInfoPage(self.homepage)
            page.act_goto_jidicial_info()
            page.act_case_material_select(select_type)

            res= page.verfc_act_case_material_select(select_type)
            self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            # name= _funcname_docstring(self, docstr.decode('utf8'))
            name = _funcname_docstring(self, docstr)
            # 截图
            self.homepage.save_screen_shot(name)

            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)

    def test_07(self):
        """在线司法确认列表-案件详情-材料选择-证据类
        """
        select_type = u"证据类"
        try:
            self.homepage.mediator_login(tjy, pwd, url=T1)
            page = TjyJudicialInfoPage(self.homepage)
            page.act_goto_jidicial_info()
            page.act_case_material_select(select_type)

            res= page.verfc_act_case_material_select(select_type)
            self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            # name= _funcname_docstring(self, docstr.decode('utf8'))
            name = _funcname_docstring(self, docstr)
            # 截图
            self.homepage.save_screen_shot(name)

            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)

    def test_08(self):
        """在线司法确认列表-案件详情-材料选择-其他类
        """
        select_type = u"其他类"
        try:
            self.homepage.mediator_login(tjy, pwd, url=T1)
            page = TjyJudicialInfoPage(self.homepage)
            page.act_goto_jidicial_info()
            page.act_case_material_select(select_type)

            res= page.verfc_act_case_material_select(select_type)
            self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            # name= _funcname_docstring(self, docstr.decode('utf8'))
            name = _funcname_docstring(self, docstr)
            # 截图
            self.homepage.save_screen_shot(name)

            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)

    def test_09(self):
        """在线司法确认列表-案件详情-材料选择-代理类
        """
        select_type = u"代理类"
        try:
            self.homepage.mediator_login(tjy, pwd, url=T1)
            page = TjyJudicialInfoPage(self.homepage)
            page.act_goto_jidicial_info()
            page.act_case_material_select(select_type)

            res= page.verfc_act_case_material_select(select_type)
            self.assertEqual(res, True)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
            # name= _funcname_docstring(self, docstr.decode('utf8'))
            name = _funcname_docstring(self, docstr)
            # 截图
            self.homepage.save_screen_shot(name)

            raise
        finally:
            self.end = datetime.datetime.now()
            duration = (self.end - self.start).seconds
            print "###case duration: {}###".format(duration)

