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


class OdrJfInput(unittest.TestCase):
    '''纠纷登记'''

    def setUp(self):
        self.homepage = HomePage()
        print "\n--------------------"

    def tearDown(self):
        self.homepage.quit()


    def test_01(self):
        '''用户-我要评估'''
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
        '''用户-我要咨询'''
        jf_consult = {"jf_type": u"消费维权",
                      "jf_desc": u"假冒商品",
                      "jf_appeal": u"假一赔十"}
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.consult(**jf_consult)
        self.homepage.user_personal_center()
        personalpage.verification_consult(jf_consult['jf_desc'])


if __name__ == '__main__':
    unittest.main()
