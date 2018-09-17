# coding: utf-8
import sys
import unittest

from odrweb.core.initdata import users
from odrweb.page.homepage import HomePage
from odrweb.page.caselistpage_ import CaseListPage

reload(sys)
sys.setdefaultencoding("utf-8")



class OdrTjyFunc(unittest.TestCase):
    '''调解员功能'''
    #
    def setUp(self):
        self.homepage = HomePage()
        print "\n--------------------"

    def tearDown(self):
        pass
        self.homepage.quit()

    def test_01(self):
        '''等待调解-调解成功'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        case_list_page = CaseListPage(self.homepage)
        case_list_page.mediate_success()
        # 获取返回页面纠纷状态
        dispute_status = case_list_page.get_detail_dispute_status()
        result = case_list_page.verification_dispute_status(dispute_status, u"调解成功")
        self.assertEqual(True, result)

    def test_02(self):
        '''等待调解-调解失败'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        case_list_page = CaseListPage(self.homepage)
        case_list_page.mediate_failed()
        # 获取返回页面纠纷状态
        dispute_status = case_list_page.get_detail_dispute_status()
        result = case_list_page.verification_dispute_status(dispute_status, u"调解失败")
        self.assertEqual(True, result)

    def test_03(self):
        '''等待调解-调解终止'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        case_list_page = CaseListPage(self.homepage)
        case_list_page.mediate_stop()
        # 获取返回页面纠纷状态
        dispute_status = case_list_page.get_detail_dispute_status()
        result = case_list_page.verification_dispute_status(dispute_status, u"终止调解")
        self.assertEqual(True, result)

    def test_04(self):
        '''等待调解-调解撤回'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        case_list_page = CaseListPage(self.homepage)
        case_list_page.mediate_revocation()
        # 获取返回页面纠纷状态
        dispute_status = case_list_page.get_detail_dispute_status()
        result = case_list_page.verification_dispute_status(dispute_status, u"撤回调解")
        self.assertEqual(True, result)

    def test_05(self):
        '''等待调解-预约调解'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        case_list_page = CaseListPage(self.homepage)
        case_list_page.mediate_vedio_create()
        # 获取返回页面纠纷状态
        conference_title = case_list_page.get_conference_title()
        result = case_list_page.verification_dispute_status(conference_title, "conference_title")
        self.assertEqual(True, result)
    #
    def test_06(self):
        '''等待调解-调解重新分配'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        case_list_page = CaseListPage(self.homepage)
        case_list_page.mediate_redistribution()
        # 获取返回页面纠纷状态
        # dispute_status = case_list_page.get_detail_dispute_status()
        # result = case_list_page.verification_dispute_status(dispute_status, u"调解撤回")
        # self.assertEqual(True, result)

    def test_07(self):
        '''正在调解-调解成功'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        case_list_page = CaseListPage(self.homepage)
        case_list_page.mediate_success(dispute_status=u'正在调解')
        # 获取返回页面纠纷状态
        dispute_status = case_list_page.get_detail_dispute_status()
        result = case_list_page.verification_dispute_status(dispute_status, u"调解成功")
        self.assertEqual(True, result)

    def test_08(self):
        '''正在调解-调解失败'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        case_list_page = CaseListPage(self.homepage)
        case_list_page.mediate_failed()
        # 获取返回页面纠纷状态
        dispute_status = case_list_page.get_detail_dispute_status()
        result = case_list_page.verification_dispute_status(dispute_status, u"调解失败")
        self.assertEqual(True, result)

    def test_09(self):
        '''正在调解-调解终止'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        case_list_page = CaseListPage(self.homepage)
        case_list_page.mediate_stop(dispute_status=u'正在调解')
        # 获取返回页面纠纷状态
        dispute_status = case_list_page.get_detail_dispute_status()
        result = case_list_page.verification_dispute_status(dispute_status, u"终止调解")
        self.assertEqual(True, result)

    def test_10(self):
        '''正在调解-调解撤回'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        case_list_page = CaseListPage(self.homepage)
        case_list_page.mediate_revocation(dispute_status=u'正在调解')
        # 获取返回页面纠纷状态
        dispute_status = case_list_page.get_detail_dispute_status()
        result = case_list_page.verification_dispute_status(dispute_status, u"撤回调解")
        self.assertEqual(True, result)

    def test_11(self):
        '''正在调解-预约调解'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        case_list_page = CaseListPage(self.homepage)
        case_list_page.mediate_vedio_create(dispute_status=u'正在调解')
        # 获取返回页面纠纷状态
        conference_title = case_list_page.get_conference_title()
        result = case_list_page.verification_dispute_status(conference_title, "conference_title")
        self.assertEqual(True, result)
    #
    def test_12(self):
        '''正在调解-调解重新分配'''
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        case_list_page = CaseListPage(self.homepage)
        case_list_page.mediate_redistribution(dispute_status=u'正在调解')
        # 获取返回页面纠纷状态
        # dispute_status = case_list_page.get_detail_dispute_status()
        # result = case_list_page.verification_dispute_status(dispute_status, u"调解撤回")
        # self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
