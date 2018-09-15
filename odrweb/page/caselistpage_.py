# -*- coding:utf-8 -*-
from selenium.webdriver.support.select import Select

from odrweb.page.browser import Page

class CaseListPage(Page):

    def _goto_detail_info(self,dispute_status=u'等待调解'):
        Select(self.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[4]/select')).select_by_visible_text(dispute_status)
        # self.find_element_by_xpath('/html/body/div[4]/div[1]/button[1]').click()
        self.find_element_by_xpath('//a[contains(text(),"纠纷详情")]').click()
        # 获取纠纷编号
        dispute_id = self.find_element_by_xpath('/html/body/section[2]/div[1]/div/span[2]').text

    def _make_mediate(self):
        '''预约调解'''
        self.find_element_by_xpath('//button[contains(text()," 预约调解")]').click()

    def _mediate_success(self):
        '''调解成功'''
        self.find_element_by_xpath('//button[contains(text()," 调解成功")]').click()
        self.find_element_by_xpath('//div[@id="reAllotSuc"]/div/div[3]/div/textarea').send_keys(u'已确认')
        self.find_element_by_xpath('//div[@id="reAllotSuc"]/div/div[4]/input').click()  # 确认
        self.find_element_by_xpath('//div[@id="toLawConfirm"]/div/div[1]/div').click()

        try:
            dispute_status = self.find_element_by_xpath('/html/body/section[1]/div[2]/i').text
        except:
            dispute_status = "**Nome**"
        self.find_element_by_xpath('//button[contains(text(),"返回列表")]').click()

        return dispute_status


    def _mediate_failed(self):
        '''预约调解'''
        self.find_element_by_xpath('//button[contains(text()," 预约调解")]').click()
        # 调解名称input
        self.find_element_by_xpath('//div[@id="newMeeting"]/div/div[2]/div[1]/ul/li/input').send_keys('111')
        # 时间框
        self.find_element_by_xpath('//li[@id="dataParent"]/input').click()
        # 时间框确定
        self.driver.switch_to.frame(self.find_element_by_xpath('//li[@id="dataParent"]/div/iframe'))        # 切换iframe
        self.driver.find_element_by_xpath('//input[@id="dpOkInput"]').click()
        self.driver.switch_to.default_content()                                                             # 从iframe返回
        #
        Select(self.find_element_by_xpath('//div[@id="newMeeting"]/div/div[2]/div[10]/ul/li[1]/select')).select_by_visible_text('0')
        Select(self.find_element_by_xpath('//div[@id="newMeeting"]/div/div[2]/div[10]/ul/li[2]/select')).select_by_visible_text('10')

        # 备注
        self.find_element_by_xpath('//div[@id="newMeeting"]/div/div[2]/div[11]/ul/li/textarea').send_keys('comment')
        self.find_element_by_xpath('//input[@value="预约"]').click()

    def _mediate_stop(self):
        '''调解终止'''
        self.find_element_by_xpath('//button[contains(text(),"调解终止")]').click()

    def _mediate_revocation(self):
        '''工作台'''
        self.find_element_by_xpath('//button[contains(text(),"调解撤回")]').click()

    def _workstaion(self):
        '''调解撤回'''
        self.find_element_by_xpath('//button[contains(text(),"工作台")]').click()

    def _redistribution(self):
        '''重新分配'''
        self.find_element_by_xpath('//button[contains(text(),"重新分配")]').click()

    def verification_dispute_status(self, expect,result):
        '''
        调解成功
        :return:
        '''
        return expect == result