# coding:utf-8
from time import sleep

from odrweb.page.browser import Page

jf_info_all = {"jf_desc": u"调解员-登记纠纷提交-申非法人组织代理人-被法人",
               "applicant_type": u"非法人组织",  # 自然人 法人 非法人组织
               "disputer_type": u"法人",  # 自然人 法人 非法人组织
               "agent_type": "common",  # "" common special,
               "agent_b_type": "",  # common special,

               "jf_appeal": u"假一赔十",
               "applicant_name": u"企业或机构名称",  #
               "world_credit_id": "abcde1234567890",
               "applicant": u"钱桂林",
               "applicant_tel": "13160077223",
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


    def _apply_info_dlr_input(self,**kwargs):
        if kwargs['applicant_type']==u'自然人':
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[2]/div/div[1]/input').send_keys(kwargs['applicant'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[4]/div/div/input').send_keys(kwargs['applicant_tel'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[5]/div/div/input').send_keys(kwargs['applicant_id'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[7]/div/div/input').send_keys(kwargs['applicant_addr'])
            # 选择地区
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/span[2]').click()
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/div/div/div[2]/div[1]/dl[4]/dd/a[5]').click()
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/div/div/div[2]/div[2]/dl/dd/a[1]').click()
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/div/div/div[2]/div[3]/dl/dd/a[1]').click()
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/div/div/div[2]/div[4]/dl/dd/a[1]').click()
        else:
            if kwargs['applicant_type']==u'法人':
                self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[1]/div/div/label[2]/span[2]').click()
            elif kwargs['applicant_type']==u'非法人组织':
                self.find_element_by_xpath('//*[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[1]/div/div/label[3]/span[2]').click()
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[2]/div/input').send_keys(kwargs['applicant_name'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[3]/div/input').send_keys(kwargs['world_credit_id'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[4]/div/div/input').send_keys(kwargs['applicant'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/div/input').send_keys(kwargs['applicant_tel'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[7]/div/div/input').send_keys(kwargs['applicant_id'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[9]/div/div/input').send_keys(kwargs['applicant_addr'])
            # 选择地区
            self.find_element_by_css_selector('#app > div > div.proposer.unActive.stepActive > div.proposerMain > div.main > form > div > div.el-form-item.rrr > div > span.city-picker-span').click()
            self.find_element_by_css_selector('#app > div > div.proposer.unActive.stepActive > div.proposerMain > div.main > form > div > div.el-form-item.rrr > div > div > div > div.city-select-content > div.city-select.province > dl:nth-child(4) > dd > a:nth-child(5)').click()
            self.find_element_by_css_selector('#app > div > div.proposer.unActive.stepActive > div.proposerMain > div.main > form > div > div.el-form-item.rrr > div > div > div > div.city-select-content > div.city-select.city > dl > dd > a:nth-child(1)').click()
            self.find_element_by_css_selector('#app > div > div.proposer.unActive.stepActive > div.proposerMain > div.main > form > div > div.el-form-item.rrr > div > div > div > div.city-select-content > div.city-select.district > dl > dd > a:nth-child(1)').click()
            self.find_element_by_css_selector('#app > div > div.proposer.unActive.stepActive > div.proposerMain > div.main > form > div > div.el-form-item.rrr > div > div > div > div.city-select-content > div.city-select.street > dl > dd > a:nth-child(1)').click()
            # 上传委托书

        js = 'app.$data.dynamicValidateForm.domains.forEach(e=>{e.Dfile={createId:null,createPersonnelRole:null,deleteMark:null,fileName:".gitconfig",filePath:"/powerOfAttorney/201808/4872c3f0440046aea35df9a6b6c2e7ee.gitconfig",fileSuffix:"gitconfig",id:null,lawCaseId:null,litigantId:null,name:"授权委托书",remarks:null,syncMark:"0",type:null}})'
        self.driver.execute_script(js)

    def _input_all_dlr(self, **kwargs):
        self._into_mediate()
        self._choose_dlr(**kwargs)
        self._mediate_info_input(**kwargs)
        # 申请人
        self._apply_info_dlr_input(**kwargs)
        # 申请人代理人默认登录用户

        # 下一步
        self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[2]/p[3]/span[2]').click()

        sleep(1)
        # 被申请人
        if kwargs['disputer_type'] == u'自然人':
            self._user_applied_natuural(**kwargs)
            if kwargs['agent_b_type']:
                self._agent_b(**kwargs)
        else:
            self._applied_info_input(**kwargs)
            if kwargs['agent_b_type']:
                self._agent_b(**kwargs)

        # 点击提交
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[2]/p[3]/span[2]').click()
        sleep(2)
        # 弹出提示框，点击确定
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
        sleep(2)

    def _input_all(self, **kwargs):
        self._into_mediate()
        self._choose_sqr()
        self._mediate_info_input(**kwargs)
        # 申请人
        if kwargs['applicant_type'] == u'自然人':
            # 个人登记纠纷，申请人信息自动获取
            if kwargs['agent_type']:
                self._agent(**kwargs)
        else:
            self._apply_info_input(**kwargs)
            if kwargs['agent_b_type']:
                self._agent(**kwargs)

        # 下一步
        self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[2]/p[3]/span[2]').click()

        sleep(1)
        # 被申请人
        if kwargs['disputer_type'] == u'自然人':
            self._user_applied_natuural(**kwargs)
            if kwargs['agent_b_type']:
                self._agent_b(**kwargs)
        else:
            self._applied_info_input(**kwargs)
            if kwargs['agent_b_type']:
                self._agent_b(**kwargs)

        # 点击提交
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[2]/p[3]/span[2]').click()
        sleep(1)
        # 弹出提示框，点击确定
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
        sleep(1)

    def _agent_b(self, **kwargs):
        if kwargs['disputer_type'] == u'自然人':
            # 展开
            if  not kwargs.get('mode'):
                self.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[9]/p[2]/em').click()
            sleep(1)
            if kwargs['agent_type'] == 'common':
                self.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[9]/div/div[1]/div/div/label[1]/span[1]/span').click()
            elif kwargs['agent_type'] == 'special':
                self.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[9]/div/div[1]/div/div/label[2]/span[1]/span').click()

            self.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[9]/div/div[2]/div/div/input').send_keys(kwargs['agent_b_name'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[9]/div/div[3]/div/div/label[1]/span[1]/span').click()
            self.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[9]/div/div[4]/div/div/input').send_keys(kwargs['agent_b_tel'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[9]/div/div[5]/div/div/input').send_keys(kwargs['agent_b_id'])

        else:
            # 展开
            if  not kwargs.get('mode'):
                self.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[11]/p[2]/em').click()
            sleep(0.5)
            if kwargs['agent_b_type'] == 'common':
                # 一般代理人
                self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[11]/div/div[1]/div/div/label[1]/span[1]/span').click()
            elif kwargs['agent_b_type'] == 'special':
                # 特别代理人
                self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[11]/div/div[1]/div/div/label[2]/span[1]/span').click()
            self.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[11]/div/div[2]/div/div/input').send_keys(kwargs['agent_b_name'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[11]/div/div[3]/div/div/label[1]/span[1]/span').click()
            self.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[11]/div/div[4]/div/div/input').send_keys(kwargs['agent_b_tel'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[11]/div/div[5]/div/div/input').send_keys(kwargs['agent_b_id'])
            # 上传委托书

    def _agent(self, **kwargs):
        if kwargs['applicant_type'] == u'自然人':
            # 展开
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[9]/p[2]/em').click()
            sleep(0.5)
            if kwargs['agent_type'] == 'common':
                self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[9]/div/div[1]/div/div/label[1]/span[1]/span').click()
            elif kwargs['agent_type'] == 'special':
                self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[9]/div/div[1]/div/div/label[2]/span[1]/span').click()

            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[9]/div/div[2]/div/div/input').send_keys(kwargs['agent_name'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[9]/div/div[3]/div/div/label[1]/span[1]/span').click()
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[9]/div/div[4]/div/div/input').send_keys(kwargs['agent_tel'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[9]/div/div[5]/div/div/input').send_keys(kwargs['agent_id'])

        else:
            # 展开
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[11]/p[2]/em').click()
            sleep(0.5)
            if kwargs['agent_type'] == 'common':
                # 一般代理人
                self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[11]/div/div[1]/div/div/label[1]/span[1]/span').click()
            elif kwargs['agent_type'] == 'special':
                # 特别代理人
                self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[11]/div/div[1]/div/div/label[2]/span[1]').click()
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[11]/div/div[2]/div/div/input').send_keys(kwargs['agent_name'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[11]/div/div[3]/div/div/label[1]/span[1]/span').click()
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[11]/div/div[4]/div/div/input').send_keys(kwargs['agent_tel'])
            self.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[11]/div/div[5]/div/div/input').send_keys(kwargs['agent_id'])
        # 上传委托书
        js = 'app.$data.dynamicValidateForm.domains.forEach(e=>{e.Dfile={createId:null,createPersonnelRole:null,deleteMark:null,fileName:".gitconfig",filePath:"/powerOfAttorney/201808/4872c3f0440046aea35df9a6b6c2e7ee.gitconfig",fileSuffix:"gitconfig",id:null,lawCaseId:null,litigantId:null,name:"授权委托书",remarks:null,syncMark:"0",type:null}})'
        self.driver.execute_script(js)

    def _into_mediate(self):
        ''' 个人中心选择我是申请人进入调解'''

        # 点击选择我要调解
        self.driver.find_element_by_xpath('//div[@id="personal-content"]/div[1]/div[2]/div[3]/div[2]').click()

        sleep(1)
        # 弹出提示框并点击
        self.driver.find_element_by_xpath('//div[@id="layui-layer1"]/div[3]/a[1]').click()

    def _choose_sqr(self):
        # 选择用户身份为我是申请人
        self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div/div[2]/div[2]/div').click()

    def _mediate_info_input(self, **kwargs):

        sleep(1)
        # 选择调解类型
        self.find_element_by_xpath('//div[@id="app"]/div/div[3]/form/div[1]/div/div/label[2]/span[2]').click()
        # self.find_element_by_xpath('//div[@id="app"]/div/div[3]/form/div[1]/div/div/label[4]/span[2]').click()
        # 输入纠纷描述、我的诉求
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/form/div[2]/div/div/div/textarea').send_keys(kwargs["jf_desc"])
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/form/div[3]/div/div/div/textarea').send_keys(kwargs["jf_appeal"])
        # 选择纠纷发生地
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/form/div[4]/div/span[2]').click()
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[3]/form/div[4]/div/div/div/div[2]/div[1]/dl[4]/dd/a[5]').click()
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[3]/form/div[4]/div/div/div/div[2]/div[2]/dl/dd/a[1]').click()
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[3]/form/div[4]/div/div/div/div[2]/div[3]/dl/dd/a[1]').click()
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[3]/form/div[4]/div/div/div/div[2]/div[4]/dl/dd/a[1]').click()
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[3]/form/div[4]/div/div/div/div[2]/div[5]/dl/dd/a[1]').click()
        # 选择调解机构
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/form/div[6]/div/div/input').click()
        sleep(1)
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[3]/div[3]/div/div/div[2]/div[2]/ul/li[1]/button').click()
        # 点击下一步
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/div[5]').click()
        # self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
        sleep(1)

    def _user_apply_logel(self):
        '''选择申请人为法人'''
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[1]/div/div/label[2]/span[2]').click()

    def _user_apply_organization(self):
        '''选择申请人为非法组织'''
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[1]/div/div/label[3]/span[2]').click()

    def _apply_info_input(self, **kwargs):
        '''申请人为法人、非法人组织信息填写'''

        # 填写申请人企业信息、社会信用代码
        if kwargs['applicant_type'] == u'法人':
            self._user_apply_logel()
        elif kwargs['applicant_type'] == u'非法人组织':
            self._user_apply_organization()

        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[2]/div/input').send_keys(kwargs["applicant_name"])
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[3]/div/input').send_keys(kwargs["world_credit_id"])
        # 点击下一步进入填写被申请人信息
        # self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[2]/p[3]/span[2]').click()
        sleep(1)

    def _user_applied_natuural(self, **kwargs):
        '''被申请人身份为自然人'''
        sleep(1)
        # 填写被申请人姓名、电话号码
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[2]/div/div/input').send_keys(kwargs["disputer"])
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[4]/div/div/input').send_keys(kwargs["disputer_tel"])
        # 点击提交弹出提示框
        # self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[2]/p[3]/span[2]').click()
        # sleep(2)
        # # 点击提示框确定
        # self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
        # sleep(2)

    def _user_applied_logel(self):
        '''选择被申请人为法人'''
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[1]/div/div/label[2]/span[2]').click()
        sleep(1)

    def _user_applied_organization(self):
        '''选择被申请人为非法人组织'''
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[1]/div/div/label[3]/span[2]').click()

        sleep(1)

    def _applied_info_input(self, **kwargs):
        '''被申请人为法人、非法人组织信息填写'''

        if kwargs['disputer_type'] == u'法人':
            self._user_applied_logel()
        elif kwargs['disputer_type'] == u'非法人组织':
            self._user_applied_organization()

        # 填写被申请人企业名称
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[2]/div/div/input').send_keys(kwargs["disputer_name"])
        # 填写被申请人社会信用代码
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[3]/div/input').send_keys(kwargs["disputer_world_credit_id"])
        # 填写被申请人法定代表人信息
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[4]/div/div/input').send_keys(kwargs["disputer"])
        # 被申请人联系电话
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[6]/div/div/input').send_keys(kwargs["disputer_tel"])
        # 被申请人单位地址
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[8]/div/span[2]').click()
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[8]/div/div/div/div[2]/div[1]/dl[4]/dd/a[5]').click()
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[8]/div/div/div/div[2]/div[2]/dl/dd/a[1]').click()
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[8]/div/div/div/div[2]/div[3]/dl/dd/a[1]').click()
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[8]/div/div/div/div[2]/div[4]/dl/dd/a[1]').click()
        # 被申请人详细地址
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[9]/div/input').send_keys(kwargs['disputer_addr'])

    def verification_apply_uatural_mediate(self, jf_desc):
        # 申请人为自然人方法校验
        try:
            mediate_desc = self.driver.find_element_by_xpath('//div[@id="mediate"]/div[1]/div[3]/ul/li[7]').text
            res = mediate_desc.split(u'：')[-1]
        except:
            res = "*None*"
        print "result: ", res
        print "expect: ", jf_desc
        return res == jf_desc

    def verfication_commit_dlr(self,**kwargs):
        try:
            res = self.find_element_by_xpath('//*[@id="mediate"]/div[1]/div[3]/ul/li[7]').text
            jf_desc = res.split(u'：')[-1]
        except:
            jf_desc = "**Nome**"
        print "result: ", kwargs['jf_desc']
        print "expect: ", jf_desc

        try:
             res = self.find_element_by_xpath('//*[@id="mediate"]/div[1]/div[3]/ul/li[3]').text
             applicant = res.split(u'：')[-1]
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


    def verification_apply_organization_mediate(self, jf_organization):
        # 申请人为法人、非法人机构方法校验
        try:
            mediate_desc = self.driver.find_element_by_xpath('//div[@id="mediate"]/div[1]/div[3]/ul/li[3]').text
            res = mediate_desc.split(u'：')[-1]
        except:
            res = "*None*"
        print "result: ", res
        print "expect: ", jf_organization
        return res == jf_organization

    def _choose_dlr(self, **kwargs):
        if kwargs['agent_type'] == "special":
            # 选择用户身认为我是特别授权代理人
            print 'specialspecialspecial'
            self.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/span[2]').click()
        # elif kwargs['agent_type'] == "common":
        #     print 'commoncommon'
        #     self.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/span[1]').click()
        # 点击申请调解
        self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div').click()

    def dlr_apply_natural(self, **kwargs):
        ''' 用户作为代理人申请人为自然人'''
        # 填写申请人姓名
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[2]/div/div/input').send_keys(kwargs["jf_applyName"])
        # 填写申请人联系电话
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[4]/div/div/input').send_keys(kwargs["jf_applyTel"])
        # 填写申请人身份证号码
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[5]/div/div/input').send_keys(kwargs["jf_applyNumber"])
        # 选择申请人常住地址
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/span[2]').click()
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/div/div/div[2]/div[1]/dl[4]/dd/a[5]').click()
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/div/div/div[2]/div[2]/dl/dd/a[1]').click()
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/div/div/div[2]/div[3]/dl/dd/a[1]').click()
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/div/div/div[2]/div[4]/dl/dd/a[1]').click()
        # 填写申请人详细地址
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[7]/div/div/input').send_keys('addr')
        # 点击下一步进入被申请人填写页面
        # self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[2]/p[3]/span[2]').click()


if __name__ == '__main__':
    pass
