# coding: utf-8
import sys
import unittest
from odrweb.core.initdata import users

from odrweb.page.simpledisputepage import SimpleDisputePage
from odrweb.page.homepage import HomePage

reload(sys)
sys.setdefaultencoding("utf-8")


class SimpleJfInputCommit(unittest.TestCase):
    '''调解员-简易案件提交'''

    def setUp(self):
        self.homepage = BrowserWhole().page
        print "\n--------------------"

    def tearDown(self):
        pass
        self.homepage.quit()

    def test_01(self):
        '''简易案件登记-申请人-被申请人'''
        simple_jf_info = {"applicant": u"段志勇",
                          "applicant_tel": "15895996954",
                          "applicant_id": "",
                          "applicant_nation": u"汉族",
                          "applicant_job": u"测试工程师",
                          "applicant_addr": u"1栋2单元303",

                          "disputer": u"王发明",
                          "disputer_tel": '13913031374',
                          "disputer_nation": u"汉族",
                          "disputer_job": "",
                          "disputer_addr": "",

                          "agent_name": u"徐传珠",
                          "agent_tel": '15295745648',
                          "agent_id": '321281199507077775',

                          "agent_name_b": u"钱桂林",
                          "agent_tel_b": '13160077223',
                          "agent_id_b": "321023199508166636",

                          "jf_desc": u"简易案件登记-申请人-被申请人",
                          "jf_appeal": u"类型是否正确",
                          "jf_action": u"验证类型",
                          "jf_time": u"三天"
                          }
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        simple_page = SimpleDisputePage(self.homepage)
        simple_page.simple_jf_input(**simple_jf_info)
        simple_page.commit()
        res = simple_page.verification_commit(**simple_jf_info)
        self.assertEqual(True, res)


    def test_02(self):
        '''简易案件-申请人-代理人-被申请人'''
        simple_jf_info = {"applicant": u"段志勇",
                          "applicant_tel": "15895996954",
                          "applicant_id": "",
                          "applicant_nation": u"汉族",
                          "applicant_job": u"测试工程师",
                          "applicant_addr": u"1栋2单元303",

                          "disputer": u"王发明",
                          "disputer_tel": '13913031374',
                          "disputer_nation": u"汉族",
                          "disputer_job": "",
                          "disputer_addr": "",

                          "agent_name": u"徐传珠",
                          "agent_tel": '15295745648',
                          "agent_id": '321281199507077775',

                          "agent_name_b": u"钱桂林",
                          "agent_tel_b": '13160077223',
                          "agent_id_b": "321023199508166636",

                          "jf_desc": u"简易案件-申请人-代理人-被申请人",
                          "jf_appeal": u"类型是否正确",
                          "jf_action": u"验证类型",
                          "jf_time": u"三天"
                          }
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        simple_page = SimpleDisputePage(self.homepage)
        simple_page.simple_jf_agent_commit(**simple_jf_info)
        simple_page.commit()
        res = simple_page.verification_commit(**simple_jf_info)
        self.assertEqual(True, res)

    def test_03(self):
        '''简易案件-申请人-被申请人-代理人'''
        simple_jf_info = {"applicant": u"段志勇",
                          "applicant_tel": "15895996954",
                          "applicant_id": "",
                          "applicant_nation": u"汉族",
                          "applicant_job": u"测试工程师",
                          "applicant_addr": u"1栋2单元303",

                          "disputer": u"王发明",
                          "disputer_tel": '13913031374',
                          "disputer_nation": u"汉族",
                          "disputer_job": "",
                          "disputer_addr": "",

                          "agent_name": u"徐传珠",
                          "agent_tel": '15295745648',
                          "agent_id": '321281199507077775',

                          "agent_name_b": u"钱桂林",
                          "agent_tel_b": '13160077223',
                          "agent_id_b": "321023199508166636",

                          "jf_desc": u"简易案件-申请人-被申请人-代理人",
                          "jf_appeal": u"类型是否正确",
                          "jf_action": u"验证类型",
                          "jf_time": u"三天"
                          }
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        simple_page = SimpleDisputePage(self.homepage)
        simple_page.simple_jf_agent_b_commit(**simple_jf_info)
        simple_page.commit()
        res = simple_page.verification_commit(**simple_jf_info)
        self.assertEqual(True, res)

    def test_04(self):
        '''简易案件-申请人-代理人-被申请人-代理人'''
        simple_jf_info = {"applicant": u"段志勇",
                          "applicant_tel": "15895996954",
                          "applicant_id": "",
                          "applicant_nation": u"汉族",
                          "applicant_job": u"测试工程师",
                          "applicant_addr": u"1栋2单元303",

                          "disputer": u"王发明",
                          "disputer_tel": '13913031374',
                          "disputer_nation": u"汉族",
                          "disputer_job": "",
                          "disputer_addr": "",

                          "agent_name": u"徐传珠",
                          "agent_tel": '15295745648',
                          "agent_id": '321281199507077775',

                          "agent_name_b": u"钱桂林",
                          "agent_tel_b": '13160077223',
                          "agent_id_b": "321023199508166636",

                          "jf_desc": u"简易案件-申请人-代理人-被申请人-代理人",
                          "jf_appeal": u"类型是否正确",
                          "jf_action": u"验证类型",
                          "jf_time": u"三天"
                          }
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        simple_page = SimpleDisputePage(self.homepage)
        simple_page.simple_jf_agent_agent_b_commit(**simple_jf_info)
        simple_page.commit()
        res = simple_page.verification_commit(**simple_jf_info)
        self.assertEqual(True, res)


    def test_05(self):
        '''简易案件登记-添加申请人、被申请人-删除申请人、被申请人'''
        simple_jf_info = {"applicant": u"段志勇",
                          "applicant_tel": "15895996954",
                          "applicant_id": "",
                          "applicant_nation": u"汉族",
                          "applicant_job": u"测试工程师",
                          "applicant_addr": u"1栋2单元303",

                          "disputer": u"王发明",
                          "disputer_tel": '13913031374',
                          "disputer_nation": u"汉族",
                          "disputer_job": "",
                          "disputer_addr": "",

                          "agent_name": u"徐传珠",
                          "agent_tel": '15295745648',
                          "agent_id": '321281199507077775',

                          "agent_name_b": u"钱桂林",
                          "agent_tel_b": '13160077223',
                          "agent_id_b": "321023199508166636",

                          "jf_desc": u"简易案件登记-添加申请人、被申请人-删除申请人、被申请人",
                          "jf_appeal": u"类型是否正确",
                          "jf_action": u"验证类型",
                          "jf_time": u"三天"
                          }
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        simple_page = SimpleDisputePage(self.homepage)
        simple_page.simple_jf_add_delete(**simple_jf_info)
        simple_page.commit()
        res = simple_page.verification_commit(**simple_jf_info)
        self.assertEqual(True, res)


    def test_06(self):
        '''简易案件-两个申请人-两个申请人代理人-两个被申请人-一个被申请人代理人'''
        simple_jf_info = {"applicant": u"段志勇",
                          "applicant_tel": "15895996954",
                          "applicant_id": "",
                          "applicant_nation": u"汉族",
                          "applicant_job": u"测试工程师",
                          "applicant_addr": u"1栋2单元303",

                          "disputer": u"王发明",
                          "disputer_tel": '13913031374',
                          "disputer_nation": u"汉族",
                          "disputer_job": "",
                          "disputer_addr": "",

                          "agent_name": u"徐传珠",
                          "agent_tel": '15295745648',
                          "agent_id": '321281199507077775',

                          "agent_name_b": u"钱桂林",
                          "agent_tel_b": '13160077223',
                          "agent_id_b": "321023199508166636",

                          "jf_desc": u"简易案件-两个申请人-两个申请人代理人-两个被申请人-一个被申请人代理人",
                          "jf_appeal": u"类型是否正确",
                          "jf_action": u"验证类型",
                          "jf_time": u"三天"
                          }
        self.homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
        simple_page = SimpleDisputePage(self.homepage)
        simple_page.simple_jf_add_applicant_disputer(**simple_jf_info)
        simple_page.commit()
        res = simple_page.verification_commit_add(**simple_jf_info)
        self.assertEqual(True,res)







if __name__ == '__main__':
    unittest.main()
