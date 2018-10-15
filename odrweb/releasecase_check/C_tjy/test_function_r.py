# coding: utf-8
import sys
import unittest

from odrweb.core.initdata import users
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
        pass
        self.homepage.quit()

    # def test_01(self):
    #     """等待调解-调解成功"""
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.mediate_success()
    #     # 获取返回页面纠纷状态
    #     dispute_status = case_list_page.get_detail_dispute_status()
    #     result = case_list_page.verification_dispute_status(dispute_status, u"调解成功")
    #     self.assertEqual(True, result)
    #
    # def test_02(self):
    #     """等待调解-调解失败"""
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.mediate_failed()
    #     # 获取返回页面纠纷状态
    #     dispute_status = case_list_page.get_detail_dispute_status()
    #     result = case_list_page.verification_dispute_status(dispute_status, u"调解失败")
    #     self.assertEqual(True, result)
    #
    # def test_03(self):
    #     """等待调解-调解终止"""
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.mediate_stop()
    #     # 获取返回页面纠纷状态
    #     dispute_status = case_list_page.get_detail_dispute_status()
    #     result = case_list_page.verification_dispute_status(dispute_status, u"终止调解")
    #     self.assertEqual(True, result)
    #
    # def test_04(self):
    #     """等待调解-调解撤回"""
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.mediate_revocation()
    #     # 获取返回页面纠纷状态
    #     dispute_status = case_list_page.get_detail_dispute_status()
    #     result = case_list_page.verification_dispute_status(dispute_status, u"撤回调解")
    #     self.assertEqual(True, result)
    #
    # def test_05(self):
    #     """等待调解-预约调解"""
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.mediate_video_create()
    #     # 获取返回页面纠纷状态
    #     conference_title = case_list_page.get_conference_title()
    #     result = case_list_page.verification_dispute_status(conference_title, "conference_title")
    #     self.assertEqual(True, result)
    #
    # #
    # def test_06(self):
    #     """等待调解-调解重新分配"""
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.mediate_redistribution()
    #     # 获取返回页面纠纷状态
    #     # dispute_status = case_list_page.get_detail_dispute_status()
    #     # result = case_list_page.verification_dispute_status(dispute_status, u"调解撤回")
    #     # self.assertEqual(True, result)
    #
    # def test_07(self):
    #     """正在调解-调解成功"""
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.mediate_success(dispute_status=u'正在调解')
    #     # 获取返回页面纠纷状态
    #     dispute_status = case_list_page.get_detail_dispute_status()
    #     result = case_list_page.verification_dispute_status(dispute_status, u"调解成功")
    #     self.assertEqual(True, result)
    #
    # def test_08(self):
    #     """正在调解-调解失败"""
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.mediate_failed()
    #     # 获取返回页面纠纷状态
    #     dispute_status = case_list_page.get_detail_dispute_status()
    #     result = case_list_page.verification_dispute_status(dispute_status, u"调解失败")
    #     self.assertEqual(True, result)

    def test_09(self):
        """正在调解-调解终止"""
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        case_list_page = CaseListPage(self.homepage)
        case_list_page.mediate_stop(dispute_status=u'正在调解')
        # 获取返回页面纠纷状态
        dispute_status = case_list_page.get_detail_dispute_status()
        result = case_list_page.verification_dispute_status(dispute_status, u"终止调解")
        self.assertEqual(True, result)

    # def test_10(self):
    #     """正在调解-调解撤回"""
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.mediate_revocation(dispute_status=u'正在调解')
    #     # 获取返回页面纠纷状态
    #     dispute_status = case_list_page.get_detail_dispute_status()
    #     result = case_list_page.verification_dispute_status(dispute_status, u"撤回调解")
    #     self.assertEqual(True, result)

    def test_11(self):
        """正在调解-预约调解"""
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        case_list_page = CaseListPage(self.homepage)
        case_list_page.mediate_video_create(dispute_status=u'正在调解')
        # 获取返回页面纠纷状态
        conference_title = case_list_page.get_conference_title()
        result = case_list_page.verification_dispute_status(conference_title, "conference_title")
        self.assertEqual(True, result)

    # #
    # def test_12(self):
    #     """正在调解-调解重新分配"""
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.mediate_redistribution(dispute_status=u'正在调解')
    #     # 获取返回页面纠纷状态
    #     # dispute_status = case_list_page.get_detail_dispute_status()
    #     # result = case_list_page.verification_dispute_status(dispute_status, u"调解撤回")
    #     # self.assertEqual(True, result)
    #
    # def test_13(self):
    #     """案件列表-纠纷编号查询"""
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     search = case_list_page._get_search()
    #     case_list_page.search(search)
    #     # 获取返回页面纠纷状态
    #     result = case_list_page.verification_search_No(search)
    #     self.assertEqual(True, result)



    # def test_15(self):
    #     """案件列表-状态筛选-等待调解"""
    #     dispute_status = u'等待调解'
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.select_dispute_status(dispute_status=dispute_status)
    #     # 获取返回页面纠纷状态
    #     result = case_list_page.verification_select_status(dispute_status)
    #     self.assertEqual(True, result)
    #
    # def test_16(self):
    #     """案件列表-状态筛选-正在调解"""
    #     dispute_status = u'正在调解'
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.select_dispute_status(dispute_status=dispute_status)
    #     # 获取返回页面纠纷状态
    #     result = case_list_page.verification_select_status(dispute_status)
    #     self.assertEqual(True, result)
    #
    # def test_17(self):
    #     """案件列表-状态筛选-调解成功"""
    #     dispute_status = u'调解成功'
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.select_dispute_status(dispute_status=dispute_status)
    #     # 获取返回页面纠纷状态
    #     result = case_list_page.verification_select_status(dispute_status)
    #     self.assertEqual(True, result)
    #
    # def test_18(self):
    #     """案件列表-状态筛选-调解失败"""
    #     dispute_status = u'调解失败'
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.select_dispute_status(dispute_status=dispute_status)
    #     # 获取返回页面纠纷状态
    #     result = case_list_page.verification_select_status(dispute_status)
    #     self.assertEqual(True, result)
    #
    # def test_19(self):
    #     """案件列表-状态筛选-撤回调解"""
    #     dispute_status = u'撤回调解'
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.select_dispute_status(dispute_status=dispute_status)
    #     # 获取返回页面纠纷状态
    #     result = case_list_page.verification_select_status(dispute_status)
    #     self.assertEqual(True, result)
    #
    # def test_20(self):
    #     """案件列表-状态筛选-调解终止"""
    #     dispute_status = u'终止调解'
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.select_dispute_status(dispute_status=dispute_status)
    #     # 获取返回页面纠纷状态
    #     result = case_list_page.verification_select_status(dispute_status)
    #     self.assertEqual(True, result)
    #
    # def test_21(self):
    #     """案件列表-等待调解-修改保存"""
    #     dispute_status = u'等待调解'
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.case_modification_save(dispute_status=dispute_status)
    #     # 获取返回页面纠纷状态
    #     result = case_list_page.verification_dispute_modification()
    #     self.assertEqual(True, result)
    #
    # def test_22(self):
    #     """案件列表-正在调解-修改保存"""
    #     dispute_status = u'正在调解'
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     case_list_page = CaseListPage(self.homepage)
    #     case_list_page.case_modification_save(dispute_status=dispute_status)
    #     # 获取返回页面纠纷状态
    #     result = case_list_page.verification_dispute_modification()
    #     self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
