# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from odrweb.page.browser import Page


class CaseListBasePage(Page):
    modifcation_dispute_desc = "**_**modification"
    modifcation_dispute_appeal = '**_**appeal'
    modifcation_dispute_type = u"金融借款合同纠纷"
    back_list = '//button[text()="返回列表"]'  # 返回列表
    x_case_input_list_a = '//div[text()="案件登记列表"]'          # 案件登记列表链接
    def _make_mediate(self):
        '''预约调解'''
        self.find_element_by_xpath('//button[contains(text()," 预约调解")]').click()
        # 调解名称input
        self.find_element_by_xpath('//div[@id="newMeeting"]/div/div[2]/div[1]/ul/li/input').send_keys('conference_title')
        # 时间框
        self.find_element_by_xpath('//li[@id="dataParent"]/input').click()
        # 时间框确定
        self.driver.switch_to.frame(self.find_element_by_xpath('//li[@id="dataParent"]/div/iframe'))  # 切换iframe
        self.driver.find_element_by_xpath('//input[@id="dpOkInput"]').click()
        self.driver.switch_to.default_content()  # 从iframe返回
        #
        Select(self.find_element_by_xpath('//div[@id="newMeeting"]/div/div[2]/div[10]/ul/li[1]/select')).select_by_visible_text('0')
        Select(self.find_element_by_xpath('//div[@id="newMeeting"]/div/div[2]/div[10]/ul/li[2]/select')).select_by_visible_text('10')
        # 备注
        self.find_element_by_xpath('//div[@id="newMeeting"]/div/div[2]/div[11]/ul/li/textarea').send_keys('comment')
        self.find_element_by_xpath('//input[@value="预约"]').click()

    def get_conference_title(self):
        '''获取视频会议名称'''
        sleep(0.5)
        try:
            conference_title = self.find_element_by_xpath('/html/body/section[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/i').text
        except:
            conference_title = "**None**"
        return conference_title

    def _mediate_success(self):
        '''调解成功'''
        self.find_element_by_xpath('//span[contains(text(),"调解成功")]').click()
        self.find_element_by_xpath('//div[@id="reAllotSuc"]/div/div[3]/div/textarea').send_keys(u'已确认')
        self.find_element_by_xpath('//div[@id="reAllotSuc"]/div/div[4]/input').click()  # 确认
        sleep(1)
        btn = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="toLawConfirm"]/div/div[1]/div')))
        btn.click()
        # self.find_element_by_xpath('//div[@id="toLawConfirm"]/div/div[1]/div').click()

    def get_detail_dispute_status(self):
        '''获取纠纷详情中的纠纷状态'''
        sleep(1)
        # self.driver.refresh()
        try:
            dispute_status = self.find_element_by_xpath('/html/body/section[1]/div[2]/i').text
        except:
            dispute_status = "**Nome**"

        if dispute_status == u"等待调解" or dispute_status == u"正在调解" or dispute_status == "**Nome**":
            sleep(1)
            try:
                dispute_status = self.find_element_by_xpath('/html/body/section[1]/div[2]/i').text
            except:
                dispute_status = "**Nome**"
        # self.find_element_by_xpath('//button[contains(text(),"返回列表")]').click()

        return dispute_status

    def _mediate_failed(self):
        '''预约调解'''
        self.find_element_by_xpath('//span[contains(text(),"调解失败")]').click()
        self.find_element_by_xpath('//div[@id="reAllotFail"]/div/div[3]/div/textarea').send_keys(u'已确认,失败')
        self.find_element_by_xpath('//div[@id="reAllotFail"]/div/div[4]/input').click()

    def _mediate_stop(self):
        '''调解终止'''
        self.find_element_by_xpath('//span[contains(text(),"调解终止")]').click()
        ok_btn = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"确定")]')))
        ok_btn.click()
        # self.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        sleep(0.5)
        # 等待输入框弹出
        btn = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//li[contains(text(),"当事人达成和解")]')))
        btn.click()
        # try:
        #     self.find_element_by_xpath().click()
        # except:
        #     sleep(0.5)
        #     self.find_element_by_xpath('//li[contains(text(),"当事人达成和解")]').click()

        self.find_element_by_xpath('//li[contains(text(), "其他")]').click()
        self.find_element_by_xpath('//li[contains(text(), "被申请人拒绝调解")]').click()
        # self.find_element_by_xpath('//span[text()="详细原因"]').parent.find_element_by_xpath('//div/textarea').send_keys(u'详细原因')
        self.find_element_by_xpath('//span[text()="详细原因"]/../div/textarea').send_keys(u'详细原因')
        # 确定
        self.find_element_by_xpath('//*[@id="myModal55"]/div/div[4]/input').click()

    def _mediate_revocation(self):
        '''调解撤回'''
        self.find_element_by_xpath('//span[contains(text(),"调解撤回")]').click()
        sleep(0.5)
        self.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        self.find_element_by_xpath('//li[contains(text(),"其他")]').click()
        self.find_element_by_xpath('//li[contains(text(),"申请人撤回调解")]').click()
        # self.find_element_by_xpath('//span[text()="详细原因"]').parent.find_element_by_xpath('//div/textarea').send_keys(u'详细原因')
        self.find_element_by_xpath('//span[text()="详细原因"]/../div/textarea').send_keys(u'详细原因')
        # 确定
        self.find_element_by_xpath('//*[@id="myModal55"]/div/div[4]/input').click()

    def _workstaion(self):
        '''工作台'''
        self.find_element_by_xpath('//button[contains(text(),"工作台")]').click()
        sleep(0.5)

    def _dispute_status(self):
        '''工作台'''
        self.find_element_by_xpath('//button[contains(text(),"调解状态")]').click()
        sleep(0.5)

    def _redistribution(self):
        '''重新分配,返回列表'''
        sleep(0.5)
        self.find_element_by_xpath('//span[contains(text(),"重新分配")]').click()
        sleep(0.5)
        self.find_element_by_xpath('//li[contains(text(),"身体不适")]').click()
        self.find_element_by_xpath('//li[contains(text(),"个人没有相关经验")]').click()
        self.find_element_by_xpath('//div[@id="reAllot"]/div/div[3]/div/textarea').send_keys(u'详细原因')
        # 确定,返回列表
        self.find_element_by_xpath('//div[@id="reAllot"]/div/div[4]/input').click()

    def _dispute_modification(self):
        '''我的案件列表-纠纷详情-保存'''
        Select(self.find_element_by_xpath('//div[@id="checkCaseform"]/form/div[1]/p/select')).select_by_visible_text(u"金融借款合同纠纷")
        self.find_element_by_xpath('//h6[text()="纠纷描述"]/following-sibling::p/textarea').clear()
        self.find_element_by_xpath('//h6[text()="纠纷描述"]/following-sibling::p/textarea').send_keys("**_**modification")
        # appeal
        self.find_element_by_xpath('//h6[text()="申请诉求"]/following-sibling::p/textarea').clear()
        self.find_element_by_xpath('//h6[text()="申请诉求"]/following-sibling::p/textarea').send_keys("**_**appeal")
        self.find_element_by_xpath('//button[text()="保存"]').click()
        sleep(2)
        self.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        sleep(0.5)
        self.find_element_by_xpath(self.back_list).click()
        sleep(2)

    def verification_dispute_modification(self):
        try:
            dispute_type = self.find_element_by_xpath('//label[contains(text(),"纠纷类型")]/following-sibling::p').text
        except:
            dispute_type = "**None**"
        try:
            appeal = self.find_element_by_xpath('//label[text()="申请人诉求"]/following-sibling::p').text
        except:
            appeal = "**None**"
        try:
            dispute_desc = self.find_element_by_xpath('//label[text()="纠纷描述"]/following-sibling::p').text
        except:
            dispute_desc = "**None**"
        print "result: ", appeal
        print "expect: ", self.modifcation_dispute_appeal
        print "result: ", dispute_desc
        print "expect: ", self.modifcation_dispute_desc
        print "result: ", dispute_type
        print "expect: ", self.modifcation_dispute_type
        return self.modifcation_dispute_appeal == appeal and self.modifcation_dispute_desc == dispute_desc and self.modifcation_dispute_type == dispute_type

    def verification_dispute_status(self, result, expect):
        '''
        调解成功
        :return:
        '''
        print "result: ", result
        print "expect: ", expect
        return expect == result


