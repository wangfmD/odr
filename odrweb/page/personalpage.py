# coding:utf-8
from time import sleep

from selenium.webdriver.support.select import Select

from odrweb.page.browser import Page

jf_consult = {"jf_type": u"消费维权",
              "jf_desc": u"假冒商品",
              "jf_appeal": u"假一赔十"}

jf_info_all = {"jf_desc": u"申自然人-被自然人",
               "applicant_type": u"非法人组织",  # 自然人 法人 非法人组织
               "disputer_type": u"自然人",  # 自然人 法人 非法人组织
               "agent_type": "special",  # "" common special,
               "agent_b_type": "special",  # common special,

               "jf_appeal": u"假一赔十",
               "applicant_name": u"企业或机构名称",  #
               "world_credit_id": "abcde1234567890",
               "applicant": u"钱桂林",
               "applicant_tel": "13160077223",
               "applicant_pwd": "123456",
               "applicant_id": "321023199508166636",
               "applicant_addr": u"1栋2单元303",

               "disputer": u"王发明",
               "disputer_tel": "13913031374",
               "disputer_world_credit_id": "zxcvbnmasdfghjk123",
               "disputer_name": u"企业或机构名称",
               "disputer_id": "",
               "disputer_addr": u"10栋1单元101",

               "agent_name": u"徐传珠",
               "agent_tel": "15295745648",
               "agent_id": "321281199507077775",

               "agent_b_name": u"段志勇",
               "agent_b_tel": "15895996954",
               "agent_b_id": ""
               }


