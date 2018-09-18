# -*- coding:utf-8 -*-
from time import sleep

from selenium.webdriver.support.select import Select

from odrweb.page.browser import Page


class CaseListPage(Page):

    case_list_select = '/html/body/div[4]/div[2]/div[1]/div[4]/select'
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
        self.find_element_by_xpath('//input[@id="searchInput1"]').send_keys(target)
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[6]/div/span/span').click()

    def _get_search(self, type_="No"):
        if type == "No":
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
        try:
            # dispute_status = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[3]/div[1]/div[4]/p').text
            #调解失败和调解终止
            # dispute_status = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[3]/div[1]/div[4]/p').text
            dispute_status=self.find_element_by_xpath('//label[text()="纠纷进度"]/following-sibling::p').text

        except:
            dispute_status = "**None**"
        print "result: ", dispute_status
        print "expect: ", expect
        return dispute_status == expect

    def _goto_detail_info(self, dispute_status=u'等待调解'):
        Select(self.find_element_by_xpath(self.case_list_select)).select_by_visible_text(dispute_status)
        sleep(0.5)
        # self.find_element_by_xpath('/html/body/div[4]/div[1]/button[1]').click()
        self.find_element_by_xpath('//a[contains(text(),"纠纷详情")]').click()
        sleep(1)
        # 获取纠纷编号
        dispute_id = self.find_element_by_xpath('/html/body/section[2]/div[1]/div/span[2]').text
        return dispute_id

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
        self.find_element_by_xpath('//div[@id="toLawConfirm"]/div/div[1]/div').click()

    def get_detail_dispute_status(self):
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
        self.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        sleep(0.5)
        try:
            self.find_element_by_xpath('//li[contains(text(),"当事人达成和解")]').click()
        except:
            sleep(0.5)
            self.find_element_by_xpath('//li[contains(text(),"当事人达成和解")]').click()

        self.find_element_by_xpath('//li[contains(text(), "其他")]').click()
        self.find_element_by_xpath('//li[contains(text(), "被申请人拒绝调解")]').click()
        self.find_element_by_xpath('//span[text()="详细原因"]').parent.find_element_by_xpath('//div/textarea').send_keys(u'详细原因')
        # 确定
        self.find_element_by_xpath('//*[@id="myModal55"]/div/div[4]/input').click()

    def _mediate_revocation(self):
        '''调解撤回'''
        self.find_element_by_xpath('//span[contains(text(),"调解撤回")]').click()
        sleep(0.5)
        self.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        self.find_element_by_xpath('//li[contains(text(),"其他")]').click()
        self.find_element_by_xpath('//li[contains(text(),"申请人撤回调解")]').click()
        self.find_element_by_xpath('//span[text()="详细原因"]').parent.find_element_by_xpath('//div/textarea').send_keys(u'详细原因')
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

    def verification_dispute_status(self, result, expect):
        '''
        调解成功
        :return:
        '''
        print "result: ", result
        print "expect: ", expect
        return expect == result