class CaseListPage(CaseListBasePage):
    case_list_select = '/html/body/div[4]/div[2]/div[1]/div[4]/select'  # 我的案件筛选选择框

    def _into_mycase_list(self):
        self.find_element_by_xpath("//button[contains(text(), '我的案件列表')]").click()

    def case_modification_save(self, dispute_status=u'等待调解'):
        self._goto_detail_info(dispute_status=dispute_status)
        self._dispute_modification()

    def mediate_vedio_create(self, dispute_status=u'等待调解'):
        '''预约调解'''
        dispute_id = self._goto_detail_info(dispute_status=dispute_status)
        print "{} 设置:{}->{}".format(dispute_id, dispute_status, u"预约调解")
        self._make_mediate()

    def mediate_success(self, dispute_status=u'等待调解'):
        dispute_id = self._goto_detail_info()
        print "{} 设置:{}->{}".format(dispute_id, dispute_status, u"调解成功")
        self._dispute_status()
        self._mediate_success()

    def mediate_failed(self, dispute_status=u'等待调解'):
        dispute_id = self._goto_detail_info(dispute_status=dispute_status)
        print "{} 设置:{}->{}".format(dispute_id, dispute_status, u"调解失败")
        self._dispute_status()
        self._mediate_failed()

    def mediate_stop(self, dispute_status=u'等待调解'):
        '''调解终止'''
        dispute_id = self._goto_detail_info(dispute_status=dispute_status)
        print "{} 设置:{}->{}".format(dispute_id, dispute_status, u"调解终止")
        self._dispute_status()
        self._mediate_stop()

    def mediate_revocation(self, dispute_status=u'等待调解'):
        '''调解撤回'''
        dispute_id = self._goto_detail_info(dispute_status=dispute_status)
        print "{} 设置:{}->{}".format(dispute_id, dispute_status, u"调解撤回")
        self._dispute_status()
        self._mediate_revocation()

    def mediate_redistribution(self, dispute_status=u'等待调解'):
        '''重新分配'''
        dispute_id = self._goto_detail_info(dispute_status=dispute_status)
        print "{} 设置:{}->{}".format(dispute_id, dispute_status, u"重新分配")
        self._workstaion()
        self._redistribution()

    def search(self, target):
        self._go_dispute_list()
        input_ = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="searchInput1"]')))
        input_.send_keys(target)
        # self.find_element_by_xpath('//input[@id="searchInput1"]').send_keys(target)
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[6]/div/span/span').click()

    def _go_dispute_list(self):
        # 进入纠纷调解案件列表
        self.find_element_by_xpath('//li[text()="纠纷调解案件列表"]').click()
        sleep(0.5)

    def _get_search(self, type_="No"):
        '''获取查询测试数据'''
        self._go_dispute_list()
        if type_ == "No":
            try:
                res = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div/div/div/div[1]').text
                search = res.split(u'：')[-1]
            except:
                search = None
        else:
            try:
                search = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div/div/div/div[4]/div[1]/div[6]/div[1]/p').text
            except:
                search = None
        return search

    def verification_search_No(self, expect):
        '''验证查询纠纷编号'''
        sleep(1)
        try:
            res = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[1]').text
            dis_id = res.split(u'：')[-1]
        except:
            dis_id = "**None**"
        print "result: ", dis_id
        print "expect: ", expect
        return dis_id == expect

    def verification_search_name(self, expect):
        '''验证查询当事人姓名'''
        sleep(1)
        try:
            result = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[4]/div[1]/div[6]/div[1]/p').text
        except:
            result = "**None**"
        print "result: ", result
        print "expect: ", expect
        return result == expect

    def select_dispute_status(self, dispute_status=u'等待调解'):
        Select(self.find_element_by_xpath(self.case_list_select)).select_by_visible_text(dispute_status)
        sleep(1.5)

    def verification_select_status(self, expect):
        '''验证查询状态'''
        try:
            # dispute_status = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[3]/div[1]/div[4]/p').text
            # 调解失败和调解终止
            # dispute_status = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[3]/div[1]/div[4]/p').text
            dispute_status = self.find_element_by_xpath('//label[text()="纠纷进度"]/following-sibling::p').text

        except:
            dispute_status = "**None**"
        print "result: ", dispute_status
        print "expect: ", expect
        return dispute_status == expect

    def _goto_detail_info(self, dispute_status=u'等待调解'):
        '''进入纠纷详情页面'''
        # 进入纠纷调解案件列表
        self.find_element_by_xpath('//li[contains(text(), "纠纷调解案件列表")]').click()
        Select(self.find_element_by_xpath(self.case_list_select)).select_by_visible_text(dispute_status)
        sleep(0.5)
        # self.find_element_by_xpath('/html/body/div[4]/div[1]/button[1]').click()
        self.find_element_by_xpath('//a[contains(text(),"纠纷详情")]').click()
        sleep(1)
        # 获取纠纷编号
        dispute_id = self.find_element_by_xpath('/html/body/section[2]/div[1]/div/span[2]').text
        return dispute_id


