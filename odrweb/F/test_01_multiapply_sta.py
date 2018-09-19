# -*- coding: utf-8 -*-
import unittest
from time import sleep
import sys
from odrweb.core.initdata import users
from odrweb.page.homepage import HomePage
from odrweb.page.InPersonalCenter import PersonalCenter
from odrweb.page.InRolerChoose import RolerChoose
from odrweb.page.InConciliationInfo import ConciliationInfo
from odrweb.page.InApplyInfo import InApplyInfo

reload(sys)
sys.setdefaultencoding("utf-8")

class multiapply(unittest.TestCase):
    '''复数申请人'''
    def setUp(self):
        self.homepage = HomePage()

    def tearDown(self):
        self.homepage.quit()

    def test_01(self):
        '''复数申请人'''

        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center() #切换到个人中心页面

        sleep(2)

        #个人中心-我要调解
        PersonalCenterPage = PersonalCenter(self.homepage)
        PersonalCenterPage.InConciliation() #切换到纠纷调解页面

        sleep(2)

        #角色身份选择

        RolerChoosePage = RolerChoose(PersonalCenterPage)
        RolerChoosePage.NormalProxy() #一般代理人身份

        #纠纷详情需要录入的信息
        ConciliationDetail = {
            "纠纷类型":"交通事故",
            "纠纷描述":u'自动化测试',
            "我的诉求":u'自动化测试成功',
            "纠纷发生省份":"浙江省",
            "纠纷发生市区":"杭州市",
            "纠纷发生区县":"",
            "纠纷发生街道":"",
            "纠纷发生社区":"",
            "调解机构":'北明心理咨询演示学习机构(西湖区)'
        }

        ConciliationInfoPage = ConciliationInfo(RolerChoosePage)
        ConciliationInfoPage.InputConciliationInfo(**ConciliationDetail)

        MultiApply = {
                 "roler":
                     [
                         {
                            "申请人类型": "自然人",
                            "申请人性别":"男",
                            "联系电话":u"15850787868",
                            "身份证号": u"320102199107292810",
                            "常住省份":"浙江省" ,
                            "常住市区":"宁波市",
                            "常住区县":"宁海县",
                            "常住街道":"茶院乡",
                            "详细地址":u"浙江宁波"
                         },
                        {
                            "申请人类型": "2",
                            "name": u"陈陈",
                            "tel": "17625908729"
                        }
                     ]
                 }

        ApplyInfoPage = InApplyInfo(ConciliationInfoPage)
        ApplyInfoPage.InputApplyInfo(**MultiApply)

        '''

        #切换到申请人页面
        #申请人1为自然人
        self.homepage.find_element_by_xpath('//div[@class="formMain"][1]/div/label[text()="申请人："]/../div/div/input').send_keys(u'陈瑶玮') #填写申请人1姓名
        #self.homepage.find_element_by_xpath('//div[@class="formMain"][1]/div/label[text()="申请人性别："]/../div/div/label/span/input[@value="男"]/../span').click() #自然人1性别点选
        self.homepage.find_element_by_xpath('//div[@class="formMain"][1]/div/label[text()="联系电话："]/../div/div/input').send_keys(u'15850787868') #自然人1电话
        self.homepage.find_element_by_xpath('//div[@class="formMain"][1]/div/label[text()="身份证号："]/../div/div/input').send_keys(u'320102199107292810') #自然人1身份证号

        self.homepage.find_element_by_xpath('//div[@class="formMain"][1]/div/label[text()="常住地区："]/../div/span[@class="city-picker-span"]').click() #唤出常住地区选项卡
        self.homepage.find_element_by_xpath('//div[@class="formMain"][1]/div/label[text()="常住地区："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select province"]/dl/dd/a[text()="浙江省"]').click() #点选常住省份
        self.homepage.find_element_by_xpath('//div[@class="formMain"][1]/div/label[text()="常住地区："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select city"]/dl/dd/a[text()="宁波市"]').click() #点选常住市区
        self.homepage.find_element_by_xpath('//div[@class="formMain"][1]/div/label[text()="常住地区："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select district"]/dl/dd/a[text()="宁海县"]').click() #点选常住区县
        self.homepage.find_element_by_xpath('//div[@class="formMain"][1]/div/label[text()="常住地区："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select street"]/dl/dd/a[text()="茶院乡"]').click() #点选常住街道

        self.homepage.find_element_by_xpath('//div[@class="formMain"][1]/div/label[text()="详细地址："]/../div/div/input').send_keys(u'浙江宁波')  # 自然人1详细地址
        '''






