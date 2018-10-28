# coding: utf-8
import sys
import unittest

from odrweb.core.initdata import users
# from odrweb.page.disputepage import DisputePage
from odrweb.page.homepage import HomePage
from odrweb.page.personalpage import PersonalPage

reload(sys)
sys.setdefaultencoding("utf-8")

jf_info = {"jf_desc": u"假冒商品",
           "jf_appeal": u"假一赔十",
           "applicant": u"徐传珠",
           "applicant_tel": "15295745648",
           "applicant_id": "321281199507077775",
           "applicant_addr": u"addr",
           "disputer": u"钱桂林",
           "disputer_tel": "13160077223"
           }


class User(unittest.TestCase):
    """用户功能"""

    def setUp(self):
        self.homepage = HomePage()
        print "\n--------------------"

    def tearDown(self):
        self.homepage.quit()


    def test_01(self):
        """个人中心-我要评估"""
        # 测试数据
        jf_consult = {"jf_type": u"消费维权",
                      "jf_desc": u"假冒商品",
                      "jf_appeal": u"假一赔十"}
        # 执行
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()

        personalpage = PersonalPage(self.homepage)
        personalpage.evaluate(**jf_consult)
        # 验证
        result = personalpage.verification_evaluate(jf_consult["jf_desc"])
        self.assertEqual(True,result)


    def test_02(self):
        """个人中心-我要咨询"""
        jf_consult = {"jf_type": u"消费维权",
                      "jf_desc": u"假冒商品",
                      "jf_appeal": u"假一赔十"}
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.consult(**jf_consult)
        self.homepage.user_personal_center()
        personalpage.verification_consult(jf_consult['jf_desc'])

    def test_03(self):
        """咨询列表-评估"""
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.act_manual_consult_2_assessment()

    def test_04(self):
        """咨询列表-人工咨询-查询"""
        name = u'吴晓洁' # 咨询师姓名
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.manual_consult_search(name)
        personalpage.verification_manual_consult_search(name)

    def test_05(self):
        """咨询列表-人工咨询-返回"""
        name = u'吴晓洁' # 咨询师姓名
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.manual_consult_select_back()


    def test_06(self):
        """咨询列表-人工咨询-结束咨询"""
        name = u'吴晓洁' # 咨询师姓名
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.manual_consult_select_end()

    def test_07(self):
        """咨询列表-申请调解"""
        #

        #
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.act_manual_consult_apply()
        #
        result= personalpage.verfc_act_manual_consult_apply()
        self.assertEqual(result, True)


    def test_08(self):
        """调解列表-查询"""
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        dispute_id = personalpage.get_dispute_search_id()
        personalpage.act_dispute_search(dispute_id)
        result= personalpage.verfc_act_dispute_search_by_id(dispute_id)
        self.assertEqual(result, True)


    def test_09(self):
        """调解列表-调解进度"""
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.act_dispute_schedule()

    def test_10(self):
        """调解列表-纠纷详情-返回列表"""
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.act_dispute_detail_info_back()

    def test_11(self):
        """调解列表-纠纷详情-保存"""
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.act_dispute_detail_info_save()

    def test_12(self):
        """调解列表-纠纷详情-解纷进度"""
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.act_dispute_detail_info_schedule()

    def test_13(self):
        """绑定手机-取消"""
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.tel_binding()

    def test_14(self):
        """绑定邮箱-取消"""
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.mail_binding()

    def test_15(self):
        """预留签名-取消"""
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.setting_signature()

    def test_16(self):
        """我的资料-保存"""
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.person_data_save()

if __name__ == '__main__':
    unittest.main()