class InputCaseListPage(CaseListBasePage):
    ''''''

    # 案件登记列表-下拉框选择
    case_list_select = '/html/body/div[4]/div[2]/div[1]/div[1]/select'

    def select_status(self, dispute_status=u'全部'):
        '''案件登记列表-状态选择（已提交、未提交）'''
        self._into_input_case_list()
        Select(self.find_element_by_xpath(self.case_list_select)).select_by_visible_text(dispute_status)
        sleep(1)

    def search(self, id_or_name):
        self.select_status()
        self.find_element_by_xpath('//input[@id="searchInput2"]').clear()
        self.find_element_by_xpath('//input[@id="searchInput2"]').send_keys(id_or_name)
        self.find_element_by_xpath('//input[@id="searchInput2"]/following-sibling::span').click()
        sleep(1)

    def dispute_delete(self):
        self.select_status(dispute_status=u"未提交")
        self._dispute_delete()

    def dispute_add_commit(self, desc_ext):
        '''案件登记列表-已提交-增加纠纷-提交
        '''
        self._into_input_case_list()
        self.select_status(dispute_status=u'已提交')
        # self._goto_detail_info()
        self._dispute_add_input(desc_ext)
        self._input_dispute_add_commit()

    def dispute_add_save(self, desc_ext):
        '''案件登记列表-已提交-增加纠纷-保存
        '''
        # 进入纠纷登记列表
        self._into_input_case_list()
        # 选择未提交查询
        self.select_status(dispute_status=u'已提交')
        # 进入纠纷详情
        # self._goto_detail_info()
        # 修改内容
        self._dispute_add_input(desc_ext)
        # 保存
        self._input_dispute_add_save()

    def case_modification_save(self):
        self.select_status(dispute_status=u'已提交')
        self._goto_detail_info()
        self._dispute_modification()

    def _goto_detail_info(self):
        '''纠纷预览'''
        self.find_element_by_xpath('//a[text()="纠纷预览"]').click()
        sleep(1)

    def _dispute_add_input(self, desc_ext):
        self.find_element_by_xpath('//a[text()="增加纠纷"]').click()
        self.find_element_by_xpath('//label[text()="纠纷描述："]/following-sibling::div/div/div/textarea').clear()
        sleep(0.5)
        self.find_element_by_xpath('//label[text()="纠纷描述："]/following-sibling::div/div/div/textarea').send_keys(desc_ext)

    def _input_dispute_add_commit(self):
        '''增加纠纷-提交'''
        # 提交
        commit_btn = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"提交")]')))
        commit_btn.click()
        # self.find_element_by_xpath('//span[contains(text(),"提交")]').click()
        # 不发送
        no_send_btn = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"不发送")]')))
        no_send_btn.click()
        # self.find_element_by_xpath('//span[contains(text(),"不发送")]').click()
        sleep(1)
        # 确定
        self.find_element_by_xpath('//span[contains(text(),"确定")]').click()

    def _input_dispute_add_save(self):
        '''增加纠纷-保存'''
        # 保存
        self.find_element_by_xpath('//span[text()="保存"]').click()
        # 查看案件列表
        self.find_element_by_xpath('//span[contains(text(),"查看案件列表")]').click()

    def _into_input_case_list(self):
        '''进入案件登记列表'''
        self.find_element_by_xpath(self.x_case_input_list_a).click()

    def _dispute_delete(self):
        self.find_element_by_xpath('//a[text()="删除"]').click()
        self.find_element_by_xpath('//a[text()="确定"]').click()
        sleep(0.5)
        self.find_element_by_xpath('//a[text()="确定"]').click()

    def get_search_No(self):
        '''获取第二条'''
        try:
            res = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div/div/div/div[1]/div[1]').text
            no = res.split(u"：")[-1]
        except:
            no = "**None**"
        return no

    def verification_search_No(self, expect):
        try:
            res = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[1]/div[1]').text
            dis_id = res.split(u"：")[-1]
        except:
            dis_id = "**None**"
        print "result: ", dis_id
        print "expect: ", expect
        return dis_id == expect

    def verification_add_save(self, expect):
        # 获取第一行纠纷描述内容
        self.select_status(u"未提交")
        try:
            dis_desc = self.find_element_by_xpath('//label[contains(text(),"纠纷描述")]/following-sibling::p').text
            # dis_desc = res.split("___")[-1]
        except:
            dis_desc = "**None**"
        print "result: ", dis_desc
        print "expect: ", expect
        return dis_desc == expect

    def verification_add_commit(self, expect):
        # 获取第一行纠纷描述内容
        self.select_status(u"已提交")
        try:
            dis_desc = self.find_element_by_xpath('//label[contains(text(),"纠纷描述")]/following-sibling::p').text
            # dis_desc = res.split("___")[-1]
        except:
            dis_desc = "**None**"
        # 打印期望值和测试值
        print "result: ", dis_desc
        print "expect: ", expect
        # 返回 比较结果
        return dis_desc == expect

    def verification_dispute_modification(self):
        '''重写父类方法，案件登记列表验证页面缺少述求'''
        try:
            dispute_type = self.find_element_by_xpath('//label[contains(text(),"纠纷类型")]/following-sibling::p').text
        except:
            dispute_type = "**None**"
        # try:
        #     appeal = self.find_element_by_xpath('//label[text()="申请人诉求"]/following-sibling::p').text
        # except:
        #     appeal = "**None**"
        try:
            dispute_desc = self.find_element_by_xpath('//label[text()="纠纷描述"]/following-sibling::p').text
        except:
            dispute_desc = "**None**"
        # print "result: ", appeal
        # print "expect: ", self.modifcation_dispute_appeal
        print "result: ", dispute_desc
        print "expect: ", self.modifcation_dispute_desc
        print "result: ", dispute_type
        print "expect: ", self.modifcation_dispute_type
        return self.modifcation_dispute_desc == dispute_desc and self.modifcation_dispute_type == dispute_type