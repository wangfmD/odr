# -*- coding:utf-8 -*-
from time import sleep

from odrweb.page.browser import Page

jf_info = {"jf_desc": u"假冒商品",
           "jf_appeal": u"假一赔十",

           "applicant_type": u"自然人",  # 法人 非法人组织
           "applicant_name": u"企业或机构名称",  #
           "world_credit_id": "abcde1234567890",
           "applicant": u"徐传珠",
           "applicant_tel": "15295745648",
           "applicant_id": "321281199507077775",
           "applicant_addr": u"addr",

           "disputer": u"",
           "disputer_tel": "",

           "agent_type": None,  # common special,
           "agent_name": u"钱桂林",
           "agent_tel": "13160077223",
           "agent_id": "321023199508166636",

           "agent_b_type": None,  # common special,
           "agent_b_name": u"段志勇",
           "agent_b_tel": "15895996954",
           "agent_b_id": ""
           }

jf_info_all = {"jf_desc": u"假冒商品",
               "jf_appeal": u"假一赔十",

               "applicant_type": u"法人",  # 法人 非法人组织
               "applicant_name": u"企业或机构名称",  #
               "world_credit_id": "abcde1234567890",
               "applicant": u"王发明",
               "applicant_tel": "13013031374",
               "applicant_id": "320830198309064815",
               "applicant_addr": u"addr",

               "disputer_type": u"法人",  # 法人 非法人组织
               "disputer": u"徐传珠",
               "disputer_tel": "13800010001",

               "agent_type": 'special',  # common special,
               "agent_name": u"钱桂林",
               "agent_tel": "13160077111",
               "agent_id": "321023199508166636",

               "agent_b_type": "special",  # common special,
               "agent_b_name": u"段志勇",
               "agent_b_tel": "15895996111",
               "agent_b_id": ""
               }


