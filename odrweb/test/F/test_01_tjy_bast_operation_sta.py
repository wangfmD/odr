# coding: utf-8
import unittest

from odrweb.page.homepage import HomePage


class TjyOperation(unittest.TestCase):
    '''调解员页面操作'''

    def setUp(self):
        self.homepage = HomePage()
        print "\n--------------------"

    def tearDown(self):
        pass
        self.homepage.quit()

    # def test_01(self):
    #     '''已提交案件列表增加纠纷-提交'''
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     caselistpage = TjyBaseOperation(self.homepage)
    #     res = caselistpage.dispute_add_commit()
    #     self.assertEqual(True,res)
    #
    #
    # def test_02(self):
    #     '''已提交案件纠纷详情页面修改保存并校验'''
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     caselistpage = TjyBaseOperation(self.homepage)
    #     res = caselistpage.dispute_info_change()
    #     self.assertEqual(True, res)
    #
    # def test_03(self):
    #     '''已提交案件进入纠纷详情页面并校验'''
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     caselistpage = TjyBaseOperation(self.homepage)
    #     res = caselistpage.into_dispute_info()
    #     self.assertEqual(True,res)
    #
    # def test_04(self):
    #     '''已提交案件我的案件列表搜索'''
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     caselistpage = TjyBaseOperation(self.homepage)
    #     caselistpage.mydispute_find()
    #     res = caselistpage.verification_dispute_id()
    #     self.assertEqual(True, res)

    # def test_05(self):
    #     '''已提交案件列表增加纠纷-保存-删除'''
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     caselistpage = TjyBaseOperation(self.homepage)
    #     caselistpage.dispute_add_save_delete()
    #     res = caselistpage.verfication_dispute_delete()
    #     self.assertEqual(True, res)

    # def test_06(self):
    #     '''进入我的案件列表纠纷详情'''
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     caselistpage = TjyBaseOperation(self.homepage)
    #     res = caselistpage.into_mydispult_info()
    #     self.assertEqual(True,res)
    #
    #
    # def test_07(self):
    #     '''我的案件列表等待调解案件修改保存'''
    #     self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    #     caselistpage = TjyBaseOperation(self.homepage)
    #     res = caselistpage.mydispute_info_change()
    #     self.assertEqual(True,res)


if __name__ == '__main__':
    unittest.main()
