# coding:utf-8
from time import sleep

from selenium.webdriver.support.select import Select

from odrweb.page.browser import Page

jf_consult = {"jf_type": u"消费维权",
              "jf_desc": u"假冒商品",
              "jf_appeal": u"假一赔十",
              "jf_applyName": u"徐传珠",
              "jf_applyTel": '15295745648',
              "jf_applyNumber": '321281199507077775',
              "jf_appliedName": u"钱桂林",
              "jf_appliedTel": '13160077223',
              "jf_agentName": u"段志勇",
              "jf_agentTel":' 15895996954 ',
              "jf_organization": u"北明测试",
              "jf_societyNumber": '123456789123456789'}


class PersonalPage_one(Page):

    # def __init__(self, page=None, ):
    #     self.driver = page.driver

    def quit(self):
        self.driver.quit()

    def into_mediate(self):

        '''
        个人中心选择我是申请人进入调解
        :param chrome:
        :return:
        '''
        # 点击选择我要调解
        self.driver.find_element_by_xpath('//div[@id="personal-content"]/div[1]/div[2]/div[3]/div[2]').click()

        sleep(1)
        # 弹出提示框并点击
        self.driver.find_element_by_xpath('//div[@id="layui-layer1"]/div[3]/a[1]').click()

    def choose_sqr(self):
        # 选择用户身份为我是申请人
        self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div/div[2]/div[2]/div').click()

    def mediate_info_input(self,**kwargs):

        sleep(2)
        # 选择调解类型
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/form/div[1]/div/div/label[2]/span[2]').click()
        # 输入纠纷描述、我的诉求
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/form/div[2]/div/div/div/textarea').send_keys( jf_consult["jf_desc"])
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/form/div[3]/div/div/div/textarea').send_keys(jf_consult["jf_appeal"])
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
        sleep(2)

    def user_apply_natural(self):
        '''申请人身份为自然人'''
        sleep(1)
        # 申请人信息默认填写，直接点击下一步进入被申请人信息填写
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[2]/p[3]/span[2]').click()

    def user_apply_logel(self):
        '''选择申请人为法人'''
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[1]/div/div/label[2]/span[2]').click()

    def user_apply_organization(self):
        '''选择申请人为非法组织'''
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[1]/div/div/label[3]/span[2]').click()

    def apply_info_input(self,**kwargs):
        '''申请人为法人、非法人组织信息填写'''
        # 填写申请人企业信息、社会信用代码
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[2]/div/input').send_keys(jf_consult["jf_organization"])
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[3]/div/input').send_keys(jf_consult["jf_societyNumber"])
        # 点击下一步进入填写被申请人信息
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[2]/p[3]/span[2]').click()
        sleep(2)

    def user_applied_natuural(self,**kwargs):
        '''被申请人身份为自然人'''
        sleep(1)
        # 填写被申请人姓名、电话号码
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[2]/div/div/input').send_keys(jf_consult["jf_appliedName"])
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[4]/div/div/input').send_keys(jf_consult["jf_appliedTel"])
        # 点击提交弹出提示框
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[2]/p[3]/span[2]').click()
        sleep(2)
        # 点击提示框确定
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()

        sleep(2)
        # 点击查看纠纷详情
        # self.driver.find_element_by_xpath('//div[@id="mediate"]/div[1]/div[4]/div[2]/a[1]').click()
        #
        # sleep(1)
        # # 点击返回列表
        # self.driver.find_element_by_xpath('/html/body/section[1]/button').click()

    def user_applied_logel(self):
        '''选择被申请人为法人'''
        self.driver.find_element_by_xpath( '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[1]/div/div/label[2]/span[2]').click()
        sleep(1)

    def user_applied_organization(self):
        '''选择被申请人为非法人组织'''
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[1]/div/div/label[3]/span[2]').click()
        sleep(1)

    def applied_info_input(self,**kwargs):
        '''被申请人为法人、非法人组织信息填写'''
        sleep(1)
        # 填写被申请人企业名称
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[2]/div/div/input').send_keys(jf_consult["jf_organization"])
        # 填写被申请人社会信用代码
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[3]/div/input').send_keys(jf_consult["jf_societyNumber"])
        # 填写被申请人法定代表人信息
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[4]/div/div/input').send_keys(jf_consult["jf_appliedName"])
        # 被申请人联系电话
        self.driver.find_element_by_xpath(
            '//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[6]/div/div/input').send_keys(jf_consult["jf_appliedTel"])
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
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[1]/form/div/div[9]/div/input').send_keys(
            'addr')
        # 点击提交
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[5]/div[2]/div[2]/p[3]/span[2]').click()
        sleep(2)
        # 弹出提示框，点击确定
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
        sleep(2)

    def verification_apply_uatural_mediate(self,jf_desc):
        # 申请人为自然人方法校验
        try:
            mediate_desc = self.driver.find_element_by_xpath('//div[@id="mediate"]/div[1]/div[3]/ul/li[7]').text
            res = mediate_desc.split(u'：')[-1]
        except:
            res = "*None*"
        print "result: ", res
        print "expect: ", jf_desc
        return res == jf_desc

    def verification_apply_organization_mediate(self,jf_organization):
        # 申请人为法人、非法人机构方法校验
        try:
            mediate_desc = self.driver.find_element_by_xpath('//div[@id="mediate"]/div[1]/div[3]/ul/li[3]').text
            res = mediate_desc.split(u'：')[-1]
        except:
            res = "*None*"
        print "result: ", res
        print "expect: ", jf_organization
        return res == jf_organization

    def choose_dlr(self):
        # 选择用户身认为我是特别授权代理人
        self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div/div[2]/div[1]/span[2]').click()
        # 点击申请调解
        self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div/div[2]/div[2]/div[2]/div').click()
        # 上传委托书
        js = 'app.$data.dynamicValidateForm.domains.forEach(e=>{e.Dfile={createId:null,createPersonnelRole:null,deleteMark:null,fileName:".gitconfig",filePath:"/powerOfAttorney/201808/4872c3f0440046aea35df9a6b6c2e7ee.gitconfig",fileSuffix:"gitconfig",id:null,lawCaseId:null,litigantId:null,name:"授权委托书",remarks:null,syncMark:"0",type:null}})'
        self.driver.execute_script(js)

    def user_dlr_apply_natural(self,**kwargs):
        ''' 用户作为代理人申请人为自然人'''
        # 填写申请人姓名
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[2]/div/div/input').send_keys(jf_consult["jf_applyName"])
        # 填写申请人联系电话
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[4]/div/div/input').send_keys(jf_consult["jf_applyTel"])
        # 填写申请人身份证号码
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[5]/div/div/input').send_keys(jf_consult["jf_applyNumber"])
        # 选择申请人常住地址
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/span[2]').click()
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/div/div/div[2]/div[1]/dl[4]/dd/a[5]').click()
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/div/div/div[2]/div[2]/dl/dd/a[1]').click()
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/div/div/div[2]/div[3]/dl/dd/a[1]').click()
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/div/div/div[2]/div[4]/dl/dd/a[1]').click()
        # 填写申请人详细地址
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[7]/div/div/input').send_keys('addr')
        # 点击下一步进入被申请人填写页面
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[2]/p[3]/span[2]').click()


    def user_apply_natural_addspe_sqr(self,**kwargs):
        pass

    def user_apply_organization_addspe_sqr(self,**kwargs):
        pass

    def user_applied_natural_addspe_sqr(self,**kwargs):
        pass

    def user_applied_organization_addspe_sqr(self,**kwargs):
        pass






    def user_sqr_natural_natural(self,personalpage_one):
        '''申请人自然人，被申请人自然人'''
        personalpage_one.into_mediate()
        personalpage_one.choose_sqr()
        personalpage_one.mediate_info_input()
        personalpage_one.user_apply_natural()
        personalpage_one.user_applied_natuural()

    def user_sqr_natural_logel(self,personalpage_one):
        '''申请人为自然人，被申请人为法人'''
        personalpage_one.into_mediate()
        personalpage_one.choose_sqr()
        personalpage_one.mediate_info_input()
        personalpage_one.user_apply_natural()
        personalpage_one.user_applied_logel()
        personalpage_one.applied_info_input()

    def user_sqr_natural_organization(self, personalpage_one):
        '''申请人为自然人，被申请人为非法人组织'''
        personalpage_one.into_mediate()
        personalpage_one.choose_sqr()
        personalpage_one.mediate_info_input()
        personalpage_one.user_apply_natural()
        personalpage_one.user_applied_organization()
        personalpage_one.applied_info_input()

    def user_sqr_logel_natural(self, personalpage_one):
        '''申请人为法人，被申请人为自然人'''
        personalpage_one.into_mediate()
        personalpage_one.choose_sqr()
        personalpage_one.mediate_info_input()
        personalpage_one.user_apply_logel()
        personalpage_one.apply_info_input()
        personalpage_one.user_applied_natuural()

    def user_sqr_logel_logel(self, personalpage_one):
        '''申请人为法人，被申请人为法人'''
        personalpage_one.into_mediate()
        personalpage_one.choose_sqr()
        personalpage_one.mediate_info_input()
        personalpage_one.user_apply_logel()
        personalpage_one.user_applied_logel()
        personalpage_one.applied_info_input()

    def user_sqr_logel_organization(self, personalpage_one):
        '''申请人为法人，被申请人为法人组织'''
        personalpage_one.into_mediate()
        personalpage_one.choose_sqr()
        personalpage_one.mediate_info_input()
        personalpage_one.user_apply_logel()
        personalpage_one.apply_info_input()
        personalpage_one.user_applied_organization()
        personalpage_one.applied_info_input()

    def user_sqr_organization_natural(self, personalpage_one):
        '''申请人为非法人组织，被申请人为自然人'''
        personalpage_one.into_mediate()
        personalpage_one.choose_sqr()
        personalpage_one.mediate_info_input()
        personalpage_one.user_apply_organization()
        personalpage_one.apply_info_input()
        personalpage_one.user_applied_natuural()

    def user_sqr_organization_logel(self, personalpage_one):
        '''申请人为非法人组织，被申请人为法人'''
        personalpage_one.into_mediate()
        personalpage_one.choose_sqr()
        personalpage_one.mediate_info_input()
        personalpage_one.user_apply_organization()
        personalpage_one.apply_info_input()
        personalpage_one.user_applied_logel()
        personalpage_one.applied_info_input()

    def user_sqr_organization_logel(self, personalpage_one):
        '''申请人为非法人组织，被申请人非法人组织'''
        personalpage_one.into_mediate()
        personalpage_one.choose_sqr()
        personalpage_one.mediate_info_input()
        personalpage_one.user_apply_organization()
        personalpage_one.apply_info_input()
        personalpage_one.user_applied_organization()
        personalpage_one.applied_info_input()











def t():
    from odrweb.page import HomePage
    from odrweb.core.initdata import users
    homepage = HomePage()
    homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
    homepage.user_personal_center()
    per = PersonalPage_one(homepage)
    per.consult(**jf_consult)


if __name__ == '__main__':
    t()
