# -*- coding:utf-8 -*-
import re
from time import sleep

import requests

from odrweb.core.utils import is_male
from odrweb.page.browser import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from odrweb.core.upload import file_upload

class TjyBasePage(Page):
    x_case_input_list_a = '//div[text()="案件登记列表"]'          # 案件登记列表链接
    x_case_list_a = '//li[text()="纠纷调解案件列表"]'  # 纠纷调解案件列表
    x_apply_judicial_list_li = '//li[text()="申请司法确认列表"]'
    x_add_judicial_btn = '//font[text()="新增司法确认"]'

class JudicialInputPage(TjyBasePage):
    # 司法确认
    x_fy_select = '' # 申请受理法院 选择

    def _goto_judicial_input_page(self, **kwargs):
        # 点击进入纠纷调解案件列表
        self.find_element_by_xpath(self.x_case_list_a).click()
        # 点击进入司法确认
        self.find_element_by_xpath(self.x_add_judicial_btn).click()
        # 地区选下拉框
        self.find_element_by_xpath('//div[contains(text(), "申请受理法院：")]/div[1]/div/input').click()
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="杭州"]')))
        el.click()
        # 法院下拉框选择
        self.find_element_by_xpath('//div[contains(text(), "申请受理法院：")]/div[2]/div/input').click()
        el = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="浙江省杭州市上城区人民法院"]')))
        el.click()

    def _applicant_1_input(self, **kwargs):
        # 申请人1
        if kwargs['applicant_type'] == u'自然人':
            self.find_element_by_xpath('//div[contains(text(), "申请人：")]/../div[2]//div[2]/input').clear()
            self.find_element_by_xpath('//div[contains(text(), "申请人：")]/../div[2]//div[2]/input').send_keys(kwargs['applicant'])
        else:
            if kwargs['applicant_type'] == u'法人':
                self.find_element_by_xpath('//div[contains(text(), "申请人：")]/../div/div[1]/div/input[@placeholder="请选择"]').click()
                self.find_element_by_xpath('(//span[text()="法人"])[2]').click()
                self.find_element_by_xpath('//div[contains(text(), "申请人：")]/../div[2]//div[2]/input[@placeholder="请输入企业名称"]').send_keys(kwargs['applicant_name'])
                self.find_element_by_xpath('//div[text()="社会信用代码："]/following-sibling::div/div/input[@placeholder="请输入社会信用代码"]').send_keys(kwargs['world_credit_id'])
                self.find_element_by_xpath('//div[text()="法定代表人："]/following-sibling::div/div/input[@placeholder="请输入法定代表人姓名"]').send_keys(kwargs['applicant'])
            elif kwargs['applicant_type'] == u'非法人组织':
                self.find_element_by_xpath('//div[contains(text(), "申请人：")]/../div/div[1]/div/input[@placeholder="请选择"]').click()
                self.find_element_by_xpath('(//span[text()="非法人组织"])[2]').click()
                self.find_element_by_xpath('//div[contains(text(), "申请人：")]/../div[2]//div[2]/input[@placeholder="请输入机构名称"]').send_keys(kwargs['applicant_name'])
                self.find_element_by_xpath('//div[text()="社会信用代码："]/following-sibling::div/div/input[@placeholder="请输入社会信用代码"]').send_keys(kwargs['world_credit_id'])
                self.find_element_by_xpath('//div[text()="机构代表人："]/following-sibling::div/div/input[@placeholder="请输入机构代表人姓名"]').send_keys(kwargs['applicant'])

        self.find_element_by_xpath('//input[@placeholder="请输入手机号码"]').clear()
        self.find_element_by_xpath('//input[@placeholder="请输入手机号码"]').send_keys(kwargs['applicant_tel'])

        # 根据身份证号，判断性别
        if is_male(kwargs['applicant_id']):
            self.find_element_by_xpath('((//div[text()="性别："])[1]/following-sibling::div/label/span/span)[1]').click()
        else:
            self.find_element_by_xpath('((//div[text()="性别："])[1]/following-sibling::div/label/span/span)[2]').click()
        # 输入身份证
        self.find_element_by_xpath('//input[@placeholder="请输入证件号码"]').clear()
        self.find_element_by_xpath('//input[@placeholder="请输入证件号码"]').send_keys(kwargs['applicant_id'])
        # 居住地址选择
        self.find_element_by_xpath('(//div[contains(text(), "居住地址：")])[1]/../div[2]/div[1]').click()  # 省
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//span[contains(text(),"浙江省")])[16]')))
        sleep(0.2)
        el.click()
        self.find_element_by_xpath('(//div[contains(text(), "居住地址：")])[1]/../div[2]/div[2]').click()  # 市
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//span[contains(text(), "杭州市")])[15]')))
        sleep(0.1)
        el.click()
        self.find_element_by_xpath('(//div[contains(text(), "居住地址：")])[1]/../div[2]/div[3]').click()  # 区
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//span[contains(text(), "上城区")])[2]')))
        sleep(0.1)
        el.click()
        self.find_element_by_xpath('(//div[contains(text(), "居住地址：")])[1]/../div[2]/div[4]').click()  # 街道
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "清波街道")]')))
        sleep(0.1)
        el.click()
        self.find_element_by_xpath('(//div[contains(text(), "居住地址：")])[1]/../div[2]/div[5]//input[@placeholder="请输入详细地址"]').send_keys(u'3#居住地址')

        # 代理人
        if kwargs['agent_type'] == 'special':
            self.find_element_by_xpath('(//div[text()="委托代理人："])[1]/following-sibling::div/div/div/input').click()
            el = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '(//span[text()="特殊授权代理人"])[2]')))
            el.click()
        elif kwargs['agent_type'] == 'common':
            self.find_element_by_xpath('(//div[text()="委托代理人："])[1]/following-sibling::div/div/div/input').click()
            el = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '(//span[text()="一般授权代理人"])[2]')))
            el.click()
        if kwargs['agent_type'] != "":
            self.find_element_by_xpath('(//div[text()="委托代理人："])[1]/following-sibling::div/div[2]//input[@placeholder="请输入代理人姓名"]').clear()
            self.find_element_by_xpath('(//div[text()="委托代理人："])[1]/following-sibling::div/div[2]//input[@placeholder="请输入代理人姓名"]').send_keys(kwargs['agent_name'])
            self.find_element_by_xpath('(//div[text()="手机号码："]/following-sibling::div/div//input[@placeholder="请输入代理人手机号码"])[1]').send_keys(kwargs['agent_tel'])
            self.find_element_by_xpath('(//div[text()="身份证号："]/following-sibling::div/div//input[@placeholder="请输入代理人身份证号码"])[1]').send_keys(kwargs['agent_id'])
            # 根据身份证号，判断性别
            if is_male(kwargs['agent_id']):
                self.find_element_by_xpath('((//div[text()="性别："])[2]/following-sibling::div/label/span/span)[1]').click()
            else:
                self.find_element_by_xpath('((//div[text()="性别："])[2]/following-sibling::div/label/span/span)[2]').click()
        # 文书地址
        self.find_element_by_xpath('(//div[text()="文书送达地址："]/following-sibling::div/div//input[@placeholder="请输入文书送达地址"])[1]').send_keys(u'3#文书地址')

    def _applicant_2_input(self, **kwargs):
        # 申请人2
        if kwargs['disputer_type'] == u'自然人':
            self.find_element_by_xpath('(//div[contains(text(), "申请人：")]/../div[2]//div[2]/input)[2]').clear()
            self.find_element_by_xpath('(//div[contains(text(), "申请人：")]/../div[2]//div[2]/input)[2]').send_keys(kwargs['disputer'])
        else:
            self.find_element_by_xpath('(//div[contains(text(), "申请人：")]/../div/div[1]/div/input[@placeholder="请选择"])[2]').click()  # 申请人类型下拉框
            if kwargs['disputer_type'] == u'法人':
                self.find_element_by_xpath('(//span[text()="法人"])[2]').click()  # 点击法人
                if kwargs['applicant_type'] != u"自然人":
                    self.find_element_by_xpath('(//div[contains(text(), "申请人：")]/../div[2]//div[2]/input)[2]').send_keys(kwargs['disputer_name'])
                    self.find_element_by_xpath('(//div[text()="社会信用代码："]/following-sibling::div/div/input[@placeholder="请输入社会信用代码"])[2]').send_keys(kwargs['world_credit_id'])
                    if kwargs['applicant_type'] == u"法人":
                        self.find_element_by_xpath('(//div[text()="法定代表人："]/following-sibling::div/div/input)[2]').send_keys(kwargs['disputer'])
                    else:
                        self.find_element_by_xpath('(//div[text()="法定代表人："]/following-sibling::div/div/input)[1]').send_keys(kwargs['disputer'])
                else:
                    self.find_element_by_xpath('(//div[contains(text(), "申请人：")]/../div[2]//div[2]/input)').send_keys(kwargs['disputer_name'])
                    self.find_element_by_xpath('//div[text()="法定代表人："]/following-sibling::div/div/input').send_keys(kwargs['disputer'])
            if kwargs['disputer_type'] == u'非法人组织':
                self.find_element_by_xpath('(//span[text()="非法人组织"])[2]').click()
                self.find_element_by_xpath('(//div[contains(text(), "申请人：")]/../div[2]//div[2]/input)[2]').send_keys(kwargs['disputer_name'])
                if kwargs['applicant_type'] != u"自然人":
                    self.find_element_by_xpath('(//div[text()="社会信用代码："]/following-sibling::div/div/input)[2]').send_keys(kwargs['world_credit_id'])
                    if kwargs['applicant_type'] == u"法人":
                        self.find_element_by_xpath('(//div[text()="机构代表人："]/following-sibling::div/div/input)[1]').send_keys(kwargs['disputer'])
                    else:
                        self.find_element_by_xpath('(//div[text()="机构代表人："]/following-sibling::div/div/input)[2]').send_keys(kwargs['disputer'])
                else:
                    self.find_element_by_xpath('(//div[text()="社会信用代码："]/following-sibling::div/div/input)[1]').send_keys(kwargs['world_credit_id'])
                    self.find_element_by_xpath('(//div[text()="机构代表人："]/following-sibling::div/div/input)[1]').send_keys(kwargs['disputer'])
        # 手机号码
        self.find_element_by_xpath('(//input[@placeholder="请输入手机号码"])[2]').clear()
        self.find_element_by_xpath('(//input[@placeholder="请输入手机号码"])[2]').send_keys(kwargs['disputer_tel'])

        # 根据身份证号，判断性别
        if is_male(kwargs['disputer_id']):
            self.find_element_by_xpath('((//div[text()="性别："])[3]/following-sibling::div/label/span/span)[1]').click()
        else:
            self.find_element_by_xpath('((//div[text()="性别："])[3]/following-sibling::div/label/span/span)[2]').click()

        # 证件号码
        self.find_element_by_xpath('(//input[@placeholder="请输入证件号码"])[2]').clear()
        self.find_element_by_xpath('(//input[@placeholder="请输入证件号码"])[2]').send_keys(kwargs['disputer_id'])

        # 居住地址选择
        self.find_element_by_xpath('(//div[contains(text(), "居住地址：")])[2]/../div[2]/div[1]').click()  # 省
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//span[contains(text(),"浙江省")])[16]')))
        sleep(0.2)
        el.click()
        self.find_element_by_xpath('(//div[contains(text(), "居住地址：")])[2]/../div[2]/div[2]').click()  # 市
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//span[contains(text(), "杭州市")])[16]')))
        sleep(0.1)
        el.click()
        self.find_element_by_xpath('(//div[contains(text(), "居住地址：")])[2]/../div[2]/div[3]').click()  # 区
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//span[contains(text(), "上城区")])[3]')))
        sleep(0.1)
        el.click()
        self.find_element_by_xpath('(//div[contains(text(), "居住地址：")])[2]/../div[2]/div[4]').click()  # 街道
        el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '(//span[contains(text(), "清波街道")])[2]')))
        sleep(0.1)
        el.click()
        self.find_element_by_xpath('(//div[contains(text(), "居住地址：")])[2]/../div[2]/div[5]//input[@placeholder="请输入详细地址"]').send_keys(u'13#居住地址')

        # 代理人2
        if kwargs['agent_b_type'] == 'special':
            self.find_element_by_xpath('(//div[text()="委托代理人："])[2]/following-sibling::div/div/div/input').click()
            el = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '(//span[text()="特殊授权代理人"])[2]')))
            el.click()
        elif kwargs['agent_b_type'] == 'common':
            self.find_element_by_xpath('(//div[text()="委托代理人："])[2]/following-sibling::div/div/div/input').click()
            el = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '(//span[text()="一般授权代理人"])[2]')))
            el.click()
        if kwargs['agent_b_type'] != "":
            self.find_element_by_xpath('(//div[text()="委托代理人："])[2]/following-sibling::div/div[2]//input[@placeholder="请输入代理人姓名"]').clear()
            self.find_element_by_xpath('(//div[text()="委托代理人："])[2]/following-sibling::div/div[2]//input[@placeholder="请输入代理人姓名"]').send_keys(kwargs['agent_b_name'])
            self.find_element_by_xpath('(//div[text()="手机号码："]/following-sibling::div/div//input[@placeholder="请输入代理人手机号码"])[2]').send_keys(kwargs['agent_b_tel'])
            self.find_element_by_xpath('(//div[text()="身份证号："]/following-sibling::div/div//input[@placeholder="请输入代理人身份证号码"])[2]').send_keys(kwargs['agent_b_id'])
            # 根据身份证号，判断性别
            if is_male(kwargs['agent_b_id']):
                self.find_element_by_xpath('((//div[text()="性别："])[4]/following-sibling::div/label/span/span)[1]').click()
            else:
                self.find_element_by_xpath('((//div[text()="性别："])[4]/following-sibling::div/label/span/span)[2]').click()
        # 文书地址
        self.find_element_by_xpath('(//div[text()="文书送达地址："]/following-sibling::div/div//input[@placeholder="请输入文书送达地址"])[2]').send_keys(u'4#文书地址')

    def _judicial_tail_input(self, **kwargs):
        # 请求事项
        self.find_element_by_xpath('//textarea[@placeholder="请输入请求内容"]').send_keys(kwargs['jf_desc'])

        # 证据材料
        self.find_element_by_xpath('//div[text()="证据附件："]/following-sibling::div/label/div').click()
        file_upload('D:\\00jt\\1.png')
        sleep(1)
        self.find_element_by_xpath('(//div[text()="证据附件："]/following-sibling::div/label/div)[2]').click()
        file_upload('D:\\00jt\\1.png')
        sleep(1)
        self.find_element_by_xpath('(//div[text()="证据附件："]/following-sibling::div/label/div)[3]').click()
        file_upload('D:\\00jt\\1.png')
        sleep(1)
        self.find_element_by_xpath('(//div[text()="证据附件："]/following-sibling::div/label/div)[4]').click()
        file_upload('D:\\00jt\\1.png')
        sleep(1)
        if kwargs['agent_type'] != "":
            # 代理人身份证明
            self.find_element_by_xpath('//div[contains(text(), " 新增材料")]').click()
            sleep(0.2)
            self.find_element_by_xpath('(//div[text()="证据附件："]/following-sibling::div/label/div)[5]').click()
            file_upload('D:\\00jt\\1.png')
            sleep(1)

        if kwargs['agent_b_type'] != "":
            # 代理人身份证明
            self.find_element_by_xpath('//div[contains(text(), " 新增材料")]').click()
            sleep(0.2)
            if kwargs['agent_type'] != "":
                self.find_element_by_xpath('(//div[text()="证据附件："]/following-sibling::div/label/div)[6]').click()
            else:
                self.find_element_by_xpath('(//div[text()="证据附件："]/following-sibling::div/label/div)[5]').click()
            file_upload('D:\\00jt\\1.png')
            sleep(0.5)

        # 其他事项
        self.find_element_by_xpath('//span[contains(text(), "调解员已核实当事人的真实身份")]/../span/span').click()
        self.find_element_by_xpath('//span[contains(text(), "确认当事人提供的证据材料为原件")]/../span/span').click()

    def _judicial_commit(self, **kwargs):
        # 提交申请
        self.find_element_by_xpath('//button[text()="提交申请"]').click()
        # 确认
        ok_el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="确定"]')))
        ok_el.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.x_apply_judicial_list_li)))

        # 进入申请司法确认列表
        self.find_element_by_xpath(self.x_apply_judicial_list_li).click()
        sleep(0.5)

    def act_judicial_commit(self, **kwargs):
        """司法确认录入
        """

        self._goto_judicial_input_page(**kwargs)
        self._applicant_1_input(**kwargs)
        self._applicant_2_input(**kwargs)
        self._judicial_tail_input(**kwargs)
        self._judicial_commit(**kwargs)

        try:
            # 获取申请司法确认列表，首条案件编号
            text = self.find_element_by_xpath('//div[contains(text(),"案件编号：")]').text
            _, judicial_case_id = text.split(u"：")
        except:
            judicial_case_id = "**None"

        print u"申请司法确认案件编号", judicial_case_id
        return judicial_case_id


    def verification_judicial_commit(self, expect):
        try:
            # 获取申请司法确认列表，首条案件的案由
            result = self.find_element_by_xpath('//div[text()="请求内容"]/following-sibling::div').text
        except:
            result = "**None**"

        print "expect: ", expect
        print "result: ", result
        return expect == result


