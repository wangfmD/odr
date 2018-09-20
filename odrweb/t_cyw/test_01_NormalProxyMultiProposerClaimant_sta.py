# -*- coding: utf-8 -*-
import unittest
from time import sleep
import sys
from odrweb.page.homepage import HomePage
from odrweb.page.InPersonalCenter import PersonalCenter
from odrweb.page.InRolerChoose import RolerChoose
from odrweb.page.InConciliationInfo import ConciliationInfo
from odrweb.page.InProposerInfo import InProposerInfo
from odrweb.page.InClaimantInfo import InClaimantInfo

reload(sys)
sys.setdefaultencoding("utf-8")

class NormalProxyMultiProposerClaimant(unittest.TestCase):
    '''复数申请人'''
    def setUp(self):
        self.homepage = HomePage()

    def tearDown(self):
        self.homepage.quit()

    def test_01(self):
        '''一般代理人身份登录录入纠纷：申请人：自然人、法人、非法人组织|被申请人：自然人、法人、非法人组织(3v3)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：自然人、法人、非法人组织|被申请人：自然人、法人、非法人组织',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "自然人",
                            "申请人": u"李雅莉",
                            "申请人性别": "女",
                            "联系电话": u"15850787868",
                            "身份证号": u"320102196709032828",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                            "申请人类型": "法人",
                            "申请人": u"发明",
                             "社会信用码": "555558888877777",
                             "法定代表人": u"哈哈",
                             "申请人性别": "女",
                             "联系电话": "13913031374",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "申请人类型": "非法人组织",
                             "申请人": u"义和团",
                             "社会信用码": "",
                             "机构代表人": u"桂林",
                             "申请人性别": "男",
                             "联系电话": "13160077223",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"江南皮革厂"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                            "被申请人类型": "自然人",
                            "被申请人姓名": u"慈禧",
                            "被申请人性别": "女",
                            "联系电话": u"15800006666",
                            "身份证号": "",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                             "被申请人类型": "法人",
                             "被申请人": u"大清王朝",
                             "社会信用码": "123451234512345",
                             "法定代表人": u"溥仪",
                             "被申请人性别": "男",
                             "联系电话": "13801240123",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "被申请人类型": "非法人组织",
                             "被申请人": u"太平天国",
                             "社会信用码": "",
                             "机构代表人": u"洪秀全",
                             "被申请人性别": "男",
                             "联系电话": "18966668888",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"宁波兴化"
                         }
                     ]
                 }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_02(self):
        '''一般代理人身份登录录入纠纷：申请人：自然人、法人|被申请人：自然人、法人、非法人组织(2v3)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：自然人、法人|被申请人：自然人、法人、非法人组织',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "自然人",
                            "申请人": u"李雅莉",
                            "申请人性别": "女",
                            "联系电话": u"15850787868",
                            "身份证号": u"320102196709032828",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                            "申请人类型": "法人",
                            "申请人": u"发明",
                             "社会信用码": "555558888877777",
                             "法定代表人": u"哈哈",
                             "申请人性别": "女",
                             "联系电话": "13913031374",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                            "被申请人类型": "自然人",
                            "被申请人姓名": u"慈禧",
                            "被申请人性别": "女",
                            "联系电话": u"15800006666",
                            "身份证号": "",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                             "被申请人类型": "法人",
                             "被申请人": u"大清王朝",
                             "社会信用码": "123451234512345",
                             "法定代表人": u"溥仪",
                             "被申请人性别": "男",
                             "联系电话": "13801240123",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "被申请人类型": "非法人组织",
                             "被申请人": u"太平天国",
                             "社会信用码": "",
                             "机构代表人": u"洪秀全",
                             "被申请人性别": "男",
                             "联系电话": "18966668888",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"宁波兴化"
                         }
                     ]
                 }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_03(self):
        '''一般代理人身份登录录入纠纷：申请人：自然人、非法人组织|被申请人：自然人、法人、非法人组织(2v3)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：自然人、非法人组织|被申请人：自然人、法人、非法人组织',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "自然人",
                            "申请人": u"李雅莉",
                            "申请人性别": "女",
                            "联系电话": u"15850787868",
                            "身份证号": u"320102196709032828",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                             "申请人类型": "非法人组织",
                             "申请人": u"义和团",
                             "社会信用码": "",
                             "机构代表人": u"桂林",
                             "申请人性别": "男",
                             "联系电话": "13160077223",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"江南皮革厂"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                            "被申请人类型": "自然人",
                            "被申请人姓名": u"慈禧",
                            "被申请人性别": "女",
                            "联系电话": u"15800006666",
                            "身份证号": "",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                             "被申请人类型": "法人",
                             "被申请人": u"大清王朝",
                             "社会信用码": "123451234512345",
                             "法定代表人": u"溥仪",
                             "被申请人性别": "男",
                             "联系电话": "13801240123",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "被申请人类型": "非法人组织",
                             "被申请人": u"太平天国",
                             "社会信用码": "",
                             "机构代表人": u"洪秀全",
                             "被申请人性别": "男",
                             "联系电话": "18966668888",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"宁波兴化"
                         }
                     ]
                 }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_04(self):
        '''一般代理人身份登录录入纠纷：申请人：法人、非法人组织|被申请人：自然人、法人、非法人组织(2v3)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：法人、非法人组织|被申请人：自然人、法人、非法人组织',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "法人",
                            "申请人": u"发明",
                             "社会信用码": "555558888877777",
                             "法定代表人": u"哈哈",
                             "申请人性别": "女",
                             "联系电话": "13913031374",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "申请人类型": "非法人组织",
                             "申请人": u"义和团",
                             "社会信用码": "",
                             "机构代表人": u"桂林",
                             "申请人性别": "男",
                             "联系电话": "13160077223",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"江南皮革厂"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                            "被申请人类型": "自然人",
                            "被申请人姓名": u"慈禧",
                            "被申请人性别": "女",
                            "联系电话": u"15800006666",
                            "身份证号": "",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                             "被申请人类型": "法人",
                             "被申请人": u"大清王朝",
                             "社会信用码": "123451234512345",
                             "法定代表人": u"溥仪",
                             "被申请人性别": "男",
                             "联系电话": "13801240123",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "被申请人类型": "非法人组织",
                             "被申请人": u"太平天国",
                             "社会信用码": "",
                             "机构代表人": u"洪秀全",
                             "被申请人性别": "男",
                             "联系电话": "18966668888",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"宁波兴化"
                         }
                     ]
                 }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_05(self):
        '''一般代理人身份登录录入纠纷：申请人：自然人、法人、非法人组织|被申请人：自然人、法人(3v2)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：自然人、法人、非法人组织|被申请人：自然人、法人',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "自然人",
                            "申请人": u"李雅莉",
                            "申请人性别": "女",
                            "联系电话": u"15850787868",
                            "身份证号": u"320102196709032828",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                            "申请人类型": "法人",
                            "申请人": u"发明",
                             "社会信用码": "555558888877777",
                             "法定代表人": u"哈哈",
                             "申请人性别": "女",
                             "联系电话": "13913031374",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "申请人类型": "非法人组织",
                             "申请人": u"义和团",
                             "社会信用码": "",
                             "机构代表人": u"桂林",
                             "申请人性别": "男",
                             "联系电话": "13160077223",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"江南皮革厂"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                            "被申请人类型": "自然人",
                            "被申请人姓名": u"慈禧",
                            "被申请人性别": "女",
                            "联系电话": u"15800006666",
                            "身份证号": "",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                             "被申请人类型": "法人",
                             "被申请人": u"大清王朝",
                             "社会信用码": "123451234512345",
                             "法定代表人": u"溥仪",
                             "被申请人性别": "男",
                             "联系电话": "13801240123",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         }
                     ]
                 }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_06(self):
        '''一般代理人身份登录录入纠纷：申请人：自然人、法人、非法人组织|被申请人：自然人、非法人组织(3v2)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：自然人、法人、非法人组织|被申请人：自然人、非法人组织',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "自然人",
                            "申请人": u"李雅莉",
                            "申请人性别": "女",
                            "联系电话": u"15850787868",
                            "身份证号": u"320102196709032828",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                            "申请人类型": "法人",
                            "申请人": u"发明",
                             "社会信用码": "555558888877777",
                             "法定代表人": u"哈哈",
                             "申请人性别": "女",
                             "联系电话": "13913031374",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "申请人类型": "非法人组织",
                             "申请人": u"义和团",
                             "社会信用码": "",
                             "机构代表人": u"桂林",
                             "申请人性别": "男",
                             "联系电话": "13160077223",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"江南皮革厂"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                            "被申请人类型": "自然人",
                            "被申请人姓名": u"慈禧",
                            "被申请人性别": "女",
                            "联系电话": u"15800006666",
                            "身份证号": "",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                             "被申请人类型": "非法人组织",
                             "被申请人": u"太平天国",
                             "社会信用码": "",
                             "机构代表人": u"洪秀全",
                             "被申请人性别": "男",
                             "联系电话": "18966668888",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"宁波兴化"
                         }
                     ]
                 }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_07(self):
        '''一般代理人身份登录录入纠纷：申请人：自然人、法人、非法人组织|被申请人：法人、非法人组织(3v2)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：自然人、法人、非法人组织|被申请人：法人、非法人组织',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "自然人",
                            "申请人": u"李雅莉",
                            "申请人性别": "女",
                            "联系电话": u"15850787868",
                            "身份证号": u"320102196709032828",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                            "申请人类型": "法人",
                            "申请人": u"发明",
                             "社会信用码": "555558888877777",
                             "法定代表人": u"哈哈",
                             "申请人性别": "女",
                             "联系电话": "13913031374",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "申请人类型": "非法人组织",
                             "申请人": u"义和团",
                             "社会信用码": "",
                             "机构代表人": u"桂林",
                             "申请人性别": "男",
                             "联系电话": "13160077223",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"江南皮革厂"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                             "被申请人类型": "法人",
                             "被申请人": u"大清王朝",
                             "社会信用码": "123451234512345",
                             "法定代表人": u"溥仪",
                             "被申请人性别": "男",
                             "联系电话": "13801240123",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "被申请人类型": "非法人组织",
                             "被申请人": u"太平天国",
                             "社会信用码": "",
                             "机构代表人": u"洪秀全",
                             "被申请人性别": "男",
                             "联系电话": "18966668888",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"宁波兴化"
                         }
                     ]
                 }

        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_08(self):
        '''一般代理人身份登录录入纠纷：申请人：法人、非法人组织|被申请人：法人、非法人组织(2v2)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：法人、非法人组织|被申请人：法人、非法人组织',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "法人",
                            "申请人": u"发明",
                             "社会信用码": "555558888877777",
                             "法定代表人": u"哈哈",
                             "申请人性别": "女",
                             "联系电话": "13913031374",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "申请人类型": "非法人组织",
                             "申请人": u"义和团",
                             "社会信用码": "",
                             "机构代表人": u"桂林",
                             "申请人性别": "男",
                             "联系电话": "13160077223",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"江南皮革厂"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                             "被申请人类型": "法人",
                             "被申请人": u"大清王朝",
                             "社会信用码": "123451234512345",
                             "法定代表人": u"溥仪",
                             "被申请人性别": "男",
                             "联系电话": "13801240123",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "被申请人类型": "非法人组织",
                             "被申请人": u"太平天国",
                             "社会信用码": "",
                             "机构代表人": u"洪秀全",
                             "被申请人性别": "男",
                             "联系电话": "18966668888",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"宁波兴化"
                         }
                     ]
                 }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_09(self):
        '''一般代理人身份登录录入纠纷：申请人：自然人、非法人组织|被申请人：自然人、非法人组织(2v2)'''
        userinfo = {
            "UserName": "17625908729",
            "PassWord": "11111111"}  # 登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center()  # 切换到个人中心页面
        sleep(0.5)
        # 个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation()  # 切换到纠纷调解页面
        sleep(0.5)
        # 角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy()  # 一般代理人身份
        # 纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型": "交通事故",
            "纠纷描述": u'一般代理人身份登录录入纠纷：申请人：自然人、非法人组织|被申请人：自然人、非法人组织',
            "我的诉求": u'自动化测试成功',
            "纠纷发生省份": "浙江省",
            "纠纷发生市区": "宁波市",
            "纠纷发生区县": "宁海县",
            "纠纷发生街道": "茶院乡",
            "纠纷发生社区": "暂不知道",
            "调解机构所在省份": "浙江省",
            "调解机构所在市区": "宁波市",
            "调解机构所在区县": "宁海县",
            "调解机构所在街道": "",
            "调解机构所在社区": "",
            "调解机构名称": u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        # 申请人信息配置
        multiproposer = {
            "roler":
                [
                    {
                        "申请人类型": "自然人",
                        "申请人": u"李雅莉",
                        "申请人性别": "女",
                        "联系电话": u"15850787868",
                        "身份证号": u"320102196709032828",
                        "常住省份": "浙江省",
                        "常住市区": "宁波市",
                        "常住区县": "宁海县",
                        "常住街道": "茶院乡",
                        "详细地址": u"浙江宁波"
                    },
                    {
                        "申请人类型": "非法人组织",
                        "申请人": u"义和团",
                        "社会信用码": "",
                        "机构代表人": u"桂林",
                        "申请人性别": "男",
                        "联系电话": "13160077223",
                        "身份证号": "",
                        "单位省份": "浙江省",
                        "单位市区": "温州市",
                        "单位区县": "",
                        "单位街道": "",
                        "详细地址": u"江南皮革厂"
                    }
                ]
        }
        # 录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        # 名词解释：Claimant被申请人
        # 录入多个被申请人
        multiclaimant = {
            "roler":
                [
                    {
                        "被申请人类型": "自然人",
                        "被申请人姓名": u"慈禧",
                        "被申请人性别": "女",
                        "联系电话": u"15800006666",
                        "身份证号": "",
                        "常住省份": "浙江省",
                        "常住市区": "宁波市",
                        "常住区县": "宁海县",
                        "常住街道": "茶院乡",
                        "详细地址": u"浙江宁波"
                    },
                    {
                        "被申请人类型": "非法人组织",
                        "被申请人": u"太平天国",
                        "社会信用码": "",
                        "机构代表人": u"洪秀全",
                        "被申请人性别": "男",
                        "联系电话": "18966668888",
                        "身份证号": "",
                        "单位省份": "浙江省",
                        "单位市区": "温州市",
                        "单位区县": "",
                        "单位街道": "",
                        "详细地址": u"宁波兴化"
                    }
                ]
        }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_10(self):
        '''一般代理人身份登录录入纠纷：申请人：自然人、法人|被申请人：自然人、法人(2v2)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：自然人、法人|被申请人：自然人、法人',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "自然人",
                            "申请人": u"李雅莉",
                            "申请人性别": "女",
                            "联系电话": u"15850787868",
                            "身份证号": u"320102196709032828",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                            "申请人类型": "法人",
                            "申请人": u"发明",
                             "社会信用码": "555558888877777",
                             "法定代表人": u"哈哈",
                             "申请人性别": "女",
                             "联系电话": "13913031374",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                            "被申请人类型": "自然人",
                            "被申请人姓名": u"慈禧",
                            "被申请人性别": "女",
                            "联系电话": u"15800006666",
                            "身份证号": "",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                             "被申请人类型": "法人",
                             "被申请人": u"大清王朝",
                             "社会信用码": "123451234512345",
                             "法定代表人": u"溥仪",
                             "被申请人性别": "男",
                             "联系电话": "13801240123",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         }
                     ]
                 }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_11(self):
        '''一般代理人身份登录录入纠纷：申请人：法人、非法人组织|被申请人：自然人、非法人组织(2v2)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：法人、非法人组织|被申请人：自然人、非法人组织',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "法人",
                            "申请人": u"发明",
                             "社会信用码": "555558888877777",
                             "法定代表人": u"哈哈",
                             "申请人性别": "女",
                             "联系电话": "13913031374",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "申请人类型": "非法人组织",
                             "申请人": u"义和团",
                             "社会信用码": "",
                             "机构代表人": u"桂林",
                             "申请人性别": "男",
                             "联系电话": "13160077223",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"江南皮革厂"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                            "被申请人类型": "自然人",
                            "被申请人姓名": u"慈禧",
                            "被申请人性别": "女",
                            "联系电话": u"15800006666",
                            "身份证号": "",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                             "被申请人类型": "非法人组织",
                             "被申请人": u"太平天国",
                             "社会信用码": "",
                             "机构代表人": u"洪秀全",
                             "被申请人性别": "男",
                             "联系电话": "18966668888",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"宁波兴化"
                         }
                     ]
                 }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_12(self):
        '''一般代理人身份登录录入纠纷：申请人：法人、非法人组织|被申请人：自然人、法人(2v2)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：法人、非法人组织|被申请人：自然人、法人',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "法人",
                            "申请人": u"发明",
                             "社会信用码": "555558888877777",
                             "法定代表人": u"哈哈",
                             "申请人性别": "女",
                             "联系电话": "13913031374",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "申请人类型": "非法人组织",
                             "申请人": u"义和团",
                             "社会信用码": "",
                             "机构代表人": u"桂林",
                             "申请人性别": "男",
                             "联系电话": "13160077223",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"江南皮革厂"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                            "被申请人类型": "自然人",
                            "被申请人姓名": u"慈禧",
                            "被申请人性别": "女",
                            "联系电话": u"15800006666",
                            "身份证号": "",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                             "被申请人类型": "法人",
                             "被申请人": u"大清王朝",
                             "社会信用码": "123451234512345",
                             "法定代表人": u"溥仪",
                             "被申请人性别": "男",
                             "联系电话": "13801240123",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         }
                     ]
                 }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_13(self):
        '''一般代理人身份登录录入纠纷：申请人：自然人、非法人组织|被申请人：法人、非法人组织(2v2)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：自然人、非法人组织|被申请人：法人、非法人组织',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "自然人",
                            "申请人": u"李雅莉",
                            "申请人性别": "女",
                            "联系电话": u"15850787868",
                            "身份证号": u"320102196709032828",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                             "申请人类型": "非法人组织",
                             "申请人": u"义和团",
                             "社会信用码": "",
                             "机构代表人": u"桂林",
                             "申请人性别": "男",
                             "联系电话": "13160077223",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"江南皮革厂"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                             "被申请人类型": "法人",
                             "被申请人": u"大清王朝",
                             "社会信用码": "123451234512345",
                             "法定代表人": u"溥仪",
                             "被申请人性别": "男",
                             "联系电话": "13801240123",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "被申请人类型": "非法人组织",
                             "被申请人": u"太平天国",
                             "社会信用码": "",
                             "机构代表人": u"洪秀全",
                             "被申请人性别": "男",
                             "联系电话": "18966668888",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"宁波兴化"
                         }
                     ]
                 }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_14(self):
        '''一般代理人身份登录录入纠纷：申请人：自然人、非法人组织|被申请人：自然人、法人(2v2)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：自然人、非法人组织|被申请人：自然人、法人',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "自然人",
                            "申请人": u"李雅莉",
                            "申请人性别": "女",
                            "联系电话": u"15850787868",
                            "身份证号": u"320102196709032828",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                             "申请人类型": "非法人组织",
                             "申请人": u"义和团",
                             "社会信用码": "",
                             "机构代表人": u"桂林",
                             "申请人性别": "男",
                             "联系电话": "13160077223",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"江南皮革厂"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                            "被申请人类型": "自然人",
                            "被申请人姓名": u"慈禧",
                            "被申请人性别": "女",
                            "联系电话": u"15800006666",
                            "身份证号": "",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                             "被申请人类型": "法人",
                             "被申请人": u"大清王朝",
                             "社会信用码": "123451234512345",
                             "法定代表人": u"溥仪",
                             "被申请人性别": "男",
                             "联系电话": "13801240123",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         }
                     ]
                 }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_15(self):
        '''一般代理人身份登录录入纠纷：申请人：自然人、法人|被申请人：法人、非法人组织(2v2)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：自然人、法人|被申请人：法人、非法人组织',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "自然人",
                            "申请人": u"李雅莉",
                            "申请人性别": "女",
                            "联系电话": u"15850787868",
                            "身份证号": u"320102196709032828",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                            "申请人类型": "法人",
                            "申请人": u"发明",
                             "社会信用码": "555558888877777",
                             "法定代表人": u"哈哈",
                             "申请人性别": "女",
                             "联系电话": "13913031374",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                             "被申请人类型": "法人",
                             "被申请人": u"大清王朝",
                             "社会信用码": "123451234512345",
                             "法定代表人": u"溥仪",
                             "被申请人性别": "男",
                             "联系电话": "13801240123",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         },
                         {
                             "被申请人类型": "非法人组织",
                             "被申请人": u"太平天国",
                             "社会信用码": "",
                             "机构代表人": u"洪秀全",
                             "被申请人性别": "男",
                             "联系电话": "18966668888",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"宁波兴化"
                         }
                     ]
                 }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)

    def test_16(self):
        '''一般代理人身份登录录入纠纷：申请人：自然人、法人|被申请人：自然人、非法人组织(2v2)'''
        userinfo={
            "UserName": "17625908729",
            "PassWord": "11111111"} #登录用户配置
        self.homepage.user_login(userinfo["UserName"], userinfo["PassWord"])
        self.homepage.user_personal_center() #切换到个人中心页面
        sleep(0.5)
        #个人中心-我要调解
        personalcenterpage = PersonalCenter(self.homepage)
        personalcenterpage.in_conciliation() #切换到纠纷调解页面
        sleep(0.5)
        #角色身份选择
        rolerchoosepage = RolerChoose(personalcenterpage)
        rolerchoosepage.normal_proxy() #一般代理人身份
        #纠纷详情需要录入的信息（纠纷发生地必须填到街道)
        conciliationdetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'一般代理人身份登录录入纠纷：申请人：自然人、法人|被申请人：自然人、非法人组织',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"宁波市",
            "纠纷发生区县":"宁海县",
            "纠纷发生街道":"茶院乡",
            "纠纷发生社区":"暂不知道",
            "调解机构所在省份":"浙江省",
            "调解机构所在市区":"宁波市",
            "调解机构所在区县":"宁海县",
            "调解机构所在街道":"",
            "调解机构所在社区":"",
            "调解机构名称":u'浙江省宁波市宁海县道路交通事故人民调解委员会'
        }
        conciliationinfopage = ConciliationInfo(rolerchoosepage)
        conciliationinfopage.input_conciliation_info(**conciliationdetail)
        #申请人信息配置
        multiproposer = {
                 "roler":
                     [
                         {
                            "申请人类型": "自然人",
                            "申请人": u"李雅莉",
                            "申请人性别": "女",
                            "联系电话": u"15850787868",
                            "身份证号": u"320102196709032828",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                            "申请人类型": "法人",
                            "申请人": u"发明",
                             "社会信用码": "555558888877777",
                             "法定代表人": u"哈哈",
                             "申请人性别": "女",
                             "联系电话": "13913031374",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "杭州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"浙江杭州"
                         }
                     ]
                 }
        #录入多个申请人信息
        proposerinfopage = InProposerInfo(conciliationinfopage)
        proposerinfopage.input_proposer_info(**multiproposer)
        #名词解释：Claimant被申请人
        #录入多个被申请人
        multiclaimant = {
                 "roler":
                     [
                         {
                            "被申请人类型": "自然人",
                            "被申请人姓名": u"慈禧",
                            "被申请人性别": "女",
                            "联系电话": u"15800006666",
                            "身份证号": "",
                            "常住省份": "浙江省" ,
                            "常住市区": "宁波市",
                            "常住区县": "宁海县",
                            "常住街道": "茶院乡",
                            "详细地址": u"浙江宁波"
                         },
                         {
                             "被申请人类型": "非法人组织",
                             "被申请人": u"太平天国",
                             "社会信用码": "",
                             "机构代表人": u"洪秀全",
                             "被申请人性别": "男",
                             "联系电话": "18966668888",
                             "身份证号": "",
                             "单位省份": "浙江省",
                             "单位市区": "温州市",
                             "单位区县": "",
                             "单位街道": "",
                             "详细地址": u"宁波兴化"
                         }
                     ]
                 }
        claimantinfopage = InClaimantInfo(proposerinfopage)
        claimantinfopage.input_claimant_info(**multiclaimant)











