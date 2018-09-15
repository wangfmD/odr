# -*- coding:utf-8 -*-
from selenium.webdriver.support.select import Select

from odrweb.page.browser import Page

class CaseListPage(Page):

    def _goto_detail_info(self):
        self.find_element_by_xpath('/html/body/div[4]/div[1]/button[1]').click()
        Select(self.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[4]/select')).select_by_visible_text(u'等待调解')


    def _make_mediate(self):
        '''预约调解'''
        self.find_element_by_xpath('//button[contains(text()," 预约调解")]').click()

    def _mediate_success(self):
        '''调解成功'''
        self.find_element_by_xpath('//button[contains(text()," 调解成功")]').click()
        self.find_element_by_xpath('//div[@id="reAllotSuc"]/div/div[3]/div/textarea').send_keys('fasfas')

    def _mediate_failed(self):
        '''预约调解'''
        self.find_element_by_xpath('//button[contains(text()," 预约调解")]').click()

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