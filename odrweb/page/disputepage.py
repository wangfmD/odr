# -*- coding:utf-8 -*-
from time import sleep

from odrweb.page.browser import Page


class DisputePageTjy(Page):
    '''调解员'''
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


    def _dispute_info_input(self, **kwargs):
        '''纠纷信息录入'''

        self.find_element_by_xpath("/html/body/div[4]/div[1]/button[2]").click()
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
        '''申请人信息录入'''

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

        self.find_element_by_xpath(self.x_applicant_non_natural_name).send_keys(kwargs["applicant_name"])
        self.find_element_by_xpath(self.x_applicant_non_natural_credit_id).send_keys(kwargs["world_credit_id"])
        self.find_element_by_xpath(self.x_applicant_non_natural_applicant).send_keys(kwargs["applicant"])
        self.find_element_by_xpath(self.x_applicant_non_natural_tel).send_keys(kwargs["applicant_tel"])
        self.find_element_by_xpath(self.x_applicant_non_natural_id).send_keys(kwargs["applicant_id"])
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
            self.find_element_by_xpath(self.x_agent_natural_name).send_keys(kwargs['agent_name'])
            # 手机号码
            self.find_element_by_xpath(self.x_agent_natural_tel).send_keys(kwargs['agent_tel'])
            # 身份证
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
            self.find_element_by_xpath(self.x_agent_non_natural_name).send_keys(kwargs['agent_name'])
            # 手机号码
            self.find_element_by_xpath(self.x_agent_non_natural_tel).send_keys(kwargs['agent_tel'])
            # 身份证
            self.find_element_by_xpath(self.x_agent_non_natural_id).send_keys(kwargs['agent_id'])
            # filename
            self.find_element_by_xpath(self.x_agent_non_natural_filename).send_keys('filename')
        js ='app.caseData.applicants[0].dyfileName="1.jpg"'
        self.driver.execute_script(js)

    def _applicant_b_input(self, **kwargs):
        '''被申请人input'''
        if kwargs['disputer_type'] == u"自然人":
            self.find_element_by_xpath(self.x_disputer_natural_disputer).clear()
            self.find_element_by_xpath(self.x_disputer_natural_disputer).send_keys(kwargs['disputer'])
            self.find_element_by_xpath(self.x_disputer_natural_tel).clear()
            self.find_element_by_xpath(self.x_disputer_natural_tel).send_keys(kwargs['disputer_tel'])
            self.find_element_by_xpath(self.x_disputer_natural_id).send_keys(kwargs["disputer_id"])
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
        self.find_element_by_xpath(self.x_disputer_non_natural_name).send_keys(kwargs["disputer_name"])
        self.find_element_by_xpath(self.x_disputer_non_natural_credit_id).send_keys(kwargs["disputer_world_credit_id"])
        self.find_element_by_xpath(self.x_disputer_non_natural_disputer).send_keys(kwargs["disputer"])
        self.find_element_by_xpath(self.x_disputer_non_natural_tel).send_keys(kwargs["disputer_tel"])
        self.find_element_by_xpath(self.x_disputer_non_natural_id).send_keys(kwargs["disputer_id"])
        self.find_element_by_xpath(self.x_disputer_non_natural_addr).send_keys(kwargs["disputer_addr"])
        # 输入地址
        self.find_element_by_xpath(self.x_disputer_non_natural_addr_selector).click()
        sleep(0.5)
        self.find_element_by_css_selector('#app > div > div.paalyMains > form > div.beApplyMan > div > div > div.el-form-item.city.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.province > dl:nth-child(4) > dd > a:nth-child(5)').click()
        self.find_element_by_css_selector('#app > div > div.paalyMains > form > div.beApplyMan > div > div > div.el-form-item.city.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.city > dl > dd > a:nth-child(1)').click()
        self.find_element_by_css_selector('#app > div > div.paalyMains > form > div.beApplyMan > div > div > div.el-form-item.city.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.district > dl > dd > a:nth-child(1)').click()
        self.find_element_by_css_selector('#app > div > div.paalyMains > form > div.beApplyMan > div > div > div.el-form-item.city.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.county > dl > dd > a:nth-child(5)').click()

    def _agent_b(self, **kwargs):

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
        '''录入纠纷信息'''
        self._dispute_info_input(**kwargs)

        self._applicant_info_input(**kwargs)
        if kwargs['agent_type']:
            self._agent(**kwargs)
        self._applicant_b_input(**kwargs)
        if kwargs['agent_b_type']:
            self._agent_b(**kwargs)

    def _commit(self):
        # 提交
        # self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[2]/p[3]/span[2]').click()
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[1]/p/span[2]').click()
        sleep(1)
        # 不发送短信
        try:
            self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]').click()
        except:
            sleep(1)
            self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]').click()
        sleep(2)
        # 确定
        try:
            try:
                self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
            except:
                sleep(2)
                self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
        except:
            sleep(3)
            self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()

    def verification_commit(self, **kwargs):
        '''调解员登记案件验证'''
        try:
            self.find_element_by_xpath('/html/body/div[4]/div[1]/button[2]').click()
        except:
            self.find_element_by_xpath('/html/body/div[4]/div[1]/button[2]').click()

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

    def _save(self):
        '''
        调解员登记纠纷-保存

        '''
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
        '''调解员登记案件验证'''
        try:
            self.find_element_by_xpath('/html/body/div[4]/div[1]/button[2]').click()
        except:
            self.find_element_by_xpath('/html/body/div[4]/div[1]/button[2]').click()

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
    '''机构登记员'''

    def _to_dispute_input(self):
        # 首页
        self.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/a[1]').click()
        # 机构登记
        self.find_element_by_xpath('/html/body/div[4]/div[1]/a').click()

    def _dispute_info_input(self, **kwargs):
        '''纠纷信息录入'''

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
        '''录入纠纷信息'''
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




