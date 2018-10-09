# coding=utf-8


import sys
import unittest
from time import sleep
from odrweb.core.initdata import users
from odrweb.page.adminorganpage import AdminOrgan
from odrweb.page.homepage import HomePage




class AdminOrigan(unittest.TestCase):
    '''行政部门测试用例'''

    def setUp(self):
        self.homepage = HomePage()
        print "\n--------------------"

    def tearDown(self):
        pass
        self.homepage.quit()

    # def test_01(self):
    #     '''首页-纠纷总量展示'''
    #     self. homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     dispute = adminorganpage.homepage_dispute()
    #     print u"纠纷总量: ", dispute
    #
    # def test_02(self):
    #     '''首页-咨询展示'''
    #     self. homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     consult = adminorganpage.homepage_consult()
    #     print u"咨询数量: ", consult
    #
    # def test_03(self):
    #     '''首页-调解展示'''
    #     self. homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     mediation = adminorganpage.homepage_mediation()
    #     print u"调解数量: ", mediation
    #
    # def test_04(self):
    #     '''首页-咨询师数量和'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     cons_1,cons_2,cons_all = adminorganpage.homepage_add_consultant()
    #     res = adminorganpage.verification_homepage_add_consultant(cons_1,cons_2,cons_all)
    #     self.assertEqual(True,res)
    #
    # def test_05(self):
    #     '''管理中心-机构'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     organ = adminorganpage.admin_center_organ()
    #     adminorganpage.change_windows()
    #     res = adminorganpage.verification_admin_center_organ(organ)
    #     self.assertEqual(True,res)
    #
    # def test_06(self):
    #     '''管理中心-人员'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     per = adminorganpage.admin_center_person()
    #     adminorganpage.change_windows()
    #     res = adminorganpage.verification_admin_center_person(per)
    #     self.assertEqual(True,res)
    #
    # def test_07(self):
    #     '''管理中心-翻页'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.admin_center_page()
    #     res = adminorganpage.verification_admin_center_page()
    #     self.assertEqual(True,res)
    #
    # def test_08(self):
    #     '''统计报表-平台地图'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_map()
    #     res = adminorganpage.verification_form_map()
    #     self.assertEqual(True,res)
    #
    # def test_09(self):
    #     '''统计报表-平台地图-日期筛选'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_map_date()
    #
    # def test_10(self):
    #     '''统计报表-业务报表'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_business()
    #     res = adminorganpage.verification_form_business()
    #     self.assertEqual(True,res)
    #
    # def test_11(self):
    #     '''统计报表-业务报表-地区筛选'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_business_area()
    #
    # def test_12(self):
    #     '''统计报表-未响应案件统计'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_unresponsive()
    #     res = adminorganpage.verification_form_unresponsive()
    #     self.assertEqual(True,res)
    #
    # def test_13(self):
    #     '''统计报表-未响应案件统计-1~7天未响应'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_unresponsive_seven()
    #
    # def test_14(self):
    #     '''统计报表-未响应案件统计-8~15天未响应'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_unresponsive_fifteen()
    #
    # def test_15(self):
    #     '''统计报表-未响应案件统计-16~30天未响应'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_unresponsive_thirty()
    #
    # def test_16(self):
    #     '''统计报表-未响应案件统计-超过30天未响应'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_unresponsive_more()
    #
    # def test_17(self):
    #     '''统计报表-未响应案件统计-结果翻页'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_unresponsive_page()
    #     res = adminorganpage.verification_form_unresponsive_page()
    #     self.assertEqual(True,res)
    #
    # def test_18(self):
    #     '''统计报表-案件类型对应表'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_casetype()
    #     res = adminorganpage.verification_form_casetype()
    #     self.assertEqual(True,res)
    #
    # def test_19(self):
    #     '''统计报表-案件类型对应表-日期筛选'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_casetype_date()
    #
    # def test_20(self):
    #     '''统计报表-案件类型对应表-导出Excel'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_casetype_excel()
    #
    # def test_21(self):
    #     '''统计报表-后续流程进行度'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_follow()
    #     res = adminorganpage.verification_form_follow()
    #     self.assertEqual(True,res)
    #
    # def test_22(self):
    #     '''统计报表-后续流程进行度-日期筛选'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_follow_date()
    #
    # def test_23(self):
    #     '''统计报表-后续流程进行度-司法确认案件量'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_follow_judicial()
    #
    # def test_24(self):
    #     '''统计报表-后续流程进行度-申请诉讼案件量'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_follow_litigation()
    #
    # def test_25(self):
    #     '''统计报表-优秀内容展示'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_show()
    #     res = adminorganpage.verification_form_show()
    #     self.assertEqual(True,res)
    #
    # def test_26(self):
    #     '''统计报表-优秀内容展示-日期筛选'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_show_date()
    #
    # def test_27(self):
    #     '''统计报表-优秀内容展示-导出'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #     adminorganpage.form_show_excel()

    def test_28(self):
        '''统计报表-优秀内容展示-金牌调解员'''
        self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
        adminorganpage = AdminOrgan(self.homepage)

    # def test_29(self):
    #     '''统计报表-优秀内容展示-优秀调解机构'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)
    #
    # def test_30(self):
    #     '''统计报表-优秀内容展示-优秀市'''
    #     self.homepage.organization_login(users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    #     adminorganpage = AdminOrgan(self.homepage)





if __name__ == '__main__':
    unittest.main()