class PersonalPage(Page):
    x_manual_consult = '//a[contains(text(), "人工咨询")]'  # 第一行人工咨询
    x_ = '//a[text()="申请调解"]/../a[2]'  # 第一行评估
    x_consultation_list= '' #咨询
    x_assessment_list = ''  #评估
    x_dispute_list = '//a[text()="调解"]' #调解
    x_dispute_list_search_input = '//a[text()="调解"]/../../following-sibling::div/input'
    x_dispute_list_search_btn = '//a[text()="调解"]/../../../div/button'
    x_lawsuit_list=''   # 诉讼
    x_judicial_list=''  # 司法确认

    def dispute_search(self, content):
        self.find_element_by_xpath(self.x_dispute_list).click()
        self.find_element_by_xpath(self.x_dispute_list_search_input).send_keys(content)
        self.find_element_by_xpath(self.x_dispute_list_search_btn).click()

    def consult(self, **kwargs):
        '''咨询录入'''
        # 进入我要咨询输入页面
        self.driver.find_element_by_xpath('//*[@id="personal-content"]/div[1]/div[2]/div[1]/div[2]').click()
        select_xpath = '/html/body/div[2]/div/div/div/form/div[1]/div/select'
        Select(self.driver.find_element_by_xpath(select_xpath)).select_by_visible_text(u'消费维权')
        self.driver.find_element_by_xpath('//textarea[@id="textarea_title"]').send_keys(kwargs["jf_desc"])
        self.driver.find_element_by_xpath('//textarea[@id="textarea_content"]').send_keys(kwargs["jf_appeal"])
        # 申请提交
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div[6]/button').click()
        sleep(1)
        # 确认
        self.driver.find_element_by_xpath('//a[text()="是"]').click()
        sleep(2)
        # 返回首页
        self.driver.find_element_by_xpath('/html/body/nav/div/div[1]/a/div[1]').click()

    def verification_consult(self, jf_info):
        ''''''
        try:
            jf_desc = self.driver.find_element_by_xpath('//div[@id="consultation"]/div[1]/div[3]/ul/li[3]').text
            res = jf_desc.split(u'：')[-1]
        except:
            res = "*None*"
        print "expect: ", jf_info
        print "result: ", res

        return res == jf_info

    def verification_consult_input(self):

        try:
            res = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[2]/counselors/div/div[1]/div[2]/div[1]/button')
        except:
            res = "*None*"
        # 校验搜索按键名称
        return res == u"搜索"

    # 婚姻继承
    def evaluate(self, **kwargs):
        '''评估录入'''

        # 进入我要评估输入页面
        self.driver.find_element_by_xpath('//div[text()="我要评估"]').click()
        select_xpath = '/html/body/div[2]/div/div/div/form/div[1]/div/select'
        Select(self.driver.find_element_by_xpath(select_xpath)).select_by_visible_text(u'消费维权')
        self.driver.find_element_by_xpath('//textarea[@id="textarea_title"]').send_keys(kwargs['jf_desc'])
        self.driver.find_element_by_xpath('//textarea[@id="textarea_content"]').send_keys(kwargs['jf_appeal'])
        # 申请提交
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div[6]/button').click()
        # 确认
        sleep(0.5)
        # self.driver.find_element_by_xpath('//a[text()="是"]').click()

    def verification_evaluate(self, jf_info):
        ''' '''
        # 验证纠纷描述内容
        try:
            mediate_desc = self.driver.find_element_by_xpath('//div[@id="assessment"]/div[1]/div[3]/ul/li[3]').text
            res = mediate_desc.split(u'：')[-1]
        except:
            res = '*None*'
        print "expect: ", jf_info
        print "result: ", res

        return res == jf_info

    def apply_mediate(self, **kwargs):

        '''
        用户申请调解
        :param chrome:
        :return:
        '''
        # 点击选择我要调解
        self.driver.find_element_by_xpath('//div[@id="personal-content"]/div[1]/div[2]/div[3]/div[2]').click()

        sleep(1)
        # 弹出提示框并点击
        self.driver.find_element_by_xpath('//div[@id="layui-layer1"]/div[3]/a[1]').click()
        # 选择申请人身份为我是申请人
        self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div/div[2]/div[2]/div').click()

        sleep(1)
        # 选择调解类型
        # self.driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div/label[2]/span[2]').click()
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/form/div[1]/div/div/label[2]/span[2]').click()
        # 输入纠纷描述、我的诉求
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/form/div[2]/div/div/div/textarea').send_keys(kwargs['jf_desc'])
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/form/div[3]/div/div/div/textarea').send_keys(kwargs['jf_appeal'])
        # 选择纠纷发生地
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/form/div[4]/div/span[2]').click()
        self.driver.find_element_by_link_text(u"浙江省").click()
        self.driver.find_element_by_link_text(u"杭州市").click()
        self.driver.find_element_by_link_text(u"上城区").click()
        self.driver.find_element_by_link_text(u"清波街道").click()
        se = '//div[@id="app"]/div/div[3]/form/div[4]/div/div/div/div[2]/div[5]/dl/dd/a[1]'
        self.driver.find_element_by_xpath(se).click()
        sleep(0.5)

        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/form/div[6]/div/div[1]/input').click()

        sleep(1)
        # 选择机构
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/div[3]/div/div/div[2]/div[2]/ul/li[1]/button').click()
        # self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()

        sleep(1)
        # 点击下一步进入填写申请人信息页面
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/div[5]').click()
        # 申请人信息默认填写，直接点击下一步进入被申请人信息填写
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[2]/p[3]/span[2]').click()

        sleep(1)
        # 填写被申请人姓名、电话号码
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[2]/div/div/input').send_keys(kwargs['disputer'])
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[4]/div/div/input').send_keys(kwargs['disputer_tel'])
        # 点击提交弹出提示框
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[2]/p[3]/span[2]').click()

        sleep(1)
        # 点击提示框确定
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()

        sleep(1)
        # 点击查看纠纷详情
        # self.driver.find_element_by_xpath('//div[@id="mediate"]/div[1]/div[4]/div[2]/a[1]').click()
        #
        # sleep(1)
        # # 点击返回列表
        # self.driver.find_element_by_xpath('/html/body/section[1]/button').click()

    def verification_apply_mediate(self, jf_desc):
        try:
            mediate_desc = self.driver.find_element_by_xpath('//div[@id="mediate"]/div[1]/div[3]/ul/li[7]').text
            res = mediate_desc.split(u'：')[-1]
        except:
            res = "*None*"
        print "result: ", res
        print "expect: ", jf_desc
        return res == jf_desc

    def _security_settings(self):
        ''''''
        self.driver.find_element_by_xpath('//div[@id="personal-title"]/div[2]/ul/li[2]/a').click()

    def modify_passwd(self, old, new):
        '''修改密码'''
        self._security_settings()
        sleep(1)
        # 点击修改
        self.find_element_by_xpath(
            '//div[@id="personal"]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]/a').click()
        # 输入原密码
        sleep(1)
        self.find_element_by_xpath(
            '//div[@id="login_password"]/div/div/div[2]/form/div[1]/div/div[1]/input').clear()
        self.find_element_by_xpath(
            '//div[@id="login_password"]/div/div/div[2]/form/div[1]/div/div[1]/input').send_keys(old)
        # 输入新密码
        self.find_element_by_xpath(
            '//div[@id="login_password"]/div/div/div[2]/form/div[2]/div/div/input').send_keys(new)
        # 确认新密码
        self.find_element_by_xpath(
            '//div[@id="login_password"]/div/div/div[2]/form/div[3]/div/div/input').send_keys(new)
        # 提交
        self.find_element_by_xpath(
            '//div[@id="login_password"]/div/div/div[2]/form/div[4]/div/button[1]/span').click()


def t():
    from odrweb.page.homepage import HomePage
    from odrweb.core.initdata import users
    homepage = HomePage()
    homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
    homepage.user_personal_center()
    per = PersonalPage(homepage)
    per.consult(**jf_consult)


if __name__ == '__main__':
    t()
