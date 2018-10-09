# coding:utf-8
from time import sleep
from odrweb.page.browser import Page
from selenium.webdriver.common.action_chains import ActionChains


class MissionCenter(Page):

    def in_mission_center(self):
        '''进入任务中心'''
        self.find_element_by_xpath('//a[@href="#/missions"]').click()
        sleep(0.5)
        i = self.case_count()
        print("当前页展示" + i + "个纠纷")

    def search_case_by_id_or_name(self, **kwargs):
        '''搜索案件'''
        self.find_element_by_xpath('//input[@id="keyword"]').send_keys(kwargs["编号/姓名/案号"])
        self.find_element_by_xpath('//a[text()="搜索"]').click()
        sleep(1)

    def clear_search_case_area(self):
        '''点击重置纠纷搜索输入框'''
        self.find_element_by_xpath('//a[text()="重置"]').click()

    def case_uptodate_check(self):
        '''临期案件检查'''
        try:
            self.find_element_by_xpath('//input[@class="case-uptoData-check"]').click()
            return True
        except:
            return False

    def case_detail(self, count=None):
        '''纠纷详情'''
        '''count为选入参数，传值可以控制操作当前页面第N个纠纷，默认为第一个'''
        if count is None:
            count = 1

        j = int(count) - 1   # 数组下标处理
        print("查看第"+ str(count) +"个纠纷的详情")
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
        '''调解进程'''
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

    def case_type(self, ctype=None):
        '''调解类型'''
        try:
            if ctype is None:
                casetype = u"所有类型"
            else:
                casetype = ctype

            casetypelist = {
                    u"所有类型",
                    u"婚姻继承",
                    u"消费维权",
                    u"劳动争议",
                    u"借贷纠纷",
                    u"物业纠纷",
                    u"相邻关系",
                    u"知识产权",
                    u"房屋买卖",
                    u"房屋租赁"
            }

            if casetype in casetypelist:
                pass
            else:
                self.find_element_by_xpath('//em[text()="更多"]').click()

            self.find_element_by_xpath("//li[contains(text(),'" + casetype + "')]").click()
            return True
        except:
            return False

    def case_status(self, cstatus=None):
        '''调解状态'''
        try:
            if cstatus is None:
                casestatus = u"所有状态"
            else:
                casestatus = cstatus

            self.find_element_by_xpath("//li[contains(text(),'" + casestatus + "')]").click()
            return True
        except:
            return False

    def case_time(self, ctime=None, startTime=None, endTime=None):
        '''登记时间'''
        try:
            if ctime is None:
                casetime = u"所有时间"
            else:
                casetime = ctime

            self.find_element_by_xpath("//li[contains(text(),'" + casetime + "')]").click()

            if ctime == u"自定义时间":
                # 如传入自定义时间 需要追加两位参数起始时间，格式YYYY-MM-DD
                self.find_element_by_xpath('//input[@id="startTime"]').click()
                self.find_element_by_xpath('//input[@id="startTime"]').send_keys(startTime)
                self.find_element_by_xpath('//input[@id="endTime"]').click()
                self.find_element_by_xpath('//input[@id="endTime"]').send_keys(endTime)
                self.find_element_by_xpath('//span[text()="登记时间"]/..//input[@value="确定"]').click()
                return True
        except:
            return False

    def get_total_case_num(self):
        total = self.find_element_by_xpath('//span[text()="案件数量"]/..//i[@class="ng-binding"]').text
        return total


    def case_count(self):
        '''统计当前页有多少纠纷'''
        i = self.find_elements_by_xpath('//div[@class="case-number ng-binding"]')
        j = str(len(i))
        return j

    def click_batch_process(self):
        '''批量受理第一页的案件'''
        self.find_element_by_xpath('//button[@class="confirm_cam"]').click()