# class DisputePageDjy(Page):
#     '''机构登记员'''
# 
#     def _to_dispute_input(self):
#         # 首页
#         self.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/a[1]').click()
#         # 机构登记
#         self.find_element_by_xpath('/html/body/div[4]/div[1]/a').click()
# 
#     def _dispute_info_input(self, **kwargs):
#         '''纠纷信息录入'''
# 
#         self.find_element_by_css_selector("textarea.el-textarea__inner").clear()
#         self.find_element_by_css_selector("textarea.el-textarea__inner").send_keys(kwargs["jf_desc"])
#         self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div[2]/div[3]/div/div/div/textarea').clear()
#         self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div[2]/div[3]/div/div/div/textarea').send_keys(kwargs["jf_appeal"])
#         self.find_element_by_css_selector("span.city-picker-span").click()
#         self.find_element_by_link_text(u"浙江省").click()
#         self.find_element_by_link_text(u"杭州市").click()
#         self.find_element_by_link_text(u"上城区").click()
#         self.find_element_by_link_text(u"清波街道").click()
#         self.find_element_by_link_text(u"清波门社区").click()
#         if not kwargs.get("none_mediator"):
#             # 选择调解员
#             self.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[7]/div/div/div/input').click()
#             sleep(1)
#             self.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/ul[1]/li/button').click()
#         sleep(1)
# 
#     def _applicant_info_input(self, **kwargs):
#         '''申请人信息录入'''
# 
#         if kwargs['applicant_type'] == u"自然人":
#             self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[2]/div/div[1]/input').clear()
#             self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[2]/div/div[1]/input').send_keys(kwargs["applicant"])
#             self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[4]/div/div/input').clear()
#             self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[4]/div/div/input').send_keys(kwargs["applicant_tel"])
#             self.find_element_by_xpath("(//input[@type='text'])[8]").clear()
#             self.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(kwargs["applicant_id"])
#             sleep(1)
#             self.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[7]/div/span/span[1]').click()
#             sleep(1)
#             self.find_element_by_link_text(u"浙江省").click()
#             sleep(0.5)
#             self.find_element_by_link_text(u"杭州市").click()
#             self.find_element_by_link_text(u"上城区").click()
#             self.find_element_by_link_text(u"清波街道").click()
#             self.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[8]/div/div/input').click()
#             # 住址
#             self.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[8]/div/div/input').clear()
#             self.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[8]/div/div/input').send_keys(kwargs["applicant_addr"])
#             return
#         elif kwargs['applicant_type'] == u"法人":
#             self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[1]/div/div/label[2]/span[2]').click()
#         elif kwargs['applicant_type'] == u"非法人组织":
#             self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[1]/div/div/label[3]/span[2]').click()
#         self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[2]/div/div[1]/input').send_keys(kwargs["applicant_name"])
#         self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[3]/div/div[1]/input').send_keys(kwargs["world_credit_id"])
#         self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[4]/div/div[1]/input').send_keys(kwargs["applicant"])
#         self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[6]/div/div[1]/input').send_keys(kwargs["applicant_tel"])
#         self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[7]/div/div[2]/input').send_keys(kwargs["applicant_id"])
#         self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[9]/div/div[1]/input').send_keys(kwargs["applicant_addr"])
#         # 输入地址
#         self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div/span').click()
#         sleep(0.5)
#         self.find_element_by_link_text(u"浙江省").click()
#         self.find_element_by_link_text(u"杭州市").click()
#         self.find_element_by_css_selector('#app > div > div:nth-child(3) > div > div.main > form > div > div.el-form-item.rrr.slocSet.fl.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.district > dl > dd > a:nth-child(5)').click()
#         self.find_element_by_css_selector('#app > div > div:nth-child(3) > div > div.main > form > div > div.el-form-item.rrr.slocSet.fl.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.street > dl > dd > a:nth-child(1)').click()
# 
#     def _agent(self, **kwargs):
#         if kwargs["applicant_type"] == u"自然人":
#             if kwargs['agent_type'] == 'common':
#                 # 一般授权代理人
#                 self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[1]/div/div/label[1]/span[1]/span').click()
#             elif kwargs['agent_type'] == 'special':
#                 # 特别授权代理人
#                 self.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/div[10]/div[2]/div[1]/div/div/label[2]/span[1]/span').click()
# 
#             # 性别
#             self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[2]/div/div/label[1]/span[1]/span').click()
# 
#             # 姓名
#             self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[3]/div/div/input').send_keys(kwargs['agent_name'])
#             # 手机号码
#             self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[4]/div/div/input').send_keys(kwargs['agent_tel'])
#             # 身份证
#             self.find_element_by_xpath(
#                 '//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[5]/div/div/input').send_keys(kwargs['agent_id'])
#             # filename
#             self.find_element_by_xpath('//*[@id="showFileName0"]').send_keys('filename')
#         else:
#             if kwargs['agent_type'] == 'common':
#                 # 一般授权代理人
#                 self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[1]/div/div/label[1]/span[1]/span').click()
#             elif kwargs['agent_type'] == 'special':
#                 # 特别授权代理人
#                 self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[1]/div/div/label[2]/span[1]/span').click()
# 
#             # 性别
#             self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[2]/div/div/label[1]/span[1]/span').click()
#             # 姓名
#             self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[3]/div/div/input').send_keys(kwargs['agent_name'])
#             # 手机号码
#             self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[4]/div/div/input').send_keys(kwargs['agent_tel'])
#             # 身份证
#             self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[5]/div/div/input').send_keys(kwargs['agent_id'])
#             # filename
#             self.find_element_by_xpath('//*[@id="showFileName0"]').send_keys('filename')
# 
#     def _applicant_b_input(self, **kwargs):
#         '''被申请人input'''
#         if kwargs['disputer_type'] == u"自然人":
#             self.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").clear()
#             self.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").send_keys(kwargs['disputer'])
#             self.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").clear()
#             self.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").send_keys(kwargs['disputer_tel'])
#             return
#         elif kwargs['disputer_type'] == u"法人":
#             pass
#             self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[1]/div/div/label[2]/span[2]').click()
#         elif kwargs['disputer_type'] == u"非法人组织":
#             pass
#             self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[1]/div/div/label[3]/span[2]').click()
#         self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[2]/div/div[1]/input').send_keys(kwargs["disputer_name"])
#         self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[4]/div/div[1]/input').send_keys(kwargs["disputer_world_credit_id"])
#         self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[5]/div/div[1]/input').send_keys(kwargs["disputer"])
#         self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[6]/div/div[1]/input').send_keys(kwargs["disputer_tel"])
#         self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[7]/div/div[2]/input').send_keys(kwargs["disputer_id"])
#         self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[9]/div/div[1]/input').send_keys(kwargs["disputer_addr"])
#         # 输入地址
#         self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div/span').click()
#         sleep(0.5)
#         self.find_element_by_css_selector('#app > div > div:nth-child(4) > div > div.main > form > div > div.el-form-item.BinfoLoc.fl.el-form-item.rrr.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.province > dl:nth-child(4) > dd > a:nth-child(5)').click()
#         self.find_element_by_css_selector('#app > div > div:nth-child(4) > div > div.main > form > div > div.el-form-item.BinfoLoc.fl.el-form-item.rrr.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.city > dl > dd > a:nth-child(1)').click()
#         self.find_element_by_css_selector('#app > div > div:nth-child(4) > div > div.main > form > div > div.el-form-item.BinfoLoc.fl.el-form-item.rrr.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.district > dl > dd > a:nth-child(5)').click()
#         self.find_element_by_css_selector('#app > div > div:nth-child(4) > div > div.main > form > div > div.el-form-item.BinfoLoc.fl.el-form-item.rrr.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.street > dl > dd > a:nth-child(1)').click()
# 
#     def _agent_b(self, **kwargs):
# 
#         if kwargs['disputer_type'] == u"自然人":
#             if kwargs['agent_b_type'] == 'common':
#                 # 一般授权代理人
#                 self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[1]/div/div/label[1]/span[1]/span').click()
#             elif kwargs['agent_b_type'] == 'special':
#                 # 特别授权代理人
#                 self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[1]/div/div/label[2]/span[1]/span').click()
#             # 性别
#             self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[2]/div/div/label[1]/span[1]/span').click()
#             # self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[2]/div/div/label[2]/span[2]/span').click() # female
#             # 姓名
#             self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[3]/div/div/input').send_keys(kwargs['agent_b_name'])
#             # 手机号码
#             self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[4]/div/div/input').send_keys(kwargs['agent_b_tel'])
#             # 身份证
#             self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[5]/div/div/input').send_keys(kwargs['agent_b_id'])
#             # filename
#             self.find_element_by_xpath('//*[@id="BDshowFileName0"]').send_keys('filename')
#         else:
#             if kwargs['agent_b_type'] == 'common':
#                 # 一般授权代理人
#                 self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[1]/div/div/label[1]/span[1]/span').click()
#             elif kwargs['agent_b_type'] == 'special':
#                 # 特别授权代理人
#                 self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[1]/div/div/label[2]/span[1]/span').click()
#             # 性别
#             self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[2]/div/div/label[1]/span[1]/span').click()
#             # self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[2]/div/div/label[2]/span[1]/span').click() # female
#             # 姓名
#             self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[3]/div/div/input').send_keys(kwargs['agent_b_name'])
#             # 手机号码
#             self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[4]/div/div/input').send_keys(kwargs['agent_b_tel'])
#             # 身份证
#             self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[5]/div/div/input').send_keys(kwargs['agent_b_id'])
#             # filename
#             self.find_element_by_xpath('//*[@id="BDshowFileName0"]').send_keys('filename')
# 
#     def _input_all(self, **kwargs):
#         '''录入纠纷信息'''
#         self._dispute_info_input(**kwargs)
# 
#         self._applicant_info_input(**kwargs)
#         if kwargs['agent_type']:
#             self._agent(**kwargs)
#         self._applicant_b_input(**kwargs)
#         if kwargs['agent_b_type']:
#             self._agent_b(**kwargs)
# 
#     def _commit(self):
#         # 提交
#         self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[2]/p[3]/span[2]').click()
#         sleep(1)
#         # 不发送短信
#         self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]').click()
#         self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]')
#         sleep(1)
#         # 确定
#         try:
#             self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
#         except:
#             sleep(1.5)
#             print u"提交后确定获取失败一次..."
#             self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
# 
#     def verification_commit(self, **kwargs):
#         try:
#             jf_desc = self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
#         except:
#             jf_desc = "*None*"
#         print "result: ", jf_desc
#         print "expect: ", kwargs['jf_desc']
# 
#         try:
#             applicant = self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/p').text
#         except:
#             applicant = "*None*"
#         if kwargs['applicant_type'] == u"自然人":
#             print "result: ", applicant
#             print "expect: ", kwargs['applicant']
#             return jf_desc == kwargs['jf_desc'] and applicant == kwargs['applicant']
#         else:
#             print "result: ", applicant
#             print "expect: ", kwargs['applicant_name']
#             return jf_desc == kwargs['jf_desc'] and applicant == kwargs['applicant_name']
# 
#     def _save(self):
#         '''
#         调解员登记纠纷-保存
# 
#         '''
#         # 保存
#         self.driver.find_element_by_css_selector("span.lastStep").click()
#         sleep(1)
#         # 查看案件列表
#         self.driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
#         sleep(1)
# 
#     def save(self, **kwargs):
#         self._input_all(**kwargs)
#         self._save()
# 
#     def commit(self, **kwargs):
#         self._input_all(**kwargs)
#         self._commit()
# 
#     def verification_save(self, **kwargs):
#         try:
#             jf_desc = self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
#         except:
#             jf_desc = "*None*"
#         print "result: ", jf_desc
#         print "expect: ", kwargs['jf_desc']
# 
#         try:
#             applicant = self.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/p').text
#         except:
#             applicant = "*None*"
#         if kwargs['applicant_type'] == u"自然人":
#             print "result: ", applicant
#             print "expect: ", kwargs['applicant']
#             return jf_desc == kwargs['jf_desc'] and applicant == kwargs['applicant']
#         else:
#             print "result: ", applicant
#             print "expect: ", kwargs['applicant_name']
#             return jf_desc == kwargs['jf_desc'] and applicant == kwargs['applicant_name']
# 
#     def dispute_save_commit(self):
#         self.driver.find_element_by_link_text(u"纠纷预览").click()
#         self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
#         sleep(1)
#         self.driver.find_element_by_link_text(u"不发送").click()
#         sleep(3)
#         self.driver.find_element_by_xpath('//div[@id="layui-layer2"]/div[3]/a').click()
#         self.driver.find_element_by_css_selector("button[type=\"button\"]").click()


if __name__ == '__main__':
    pass
