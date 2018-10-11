# coding:utf-8

from time import sleep

from odrweb.page.browser import Page



simple_jf_info = { "applicant": u"段志勇",
                   "applicant_tel": "15895996954",
                   "applicant_id": "",
                   "applicant_nation":u"汉族",
                   "applicant_job":u"测试工程师",
                   "applicant_addr": u"1栋2单元303",

                   "disputer":u"王发明",
                   "disputer_tel":'13913031374',
                   "disputer_nation":u"汉族",
                   "disputer_job":"",
                   "disputer_addr":"",

                   "agent_name":u"徐传珠",
                   "agent_tel":'15295745648',
                   "agent_id":'321281199507077775',

                   "agent_name_b":u"钱桂林",
                   "agent_tel_b":'13160077223',
                   "agent_id_b":"321023199508166636",

                   "jf_desc":u"填写简易纠纷类型",
                   "jf_appeal":u"类型是否正确",
                   "jf_action":u"验证类型",
                   "jf_time":u"三天"
                   }


class SimpleDisputePage(Page):

    x_caseregisrer_list = '//div[contains(text(), "案件登记列表")]'

    def _into_simple_jf(self):
        '''进入添加简易纠纷登记页面'''
        # # 点击调解员页面案件登记列表
        # self.find_element_by_xpath('/html/body/div[4]/div[1]/button[2]').click()
        # 调解员登记列表-点击
        self.find_element_by_xpath(self.x_caseregisrer_list).click()
        sleep(1)
        # 点击简易案件登记
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/a[1]').click()
        sleep(1)

    def _input_applicant_info(self,**kwargs):
        '''填写申请人信息'''
        # 填写申请人姓名
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div/div[2]/div/div/input').send_keys(kwargs["applicant"])
        # 填写申请人电话号码
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div/div[4]/div/div/input').send_keys(kwargs["applicant_tel"])

    def _input_disputer_info(self, **kwargs):
        '''填写被申请人信息'''
        # 填写被申请人姓名
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[2]/div/div/input').send_keys(kwargs["disputer"])
        # 填写被申请人电话号码
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[4]/div/div/input').send_keys(kwargs["disputer_tel"])

    def _input_agent_info(self,**kwargs):
        '''填写申请人代理人信息'''
        # 填写申请人代理人姓名
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div/div[13]/div[2]/div[1]/div/div/input').send_keys(kwargs["agent_name"])
        # 填写申请人代理人电话号码
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div/div[13]/div[2]/div[3]/div/div/input').send_keys(kwargs["agent_tel"])
        # 填写申请人代理人身份证
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div/div[13]/div[2]/div[4]/div/div/input').send_keys(kwargs["agent_id"])

    def _input_agent_b_info(self,**kwargs):
        '''填写被申请人代理人信息'''
        # 填写被申请人代理人姓名
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[13]/div[2]/div[1]/div/div/input').send_keys(kwargs["agent_name_b"])
        # 填写被申请人代理人电话号码
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[13]/div[2]/div[3]/div/div/input').send_keys(kwargs["agent_tel_b"])
        # 填写被申请人代理人身份证信息
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[13]/div[2]/div[4]/div/div/input').send_keys(kwargs["agent_id_b"])

    def _input_dispute_info(self,**kwargs):
        '''填写纠纷详情'''
        # 选择纠纷类型为消费维权
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[3]/div[2]/div[1]/div/div/label[2]/span[2]').click()
        # 填写纠纷争议事实事项
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[3]/div[2]/div[2]/div/div/div/textarea').send_keys(kwargs["jf_desc"])
        # 填写自愿达成协议
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[3]/div[2]/div[3]/div/div/div/textarea').send_keys(kwargs["jf_appeal"])
        # 选择纠纷发生地
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[3]/div[2]/div[4]/div/span[2]').click()
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[3]/div[2]/div[4]/div/div[1]/div/div[2]/div[1]/dl[4]/dd/a[5]').click()
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[3]/div[2]/div[4]/div/div[1]/div/div[2]/div[2]/dl/dd/a[1]').click()
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[3]/div[2]/div[4]/div/div[1]/div/div[2]/div[3]/dl/dd/a[1]').click()
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[3]/div[2]/div[4]/div/div[1]/div/div[2]/div[4]/dl/dd/a[1]').click()
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[3]/div[2]/div[4]/div/div[1]/div/div[2]/div[5]/dl/dd/a[1]').click()
        # 填写履行方式
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[3]/div[2]/div[8]/div/div/input').send_keys(kwargs["jf_action"])
        # 填写时限
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[3]/div[2]/div[9]/div/div/input').send_keys(kwargs["jf_time"])

    def save(self):
        '''点击保存按钮'''
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[1]/p/span[1]').click()
        sleep(1)
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
        sleep(0.5)
        self.find_element_by_xpath(self.x_caseregisrer_list).click()

    def commit(self):
        '''点击提交按钮'''
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[1]/p/span[2]').click()
        sleep(1)
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
        sleep(0.5)
        self.find_element_by_xpath(self.x_caseregisrer_list).click()

    def verification_commit(self,**kwargs):
        try:
            jf_desc = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
        except:
            jf_desc = "*None*"
        print "result",jf_desc
        print "except",kwargs["jf_desc"]
        res = jf_desc == kwargs["jf_desc"]
        return res

    def verification_commit_add(self,**kwargs):
        try:
            jf_desc = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[8]/p').text
        except:
            jf_desc = "*None*"
        print "result",jf_desc
        print "except",kwargs["jf_desc"]
        res = jf_desc == kwargs["jf_desc"]
        return res



    def verification_save(self,**kwargs):
        try:
            jf_desc = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
        except:
            jf_desc = "*None*"
        print "result",jf_desc
        print "except",kwargs["jf_desc"]
        res =  jf_desc == kwargs["jf_desc"]
        return res


    def simple_jf_input(self,**kwargs):
        '''简易案件-申请人-被申请人'''
        self._into_simple_jf()
        self._input_applicant_info(**kwargs)
        self._input_disputer_info(**kwargs)
        self._input_dispute_info(**kwargs)



    def simple_jf_agent_commit(self,**kwargs):
        '''简易案件-申请人-代理人-被申请人'''
        self._into_simple_jf()
        self._input_applicant_info(**kwargs)
        self._input_agent_info(**kwargs)
        self._input_disputer_info(**kwargs)
        self._input_dispute_info(**kwargs)

    def simple_jf_agent_b_commit(self,**kwargs):
        '''简易案件-申请人-被申请人-代理人'''
        self._into_simple_jf()
        self._input_applicant_info(**kwargs)
        self._input_disputer_info(**kwargs)
        self._input_agent_b_info(**kwargs)
        self._input_dispute_info(**kwargs)

    def simple_jf_agent_agent_b_commit(self,**kwargs):
        '''简易案件-申请人-代理人-被申请人-代理人'''
        self._into_simple_jf()
        self._input_applicant_info(**kwargs)
        self._input_agent_info(**kwargs)
        self._input_disputer_info(**kwargs)
        self._input_agent_b_info(**kwargs)
        self._input_dispute_info(**kwargs)



    def simple_jf_add_delete(self,**kwargs):
        '''简易案件-添加申请人-删除申请人'''
        self._into_simple_jf()
        self._input_applicant_info(**kwargs)
        # 点击添加申请人
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div/div[14]/p[1]').click()
        # 点击删除按钮
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div[2]/div[14]').click()
        self._input_disputer_info(**kwargs)
        # 点击添加被申请人
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[14]/p[1]').click()
        # 点击删除按钮
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div[2]/div[14]').click()
        self._input_dispute_info(**kwargs)


    def simple_jf_add_applicant_disputer(self,**kwargs):
        '''简易案件-两个申请人-两个申请人代理人-两个被申请人-一个被申请人代理人'''
        self._into_simple_jf()
        self._input_applicant_info(**kwargs)
        self._input_agent_info(**kwargs)
        # 点击添加申请人
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div/div[14]/p[1]').click()
        # 填写申请人2姓名
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div[2]/div[2]/div/div/input').send_keys(u"王文志")
        # 填写申请人2手机号码
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div[2]/div[4]/div/div/input').send_keys('15396759623')
        # 填写申请人2代理人姓名
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div[2]/div[13]/div[2]/div[1]/div/div/input').send_keys(u"常景国")
        # 填写申请人2代理人手机号码
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div[2]/div[13]/div[2]/div[3]/div/div/input').send_keys('17625906164')
        # 填写申请人2代理人身份证
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div[2]/div[13]/div[2]/div[4]/div/div/input').send_keys('340621199408101694')
        # 填写被申请人姓名
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[2]/div/div/input').send_keys(kwargs["disputer"])
        # 填写被申请人手机号码
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[4]/div/div/input').send_keys(kwargs["disputer_tel"])
        # 填写被申请人代理人姓名
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[13]/div[2]/div[1]/div/div/input').send_keys(kwargs["agent_name_b"])
        # 填写被申请人代理人手机号码
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[13]/div[2]/div[3]/div/div/input').send_keys(kwargs["agent_tel_b"])
        # 填写被申请人代理人身份证
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[13]/div[2]/div[4]/div/div/input').send_keys(kwargs["agent_id_b"])
        # 点击添加被申请人
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div[14]/p[1]').click()
        # 填写被申请人2姓名
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/input').send_keys(u"吴饶新")
        # 填写被申请人2手机号码
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/input').send_keys('15295745678')
        # 填写纠纷信息
        self._input_dispute_info(**kwargs)




