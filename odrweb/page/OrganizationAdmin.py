# coding:utf-8
from time import sleep
from odrweb.page.browser import Page
from selenium.webdriver.common.action_chains import ActionChains


class OrganizationAdmin(Page):

    def in_mission_center(self):
        '''进入任务中心'''
        self.find_element_by_xpath('//a[@href="#/missions"]').click()
        sleep(0.5)
        i = self._case_count()
        print("当前页展示" + i + "个纠纷")


    def search_case_by_id_or_name(self, **kwargs):
        '''搜索案件'''
        self.find_element_by_xpath('//input[@id="keyword"]').send_keys(kwargs["编号/姓名/案号"])
        self.find_element_by_xpath('//a[text()="搜索"]').click()
        sleep(1)

    def clear_search_case_area(self):
        '''点击重置纠纷搜索输入框'''
        self.find_element_by_xpath('//a[text()="重置"]').click()



    def case_detail(self, count=None):
        '''纠纷详情'''
        '''count为选入参数，传值可以控制操作当前页面第N个纠纷，默认为第一个'''
        if count is None:
            count = 1

        j = int(count) - 1   # 数组下标处理
        print("查看第"+str(count)+"个纠纷的详情")
        k = self.find_elements_by_xpath('//div[@class="details ng-scope"]/div/div/button[@ng-click="detailsDispute(one)"]')
        k[j].click()
        sleep(1)
        self.driver.switch_to_window(self.driver.window_handles[1])  # 切换到详情窗口

    def case_acceptance(self, count=None):
        '''受理'''
        '''count为选入参数，传值可以控制操作当前页面第N个纠纷，默认为第一个'''
        if count is None:
            count = 1

        j = int(count) - 1   # 数组下标处理
        print("受理第"+str(count)+"个纠纷")
        k = self.find_elements_by_xpath('//div[@class="details ng-scope"]/div/div/button[@ng-click="acceptance($index)"]')
        k[j].click()

    def case_refuse(self, count=None):
        '''不受理'''
        '''count为选入参数，传值可以控制操作当前页面第N个纠纷，默认为第一个'''
        if count is None:
            count = 1

        j = int(count) - 1   # 数组下标处理
        print("拒绝受理第"+str(count)+"个纠纷")
        k = self.find_elements_by_xpath('//div[@class="details ng-scope"]/div/div/button[@ng-click="refuse_Acceptance_LawCase($index)"]')
        k[j].click()

    def case_select_mediator(self, count=None):
        '''分配调解员/重新分配'''
        '''count为选入参数，传值可以控制操作当前页面第N个纠纷，默认为第一个'''
        if count is None:
            count = 1


        j = int(count) - 1   # 数组下标处理
        print("给第"+str(count)+"个纠纷分配调解员")
        k = self.driver.find_elements_by_xpath('//div[@class="details ng-scope"]/div/div/button[@ng-click="selMediator($index)"]')
        sleep(1)
        ActionChains(self.driver).move_to_element(k[j]).click(k[j]).perform()
        #k[j].click()




    def case_change_organization(self, count=None):
        '''转移调解机构'''
        '''count为选入参数，传值可以控制操作当前页面第N个纠纷，默认为第一个'''
        if count is None:
            count = 1

        j = int(count) - 1   # 数组下标处理
        print("给第"+str(count)+"个纠纷转移调解机构")
        k = self.find_elements_by_xpath('//div[@class="details ng-scope"]/div/div/button[@ng-click="changeOrg(one.caseNo,one.orgName)"]')
        k[j].click()

    def case_progress(self, count=None):
        '''转移调解机构'''
        '''count为选入参数，传值可以控制操作当前页面第N个纠纷，默认为第一个'''
        if count is None:
            count = 1

        j = int(count) - 1   # 数组下标处理
        print("查看第"+str(count)+"个纠纷调解进度")
        k = self.find_elements_by_xpath('//div[@class="details ng-scope"]/div/div/button[@ng-click="progress(one.id,one.statusName)"]')
        k[j].click()

    def tip_agree(self):
        '''重要提示-确定'''
        self.find_element_by_xpath('//div[text()="重要提示"]/../div/a[text()="确定"]').click()

    def info_agree(self):
        '''信息-确定'''
        self.find_element_by_xpath('//div[text()="信息"]/../div/a[text()="确定"]').click()

    def case_mediator_choose(self, **kwargs):
        '''案件分配调解员选择,需要传调解员姓名'''
        k = self.find_element_by_xpath('//h4[text()="选择调解员"]/../div/div[@class="search-counselor"]/input').text
        if k != "":
            self.find_element_by_xpath('//h4[text()="选择调解员"]/../div/div[@class="search-counselor"]/input').clear()
        self.find_element_by_xpath('//h4[text()="选择调解员"]/../div/div[@class="search-counselor"]/input').send_keys(kwargs["分配调解员姓名"])
        self.find_element_by_xpath('//h4[text()="选择调解员"]/../div/div[@class="search-counselor"]/button').click()
        self.find_element_by_xpath('//span[text()="'+kwargs["分配调解员姓名"]+'"]/../../../div/button').click()
        self.info_agree()







    def _case_count(self):
        '''统计当前页有多少纠纷'''
        i = self.find_elements_by_xpath('//div[@class="case-number ng-binding"]')
        j = str(len(i))
        return j

    def _click_batch_process(self):
        '''点击批量受理'''
        self.find_element_by_xpath('//button[@class="confirm_cam"]').click()









