# coding:utf-8
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    # 咨询
    x_consultation_list = ''  # 咨询
    x_manual_consult_a = '//a[contains(text(), "人工咨询")]'                # 咨询-第一行人工咨询
    x_manual_consult_search_btn = '//button[contains(text(), "搜索")]'      # 咨询-人工咨询-搜索
    x_manual_consult_search_input = '//button[contains(text(), "搜索")]/preceding-sibling::div/input' # 咨询-人工咨询-搜索输入框
    x_manual_consult_select_btn = '//button[contains(text(),"选择")]'         # 咨询-人工咨询-选择
    #
    x_manual_consult_p2p_end_span = '(//span[contains(text(),"案件类型")]/../following-sibling::div/a)[1]'  # 咨询-人工咨询-选择-结束咨询
    x_manual_consult_p2p_end_star_span = '//p[contains(text(),"请对咨询师进行星级评价")]/preceding-sibling::span'  # 结束咨询-选星
    x_manual_consult_p2p_end_input = '//p[contains(text(),"请对咨询师进行星级评价")]/../following-sibling::div/div/textarea' # 结束咨询-咨询评价输入
    x_manual_consult_p2p_commit_btn = '//button[contains(text(),"提交评价")]'       # 结束咨询-咨询评价提交
    x_manual_consult_p2p_back_span = '(//span[contains(text(),"案件类型")]/../following-sibling::div/a)[2]'  # 咨询-人工咨询-选择-返回列表
    x_manual_consult_assessment = '(//a[text()="评估"])[2]'       # 咨询列表-第一行评估
    x_manual_consult_apply='//a[contains(text(),"申请调解")]'     # 咨询列表-申请调解
    # 评估
    x_assessment_list = '(//a[contains(text(),"评估")])[2]'  # 评估
    x_assessment_apply_report = '//a[contains(text(),"申请评估报告")]'
    # 调解mediate
    x_dispute_list = '//a[text()="调解"]'  # 调解 (//a[contains(text(),"调解")])[2]
    x_dispute_list_search_input = '//a[text()="调解"]/../../following-sibling::div/input'
    x_dispute_list_search_btn = '//a[text()="调解"]/../../../div/button'
    x_lawsuit_list = ''  # 诉讼
    x_judicial_list = ''  # 司法确认

    #
    x_person_data_link_a = '//a[contains(text(),"我的资料")]'
    x_person_data_input = '//div[contains(text(), "详细地址")]/following-sibling::div/div/input'
    x_person_data_save_btn = '//div[text()="保存"]'
    x_person_data_save_suc_a = '//a[text()="确定"]'
    x_security_setting = '//a[contains(text(),"安全设置")]'


    def apply_revocation(self):
        pass

    def dispute_search(self, content):
        self.find_element_by_xpath(self.x_dispute_list).click()
        self.find_element_by_xpath(self.x_dispute_list_search_input).send_keys(content)
        self.find_element_by_xpath(self.x_dispute_list_search_btn).click()

    def consult(self, **kwargs):
        """咨询录入"""
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
        """"""
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
            res = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/counselors/div/div[1]/div[2]/div[1]/button')
        except:
            res = "*None*"
        # 校验搜索按键名称
        return res == u"搜索"

    # 婚姻继承
    def evaluate(self, **kwargs):
        """评估录入"""

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
        """ """
        # 验证纠纷描述内容
        try:
            mediate_desc = self.driver.find_element_by_xpath('//div[@id="assessment"]/div[1]/div[3]/ul/li[3]').text
            res = mediate_desc.split(u'：')[-1]
        except:
            res = '*None*'
        print "expect: ", jf_info
        print "result: ", res

        return res == jf_info

    def _security_settings(self):
        """进入安全设置
        """
        self.driver.find_element_by_xpath('//div[@id="personal-title"]/div[2]/ul/li[2]/a').click()

    def modify_passwd(self, old, new):
        """修改密码
        """
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

    def manual_consult(self):
        self.find_element_by_xpath(self.x_manual_consult_a).click()

    def manual_consult_search(self, search_ctx):
        """进入人工咨询页面-查询
        """
        self.find_element_by_xpath(self.x_manual_consult_a).click()
        self.find_element_by_xpath(self.x_manual_consult_search_input).send_keys(search_ctx)
        self.find_element_by_xpath(self.x_manual_consult_search_btn).click()
        sleep(1)

    def verification_manual_consult_search(self, expect_name):
        try:
            name = self.find_element_by_xpath('//div[@id="table"]/div[2]/table/tbody/tr/td[2]').text
        except:
            name = "**None**"
        print "result: ", name
        print "expect: ", expect_name
        return name == expect_name

    def manual_consult_select_back(self):
        """进入人工咨询页面-选择
        """
        self.find_element_by_xpath(self.x_manual_consult_a).click()
        # 选择咨询师
        self.find_element_by_xpath(self.x_manual_consult_select_btn).click()
        #
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.x_manual_consult_p2p_back_span)))
        # sleep(3)
        element.click()
        sleep(1)


    def manual_consult_select_end(self):
        """进入人工咨询页面-结束
        """
        self.find_element_by_xpath(self.x_manual_consult_a).click()
        # 选择咨询师
        # self.find_element_by_xpath(self.x_manual_consult_select_btn).click()
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.x_manual_consult_p2p_end_span)))
        #
        # self.find_element_by_xpath(self.x_manual_consult_p2p_end_span).click()
        element.click()
        self.find_element_by_xpath(self.x_manual_consult_p2p_end_star_span)
        self.find_element_by_xpath(self.x_manual_consult_p2p_end_input).send_keys(u"能够完美解答我的问题，好评")
        self.find_element_by_xpath(self.x_manual_consult_p2p_commit_btn).click()
        sleep(1)

    def act_manual_consult_apply(self):
        """咨询列表-申请调解
        """
        self.find_element_by_xpath(self.x_manual_consult_apply).click()

    def verfc_act_manual_consult_apply(self):
        ecpect_res = u"下一步"
        try:
            res = self.find_element_by_xpath('//div[text()="下一步"]').text
        except:
            res="**None**"
        print "result: ", res
        print "expect: ", ecpect_res
        return res == ecpect_res

    def act_manual_consult_2_assessment(self):
        """咨询列表-评估
        """
        self.find_element_by_xpath(self.x_manual_consult_assessment).click()
        # 等待申请评估报告btn
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="申请评估报告"]')))

    def act_dispute_search(self,search_by_name_or_id):
        """调解列表-查询
        """
        self.find_element_by_xpath(self.x_dispute_list).click()
        sleep(0.5)
        self.find_element_by_xpath(self.x_dispute_list_search_input).clear()
        self.find_element_by_xpath(self.x_dispute_list_search_input).send_keys(search_by_name_or_id)
        self.find_element_by_xpath(self.x_dispute_list_search_btn).click()

    def get_dispute_search_id(self):
        """获取第二行的纠纷编号，用于查询
        """
        self.find_element_by_xpath(self.x_dispute_list).click()
        try:
            res = self.find_element_by_xpath('//div[@id="mediate"]/div[2]/div[3]/ul/li[2]').text
            _, id = res.split(u'：')
        except:
            id= None
        return id

    def verfc_act_dispute_search_by_id(self, ecpect_res):
        """by id
        """
        sleep(1)
        try:
            res = self.find_element_by_xpath('//div[@id="mediate"]/div[1]/div[3]/ul/li[2]').text  # 调解编号：1665792F2D099
            _,id = res.split(u'：')
        except:
            id = '**None**'

        print "result: ", id
        print "expect: ", ecpect_res
        return id == ecpect_res

    def act_dispute_schedule(self):
        """调解列表-调解进度
        """
        self.find_element_by_xpath(self.x_dispute_list).click()
        sleep(2)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="调解进度"]')))
        self.find_element_by_xpath('//a[text()="调解进度"]').click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="确定"]')))
        self.find_element_by_xpath('//button[text()="确定"]').click()


    def act_dispute_detail_info_back(self):
        """调解列表-纠纷详情-返回列表
        """
        self.find_element_by_xpath(self.x_dispute_list).click()
        sleep(2)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="纠纷详情"]')))
        self.find_element_by_xpath('//a[text()="纠纷详情"]').click()
        self.find_element_by_xpath('//button[text()="返回列表"]').click()

    def act_dispute_detail_info_save(self):
        """调解列表-纠纷详情-保存
        """
        self.find_element_by_xpath(self.x_dispute_list).click()
        sleep(2)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="纠纷详情"]')))
        self.find_element_by_xpath('//a[text()="纠纷详情"]').click()
        self.find_element_by_xpath('//button[text()="返回列表"]').click()

    def act_dispute_detail_info_schedule(self):
        """调解列表-纠纷详情-解纷进度
        """
        self.find_element_by_xpath(self.x_dispute_list).click()
        sleep(2)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="纠纷详情"]')))
        self.find_element_by_xpath('//a[text()="纠纷详情"]').click()
        self.find_element_by_xpath('//span[text()="解纷进度"]').click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//button[text()="确定"])[3]')))
        self.find_element_by_xpath('(//button[text()="确定"])[3]').click()

    def act_case_revocation(self):
        """案件撤回"""
        sleep(0.5)
        revocation_el = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="撤回案件"]')))
        revocation_el.click()

        ok_el = WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="确定"]'))) # 确定，取消
        ok_el.click()
        sleep(0.5)
        ok_el = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="确定"]'))) # 确定后确认
        ok_el.click()

    def verfc_case_revocation(self):
        # 进度状态
        result = self.find_element_by_xpath('//span[text()="提交申请"]/../../li[3]/span').text
        return result == u'撤回调解'

    def tel_binding(self):
        """绑定手机-取消
        """
        self.find_element_by_xpath(self.x_security_setting).click()
        # 等待修改按键
        modify_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//td[text()="绑定手机"]/../td[4]/a')))
        modify_btn.click()
        # self.find_element_by_xpath('//td[text()="绑定手机"]/../td[4]/a').click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//span[text()="取消"])[2]')))
        element.click()

    def mail_binding(self):
        """绑定邮箱-取消
        """
        self.find_element_by_xpath(self.x_security_setting).click()
        # 等待修改按键
        modify_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//td[text()="绑定邮箱"]/../td[4]/a')))
        modify_btn.click()
        # self.find_element_by_xpath('//td[text()="绑定邮箱"]/../td[4]/a').click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//span[text()="取消"])[3]')))
        element.click()
        # self.find_element_by_xpath('(//span[text()="取消"])[3]').click()

    def setting_signature(self):
        """预留签名-取消
        """
        self.find_element_by_xpath(self.x_security_setting).click()
        # 等待修改按键
        modify_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//td[text()="预留签名"]/../td[4]/a')))
        modify_btn.click()
        # self.find_element_by_xpath('//td[text()="预留签名"]/../td[4]/a').click()
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="取 消"]')))
        element.click()
        # self.find_element_by_xpath('//span[text()="取 消"]').click()

    def person_data_save(self):
        """我的资料-保存"""
        # 点击我的资料链接
        self.find_element_by_xpath(self.x_person_data_link_a).click()
        # 输入详细地址
        self.find_element_by_xpath(self.x_person_data_input).clear()
        self.find_element_by_xpath(self.x_person_data_input).send_keys('30#')
        # 点击保存
        self.find_element_by_xpath(self.x_person_data_save_btn).click()
        # 等待更新成功-确定btn
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.x_person_data_save_suc_a)))
        element.click()


