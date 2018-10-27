# coding:utf-8

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from odrweb.page.browser import Page


class AdminOrgan(Page):
    """行政机构帐号登陆
    """
    # 选择除响应期2天外
    x_choose_unresponsive_case = '//small[text()="（除响应期2天外）"]'
    # 进入案件记录列表页面
    x_form_record = '//a[contains(text()," 案件记录")]'
    # 案件列表进入司法确认
    x_form_record_judicial = '//a[contains(text(),"司法确认")]'
    # 司法确认登记时间选择所有时间
    x_form_record_judicial_alltime = '//li[contains(text(),"所有时间")]'

    def change_windows(self):
        """切换窗口
        """
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[1])

    def homepage_dispute(self):
        """纠纷总量获取
        """
        # 获取纠纷总量
        dispute = self.find_element_by_xpath('//div[@class="home-tops ng-scope"]/div[@class="top top1"]/span').text
        return dispute

    def homepage_consult(self):
        """咨询获取
        """
        # 获取咨询数量
        consut = self.find_element_by_xpath('//div[@class="home-tops ng-scope"]//div[@class="top top1"]').text
        return consut

    def homepage_mediation(self):
        """调解获取
        """
        # 获取调解数量
        mediation = self.find_element_by_xpath('//div[@class="home-tops ng-scope"]//div[@class="top top4"]/span').text
        return mediation

    def homepage_add_consultant(self):
        """咨询师数量总和
        """
        # 获取心理评估咨询师数量
        cons_1 = self.find_element_by_xpath('//div[@class="white-right"]/div/span').text
        # 获取法律服务咨询师数量
        cons_2 = self.find_element_by_xpath('//div[@class="white-right"]/div[2]/span').text
        # 获取咨询师数量总和
        cons_all = self.find_element_by_xpath('//div[@class="home-blue-right"][2]/span').text
        return cons_1, cons_2, cons_all

    def verification_homepage_add_consultant(self, cons_1, cons_2, cons_all):
        """咨询师数量总和校验
        """
        print u"心理评估咨询师: ", cons_1
        print u"法律服务咨询师: ", cons_2
        print u"咨询师总数: ", cons_all
        cons = int(cons_1) + int(cons_2)
        res = cons == int(cons_all)
        return res

    def _admin_center(self):
        """管理中心主页
        """
        # 首页点击管理中心进入
        self.find_element_by_xpath('//a[contains(text(),"管理中心")]').click()
        sleep(1)

    def admin_center_organ(self):
        """管理中心-机构
        """
        self._admin_center()
        # 获取第一个法院名称并点击
        organ = self.find_element_by_xpath('//td[text()="负责人"]/../../tr[2]/td[1]/a').text
        self.find_element_by_xpath('//td[text()="负责人"]/../../tr[2]/td[1]/a').click()
        sleep(1)
        return organ

    def verification_admin_center_organ(self, organ):
        """验证-管理中心-机构
        """
        try:
            organ_in = self.find_element_by_xpath('//label[text()="机构名称："]/../span').text
        except:
            organ_in = "*None*"
        print "result: ", organ_in
        print "except: ", organ
        res = organ_in == organ
        return res

    def admin_center_person(self):
        """管理中心-人员
        """
        self._admin_center()
        # 点击人员按钮
        self.find_element_by_xpath('//button[contains(text(),"人员")]').click()
        # 获取第一个姓名并点击
        per = self.find_element_by_xpath('//th[text()="姓名"]/../../tr[2]/td/a').text
        self.find_element_by_xpath('//th[text()="姓名"]/../../tr[2]/td/a').click()
        sleep(1)
        return per

    def verification_admin_center_person(self, per):
        """验证-管理中心-人员
        """
        try:
            per_in = self.find_element_by_xpath('//span[text()="法院"]/../span[1]').text
        except:
            per_in = "*None*"
        print "result: ", per_in
        print "except: ", per
        res = per_in == per
        return res

    def admin_center_page(self):
        """管理中心-翻页
        """
        self._admin_center()
        # 点击下一页
        self.find_element_by_xpath('//button[text()="下一页"][1]').click()

    def verification_admin_center_page(self):
        """验证-管理中心-翻页
        """
        try:
            page = self.find_element_by_xpath('//div[contains(text(),"当前页")][1]').text
        except:
            page = "*None*"
        print "result: ", page
        print "except: ", u"当前页：2"
        res = page == u"当前页：2"
        return res

    def form_map(self):
        """统计报表-平台地图
        """
        # 点击统计报表
        self.find_element_by_xpath('//a[contains(text(),"统计报表")]').click()
        sleep(1)

    def verification_form_map(self):
        """验证-统计报表-平台地图
        """
        try:
            map_1 = self.find_element_by_xpath('//div[@class="choice"]/span[text()="浙江省"]').text
        except:
            map_1 = "*None*"
        print "result: ", map_1
        print "except: ", u"浙江省"
        res = map_1 == u"浙江省"
        return res

    def form_map_date(self):
        """统计报表-平台地图-日期筛选
        """
        self.form_map()
        # 点击第一个日期输入框
        # self.find_element_by_xpath('//div[@class="ng-hide"]/../input[1]').click()
        # 输入日期，选择日期输入框第一个
        # self.find_element_by_xpath('//tr[@class="MTitle"]/../tr[2]/td[1]').click()
        # 点击查询按钮
        sleep(1)
        sel_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="ng-hide"]/../button[text()="查询"]')))
        sel_btn.click()
        # self.find_element_by_xpath('//div[@class="ng-hide"]/../button[text()="查询"]').click()
        # 输出该段时间平台访问量数量
        print self.find_element_by_xpath('//div[text()="浙江省 (平台总访问量："]/span').text

    def form_business(self):
        """统计报表-业务报表
        """
        self.form_map()
        # 点击业务报表
        sleep(1)
        form_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//li[text()="业务报表"]')))
        form_btn.click()
        # self.find_element_by_xpath('//li[text()="业务报表"]').click()

    def verification_form_business(self):
        """验证-统计报表-业务报表
        """
        try:
            business = self.find_element_by_xpath('//div[text()="浙江省"]').text
        except:
            business = "*None*"
        print "result: ", business
        print "except: ", u"浙江省"
        res = business == u"浙江省"
        return res

    def form_business_area(self):
        """统计报表-业务报表-地区筛选
        """
        self.form_business()
        # 选择地区为杭州市
        self.find_element_by_xpath('//div[text()="浙江省"]/../div[2]/select').click()
        self.find_element_by_xpath('//option[text()="杭州市"]').click()
        # 点击查询按钮
        self.find_element_by_xpath('//span[text()="查询"]/..').click()
        # 点击导出按钮
        self.find_element_by_xpath('//span[text()="导出"]/..').click()
        # 输出在线调解案件数
        case = self.find_element_by_xpath('//div[text()="在线调处案件数"]/../div[2]').text
        print u"在线调解案件数: ", case

    def form_unresponsive(self):
        """统计报表-未响应案件统计
        """
        self.form_map()
        sleep(1)
        # 点击未响应案件统计
        no_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//li[text()="未响应案件统计"]')))
        no_btn.click()
        # self.find_element_by_xpath('//li[text()="未响应案件统计"]').click()

    def verification_form_unresponsive(self):
        """验证-统计报表-未响应案件统计
        """
        try:
            resp = self.find_element_by_xpath(self.x_choose_unresponsive_case).text
        except:
            resp = "*None*"
        print "result: ", resp
        print "except: ", u"（除响应期2天外）"
        res = resp == u"（除响应期2天外）"
        return res

    def form_unresponsive_seven(self):
        """统计报表-未响应案件统计-1~7天未响应
        """
        self.form_unresponsive()
        # 输出未响应案件数
        case = self.find_element_by_xpath(self.x_choose_unresponsive_case + '/../span').text
        print u"1-7天未响应合计: ", case

    def form_unresponsive_fifteen(self):
        """统计报表-未响应案件统计-8~15天未响应
        """
        self.form_unresponsive()
        # 选择8~15天未响应案件
        self.find_element_by_xpath(self.x_choose_unresponsive_case + '/../../div/div/label[2]/span').click()
        sleep(0.5)
        # 输出未响应案件数
        case = self.find_element_by_xpath(self.x_choose_unresponsive_case + '/../span').text
        print u"8-15天未响应合计: ", case

    def form_unresponsive_thirty(self):
        """统计报表-未响应案件统计-16~30天未响应
        """
        self.form_unresponsive()
        # 选择16~30天未响应案件
        self.find_element_by_xpath(self.x_choose_unresponsive_case + '/../../div/div/label[3]/span').click()
        sleep(0.5)
        # 输出未响应案件数
        case = self.find_element_by_xpath(self.x_choose_unresponsive_case + '/../span').text
        print u"16-30天未响应合计: ", case

    def form_unresponsive_more(self):
        """统计报表-未响应案件统计-超过30天未响应
        """
        self.form_unresponsive()
        # 选择超过30天未响应案件
        self.find_element_by_xpath(self.x_choose_unresponsive_case + '/../../div/div/label[4]/span').click()
        sleep(0.5)
        # 输出未响应案件数
        case = self.find_element_by_xpath(self.x_choose_unresponsive_case + '/../span').text
        print u"超过30天未响应合计: ", case

    def form_unresponsive_page(self):
        """统计报表-未响应案件统计-结果翻页
        """
        self.form_unresponsive_more()
        sleep(0.5)
        # 点击翻到第二页页面
        self.find_element_by_xpath('//span[text()="2"]').click()

    def verification_form_unresponsive_page(self):
        """验证-统计报表-未响应案件统计-结果翻页
        """
        sleep(0.5)
        try:
            page = self.find_element_by_xpath('//th[text()="序号"]/../../../tbody/tr[1]/td').text
        except:
            page = "*None*"
        print "result: ", page
        print "except: ", "11"
        res = page == "11"
        return res

    def form_casetype(self):
        """统计报表-案件类型对应表
        """
        self.form_map()
        # 点击进入案件类型对应表
        sleep(0.5)
        self.find_element_by_xpath('//li[text()="案件类型对应表"]').click()

    def verification_form_casetype(self):
        """验证-统计报表-案件类型对应表
        """
        try:
            case = self.find_element_by_xpath('//span[text()="浙江省各区域纠纷类型统计"]').text
        except:
            case = "*None*"
        print "result: ", case
        print "except: ", u"浙江省各区域纠纷类型统计"
        res = case == u"浙江省各区域纠纷类型统计"
        return res

    def form_casetype_date(self):
        """统计报表-案件类型对应表-日期筛选
        """
        self.form_casetype()
        # 点击查询按钮
        self.find_element_by_xpath('//input[@id="endTimeRep"]/../button').click()
        print u"点击查询成功"

    def form_casetype_excel(self):
        """统计报表-案件类型对应表-导出Excel
        """
        self.form_casetype()
        # 点击导出Excel按钮
        self.find_element_by_xpath('//button[text()="导出excel"]')
        print u"点击导出成功"

    def form_follow(self):
        """统计报表-后续流程进行度
        """
        self.form_map()
        # 点击进入后续流程进行度
        self.find_element_by_xpath('//li[text()="后续流程进行度"]').click()

    def verification_form_follow(self):
        """验证-统计报表-后续流程进行度
        """
        try:
            pro = self.find_element_by_xpath('//span[@id="fourProvince"]').text
        except:
            pro = "*None*"
        print "result: ", pro
        print "except: ", u"浙江省"
        res = pro == u"浙江省"
        return res

    def form_follow_date(self):
        """统计报表-后续流程进行度-日期筛选
        """
        self.form_follow()
        # 点击查询按钮
        self.find_element_by_xpath('//input[@id="startDate4"]/../button').click()
        print u"点击查询按钮成功"

    def form_follow_judicial(self):
        """统计报表-后续流程进行度-司法确认案件量
        """
        self.form_follow()
        # 获取司法确认案件数量
        num = self.find_element_by_xpath('//label[text()="浙江省申请司法确认案件量："]/b').text
        print u"浙江省申请司法确认案件量：", num

    def form_follow_litigation(self):
        """统计报表-后续流程进行度-申请诉讼案件量
        """
        self.form_follow()
        # 获取申请诉讼案件数量
        num = self.find_element_by_xpath('//label[text()="浙江省申请诉讼案件量："]/b').text
        print u"浙江省申请诉讼案件量：", num

    def form_show(self):
        """统计报表-优秀内容展示
        """
        self.form_map()
        # 点击进入优秀内容展示
        self.find_element_by_xpath('//li[contains(text(),"优秀内容展示")]').click()
        sleep(1)

    def verification_form_show(self):
        """验证-统计报表-优秀内容展示
        """
        try:
            show = self.find_element_by_xpath('//label[text()="金牌调解员"]').text
        except:
            show = "*None*"
        print "result: ", show
        print "except: ", u"金牌调解员"
        res = show == u"金牌调解员"
        return res

    def form_show_date(self):
        """统计报表-优秀内容展示-日期筛选
        """
        self.form_show()
        # 点击查询按钮
        self.find_element_by_xpath('//input[@id="startDateGoods"]/../button').click()
        print u"点击查询按钮成功"

    def form_show_excel(self):
        """统计报表-优秀内容展示-导出
        """
        self.form_show()
        # 点击导出按钮
        self.find_element_by_xpath('//input[@id="startDateGoods"]/../../button').click()
        print u"点击导出按钮成功"

    def form_show_tjy(self):
        """统计报表-优秀内容展示-金牌调解员
        """
        self.form_show()
        # 金牌调解员选择调解成功率
        self.find_element_by_xpath('//label[text()="金牌调解员"]/../select').click()
        self.find_element_by_xpath('//label[text()="金牌调解员"]/../select/option[2]').click()
        tjy = self.find_element_by_xpath('//label[text()="金牌调解员"]/../select/option[2]').text
        return tjy

    def verification_form_show_tjy(self, tjy):
        """验证-统计报表-优秀内容展示-金牌调解员
        """
        try:
            tjy_v = self.find_element_by_xpath('//th[text()="调解成功率"]').text
        except:
            tjy_v = "*None*"
        print "result: ", tjy_v
        print "except: ", tjy
        res = tjy_v == tjy
        return res

    def form_show_organ(self):
        """统计报表-优秀内容展示-优秀调解机构
        """
        self.form_show()
        # 优秀调解机构选择及时响应率
        self.find_element_by_xpath('//label[text()="优秀调解机构"]/../select').click()
        self.find_element_by_xpath('//label[text()="优秀调解机构"]/../select/option[2]').click()
        organ = self.find_element_by_xpath('//label[text()="优秀调解机构"]/../select/option[2]').text
        return organ

    def verification_form_show_organ(self, organ):
        """验证-统计报表-优秀内容展示-优秀调解机构
        """
        try:
            organ_v = self.find_element_by_xpath('//th[text()="及时响应率"]').text
        except:
            organ_v = "*None*"
        print "result: ", organ_v
        print "except: ", organ
        res = organ_v == organ
        return res

    def form_show_city(self):
        """统计报表-优秀内容展示-优秀调解机构
        """
        self.form_show()
        # 优秀调解机构选择及时响应率
        self.find_element_by_xpath('//label[text()="优秀市"]/../select').click()
        self.find_element_by_xpath('//label[text()="优秀市"]/../select/option[2]').click()
        city = self.find_element_by_xpath('//label[text()="优秀市"]/../select/option[2]').text
        return city

    def verification_form_show_city(self, city):
        """验证-统计报表-优秀内容展示-优秀市
        """
        try:
            city_v = self.find_element_by_xpath('//th[text()="及时响应率"]').text
        except:
            city_v = "*None*"
        print "result: ", city_v
        print "except: ", city
        res = city_v == city
        return res

    def form_record_dispute_type(self):
        """案件记录-纠纷调解-调解类型
        """
        # 进入案件记录页面
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        # 点击选择调解类型为消费维权
        tp_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//li[contains(text(),"消费维权")]')))
        tp_btn.click()
        # self.find_element_by_xpath('//li[contains(text(),"消费维权")]').click()
        sleep(1)

    def verification_form_record_dispute_type(self):
        """验证-案件记录-纠纷调解-调解类型
        """
        # 获取所选调解类型
        type_1 = self.find_element_by_xpath('//li[contains(text(),"消费维权")]').text
        # 获取第一条案件纠纷类型
        try:
            type_v = self.find_element_by_xpath('//label[text()="纠纷类型"]/../p').text
        except:
            type_v = "*None*"
        print "result: ", type_v
        print "except: ", type_1
        res = type_v == type_1
        return res

    def form_record_dispute_state(self):
        """案件记录-纠纷调解-调解状态
        """
        # 进入案件记录页面
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        # 点击选择调解状态为等待调解
        self.find_element_by_xpath('//li[contains(text(),"等待调解")]').click()
        sleep(1)

    def verification_form_record_dispute_state(self):
        """验证-案件记录-纠纷调解-调解类型
        """
        # 获取所选调解类型
        type_1 = self.find_element_by_xpath('//li[contains(text(),"等待调解")]').text
        # 获取第一条案件纠纷类型
        try:
            type_v = self.find_element_by_xpath('//div[contains(text(),"等待调解")]').text
        except:
            type_v = "*None*"
        print "result: ", type_v
        print "except: ", type_1
        res = type_v == type_1
        return res

    def form_record_dispute_time(self):
        """案件记录-纠纷调解-登记时间
        """
        # 进入案件记录页面
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        # 点击登记时间所有时间
        altm_btm = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.x_form_record_judicial_alltime)))
        altm_btm.click()
        # self.find_element_by_xpath(self.x_form_record_judicial_alltime).click()
        sleep(1)

    def verification_form_record_dispute_time(self):
        """验证-案件记录-纠纷调解-登记时间
        """
        # 获取所有时间案件数量
        num = self.find_element_by_xpath('//span[contains(text(),"案件数量")]/../span[2]/i[2]').text
        if int(num) > 10000:
            nu = "true"
        else:
            nu = "false"
        print u"案件数量: ", num
        res = nu == "true"
        return res

    def form_record_dispute_area(self):
        """案件记录-纠纷调解-选择地区
        """
        # 进入案件记录页面
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        # 选择市区为杭州市上城区
        city_a = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//option[contains(text(),"请选择市")]/..')))
        city_a.click()
        # self.find_element_by_xpath('//option[contains(text(),"请选择市")]/..').click()
        # 等待市可被选择点击
        element_city = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//option[text()="杭州市"]')))
        element_city.click()
        # self.find_element_by_xpath('//option[text()="杭州市"]').click()
        # 等待区/镇可被选择点击
        element_cty_a = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//option[contains(text(),"请选择区/镇")]/..')))
        element_cty_a.click()
        # self.find_element_by_xpath('//option[contains(text(),"请选择区/镇")]/..').click()
        element_cty = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//option[text()="上城区"]')))
        element_cty.click()
        # self.find_element_by_xpath('//option[text()="上城区"]').click()
        sleep(0.5)

    def verification_form_record_dispute_area(self):
        """验证-案件记录-纠纷调解-选择地区
        """
        try:
            area = self.find_element_by_xpath('//label[text()="调解机构"]/../p').text
        except:
            area = "*None*"
        area = area[0:9]
        print "result: ", area
        res = area == u"浙江省杭州市上城区"
        return res

    def form_record_dispute_number(self):
        """案件记录-纠纷调解-案件数量
        """
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        # 获取案件数量
        num = self.find_element_by_xpath('//span[contains(text(),"案件数量")]/../span[2]/i[2]').text
        print u"案件数量: ", num

    def form_record_dispute_search(self):
        """案件记录-纠纷调解-搜索
        """
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        # 选择第二个案件编号
        sea = self.find_element_by_xpath('//div[contains(text(),"纠纷编号")]/../../../div[4]/div/div').text
        # 获取案件编号
        search = sea[5:]
        # 输入框输入案件编号
        self.find_element_by_xpath('//input[@id="keyword"]').send_keys(search)
        # 点击搜索按钮
        self.find_element_by_xpath('//input[@id="keyword"]/../../a').click()
        sleep(1)
        return sea

    def verification_form_record_dispute_search(self, sea):
        """验证-案件记录-纠纷调解-搜索
        """
        try:
            try:
                try:
                    sea_v = self.find_element_by_xpath('//div[contains(text(),"纠纷编号")]/../../../div[3]/div/div').text
                except:
                    sea_v = self.find_element_by_xpath('//div[contains(text(),"纠纷编号")]/../../../div[3]/div/div').text
                    sleep(1)
            except:
                sea_v = "*None*"
                sleep(1)
        except:
            sea_v = "*None*"
        print "result: ", sea_v
        print "except: ", sea
        res = sea == sea_v
        return res

    def form_record_dispute_reset(self):
        """案件记录-纠纷调解-重置
        """
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        # 选择第二个案件编号
        sea = self.find_element_by_xpath('//div[contains(text(),"纠纷编号")]/../../../div[4]/div/div').text
        # 获取案件编号
        search = sea[5:]
        # 输入框输入案件编号
        self.find_element_by_xpath('//input[@id="keyword"]').send_keys(search)
        # 点击搜索按钮
        self.find_element_by_xpath('//input[@id="keyword"]/../../a').click()
        sleep(0.5)
        # 点击重置按钮
        reset = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="keyword"]/../../a[2]')))
        reset.click()
        # self.find_element_by_xpath('//input[@id="keyword"]/../../a[2]').click()
        return sea

    def verification_form_record_dispute_reset(self, sea):
        """验证-案件记录-纠纷调解-重置
        """
        try:
            try:
                sea_v = self.find_element_by_xpath('//div[contains(text(),"纠纷编号")]/../../../div[4]/div/div').text
            except:
                sea_v = self.find_element_by_xpath('//div[contains(text(),"纠纷编号")]/../../../div[4]/div/div').text
                sleep(1)
        except:
            sea_v = "*None*"
        print "result: ", sea_v
        print "except: ", sea
        res = sea == sea_v
        return res

    def form_record_dispute_excel(self):
        """案件记录-纠纷调解-批量导出
        """
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        self.find_element_by_xpath('//button[contains(text(),"批量导出")]').click()
        print u"批量导出成功"

    def form_record_judicial_type(self):
        """案件记录-司法确认-案件类型
        """
        # 进入案件记录页面
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        self.find_element_by_xpath(self.x_form_record_judicial).click()
        sleep(0.5)
        self.find_element_by_xpath(self.x_form_record_judicial_alltime).click()
        sleep(0.5)
        # 点击选择调解类型为消费维权
        self.find_element_by_xpath('//li[contains(text(),"消费维权")]').click()
        type_i = self.find_element_by_xpath('//li[contains(text(),"消费维权")]').text
        # sleep(1)
        return type_i

    def verification_form_record_judicial_type(self, type_i):
        """验证-案件记录-司法确认-案件类型
        """
        # 进入第一个案件的案件详情页面
        page_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(text(),"案件编号")]/following-sibling::*')))
        page_btn.click()
        # self.find_element_by_xpath('//div[contains(text(),"案件编号")]/following-sibling::*').click()
        sleep(1)
        # 获取第一条案件纠纷类型
        try:
            try:
                type_v = self.find_element_by_xpath('//h6[contains(text(),"案件类型")]/../p').text
            except:
                type_v = self.find_element_by_xpath('//h6[contains(text(),"案件类型")]/../p').text
                sleep(1)
        except:
            type_v = "*None*"
        print "result: ", type_v
        print "except: ", type_i
        res = type_v == type_i
        return res

    def form_record_judicial_state(self):
        """案件记录-司法确认-案件状态
        """
        # 进入案件记录页面
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        self.find_element_by_xpath(self.x_form_record_judicial).click()
        sleep(0.5)
        self.find_element_by_xpath(self.x_form_record_judicial_alltime).click()
        sleep(0.5)
        # 点击选择调解状态为等待调解
        self.find_element_by_xpath('//li[contains(text(),"不予受理")]').click()
        sleep(1)

    def verification_form_record_judicial_state(self):
        """验证-案件记录-司法确认-案件类型
        """
        # 获取所选案件类型
        type_1 = self.find_element_by_xpath('//li[contains(text(),"不予受理")]').text
        # 获取第一条案件案件类型
        try:
            type_v = self.find_element_by_xpath('//p[contains(text(),"不予受理")]').text
        except:
            type_v = "*None*"
        # 字符串收尾去空处理
        type_v = type_v.strip()
        type_v = type_v.replace(" ", " ")
        print "result: ", type_v
        print "except: ", type_1
        res = type_v == type_1
        return res

    def form_record_judicial_time(self):
        """案件记录-司法确认-登记时间
        """
        # 进入案件记录页面
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        self.find_element_by_xpath(self.x_form_record_judicial).click()
        sleep(0.5)
        # 选择全部时间
        atm = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.x_form_record_judicial_alltime)))
        atm.click()
        # self.find_element_by_xpath(self.x_form_record_judicial_alltime).click()

    def verification_form_record_judicial_time(self):
        """案件记录-司法确认-登记时间
        """
        # 获取所有时间案件数量
        try:
            try:
                num = self.find_element_by_xpath('//span[contains(text(),"案件数量")]/../span[2]/i[2]').text
            except:
                num = self.find_element_by_xpath('//span[contains(text(),"案件数量")]/../span[2]/i[2]').text
                sleep(1)
        except:
            num = "*None*"
        if int(num) > 250:
            nu = "true"
        else:
            nu = "false"
        print u"案件数量: ", num
        res = nu == "true"
        return res

    def form_record_judicial_area(self):
        """案件记录-司法确认-选择地区
        """
        # 进入案件记录页面
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        self.find_element_by_xpath(self.x_form_record_judicial).click()
        sleep(0.5)
        self.find_element_by_xpath(self.x_form_record_judicial_alltime).click()
        sleep(0.5)
        # 选择市区为浙江省杭州市上城区
        pro_a = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//option[contains(text(),"请选择省")]/..')))
        pro_a.click()
        # self.find_element_by_xpath('//option[contains(text(),"请选择省")]/..').click()
        pro = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//option[contains(text(),"浙江省")]')))
        pro.click()
        # self.find_element_by_xpath('//option[contains(text(),"浙江省")]').click()
        sleep(0.5)
        city = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//option[contains(text(),"请选择市")]/..')))
        city.click()
        # self.find_element_by_xpath('//option[contains(text(),"请选择市")]/..').click()
        city = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//option[contains(text(),"杭州市")]')))
        city.click()
        # self.find_element_by_xpath('//option[contains(text(),"杭州市")]').click()
        cty = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//option[contains(text(),"请选择区/镇")]/..')))
        cty.click()
        # self.find_element_by_xpath('//option[contains(text(),"请选择区/镇")]/..').click()
        cty = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//option[contains(text(),"上城区")]')))
        cty.click()
        # self.find_element_by_xpath('//option[contains(text(),"上城区")]').click()
        sleep(0.5)
        num = self.find_element_by_xpath('//i[text()="共"]/../i[2]').text
        print u"案件数量: ", num

    # def verification_form_record_judicial_area(self):
    #     """验证-案件记录-纠纷调解-选择地区
    #     """
    #     try:
    #         area = self.find_element_by_xpath('//label[text()="申请法院"]/../p').text
    #     except:
    #         area = "*None*"
    #     area = area[0:9]
    #     print "result: ", area
    #     res = area == u"浙江省杭州市上城区"
    #     return res

    def form_record_judicial_number(self):
        """案件记录-司法确认-案件数量
        """
        # 进入案件记录页面
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        self.find_element_by_xpath(self.x_form_record_judicial).click()
        sleep(0.5)
        self.find_element_by_xpath(self.x_form_record_judicial_alltime).click()
        sleep(0.5)
        # 获取案件数量
        num = self.find_element_by_xpath('//span[contains(text(),"案件数量")]/../span[2]/i[2]').text
        print u"案件数量: ", num

    def form_record_judicial_search(self):
        """案件记录-司法确认-搜索
        """
        # 进入案件记录页面
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        self.find_element_by_xpath(self.x_form_record_judicial).click()
        sleep(0.5)
        self.find_element_by_xpath(self.x_form_record_judicial_alltime).click()
        sleep(0.5)
        # 选择第二个案件编号
        sea = self.find_element_by_xpath('//div[contains(text(),"案件编号")]/../../../div[4]/div[1]/div[1]').text
        # 获取案件编号
        search = sea[5:]
        print search
        # 输入框输入案件编号
        self.find_element_by_xpath('//input[@id="fuzzyContent"]').send_keys(search)
        # 点击搜索按钮
        self.find_element_by_xpath('//input[@id="fuzzyContent"]/../../a[1]').click()
        sleep(0.5)
        return sea

    def verification_form_record_judicial_search(self, sea):
        """验证-案件记录-司法确认-搜索
        """
        try:
            sea_v = self.find_element_by_xpath('//div[contains(text(),"案件编号")]/../../../div[3]/div[1]/div[1]').text
        except:
            sea_v = "*None*"
        print "result: ", sea_v
        print "except: ", sea
        res = sea == sea_v
        return res

    def form_record_judicial_reset(self):
        """案件记录-司法确认-重置
        """
        # 进入案件记录页面
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        self.find_element_by_xpath(self.x_form_record_judicial).click()
        sleep(0.5)
        self.find_element_by_xpath(self.x_form_record_judicial_alltime).click()
        sleep(0.5)
        # 选择第二个案件编号
        sea = self.find_element_by_xpath('//div[contains(text(),"案件编号")]/../../../div[4]/div[1]/div[1]').text
        # 获取案件编号
        search = sea[5:]
        # 输入框输入案件编号
        self.find_element_by_xpath('//input[@id="fuzzyContent"]').send_keys(search)
        # 点击搜索按钮
        self.find_element_by_xpath('//input[@id="fuzzyContent"]/../../a').click()
        sleep(0.5)
        # 点击重置按钮
        self.find_element_by_xpath('//input[@id="fuzzyContent"]/../../a[2]').click()
        return sea

    def verification_form_record_judicial_reset(self, sea):
        """验证-案件记录-纠纷调解-重置
        """
        try:
            sea_v = self.find_element_by_xpath('//div[contains(text(),"案件编号")]/../../../div[4]/div[1]/div[1]').text
        except:
            sea_v = "*None*"
        print "result: ", sea_v
        print "except: ", sea
        res = sea == sea_v
        return res

    def form_record_judicial_excel(self):
        """案件记录-司法确认-批量导出
        """
        # 进入案件记录页面
        self.find_element_by_xpath(self.x_form_record).click()
        sleep(1)
        self.find_element_by_xpath(self.x_form_record_judicial).click()
        sleep(0.5)
        self.find_element_by_xpath(self.x_form_record_judicial_alltime).click()
        sleep(0.5)
        self.find_element_by_xpath('//button[contains(text(),"批量导出")]').click()
        print u"批量导出成功"
