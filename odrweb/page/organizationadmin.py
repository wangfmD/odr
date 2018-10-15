# coding:utf-8
from time import sleep
from odrweb.page.browser import Page
from selenium.webdriver.common.action_chains import ActionChains
from utils.tools import DbConn


class MissionCenter(Page):

    def in_mission_center(self):
        """进入任务中心"""
        self.find_element_by_xpath('//a[@href="#/missions"]').click()
        sleep(0.5)
        i = self.case_count()
        print("当前页展示" + i + "个纠纷")

    def search_case_by_id_or_name(self, **kwargs):
        """搜索案件"""
        self.find_element_by_xpath('//input[@id="keyword"]').send_keys(kwargs["编号/姓名/案号"])
        self.find_element_by_xpath('//a[text()="搜索"]').click()
        sleep(1)

    def clear_search_case_area(self):
        """点击重置纠纷搜索输入框"""
        self.find_element_by_xpath('//a[text()="重置"]').click()

    def case_uptodate_check(self):
        """临期案件检查"""
        try:
            self.find_element_by_xpath('//input[@class="case-uptoData-check"]').click()
            return True
        except:
            return False

    def case_detail(self, count=None):
        """纠纷详情"""
        """count为选入参数，传值可以控制操作当前页面第N个纠纷，默认为第一个"""
        if count is None:
            count = 1

        j = int(count) - 1   # 数组下标处理
        print("查看第"+ str(count) +"个纠纷的详情")
        k = self.find_elements_by_xpath('//div[@class="details ng-scope"]/div/div/button[@ng-click="detailsDispute(one)"]')
        k[j].click()
        sleep(1)
        try:
            self.driver.switch_to_window(self.driver.window_handles[1])  # 切换到详情窗口
            return True
        except:
            return False




    def case_acceptance(self, count=None):
        """受理"""
        """count为选入参数，传值可以控制操作当前页面第N个纠纷，默认为第一个"""
        if count is None:
            count = 1

        j = int(count) - 1   # 数组下标处理
        print("受理第"+str(count)+"个纠纷")
        k = self.find_elements_by_xpath('//div[@class="details ng-scope"]/div/div/button[@ng-click="acceptance($index)"]')
        k[j].click()

    def case_refuse(self, count=None):
        """不受理"""
        """count为选入参数，传值可以控制操作当前页面第N个纠纷，默认为第一个"""
        if count is None:
            count = 1

        j = int(count) - 1   # 数组下标处理
        print("拒绝受理第"+str(count)+"个纠纷")
        k = self.find_elements_by_xpath('//div[@class="details ng-scope"]/div/div/button[@ng-click="refuse_Acceptance_LawCase($index)"]')
        k[j].click()

    def case_select_mediator(self, count=None):
        """分配调解员/重新分配"""
        """count为选入参数，传值可以控制操作当前页面第N个纠纷，默认为第一个"""
        if count is None:
            count = 1


        j = int(count) - 1   # 数组下标处理
        print("给第"+str(count)+"个纠纷分配调解员")
        k = self.driver.find_elements_by_xpath('//div[@class="details ng-scope"]/div/div/button[@ng-click="selMediator($index)"]')
        sleep(1)
        ActionChains(self.driver).move_to_element(k[j]).click(k[j]).perform()
        #k[j].click()

    def case_change_organization(self, count=None):
        """转移调解机构"""
        """count为选入参数，传值可以控制操作当前页面第N个纠纷，默认为第一个"""
        if count is None:
            count = 1

        j = int(count) - 1   # 数组下标处理
        print("给第"+str(count)+"个纠纷转移调解机构")
        k = self.find_elements_by_xpath('//div[@class="details ng-scope"]/div/div/button[@ng-click="changeOrg(one.caseNo,one.orgName)"]')
        k[j].click()

    def input_change_reason(self, reason_):
        """输入转移机构理由"""
        self.find_element_by_xpath('//div[@class="toReason_div"]/textarea').send_keys(reason_)

    def choose_change_organization(self, name_):
        """选择转移机构"""
        k = self.find_element_by_xpath('//input[@data-ng-model="orn.name"]').text
        if k != "":
            self.find_element_by_xpath('//input[@data-ng-model="orn.name"]').clear()
        self.find_element_by_xpath('//input[@data-ng-model="orn.name"]').send_keys(name_)
        self.find_element_by_xpath('//h4[text()="调解机构筛选"]/..//button[text()="搜索"]').click()
        self.find_element_by_xpath('//button[text()="转出"]').click()
        self.find_element_by_xpath('//div[text()="温馨提示"]/..//a[text()="确认"]').click()  #温馨提示-确认
        sleep(2)

    def verfc_change_organization(self, casenumber):
        """调解机构转移校验"""
        connect = DbConn()
        sql = "SELECT ORGANIZATION_ID FROM `LAW_CASE`WHERE CASE_NO='" + casenumber + "'"
        result = connect.execQury(sql)
        ogr_id = str(result[0]["ORGANIZATION_ID"])
        if ogr_id != "3300000000000005":
            return True
        else:
            return False


    def case_progress(self, count=None):
        try:
            """调解进程"""
            """count为选入参数，传值可以控制操作当前页面第N个纠纷，默认为第一个"""
            if count is None:
                count = 1

            j = int(count) - 1   # 数组下标处理
            print("查看第"+str(count)+"个纠纷调解进度")
            k = self.find_elements_by_xpath('//div[@class="details ng-scope"]/div/div/button[@ng-click="progress(one.id,one.statusName)"]')
            k[j].click()
            return True
        except:
            return False

    def tip_agree(self):
        """重要提示-确定"""
        self.find_element_by_xpath('//div[text()="重要提示"]/../div/a[text()="确定"]').click()

    def info_agree(self):
        """信息-确定"""
        self.find_element_by_xpath('//div[text()="信息"]/../div/a[text()="确定"]').click()

    def case_mediator_choose(self, **kwargs):
        """案件分配调解员选择,需要传调解员姓名"""
        k = self.find_element_by_xpath('//h4[text()="选择调解员"]/../div/div[@class="search-counselor"]/input').text
        if k != "":
            self.find_element_by_xpath('//h4[text()="选择调解员"]/../div/div[@class="search-counselor"]/input').clear()
        self.find_element_by_xpath('//h4[text()="选择调解员"]/../div/div[@class="search-counselor"]/input').send_keys(kwargs["分配调解员姓名"])
        self.find_element_by_xpath('//h4[text()="选择调解员"]/../div/div[@class="search-counselor"]/button').click()
        self.find_element_by_xpath('//span[text()="'+kwargs["分配调解员姓名"]+'"]/../../../div/button').click()
        self.info_agree()

    def case_type(self, ctype=None):
        """调解类型"""
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
        """调解状态"""
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
        """登记时间"""
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
        print("案件计数："+ total)
        return total


    def case_count(self):
        """统计当前页有多少纠纷"""
        i = self.find_elements_by_xpath('//div[@class="case-number ng-binding"]')
        j = str(len(i))
        return j

    def click_batch_process(self):
        """批量受理案件按钮"""
        try:
            self.find_element_by_xpath('//button[@class="confirm_cam"]').click()
            return True
        except:
            return False

    def click_refuse_type(self, type_=None):
        """拒绝原因"""
        if type_ is None:
            refusetype = u"非本机构管辖"
        else:
            refusetype = type_

        self.find_element_by_xpath('//span[text()="原因"]/../ul/li[text()="' + refusetype + '"]').click()

    def input_refuse_detail(self, detail_):
        """填写拒绝理由"""
        self.find_element_by_xpath('//div[@class="box-textarea"]/textarea').send_keys(detail_)

    def click_commit_refuse(self):
        """确认拒绝"""
        self.find_element_by_xpath('//div[@class="btn-box"]/input[@value="确定"]').click()



    def verfc_total_case_number_visitable(self,totalnumber):
        """案件总量是否数字"""
        try:
            check = int(totalnumber)
            return True
        except:
            return False

    def verfc_case_search_successful(self, totalnumber):
        """搜索结果是否唯一"""
        try:
            check1 = int(totalnumber)
            check2 = int(self.case_count())
            if check1 == 1 and check2 == 1:
                return True
            else:
                return False
        except:
            return False

    def verfc_case_search_clear_successful(self, totalnumber1_, totalnumber2_, totalnumber3_):
        """搜索结果重置校验"""
        try:
            check = int(totalnumber2_)
            if check == 1 and totalnumber1_ == totalnumber3_:
                return True
            else:
                return False
        except:
            return False

    def get_an_unaccept_case(self):
        """获取一个未受理纠纷编号（status=20）"""
        status = "20"  # 未受理纠纷状态枚举值
        ORGANIZATION_ID = "3300000000000005"  # 北明测试机构
        connect = DbConn()
        sql = "SELECT CASE_NO FROM `LAW_CASE`WHERE status='" + status + "' and ORGANIZATION_ID='" + ORGANIZATION_ID + "' order by CREATE_DATE desc"
        result = connect.execQury(sql)
        casenumber = result[0]["CASE_NO"]
        print("获取的纠纷编号为：" + casenumber)
        return casenumber

    def verfc_case_acceptable(self, casenumber):
        """断言：案件状态是否为已受理（status=06）"""
        connect = DbConn()
        sql = "SELECT status FROM `LAW_CASE`WHERE CASE_NO='" + casenumber + "'"
        result = connect.execQury(sql)
        status = str(result[0]["status"])
        if status == "06":
            return True
        else:
            return False

    def verfc_case_unacceptable(self, casenumber):
        """断言：案件状态是否为不受理（status=05）"""
        connect = DbConn()
        sql = "SELECT status FROM `LAW_CASE`WHERE CASE_NO='" + casenumber + "'"
        result = connect.execQury(sql)
        status = str(result[0]["status"])
        print(status)
        if status == "05":
            return True
        else:
            return False

    def verfc_case_assignable(self, casenumber):
        """断言：案件状态是否为已分配（status=21）"""
        connect = DbConn()
        sql = "SELECT status FROM `LAW_CASE`WHERE CASE_NO='" + casenumber + "'"
        result = connect.execQury(sql)
        status = result[0]["status"]
        if status == "21":
            return True
        else:
            return False