class DisputePageTjy(Page):
    """调解员纠纷登记
    """
    x_case_input_list_a = '//div[text()="案件登记列表"]'          # 案件登记列表链接
    x_case_list_a = '//li[text()="纠纷调解案件列表"]'             #纠纷调解案件列表

    # 申请人代理人
    x_agent_natural_common      = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[10]/div[2]/div[1]/div/div/label[1]/span[1]/span'
    x_agent_non_natural_common  = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[12]/div[2]/div[1]/div/div/label[1]/span[1]/span'
    x_agent_natural_special     = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[10]/div[2]/div[1]/div/div/label[2]/span[1]/span'
    x_agent_non_natural_special = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[12]/div[2]/div[1]/div/div/label[2]/span[1]/span'
    x_agent_natural_sex         = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[10]/div[2]/div[2]/div/div/label[1]/span[1]/span'
    x_agent_non_natural_sex     = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[12]/div[2]/div[2]/div/div/label[1]/span[1]/span'
    x_agent_natural_name        = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[10]/div[2]/div[3]/div/div/input'
    x_agent_non_natural_name    = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[12]/div[2]/div[3]/div/div/input'
    x_agent_natural_tel         = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[10]/div[2]/div[4]/div/div/input'
    x_agent_non_natural_tel     = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[12]/div[2]/div[4]/div/div/input'
    x_agent_natural_id          = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[10]/div[2]/div[5]/div/div/input'
    x_agent_non_natural_id      = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[12]/div[2]/div[5]/div/div/input'
    x_agent_natural_filename    = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[10]/div[2]/div[6]/div/div/div/div/input'
    x_agent_non_natural_filename= '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[12]/div[2]/div[6]/div/div/div/div/input'
    # 被申请人代理人
    x_b_agent_natural_common      = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[10]/div[2]/div[1]/div/div/label[1]/span[1]/span'
    x_b_agent_non_natural_common  = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[12]/div[2]/div[1]/div/div/label[1]/span[1]/span'
    x_b_agent_natural_special     = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[10]/div[2]/div[1]/div/div/label[2]/span[1]/span'
    x_b_agent_non_natural_special = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[12]/div[2]/div[1]/div/div/label[2]/span[1]/span'
    x_b_agent_natural_sex         = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[10]/div[2]/div[2]/div/div/label[1]/span[1]/span'
    x_b_agent_non_natural_sex     = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[12]/div[2]/div[2]/div/div/label[1]/span[1]/span'
    x_b_agent_natural_name        = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[10]/div[2]/div[3]/div/div/input'
    x_b_agent_non_natural_name    = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[12]/div[2]/div[3]/div/div/input'
    x_b_agent_natural_tel         = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[10]/div[2]/div[4]/div/div/input'
    x_b_agent_non_natural_tel     = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[12]/div[2]/div[4]/div/div/input'
    x_b_agent_natural_id          = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[10]/div[2]/div[5]/div/div/input'
    x_b_agent_non_natural_id      = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[12]/div[2]/div[5]/div/div/input'
    x_b_agent_natural_filename    = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[10]/div[2]/div[6]/div/div/div/div/input'
    x_b_agent_non_natural_filename= '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[12]/div[2]/div[6]/div/div/div/div/input'
    # 被申请人
    x_disputer_natural_disputer         = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[2]/div/div/input'
    x_disputer_natural_tel              = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[4]/div/div/input'
    x_disputer_natural_id               = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[6]/div/div/input'
    x_disputer_natural_addr             = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[8]/div/div/input'
    x_disputer_natural_addr_selector    = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[7]/div/span/span[1]'

    x_disputer_non_natural_legal        = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[1]/div/div/label[2]/span[2]'
    x_disputer_non_natural_organization = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[1]/div/div/label[3]/span[2]'
    x_disputer_non_natural_name         = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[2]/div/div[1]/input'
    x_disputer_non_natural_credit_id    = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[3]/div/div/input'
    x_disputer_non_natural_disputer     = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[4]/div/div/input'
    x_disputer_non_natural_tel          = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[6]/div/div/input'
    x_disputer_non_natural_id           = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[8]/div/div/input'
    x_disputer_non_natural_addr         = '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[10]/div/div/input'
    x_disputer_non_natural_addr_selector= '//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[9]/div/span/span[1]'
    # 被申请人
    x_applicant_natural_applicant        = '//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[2]/div/div[1]/input'
    x_applicant_natural_tel              = '//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[4]/div/div/input'
    x_applicant_natural_addr             = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[8]/div/div/input'
    x_applicant_natural_id               = "(//input[@type='text'])[8]"
    x_applicant_natural_addr_selector    = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[7]/div/span/span[1]'

    x_applicant_non_natural_legal        = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[1]/div/div/label[2]/span[2]'
    x_applicant_non_natural_organization = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[1]/div/div/label[3]/span[2]'
    x_applicant_non_natural_name         = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[2]/div/div[1]/input'
    x_applicant_non_natural_credit_id    = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[3]/div/div/input'
    x_applicant_non_natural_applicant    = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[4]/div/div/input'
    x_applicant_non_natural_tel          = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[6]/div/div/input'
    x_applicant_non_natural_id           = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[8]/div/div/input'
    x_applicant_non_natural_addr         = '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[10]/div/div/input'
    x_applicant_non_natural_addr_selector= '//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[9]/div/span/span[1]'

    x_no_sendmsg = '//span[contains(text(),"不发送")]'
    x_inputlist_1_case_id_div = '//div[contains(text(), "纠纷编号：")]' # 案件登记列表，一个行的案件编号



    def _dispute_info_input(self, **kwargs):
        """纠纷信息录入
        """
        # 调解员登记列表-点击
        self.find_element_by_xpath('//div[contains(text(), "案件登记列表")]').click()
        # 点击案件登记列表
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/a[2]').click()
        # 点击登记纠纷添加
        self.find_element_by_css_selector("textarea.el-textarea__inner").clear()
        self.find_element_by_css_selector("textarea.el-textarea__inner").send_keys(kwargs["jf_desc"])
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div[2]/div[3]/div/div/div/textarea').clear()
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div[2]/div[3]/div/div/div/textarea').send_keys(kwargs["jf_appeal"])
        self.find_element_by_css_selector("span.city-picker-span").click()
        self.find_element_by_link_text(u"浙江省").click()
        self.find_element_by_link_text(u"杭州市").click()
        self.find_element_by_link_text(u"上城区").click()
        self.find_element_by_link_text(u"清波街道").click()
        self.find_element_by_link_text(u"清波门社区").click()
        sleep(1)

    def _applicant_info_input(self, **kwargs):
        """申请人信息录入
        """

        if kwargs['applicant_type'] == u"自然人":
            self.find_element_by_xpath(self.x_applicant_natural_applicant).clear()
            self.find_element_by_xpath(self.x_applicant_natural_applicant).send_keys(kwargs["applicant"])
            self.find_element_by_xpath(self.x_applicant_natural_tel).clear()
            self.find_element_by_xpath(self.x_applicant_natural_tel).send_keys(kwargs["applicant_tel"])
            self.find_element_by_xpath(self.x_applicant_natural_id).clear()
            self.find_element_by_xpath(self.x_applicant_natural_id).send_keys(kwargs["applicant_id"])
            sleep(1)
            self.find_element_by_xpath(self.x_applicant_natural_addr_selector).click()
            sleep(1)
            self.find_element_by_link_text(u"浙江省").click()
            sleep(0.5)
            self.find_element_by_link_text(u"杭州市").click()
            self.find_element_by_link_text(u"上城区").click()
            sleep(0.5)
            self.find_element_by_link_text(u"清波街道").click()
            # 住址
            self.find_element_by_xpath(self.x_applicant_natural_addr).clear()
            self.find_element_by_xpath(self.x_applicant_natural_addr).send_keys(kwargs["applicant_addr"])
            return
        elif kwargs['applicant_type'] == u"法人":
            self.find_element_by_xpath(self.x_applicant_non_natural_legal).click()
        elif kwargs['applicant_type'] == u"非法人组织":
            self.find_element_by_xpath(self.x_applicant_non_natural_organization).click()
        self.find_element_by_xpath(self.x_applicant_non_natural_name).clear()
        self.find_element_by_xpath(self.x_applicant_non_natural_name).send_keys(kwargs["applicant_name"])
        self.find_element_by_xpath(self.x_applicant_non_natural_credit_id).clear()
        self.find_element_by_xpath(self.x_applicant_non_natural_credit_id).send_keys(kwargs["world_credit_id"])
        self.find_element_by_xpath(self.x_applicant_non_natural_applicant).clear()
        self.find_element_by_xpath(self.x_applicant_non_natural_applicant).send_keys(kwargs["applicant"])
        self.find_element_by_xpath(self.x_applicant_non_natural_tel).clear()
        self.find_element_by_xpath(self.x_applicant_non_natural_tel).send_keys(kwargs["applicant_tel"])
        self.find_element_by_xpath(self.x_applicant_non_natural_id).clear()
        self.find_element_by_xpath(self.x_applicant_non_natural_id).send_keys(kwargs["applicant_id"])
        self.find_element_by_xpath(self.x_applicant_non_natural_addr).clear()
        self.find_element_by_xpath(self.x_applicant_non_natural_addr).send_keys(kwargs["applicant_addr"])
        # 输入地址
        self.find_element_by_xpath(self.x_applicant_non_natural_addr_selector).click()
        sleep(0.5)
        try:
            self.find_element_by_link_text(u"浙江省").click()
        except:
            sleep(1)
            self.find_element_by_link_text(u"浙江省").click()
        try:
            self.find_element_by_link_text(u"杭州市").click()
        except:
            sleep(1)
            self.find_element_by_link_text(u"杭州市").click()
        try:
            self.find_element_by_link_text(u"上城区").click()
        except:
            sleep(1)
            self.find_element_by_link_text(u"上城区").click()
        try:
            self.find_element_by_link_text(u"清波街道").click()
        except:
            sleep(1)
            self.find_element_by_link_text(u"清波街道").click()

    def _agent(self, **kwargs):
        if kwargs["applicant_type"] == u"自然人":
            if kwargs['agent_type'] == 'common':
                # 一般授权代理人
                self.find_element_by_xpath(self.x_agent_natural_common).click()
            elif kwargs['agent_type'] == 'special':
                # 特别授权代理人
                self.find_element_by_xpath(self.x_agent_natural_special).click()

            # 性别
            self.find_element_by_xpath(self.x_agent_natural_sex).click()
            # 姓名
            self.find_element_by_xpath(self.x_agent_natural_name).clear()
            self.find_element_by_xpath(self.x_agent_natural_name).send_keys(kwargs['agent_name'])
            # 手机号码
            self.find_element_by_xpath(self.x_agent_natural_name).clear()
            self.find_element_by_xpath(self.x_agent_natural_tel).send_keys(kwargs['agent_tel'])
            # 身份证
            self.find_element_by_xpath(self.x_agent_natural_id).clear()
            self.find_element_by_xpath(self.x_agent_natural_id).send_keys(kwargs['agent_id'])
            # filename
            self.find_element_by_xpath(self.x_agent_natural_filename).send_keys('filename')
        else:
            if kwargs['agent_type'] == 'common':
                # 一般授权代理人
                self.find_element_by_xpath(self.x_agent_non_natural_common).click()
            elif kwargs['agent_type'] == 'special':
                # 特别授权代理人
                self.find_element_by_xpath(self.x_agent_non_natural_special).click()

            # 性别
            self.find_element_by_xpath(self.x_agent_non_natural_sex).click()
            # 姓名
            self.find_element_by_xpath(self.x_agent_non_natural_name).clear()
            self.find_element_by_xpath(self.x_agent_non_natural_name).send_keys(kwargs['agent_name'])
            # 手机号码
            self.find_element_by_xpath(self.x_agent_non_natural_tel).clear()
            self.find_element_by_xpath(self.x_agent_non_natural_tel).send_keys(kwargs['agent_tel'])
            # 身份证
            self.find_element_by_xpath(self.x_agent_non_natural_id).clear()
            self.find_element_by_xpath(self.x_agent_non_natural_id).send_keys(kwargs['agent_id'])
            # filename
            self.find_element_by_xpath(self.x_agent_non_natural_filename).send_keys('filename')
        # 规避上传文件操作
        js ='app.caseData.applicants[0].dyfileName="1.jpg"'
        self.driver.execute_script(js)

    def _applicant_b_input(self, **kwargs):
        """被申请人input
        """
        if kwargs['disputer_type'] == u"自然人":
            self.find_element_by_xpath(self.x_disputer_natural_disputer).clear()
            self.find_element_by_xpath(self.x_disputer_natural_disputer).send_keys(kwargs['disputer'])
            self.find_element_by_xpath(self.x_disputer_natural_tel).clear()
            self.find_element_by_xpath(self.x_disputer_natural_tel).send_keys(kwargs['disputer_tel'])
            self.find_element_by_xpath(self.x_disputer_natural_id).clear()
            self.find_element_by_xpath(self.x_disputer_natural_id).send_keys(kwargs["disputer_id"])
            self.find_element_by_xpath(self.x_disputer_natural_addr).clear()
            self.find_element_by_xpath(self.x_disputer_natural_addr).send_keys(kwargs['disputer_addr'])
            self.find_element_by_xpath(self.x_disputer_natural_addr_selector).click()
            sleep(0.5)
            self.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[7]/div/div[1]/div/div[2]/div[1]/dl[4]/dd/a[5]').click() #浙江
            self.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[7]/div/div[1]/div/div[2]/div[2]/dl/dd/a[1]').click()  #市
            self.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[7]/div/div[1]/div/div[2]/div[3]/dl/dd/a[1]').click()  #区
            self.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/div/div/div[7]/div/div[1]/div/div[2]/div[4]/dl/dd/a[1]').click()  #街道
            return
        elif kwargs['disputer_type'] == u"法人":
            self.find_element_by_xpath(self.x_disputer_non_natural_legal).click()
        elif kwargs['disputer_type'] == u"非法人组织":
            self.find_element_by_xpath(self.x_disputer_non_natural_organization).click()
        self.find_element_by_xpath(self.x_disputer_non_natural_name).clear()
        self.find_element_by_xpath(self.x_disputer_non_natural_name).send_keys(kwargs["disputer_name"])
        self.find_element_by_xpath(self.x_disputer_non_natural_credit_id).clear()
        self.find_element_by_xpath(self.x_disputer_non_natural_credit_id).send_keys(kwargs["disputer_world_credit_id"])
        self.find_element_by_xpath(self.x_disputer_non_natural_disputer).clear()
        self.find_element_by_xpath(self.x_disputer_non_natural_disputer).send_keys(kwargs["disputer"])
        self.find_element_by_xpath(self.x_disputer_non_natural_tel).clear()
        self.find_element_by_xpath(self.x_disputer_non_natural_tel).send_keys(kwargs["disputer_tel"])
        self.find_element_by_xpath(self.x_disputer_non_natural_id).clear()
        self.find_element_by_xpath(self.x_disputer_non_natural_id).send_keys(kwargs["disputer_id"])
        self.find_element_by_xpath(self.x_disputer_non_natural_addr).clear()
        self.find_element_by_xpath(self.x_disputer_non_natural_addr).send_keys(kwargs["disputer_addr"])
        # 输入地址
        self.find_element_by_xpath(self.x_disputer_non_natural_addr_selector).click()
        sleep(0.5)
        self.find_element_by_css_selector('#app > div > div.paalyMains > form > div.beApplyMan > div > div > div.el-form-item.city.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.province > dl:nth-child(4) > dd > a:nth-child(5)').click()
        self.find_element_by_css_selector('#app > div > div.paalyMains > form > div.beApplyMan > div > div > div.el-form-item.city.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.city > dl > dd > a:nth-child(1)').click()
        self.find_element_by_css_selector('#app > div > div.paalyMains > form > div.beApplyMan > div > div > div.el-form-item.city.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.district > dl > dd > a:nth-child(1)').click()
        self.find_element_by_css_selector('#app > div > div.paalyMains > form > div.beApplyMan > div > div > div.el-form-item.city.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.county > dl > dd > a:nth-child(5)').click()

    def _agent_b(self, **kwargs):
        """被申请人代理人输入
        """
        if kwargs['disputer_type'] == u"自然人":
            if kwargs['agent_b_type'] == 'common':
                # 一般授权代理人
                self.find_element_by_xpath(self.x_b_agent_natural_common).click()
            elif kwargs['agent_b_type'] == 'special':
                # 特别授权代理人
                self.find_element_by_xpath(self.x_b_agent_natural_special).click()
            # 性别
            self.find_element_by_xpath(self.x_b_agent_natural_sex).click()
            # 姓名
            self.find_element_by_xpath(self.x_b_agent_natural_name).send_keys(kwargs['agent_b_name'])
            # 手机号码
            self.find_element_by_xpath(self.x_b_agent_natural_tel).send_keys(kwargs['agent_b_tel'])
            # 身份证
            self.find_element_by_xpath(self.x_b_agent_natural_id).send_keys(kwargs['agent_b_id'])
            # filename
            self.find_element_by_xpath(self.x_b_agent_natural_filename).send_keys('filename')
        else:
            if kwargs['agent_b_type'] == 'common':
                # 一般授权代理人
                self.find_element_by_xpath(self.x_b_agent_non_natural_common).click()
            elif kwargs['agent_b_type'] == 'special':
                # 特别授权代理人
                self.find_element_by_xpath(self.x_b_agent_non_natural_special).click()
            # 性别
            self.find_element_by_xpath(self.x_b_agent_non_natural_sex).click()
            # 姓名
            self.find_element_by_xpath(self.x_b_agent_non_natural_name).send_keys(kwargs['agent_b_name'])
            # 手机号码
            self.find_element_by_xpath(self.x_b_agent_non_natural_tel).send_keys(kwargs['agent_b_tel'])
            # 身份证
            self.find_element_by_xpath(self.x_b_agent_non_natural_id).send_keys(kwargs['agent_b_id'])
            # filename
            self.find_element_by_xpath(self.x_b_agent_non_natural_filename).send_keys('filename')

    def _input_all(self, **kwargs):
        """录入纠纷信息
        """
        self._dispute_info_input(**kwargs)

        self._applicant_info_input(**kwargs)
        if kwargs['agent_type']:
            self._agent(**kwargs)
        self._applicant_b_input(**kwargs)
        if kwargs['agent_b_type']:
            self._agent_b(**kwargs)

    def _commit(self):
        """提交
        """
        # self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[2]/p[3]/span[2]').click()
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[1]/p/span[2]').click()
        sleep(1)
        # 不发送短信
        try:
            self.find_element_by_xpath(self.x_no_sendmsg).click()
        except:
            sleep(1)
            self.find_element_by_xpath(self.x_no_sendmsg).click()
        sleep(2)
        # 确定
        ok_btn = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "确定")]')))
        ok_btn.click()

    def verification_commit(self, **kwargs):
        """调解员登记案件验证
        """
        # 用例有执行失败的场景，添加异常处理，提高执行成功率。
        # 进入案件登记列表
        try:
            ok_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.x_case_input_list_a)))
            ok_btn.click()
        except:
            self.driver.refresh()
            ok_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.x_case_input_list_a)))
            ok_btn.click()

        # 打印提交成功的case id
        case_id = self.find_element_by_xpath(self.x_inputlist_1_case_id_div).text
        print "case commit suc {}".format(case_id)

        try:
            # 获取纠纷信息
            jf_desc = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
        except:
            jf_desc = "*None*"

        print "result: ", jf_desc
        print "expect: ", kwargs['jf_desc']

        try:
            # 获取申请人姓名
            applicant = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/p').text
        except:
            applicant = "*None*"



        if kwargs['applicant_type'] == u"自然人":
            print "result: ", applicant
            print "expect: ", kwargs['applicant']
            return jf_desc == kwargs['jf_desc'] and applicant == kwargs['applicant']
        else:
            print "result: ", applicant
            print "expect: ", kwargs['applicant_name']
            return jf_desc == kwargs['jf_desc'] and applicant == kwargs['applicant_name']

    def _save(self):
        """ 调解员登记纠纷-保存
        """
        # 保存
        self.driver.find_element_by_css_selector("span.lastStep").click()

        sleep(1)
        # 查看案件列表
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()

        sleep(1)

    def save(self, **kwargs):
        self._input_all(**kwargs)
        self._save()

    def commit(self, **kwargs):
        self._input_all(**kwargs)
        self._commit()

    def verification_save(self, **kwargs):
        """调解员登记案件验证
        """
        try:
            self.find_element_by_xpath(self.x_case_input_list_a).click()
        except:
            self.find_element_by_xpath(self.x_case_input_list_a).click()

        # 打印 保存成功的case id
        case_id = self.find_element_by_xpath(self.x_inputlist_1_case_id_div).text
        print "case save suc {}".format(case_id)

        try:
            jf_desc = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
        except:
            jf_desc = "*None*"
        print "result: ", jf_desc
        print "expect: ", kwargs['jf_desc']
        try:
            applicant = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/p').text
        except:
            applicant = "*None*"


        if kwargs['applicant_type'] == u"自然人":
            print "result: ", applicant
            print "expect: ", kwargs['applicant']
            return jf_desc == kwargs['jf_desc'] and applicant == kwargs['applicant']
        else:
            print "result: ", applicant
            print "expect: ", kwargs['applicant_name']
            return jf_desc == kwargs['jf_desc'] and applicant == kwargs['applicant_name']

    def dispute_save_commit(self):
        self.driver.find_element_by_link_text(u"纠纷预览").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        sleep(1)
        self.driver.find_element_by_link_text(u"不发送").click()
        sleep(3)
        self.driver.find_element_by_xpath('//div[@id="layui-layer2"]/div[3]/a').click()
        self.driver.find_element_by_css_selector("button[type=\"button\"]").click()