def t():
    from odrweb.page.homepage import HomePage
    from odrweb.core.initdata import users
    homepage = HomePage()
    homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
    homepage.user_personal_center()
    per = PersonalPage(homepage)
    per.consult(**jf_consult)

class PersonalCenter(Page):

    def conciliation_list(self):
        # 点开调解列表
        self.find_element_by_xpath('//a[text()="调解"]').click()

    def get_last_conciliation_number(self):
        # 获取最新的纠纷编号
        number = self.find_element_by_xpath('//div[@class="list-item"][1]//div[@class="case-detail"]//li[2]').text
        return number

    def in_conciliation(self):
        # 选择我要调解
        self.find_element_by_xpath('//div[text()="我要调解"]').click() #点击我要调解
        sleep(1)
        self.find_element_by_xpath('//div[text()="重要提示"]/..//a[text()="确定"]').click() #重要提示-确定

    def verfc_conciliation_create_successful(self,  number1, number2):
        # 新旧案件编号不等说明新增成功
        if number1 == number2:
            return False
        else:
            return True

class RolerChoose(Page):

    def normal_proxy(self):
        # 选择一般代理人身份
        self.find_element_by_xpath("//div[contains(text(),'我是代理人')]/../div/div/div/div[contains(text(),'申请调解')]").click()


if __name__ == '__main__':
    t()
