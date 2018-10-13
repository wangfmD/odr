# -*- coding:utf-8 -*-

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from odrweb.page.browser import Page


class JudgePage(Page):
    """办案法官页面
    """
    x_search_select = '//select'
    x_search_input = '//input[@placeholder="请输入编号/案号"]'
    x_search_btn = '//input[@placeholder="请输入编号/案号"]/following-sibling::span'
    x_case_detail_btn = '//a[text()="案件详情"]'
    x_case_detail_back = '//button[text()="返回列表"]'
    x_case_schedule_btn = '//a[text()="案件进度"]'
    x_account_info_link = '//a[contains(text(), "账号：")]'                 # 账号链接
    x_account_info_whcd_input = '//div[text()="文化程度："]/../div[2]/div/input'  # 个人详情页面-文化程度输入框
    x_account_save_btn = '//span[contains(text(), "保 存")]'                # 个人信息-保存

    def act_search_select(self, text):
        """选择查询
            待确认
            确认有效
            驳回申请
        """
        Select(self.find_element_by_xpath(self.x_search_select)).select_by_visible_text(text)
        sleep(0.5)

    def verfc_act_search_select(self, text):
        """验证选择查询
        查询列表第一行的案件状态
        """
        try:
            case_status = self.find_element_by_xpath('//div[text()="案件状态"]/following-sibling::div').text
        except:
            case_status ='**None**'
        print "result: ",case_status
        print "expect: ", text
        return case_status == text


    def act_seacrh_input(self, search_ctx):
        """输入查询
        """
        self.find_element_by_xpath(self.x_search_input).clear()
        self.find_element_by_xpath(self.x_search_input).send_keys(search_ctx)
        self.find_element_by_xpath(self.x_search_btn).click()
        sleep(0.5)

    def verfc_act_seacrh_input(self, id):
        """验证输入查询
        查询列表第一行的案件状态
        """
        try:
            res = self.find_element_by_xpath('//div[contains(text(), "案件编号：")]').text
            _, case_id = res.split(u'：')
        except:
            case_id ='**None**'
        print "result: ",case_id
        print "expect: ", id
        return case_id == id

    def act_goto_case_detail(self):
        """进入案件详情
        """
        self.find_element_by_xpath(self.x_case_detail_btn).click()

    def act_goto_case_detail_back(self):
        """案件详情页面放回列表
        """
        self.find_element_by_xpath(self.x_case_detail_btn).click()
        self.find_element_by_xpath(self.x_case_detail_back).click()

    def act_account_save(self):
        """个人信息修改保存"""
        self.find_element_by_xpath(self.x_account_info_link).click()
        self.find_element_by_xpath(self.x_account_info_whcd_input).clear()
        self.find_element_by_xpath(self.x_account_info_whcd_input).send_keys(u"大学")

    def _get_case_id(self):
        """获取案件编号
        """
        try:
            res = self.find_element_by_xpath('(//div[contains(text(),"案件编号：")])[2]').text
            _,id_ = res.split(u'：')
        except:
            id_ = ""
        return id_