class DisputePageDjy(DisputePageTjy):
    """机构登记员纠纷登记
    """
    x_homepage_a = '//a[text()="首页"]'
    x_dispute_input_btn ='//input[@placeholder="请输入编号/姓名/案号"]/../../../a'  # 机构登记按键
    x_search_input = '//input[@placeholder="请输入编号/姓名/案号"]'
    x_search_btn = '//input[@placeholder="请输入编号/姓名/案号"]/following-sibling::span'
    x_dispute_list_info = '//a[text()="纠纷预览"]' # 纠纷预览
    x_dispute_list_info_back_a = '//button[text()="返回列表"]'  # 返回列表
    x_dispute_list_add = '//a[text()="增加纠纷"]' # 增加纠纷
    x_dispute_list_del = '//a[text()="删除"]'  # 删除

    def _goto_dispute_input(self):
        # 首页
        self.find_element_by_xpath(self.x_homepage_a).click()
        # 机构登记
        input_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.x_dispute_input_btn)))
        input_btn.click()
        # self.find_element_by_xpath(self.x_dispute_input_btn).click()

    def _dispute_info_input(self, **kwargs):
        """纠纷信息录入
        """

        self.find_element_by_css_selector("textarea.el-textarea__inner").clear()
        self.find_element_by_css_selector("textarea.el-textarea__inner").send_keys(kwargs["jf_desc"])
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div[2]/div[3]/div/div/div/textarea').clear()
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div[2]/div[3]/div/div/div/textarea').send_keys(kwargs["jf_appeal"])
        self.find_element_by_css_selector("span.city-picker-span").click()
        self.find_element_by_link_text(u"浙江省").click()
        self.find_element_by_link_text(u"杭州市").click()
        self.find_element_by_link_text(u"上城区").click()
        self.find_element_by_link_text(u"清波街道").click()
        self.find_element_by_link_text(u"清波门社区").click()
        if not kwargs.get("none_mediator"):
            # 选择调解员
            # self.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[7]/div/div/div/input').click()
            self.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[1]/div[2]/div[7]/div/div/div/input').click()
            sleep(1)
            self.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div[3]/ul[1]/li/button').click()
        sleep(1)

    def _input_all(self, **kwargs):
        """录入纠纷信息
        """
        self._dispute_info_input(**kwargs)

        self._applicant_info_input(**kwargs)
        if kwargs['agent_type']:
            self._agent(**kwargs)
        self._applicant_b_input(**kwargs)
        if kwargs['agent_b_type']:
            self._agent_b(**kwargs)

    def save(self, **kwargs):
        self._input_all(**kwargs)
        self._save()

    def commit(self, **kwargs):
        self._input_all(**kwargs)
        self._commit()

    def verification_save(self, **kwargs):
        try:
            jf_desc = self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
        except:
            jf_desc = "*None*"
        print "result: ", jf_desc
        print "expect: ", kwargs['jf_desc']

        try:
            applicant = self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/p').text
        except:
            applicant = "*None*"
        if kwargs['applicant_type'] == u"自然人":
            print "result: ", applicant
            print "expect: ", kwargs['applicant']
            return jf_desc == kwargs['jf_desc'] and applicant == kwargs['applicant']
        else:
            print "result: ", applicant
            print "expect: ", kwargs['applicant_name']
            return jf_desc == kwargs['jf_desc'] and applicant == kwargs['applicant_name']

    def verification_commit(self, **kwargs):
        try:
            jf_desc = self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
        except:
            jf_desc = "*None*"
        print "result: ", jf_desc
        print "expect: ", kwargs['jf_desc']

        try:
            applicant = self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/p').text
        except:
            applicant = "*None*"
        if kwargs['applicant_type'] == u"自然人":
            print "result: ", applicant
            print "expect: ", kwargs['applicant']
            return jf_desc == kwargs['jf_desc'] and applicant == kwargs['applicant']
        else:
            print "result: ", applicant
            print "expect: ", kwargs['applicant_name']
            return jf_desc == kwargs['jf_desc'] and applicant == kwargs['applicant_name']

    def act_search_by_name_or_id(self, search_ctx):
        """登记员案件查询
        """
        self.find_element_by_xpath(self.x_search_input).clear()
        self.find_element_by_xpath(self.x_search_input).send_keys(search_ctx)
        self.find_element_by_xpath(self.x_search_btn).click()
        sleep(1)

    def get_search_No(self):
        """获取第二条案件编号，查询使用
        """
        try:
            res = self.find_element_by_xpath('//div[contains(text(), "纠纷编号：")]').text
            _, no = res.split(u"：")
        except:
            no = "**None**"
        return no

    def act_list_add_dispute(self):
        """机构登记列表-增加纠纷
        """
        self.find_element_by_xpath(self.x_dispute_list_add).click()
        sleep(0.5)

    def act_list_del_dispute(self):
        """机构登记列表-删除
        """
        self.find_element_by_xpath(self.x_dispute_list_del).click()
        # 等待是否删除的确认btn
        ok_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="确定"]')))
        ok_btn.click()
        # 等待删除成功的btn
        ok_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="确定"]')))
        ok_btn.click()

    def act_goto_homepage(self):
        """首页
        """
        self.find_element_by_xpath(self.x_homepage_a).click()

    def act_dispute_list_info_back(self):
        """机构登记列表-纠纷预览-返回列表
        """
        self.act_goto_homepage()
        self.find_element_by_xpath(self.x_dispute_list_info).click()        # 进入纠纷预览
        self.find_element_by_xpath(self.x_dispute_list_info_back_a).click()

    def act_dispute_list_info_save(self):
        """机构登记列表-纠纷预览-保存
        """
        self.act_goto_homepage()
        self.find_element_by_xpath(self.x_dispute_list_info).click()        # 进入纠纷预览
        self.find_element_by_xpath('//h6[text()="纠纷描述"]/../p/textarea').clear()
        self.find_element_by_xpath('//h6[text()="纠纷描述"]/../p/textarea').send_keys(u"进入纠纷预览-保存")
        self.find_element_by_xpath('//button[contains(text(),"保存")]').click()
        # 等待点击保存后的确定btn
        ok_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="确定"]')))
        ok_btn.click()

    def act_dispute_list_info_commit(self):
        """机构登记列表-纠纷预览-提交
        """
        self.act_goto_homepage()
        self.find_element_by_xpath(self.x_dispute_list_info).click()        # 进入纠纷预览
        self.find_element_by_xpath('//h6[text()="纠纷描述"]/../p/textarea').clear()
        self.find_element_by_xpath('//h6[text()="纠纷描述"]/../p/textarea').send_keys(u"进入纠纷预览-保存")
        self.find_element_by_xpath('//button[contains(text(),"提交")]').click()
        # 等待点击提交后是否发送短信btn
        ok_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="不发送"]')))
        ok_btn.click()
        # 等待点击保存后的确定btn
        ok_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="确定"]')))
        ok_btn.click()

    def act_dispute_list_info_schedule(self):
        """机构登记列表-纠纷预览-解纷进度
        """
        self.act_goto_homepage()
        self.find_element_by_xpath(self.x_dispute_list_info).click()        # 进入纠纷预览
        self.find_element_by_xpath('//span[text()="解纷进度"]').click()
        # 等待纠纷进度弹出框的确定btn
        ok_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//h4[text()="纠纷进度"]/../../div[3]/button')))
        ok_btn.click()

def org_process(status, case_id):
    """司法确认接口受理状态
    """
    # status：id=0 不受理；id=1；受理；id=2 退回
    url_pre = 'https://train.odrcloud.cn:8443/lawsuit/confirmStatus?id={}&caseNo='.format(status)

    url = "".join([url_pre,case_id])
    # print url
    try:
        r = requests.get(url)
        res_content = r.text
    except:
        res_content  = r'{"msg": "request failed"}'
    # print r.text
    obj = re.search(r'{"msg":.*}', res_content)     # 匹配内容
    print obj.group()


#     str_= """
#     <!DOCTYPE html>
# <html>
# <head>
# <meta charset="utf-8">
# <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
# <title>首页</title>
# </head>
# <body>
# <script type="text/javascript">
# var jsonObject = {"msg":"状态设置成功","status":true};
# if(jsonObject.status){
# 	alert("设置成功");
# }else {
# 	alert(jsonObject.msg);
# }
# </script>
# </body>
# </html>
#     """

if __name__ == '__main__':
    org_process("1", '166A401D29591')