class DisputePageTjy(Page):
    '''调解员'''

    def _dispute_applicant_input(self, **kwargs):
        '''纠纷信息录入'''

        self.find_element_by_xpath("/html/body/div[4]/div[1]/button[2]").click()
        # 点击案件登记列表
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/a[2]').click()
        # 点击登记纠纷添加
        self.find_element_by_css_selector("textarea.el-textarea__inner").clear()
        self.find_element_by_css_selector("textarea.el-textarea__inner").send_keys(kwargs["jf_desc"])
        self.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").clear()
        self.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").send_keys(kwargs["jf_appeal"])
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
            self.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").clear()
            self.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").send_keys(kwargs["applicant"])
            self.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").clear()
            self.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").send_keys(kwargs["applicant_tel"])
            self.find_element_by_xpath("(//input[@type='text'])[8]").clear()
            self.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(kwargs["applicant_id"])
            sleep(1)
            self.find_element_by_xpath('//div[@id="app"]/div/div[3]/div/div[1]/form/div/div[6]/div/span').click()
            sleep(1)
            self.find_element_by_link_text(u"浙江省").click()
            sleep(0.5)
            self.find_element_by_link_text(u"杭州市").click()
            self.find_element_by_link_text(u"上城区").click()
            self.find_element_by_link_text(u"清波街道").click()
            self.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").click()
            # 住址
            self.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").clear()
            self.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").send_keys(kwargs["applicant_addr"])
            return
        elif kwargs['applicant_type'] == u"法人":
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[1]/div/div/label[2]/span[2]').click()
        elif kwargs['applicant_type'] == u"非法人组织":
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[1]/div/div/label[3]/span[2]').click()
        self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[2]/div/div[1]/input').send_keys(kwargs["applicant_name"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[3]/div/div[1]/input').send_keys(kwargs["world_credit_id"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[4]/div/div[1]/input').send_keys(kwargs["applicant"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[6]/div/div[1]/input').send_keys(kwargs["applicant_tel"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[7]/div/div[2]/input').send_keys(kwargs["applicant_id"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[9]/div/div[1]/input').send_keys(kwargs["applicant_addr"])
        # 输入地址
        self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div/span').click()
        sleep(0.5)
        self.find_element_by_link_text(u"浙江省").click()
        self.find_element_by_link_text(u"杭州市").click()
        self.find_element_by_css_selector('#app > div > div:nth-child(3) > div > div.main > form > div > div.el-form-item.rrr.slocSet.fl.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.district > dl > dd > a:nth-child(5)').click()
        self.find_element_by_css_selector('#app > div > div:nth-child(3) > div > div.main > form > div > div.el-form-item.rrr.slocSet.fl.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.street > dl > dd > a:nth-child(1)').click()

    def _agent(self, **kwargs):
        if kwargs["applicant_type"] == u"自然人":
            if kwargs['agent_type'] == 'common':
                # 一般授权代理人
                self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[1]/div/div/label[1]/span[1]/span').click()
            elif kwargs['agent_type'] == 'special':
                # 特别授权代理人
                self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[1]/div/div/label[2]/span[1]/span').click()

            # 性别
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[2]/div/div/label[1]/span[1]/span').click()

            # 姓名
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[3]/div/div/input').send_keys(kwargs['agent_name'])
            # 手机号码
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[4]/div/div/input').send_keys(kwargs['agent_tel'])
            # 身份证
            self.find_element_by_xpath(
                '//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[5]/div/div/input').send_keys(kwargs['agent_id'])
            # filename
            self.find_element_by_xpath('//*[@id="showFileName0"]').send_keys('filename')
        else:
            if kwargs['agent_type'] == 'common':
                # 一般授权代理人
                self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[1]/div/div/label[1]/span[1]/span').click()
            elif kwargs['agent_type'] == 'special':
                # 特别授权代理人
                self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[1]/div/div/label[2]/span[1]/span').click()

            # 性别
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[2]/div/div/label[1]/span[1]/span').click()
            # 姓名
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[3]/div/div/input').send_keys(kwargs['agent_name'])
            # 手机号码
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[4]/div/div/input').send_keys(kwargs['agent_tel'])
            # 身份证
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[5]/div/div/input').send_keys(kwargs['agent_id'])
            # filename
            self.find_element_by_xpath('//*[@id="showFileName0"]').send_keys('filename')

    def _dispute_applicant_b_input(self, **kwargs):
        '''被申请人input'''
        if kwargs['disputer_type'] == u"自然人":
            self.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").clear()
            self.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").send_keys(kwargs['disputer'])
            self.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").clear()
            self.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").send_keys(kwargs['disputer_tel'])
            return
        elif kwargs['disputer_type'] == u"法人":
            pass
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[1]/div/div/label[2]/span[2]').click()
        elif kwargs['disputer_type'] == u"非法人组织":
            pass
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[1]/div/div/label[3]/span[2]').click()
        self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[2]/div/div[1]/input').send_keys(kwargs["disputer_name"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[4]/div/div[1]/input').send_keys(kwargs["disputer_world_credit_id"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[5]/div/div[1]/input').send_keys(kwargs["disputer"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[6]/div/div[1]/input').send_keys(kwargs["disputer_tel"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[7]/div/div[2]/input').send_keys(kwargs["disputer_id"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[9]/div/div[1]/input').send_keys(kwargs["disputer_addr"])
        # 输入地址
        self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div/span').click()
        sleep(0.5)
        self.find_element_by_css_selector('#app > div > div:nth-child(4) > div > div.main > form > div > div.el-form-item.BinfoLoc.fl.el-form-item.rrr.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.province > dl:nth-child(4) > dd > a:nth-child(5)').click()
        self.find_element_by_css_selector('#app > div > div:nth-child(4) > div > div.main > form > div > div.el-form-item.BinfoLoc.fl.el-form-item.rrr.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.city > dl > dd > a:nth-child(1)').click()
        self.find_element_by_css_selector('#app > div > div:nth-child(4) > div > div.main > form > div > div.el-form-item.BinfoLoc.fl.el-form-item.rrr.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.district > dl > dd > a:nth-child(5)').click()
        self.find_element_by_css_selector('#app > div > div:nth-child(4) > div > div.main > form > div > div.el-form-item.BinfoLoc.fl.el-form-item.rrr.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.street > dl > dd > a:nth-child(1)').click()

    def _agent_b(self, **kwargs):

        if kwargs['disputer_type'] == u"自然人":
            if kwargs['agent_b_type'] == 'common':
                # 一般授权代理人
                self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[1]/div/div/label[1]/span[1]/span').click()
            elif kwargs['agent_b_type'] == 'special':
                # 特别授权代理人
                self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[1]/div/div/label[2]/span[1]/span').click()
            # 性别
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[2]/div/div/label[1]/span[1]/span').click()
            # self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[2]/div/div/label[2]/span[2]/span').click() # female
            # 姓名
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[3]/div/div/input').send_keys(kwargs['agent_b_name'])
            # 手机号码
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[4]/div/div/input').send_keys(kwargs['agent_b_tel'])
            # 身份证
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[5]/div/div/input').send_keys(kwargs['agent_b_id'])
            # filename
            self.find_element_by_xpath('//*[@id="BDshowFileName0"]').send_keys('filename')
        else:
            if kwargs['agent_b_type'] == 'common':
                # 一般授权代理人
                self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[1]/div/div/label[1]/span[1]/span').click()
            elif kwargs['agent_b_type'] == 'special':
                # 特别授权代理人
                self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[1]/div/div/label[2]/span[1]/span').click()
            # 性别
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[2]/div/div/label[1]/span[1]/span').click()
            # self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[2]/div/div/label[2]/span[1]/span').click() # female
            # 姓名
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[3]/div/div/input').send_keys(kwargs['agent_b_name'])
            # 手机号码
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[4]/div/div/input').send_keys(kwargs['agent_b_tel'])
            # 身份证
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[5]/div/div/input').send_keys(kwargs['agent_b_id'])
            # filename
            self.find_element_by_xpath('//*[@id="BDshowFileName0"]').send_keys('filename')

    def _input_all(self, **kwargs):
        '''录入纠纷信息'''
        self._dispute_applicant_input(**kwargs)

        self._applicant_info_input(**kwargs)
        if kwargs['agent_type']:
            self._agent(**kwargs)
        self._dispute_applicant_b_input(**kwargs)
        if kwargs['agent_b_type']:
            self._agent_b(**kwargs)

    def _commit(self):
        # 提交
        self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[2]/p[3]/span[2]').click()
        sleep(1)
        # 不发送短信
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]').click()
        sleep(2)
        # 确定
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
        self.driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
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


class DisputePageDjy(Page):
    '''机构登记员'''

    def _to_dispute_input(self):
        # 首页
        self.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/a[1]').click()
        # 机构登记
        self.find_element_by_xpath('/html/body/div[4]/div[1]/a').click()

    def _dispute_applicant_input(self, **kwargs):
        '''纠纷信息录入'''

        self.find_element_by_css_selector("textarea.el-textarea__inner").clear()
        self.find_element_by_css_selector("textarea.el-textarea__inner").send_keys(kwargs["jf_desc"])
        self.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").clear()
        self.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").send_keys(kwargs["jf_appeal"])
        self.find_element_by_css_selector("span.city-picker-span").click()
        self.find_element_by_link_text(u"浙江省").click()
        self.find_element_by_link_text(u"杭州市").click()
        self.find_element_by_link_text(u"上城区").click()
        self.find_element_by_link_text(u"清波街道").click()
        self.find_element_by_link_text(u"清波门社区").click()
        if not kwargs.get("none_mediator"):
            # 选择调解员
            self.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[7]/div/div/div/input').click()
            sleep(1)
            self.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div[3]/ul[1]/li/button').click()
        sleep(1)

    def _applicant_info_input(self, **kwargs):
        '''申请人信息录入'''

        if kwargs['applicant_type'] == u"自然人":
            self.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").clear()
            self.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").send_keys(kwargs["applicant"])
            self.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").clear()
            self.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").send_keys(kwargs["applicant_tel"])
            self.find_element_by_xpath("(//input[@type='text'])[8]").clear()
            self.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(kwargs["applicant_id"])
            sleep(1)
            self.find_element_by_xpath('//div[@id="app"]/div/div[3]/div/div[1]/form/div/div[6]/div/span').click()
            sleep(1)
            self.find_element_by_link_text(u"浙江省").click()
            sleep(0.5)
            self.find_element_by_link_text(u"杭州市").click()
            self.find_element_by_link_text(u"上城区").click()
            self.find_element_by_link_text(u"清波街道").click()
            self.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").click()
            # 住址
            self.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").clear()
            self.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").send_keys(kwargs["applicant_addr"])
            return
        elif kwargs['applicant_type'] == u"法人":
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[1]/div/div/label[2]/span[2]').click()
        elif kwargs['applicant_type'] == u"非法人组织":
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[1]/div/div/label[3]/span[2]').click()
        self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[2]/div/div[1]/input').send_keys(kwargs["applicant_name"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[3]/div/div[1]/input').send_keys(kwargs["world_credit_id"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[4]/div/div[1]/input').send_keys(kwargs["applicant"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[6]/div/div[1]/input').send_keys(kwargs["applicant_tel"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[7]/div/div[2]/input').send_keys(kwargs["applicant_id"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[9]/div/div[1]/input').send_keys(kwargs["applicant_addr"])
        # 输入地址
        self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div/span').click()
        sleep(0.5)
        self.find_element_by_link_text(u"浙江省").click()
        self.find_element_by_link_text(u"杭州市").click()
        self.find_element_by_css_selector('#app > div > div:nth-child(3) > div > div.main > form > div > div.el-form-item.rrr.slocSet.fl.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.district > dl > dd > a:nth-child(5)').click()
        self.find_element_by_css_selector('#app > div > div:nth-child(3) > div > div.main > form > div > div.el-form-item.rrr.slocSet.fl.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.street > dl > dd > a:nth-child(1)').click()

    def _agent(self, **kwargs):
        if kwargs["applicant_type"] == u"自然人":
            if kwargs['agent_type'] == 'common':
                # 一般授权代理人
                self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[1]/div/div/label[1]/span[1]/span').click()
            elif kwargs['agent_type'] == 'special':
                # 特别授权代理人
                self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[1]/div/div/label[2]/span[1]/span').click()

            # 性别
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[2]/div/div/label[1]/span[1]/span').click()

            # 姓名
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[3]/div/div/input').send_keys(kwargs['agent_name'])
            # 手机号码
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[4]/div/div/input').send_keys(kwargs['agent_tel'])
            # 身份证
            self.find_element_by_xpath(
                '//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[8]/div[2]/div[5]/div/div/input').send_keys(kwargs['agent_id'])
            # filename
            self.find_element_by_xpath('//*[@id="showFileName0"]').send_keys('filename')
        else:
            if kwargs['agent_type'] == 'common':
                # 一般授权代理人
                self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[1]/div/div/label[1]/span[1]/span').click()
            elif kwargs['agent_type'] == 'special':
                # 特别授权代理人
                self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[1]/div/div/label[2]/span[1]/span').click()

            # 性别
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[2]/div/div/label[1]/span[1]/span').click()
            # 姓名
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[3]/div/div/input').send_keys(kwargs['agent_name'])
            # 手机号码
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[4]/div/div/input').send_keys(kwargs['agent_tel'])
            # 身份证
            self.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[1]/form/div/div[10]/div[2]/div[5]/div/div/input').send_keys(kwargs['agent_id'])
            # filename
            self.find_element_by_xpath('//*[@id="showFileName0"]').send_keys('filename')

    def _dispute_applicant_b_input(self, **kwargs):
        '''被申请人input'''
        if kwargs['disputer_type'] == u"自然人":
            self.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").clear()
            self.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").send_keys(kwargs['disputer'])
            self.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").clear()
            self.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").send_keys(kwargs['disputer_tel'])
            return
        elif kwargs['disputer_type'] == u"法人":
            pass
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[1]/div/div/label[2]/span[2]').click()
        elif kwargs['disputer_type'] == u"非法人组织":
            pass
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[1]/div/div/label[3]/span[2]').click()
        self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[2]/div/div[1]/input').send_keys(kwargs["disputer_name"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[4]/div/div[1]/input').send_keys(kwargs["disputer_world_credit_id"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[5]/div/div[1]/input').send_keys(kwargs["disputer"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[6]/div/div[1]/input').send_keys(kwargs["disputer_tel"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[7]/div/div[2]/input').send_keys(kwargs["disputer_id"])
        self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[9]/div/div[1]/input').send_keys(kwargs["disputer_addr"])
        # 输入地址
        self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div/span').click()
        sleep(0.5)
        self.find_element_by_css_selector('#app > div > div:nth-child(4) > div > div.main > form > div > div.el-form-item.BinfoLoc.fl.el-form-item.rrr.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.province > dl:nth-child(4) > dd > a:nth-child(5)').click()
        self.find_element_by_css_selector('#app > div > div:nth-child(4) > div > div.main > form > div > div.el-form-item.BinfoLoc.fl.el-form-item.rrr.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.city > dl > dd > a:nth-child(1)').click()
        self.find_element_by_css_selector('#app > div > div:nth-child(4) > div > div.main > form > div > div.el-form-item.BinfoLoc.fl.el-form-item.rrr.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.district > dl > dd > a:nth-child(5)').click()
        self.find_element_by_css_selector('#app > div > div:nth-child(4) > div > div.main > form > div > div.el-form-item.BinfoLoc.fl.el-form-item.rrr.is-required > div > div.city-picker-dropdown > div > div.city-select-content > div.city-select.street > dl > dd > a:nth-child(1)').click()

    def _agent_b(self, **kwargs):

        if kwargs['disputer_type'] == u"自然人":
            if kwargs['agent_b_type'] == 'common':
                # 一般授权代理人
                self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[1]/div/div/label[1]/span[1]/span').click()
            elif kwargs['agent_b_type'] == 'special':
                # 特别授权代理人
                self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[1]/div/div/label[2]/span[1]/span').click()
            # 性别
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[2]/div/div/label[1]/span[1]/span').click()
            # self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[2]/div/div/label[2]/span[2]/span').click() # female
            # 姓名
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[3]/div/div/input').send_keys(kwargs['agent_b_name'])
            # 手机号码
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[4]/div/div/input').send_keys(kwargs['agent_b_tel'])
            # 身份证
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[8]/div[2]/div[5]/div/div/input').send_keys(kwargs['agent_b_id'])
            # filename
            self.find_element_by_xpath('//*[@id="BDshowFileName0"]').send_keys('filename')
        else:
            if kwargs['agent_b_type'] == 'common':
                # 一般授权代理人
                self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[1]/div/div/label[1]/span[1]/span').click()
            elif kwargs['agent_b_type'] == 'special':
                # 特别授权代理人
                self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[1]/div/div/label[2]/span[1]/span').click()
            # 性别
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[2]/div/div/label[1]/span[1]/span').click()
            # self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[2]/div/div/label[2]/span[1]/span').click() # female
            # 姓名
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[3]/div/div/input').send_keys(kwargs['agent_b_name'])
            # 手机号码
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[4]/div/div/input').send_keys(kwargs['agent_b_tel'])
            # 身份证
            self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div[1]/form/div/div[10]/div[2]/div[5]/div/div/input').send_keys(kwargs['agent_b_id'])
            # filename
            self.find_element_by_xpath('//*[@id="BDshowFileName0"]').send_keys('filename')

    def _input_all(self, **kwargs):
        '''录入纠纷信息'''
        self._dispute_applicant_input(**kwargs)

        self._applicant_info_input(**kwargs)
        if kwargs['agent_type']:
            self._agent(**kwargs)
        self._dispute_applicant_b_input(**kwargs)
        if kwargs['agent_b_type']:
            self._agent_b(**kwargs)

    def _commit(self):
        # 提交
        self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[2]/p[3]/span[2]').click()
        sleep(1)
        # 不发送短信
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]').click()
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]')
        sleep(1)
        # 确定
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()

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

    def _save(self):
        '''
        调解员登记纠纷-保存

        '''
        # 保存
        self.driver.find_element_by_css_selector("span.lastStep").click()
        sleep(1)
        # 查看案件列表
        self.driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
        sleep(1)

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

    def dispute_save_commit(self):
        self.driver.find_element_by_link_text(u"纠纷预览").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        sleep(1)
        self.driver.find_element_by_link_text(u"不发送").click()
        sleep(3)
        self.driver.find_element_by_xpath('//div[@id="layui-layer2"]/div[3]/a').click()
        self.driver.find_element_by_css_selector("button[type=\"button\"]").click()


# class DisputePage(Page):
#     # def __init__(self, page=None):
#     #     self.driver = page.driver
#
#     def _dispute_djy_input(self, **kwargs):
#         '''
#         机构登记员登记纠纷
#         保存提交
#
#         '''
#         # 点击消费维权
#         self.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/form/div/div/div/label[2]/span[2]").click()
#         # 输入纠纷描述
#         self.driver.find_element_by_css_selector("textarea.el-textarea__inner").clear()
#         self.driver.find_element_by_css_selector("textarea.el-textarea__inner").send_keys(kwargs["jf_desc"])
#         # 输入我的诉求
#         self.driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").clear()
#         self.driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").send_keys(
#             kwargs["jf_appeal"])
#         #  点击纠纷发生地
#         self.driver.find_element_by_css_selector("span.city-picker-span").click()
#         self.driver.find_element_by_link_text(u"浙江省").click()
#         self.driver.find_element_by_link_text(u"杭州市").click()
#         self.driver.find_element_by_link_text(u"上城区").click()
#         self.driver.find_element_by_link_text(u"清波街道").click()
#         self.driver.find_element_by_link_text(u"清波门社区").click()
#         # click选择调解员
#         self.driver.find_element_by_css_selector(
#             "div.el-form-item__content > div > div.el-input > input.el-input__inner").click()
#         sleep(1)
#         # 确定调解员
#         self.driver.find_element_by_css_selector("button.choice").click()
#         # 申请人
#         self.driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").clear()
#         self.driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").send_keys(
#             kwargs["applicant"])
#         # 电话
#         self.driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").clear()
#         self.driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").send_keys(
#             kwargs["applicant_tel"]
#         )
#         # 身份证
#         self.driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
#         self.driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(kwargs["applicant_id"])
#         sleep(1)
#         # 选择常驻地址
#         self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/div/div[1]/form/div/div[6]/div/span').click()
#         sleep(1)
#         self.driver.find_element_by_link_text(u"浙江省").click()
#         self.driver.find_element_by_link_text(u"杭州市").click()
#         self.driver.find_element_by_link_text(u"上城区").click()
#         self.driver.find_element_by_link_text(u"清波街道").click()
#         #
#         self.driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").click()
#         # 详细地址
#         self.driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").clear()
#         self.driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").send_keys(
#             kwargs['applicant_addr'])
#
#         # 被申请人姓名
#         self.driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").clear()
#         self.driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").send_keys(
#             kwargs['disputer'])
#         # 电话
#         self.driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").clear()
#         self.driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").send_keys(
#             kwargs['disputer_tel'])
#
#     def dispute_djy_save(self, **kwargs):
#         '''
#         机构登记员登记纠纷
#         保存提交
#         '''
#
#         self._dispute_djy_input(**kwargs)
#
#         # 保存
#         self.driver.find_element_by_css_selector("span.lastStep").click()
#         sleep(1)
#         # 查看案件列表
#         self.driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
#         sleep(1)
#         # 纠纷预览
#         self.driver.find_element_by_link_text(u"纠纷预览").click()
#         # 提交
#         self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
#         sleep(1.5)
#         # 不发送
#         self.driver.find_element_by_link_text(u"不发送").click()
#         sleep(2)
#         # 确定
#         self.driver.find_element_by_xpath('//div[@id="layui-layer2"]/div[3]/a').click()
#         # 返回列表
#         self.driver.find_element_by_css_selector("button[type=\"button\"]").click()
#         #
#         # self.driver.find_element_by_link_text(u"机构登记").click()
#         # self.driver.find_element_by_xpath(u"(//a[contains(text(),'返回>')])[2]").click()
#         # 保存提交方式
#
#     def dispute_djy_commit(self, **kwargs):
#         '''
#         机构登记员
#         提交
#         :param driver:
#         :return:
#         '''
#         self._dispute_djy_input(**kwargs)
#         # 提交
#         self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[2]/p[3]/span[2]').click()
#         sleep(1)
#         # 短信提醒
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]/span').click()
#         sleep(2)
#         # 确认
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
#         # 直接点击保存方式
#
#     def dispute_djy_commit_verification(self, jf_desc):
#         try:
#             jf_desc = self.driver.find_element_by_xpath(
#                 '/html/body/div[4]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
#         except:
#             jf_desc = "*None*"
#         print "expect: ", jf_desc
#         print "result: ", jf_info["jf_desc"]
#         return jf_desc == jf_info["jf_desc"]
#
#     def _dispute_tjy_input(self, **kwargs):
#         '''
#         调解员登记纠纷
#         提交
#         :param self.driver:
#         :return:
#         '''
#
#         self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/button[2]").click()
#         # 点击案件登记列表
#         self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/a[2]').click()
#         # 点击登记纠纷添加
#         self.driver.find_element_by_css_selector("textarea.el-textarea__inner").clear()
#         self.driver.find_element_by_css_selector("textarea.el-textarea__inner").send_keys(kwargs["jf_desc"])
#         self.driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").clear()
#         self.driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").send_keys(
#             kwargs["jf_appeal"])
#         self.driver.find_element_by_css_selector("span.city-picker-span").click()
#         self.driver.find_element_by_link_text(u"浙江省").click()
#         self.driver.find_element_by_link_text(u"杭州市").click()
#         self.driver.find_element_by_link_text(u"上城区").click()
#         self.driver.find_element_by_link_text(u"清波街道").click()
#         self.driver.find_element_by_link_text(u"清波门社区").click()
#         sleep(1)
#         self.driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").clear()
#         self.driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").send_keys(
#             kwargs["applicant"])
#         self.driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").clear()
#         self.driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").send_keys(
#             kwargs["applicant_tel"])
#         self.driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
#         self.driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(kwargs["applicant_id"])
#         sleep(1)
#         self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/div/div[1]/form/div/div[6]/div/span').click()
#         sleep(1)
#         self.driver.find_element_by_link_text(u"浙江省").click()
#         self.driver.find_element_by_link_text(u"杭州市").click()
#         self.driver.find_element_by_link_text(u"上城区").click()
#         self.driver.find_element_by_link_text(u"清波街道").click()
#         self.driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").click()
#         # 住址
#         self.driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").clear()
#         self.driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").send_keys(kwargs[
#                                                                                                                   "applicant_addr"])
#         self.driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").clear()
#         self.driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").send_keys(
#             kwargs['disputer'])
#         self.driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").clear()
#         self.driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").send_keys(
#             kwargs['disputer_tel'])
#
#     def dispute_tjy_commit(self, **kwargs):
#         '''
#         调解员登记纠纷
#         提交
#         :param self.driver:
#         :return:
#         '''
#         self._dispute_tjy_input(**kwargs)
#
#         # 提交
#         self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[2]/p[3]/span[2]').click()
#         sleep(1)
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]/span').click()
#         sleep(2)
#         self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
#
#     def verification_dispute_tjy_commit(self, jf_info):
#         try:
#             # jf_desc = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
#             jf_desc = self.driver.find_element_by_xpath(
#                 '/html/body/div[4]/div[2]/div[2]/div/div/div/div[4]/div[1]/div[9]/p').text
#         except:
#             jf_desc = "*None*"
#         print "result: ", jf_desc
#         print "expect: ", jf_info
#         return jf_desc == jf_info
#
#     def dispute_tjy_save(self, **kwargs):
#         '''
#         调解员登记纠纷
#         保存提交
#         :param self.driver:
#         :return:
#         '''
#         self._dispute_tjy_input(**kwargs)
#
#         # 保存
#         self.driver.find_element_by_css_selector("span.lastStep").click()
#         sleep(1)
#         # 查看案件列表
#         self.driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
#         sleep(1)
#
#     def verification_dispute_tjy_save(self, jf_info):
#         try:
#             jf_desc = self.driver.find_element_by_xpath(
#                 '/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
#         except:
#             jf_desc = "*None*"
#         print "result: ", jf_desc
#         print "expect: ", jf_info
#         return jf_desc == jf_info
#
#     def dispute_tjy_save_commit(self):
#         self.driver.find_element_by_link_text(u"纠纷预览").click()
#         self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
#         sleep(1)
#         self.driver.find_element_by_link_text(u"不发送").click()
#         sleep(3)
#         self.driver.find_element_by_xpath('//div[@id="layui-layer2"]/div[3]/a').click()
#         self.driver.find_element_by_css_selector("button[type=\"button\"]").click()
#
#     # '/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[6]/p'


def jf1():
    from odrweb.page.homepage import HomePage
    from odrweb.core.initdata import users
    homepage = HomePage()
    homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    sleep(10)


def jf2():
    from odrweb.page.homepage import HomePage
    from odrweb.core.initdata import users
    homepage = HomePage()
    homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
    # sleep(10)
    # dis = DisputePage(homepage)
    # dis.dispute_djy_commit()
    # dis.dispute_djy_save(**jf_info)


if __name__ == '__main__':
    jf2()
