# coding:utf-8
from time import sleep

from odrweb.core.initdata import init
from odrweb.page.browser import Page

base_url = init.base_url

consult = {"consult_desc": u"假冒伪劣",
           "consult_ask": u"假一赔十"}


class NoLoginHomePage(Page):
    """未登录首页操作"""

    # 服务内容
    x_head_service = '//div[@id="app"]/header/div[3]/div[2]/ul/li[2]/a'
    # 服务内容-法律咨询
    x_head_service_law = '//div[@id="app"]/header/div[3]/div[2]/ul/li[2]/div/div[1]/a'
    # 服务内容--法律咨询-在线咨询
    x_head_service_law_online = '//div[@id="app"]/div[1]/div[2]/div[1]/div[2]/div[2]/div[4]/a'
    # 服务内容-法律咨询-人工咨询
    x_head_service_manwork = '//div[@id="app"]/div[1]/div[2]/div[2]/div[2]/div[2]/div[4]/a'
    # 服务内容-在线调解
    x_head_service_dispute = '//div[@id="app"]/header/div[3]/div[2]/ul/li[2]/div/div[3]/a'
    # 服务内容-在线调解-选择调解类别为婚姻调解
    x_head_service_dispute_type = '//div[@id="app"]/div[1]/div/div[1]/ul/li[1]/a/img'
    # 服务资源
    x_head_resource = '//div[@id="app"]/header/div[3]/div[2]/ul/li[3]/a'
    # 服务资源-服务人员
    x_head_resource_serpersonal = '//div[@id="app"]/div[1]/div[1]/div[1]/div[1]/div[2]/a'
    # 帮助中心
    x_head_help = '//div[@id="app"]/header/div[3]/div[2]/ul/li[5]/a'
    # 获取常见问题页面第一个问题词条
    x_head_common_first = '//div[@id="app"]/div[3]/div/div[2]/h4'
    # 获取点击申请调解页面的调解类型
    x_tail_law = '//div[@id="app"]/div[1]/div[1]/div[2]/dl/dt'

    def get_url(self):
        """进入T2环境ODR"""
        self.driver.get(base_url)

    def head_service_online(self):
        """进入在线咨询"""
        # 点击服务内容
        self.find_element_by_xpath(self.x_head_service).click()
        # 点击法律咨询
        self.find_element_by_xpath(self.x_head_service_law).click()
        # 点击选择在线咨询
        self.find_element_by_xpath(self.x_head_service_law_online).click()

    def change_windows(self):
        """切换窗口"""
        windows = self.driver.window_handles
        self.driver.switch_to_window(windows[1])

    def verification_head_service_online_chat(self):
        """验证在线咨询进入智能机器人"""
        try:
            chat = self.find_element_by_xpath('//div[@id="robotTalk"]/div[2]/div[1]/div/div/div[2]/div[2]').text
        except:
            chat = "**None**"
        print "result:", chat
        print "except:", u"您好，我是平台咨询机器人"
        res = chat == u"您好，我是平台咨询机器人"
        return res

    def head_service_online_law(self):
        """在线咨询法律咨询"""
        # 点击法律知识
        self.find_element_by_xpath('/html/body/div/div/div/header/div/div[2]/ul/li[2]/a/a/div[1]').click()
        sleep(1)
        # 弹出框点击确定
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]/span').click()

    def verification_head_service_online_law(self):
        """验证在线咨询法律知识"""
        try:
            law = self.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/div/ul/li').text
        except:
            law = "**None**"
        print "result:", law
        print "except:", u"法律法规"
        res = law == u"法律法规"
        return res

    def head_service_online_way(self):
        """在线咨询解纷方式"""
        # 点击解纷方式
        self.find_element_by_xpath('/html/body/div[1]/div/div/header/div/div[2]/ul/li[3]/a/a/div[1]').click()

    def verification_head_service_online_way(self):
        """校验在线咨询解纷方式"""
        try:
            way = self.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[1]/h4').text
        except:
            way = "**None**"
        print "result:", way
        print "except:", u"为您推荐以下解纷方式："
        res = way == u"为您推荐以下解纷方式："
        return res

    def head_service_online_case(self):
        """在线咨询相关案例"""
        # 点击相关案例
        self.find_element_by_xpath("/html/body/div[1]/div/div/header/div/div[2]/ul/li[4]/a/a/div[1]").click()
        # 提示框点击确定
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]/span').click()

    def verification_head_service_online_case(self):
        """验证在线咨询相关案例"""
        try:
            case = self.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[1]/div[1]/h3').text
        except:
            case = "**None**"
        print "result:", case
        print "except:", u"诉讼请求"
        res = case == u"诉讼请求"
        return res

    def head_service_online_assist(self):
        """在线咨询辅助工具"""
        # 点击辅助工具
        self.find_element_by_xpath('/html/body/div/div/div/header/div/div[2]/ul/li[5]/a/a/div[1]').click()

    def verification_head_service_online_assist(self):
        """验证在线咨询辅助工具"""
        try:
            assist = self.find_element_by_xpath('/html/body/div/div/div/div/div/div[1]/h3').text
        except:
            assist = "**None**"
        print "result:", assist
        print "except:", u"诉讼费计算器"
        res = assist == u"诉讼费计算器"
        return res

    def head_service_manwork_login(self):
        """人工咨询登陆咨询"""
        # 点击服务内容
        self.find_element_by_xpath(self.x_head_service).click()
        # 点击法律咨询
        self.find_element_by_xpath(self.x_head_service_law).click()
        # 点击选择人工咨询
        self.find_element_by_xpath(self.x_head_service_manwork).click()
        # 点击登陆咨询
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]').click()

    def verification_skip_login_page(self):
        """跳转登陆页面校验"""
        try:
            login = self.find_element_by_xpath('//div[@id="app"]/div[2]/div[2]').text
        except:
            login = "**None**"
        print "result:", login
        print "except:", u"欢迎登录"
        res = login == u"欢迎登录"
        return res

    def head_service_manwork_consult(self, **kwargs):
        """人工咨询直接发起咨询"""
        # 点击服务内容
        self.find_element_by_xpath(self.x_head_service).click()
        # 点击法律咨询
        self.find_element_by_xpath(self.x_head_service_law).click()
        # 点击选择人工咨询
        self.find_element_by_xpath(self.x_head_service_manwork).click()
        # 点击确定发起咨询
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]/span').click()
        # # 选择矛盾纠纷类型借贷纠纷
        # self.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div[1]/div/select').click()
        # self.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div[1]/div/select/option[4]').click()
        # 填写纠纷描述
        self.find_element_by_xpath('//textarea[@id="textarea_title"]').send_keys(kwargs["consult_desc"])
        # 填写您的诉求
        self.find_element_by_xpath('//textarea[@id="textarea_content"]').send_keys(kwargs["consult_ask"])
        # 点击提交申请
        self.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div[6]/button').click()
        sleep(1)
        # 提示框点击是
        self.find_element_by_xpath('//div[@id="tool_meg"]/div/div/div[2]/a').click()
        sleep(1)
        # 选择第一个咨询师
        self.find_element_by_xpath('//div[@id="table"]/div[2]/table/tbody/tr[1]/td[6]/button').click()
        sleep(1)

    def verification_head_service_manwork_consult(self, **kwargs):
        """验证人工咨询直接发起咨询"""
        # 点击查看纠纷详情
        self.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div[1]/div[1]/div[2]/button[1]').click()
        sleep(1)
        # 获取consult_desc校验
        try:
            desc = self.find_element_by_xpath('//div[@id="checkReports"]/div/div/div[2]/div/div[1]/p').text
        except:
            desc = "**None**"
        print "result:", desc
        print "except:", kwargs["consult_desc"]
        res = desc == kwargs["consult_desc"]
        return res

    def head_service_assessment(self):
        """服务内容在线评估"""
        # 点击服务内容
        self.find_element_by_xpath(self.x_head_service).click()
        sleep(1)
        # 点击在线评估
        self.find_element_by_xpath('//div[@id="app"]/header/div[3]/div[2]/ul/li[2]/div/div[2]/a').click()

    def head_dispute_type_dispute(self):
        """在线调解申请调解"""
        # 点击服务内容
        self.find_element_by_xpath(self.x_head_service).click()
        sleep(1)
        # 点击在线调解
        self.find_element_by_xpath(self.x_head_service_dispute).click()
        # 点击选择调解类别
        self.find_element_by_xpath(self.x_head_service_dispute_type).click()
        # 点击申请调解
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[2]/div/button[1]').click()
        # 我是申请人点击调解
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div/div[2]/div[2]/div').click()
        # 提示框点击去登陆
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button').click()

    def head_dispute_type_consult(self):
        """在线调解法律咨询"""
        # 点击服务内容
        self.find_element_by_xpath(self.x_head_service).click()
        sleep(1)
        # 点击在线调解
        self.find_element_by_xpath(self.x_head_service_dispute).click()
        # 点击选择调解类别
        self.find_element_by_xpath(self.x_head_service_dispute_type).click()
        # 点击法律咨询
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[2]/div/button[2]').click()
        sleep(1)

    def head_dispute_center_marriage(self):
        """在线调解婚姻家事"""
        # 点击服务内容
        self.find_element_by_xpath(self.x_head_service).click()
        sleep(1)
        # 点击在线调解
        self.find_element_by_xpath(self.x_head_service_dispute).click()
        # 点击调解中心婚姻家事,进入反家暴服务平台
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div/div[2]/div/ul/li[1]/a/div[2]/span[2]').click()
        sleep(1)

    def verification_fjb_service_url(self):
        """校验反家暴服务平台URL"""
        try:
            url = self.driver.current_url
        except:
            url = "*None*"
        print "result:", url
        print "except:", 'https://fanjiabao.net/'
        res = url == 'https://fanjiabao.net/'
        return res

    def head_dispute_center_traffic(self):
        """在线调解道交纠纷"""
        # 点击服务内容
        self.find_element_by_xpath(self.x_head_service).click()
        sleep(1)
        # 点击在线调解
        self.find_element_by_xpath(self.x_head_service_dispute).click()
        # 点击道交纠纷,进入交通事故网上法庭
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div/div[2]/div/ul/li[2]/a/div[2]/span[2]').click()
        sleep(1)

    def verification_jtsp_traffic_url(self):
        """校验交通事故网上法庭URL"""
        try:
            url = self.driver.current_url
        except:
            url = "*None*"
        print "result:", url
        print "except:", 'http://www.jtsp.gov.cn/online_court/'
        res = url == 'http://www.jtsp.gov.cn/online_court/'
        return res

    def head_dispute_center_lawer(self):
        # 点击服务内容
        self.find_element_by_xpath(self.x_head_service).click()
        sleep(1)
        # 点击在线调解
        self.find_element_by_xpath(self.x_head_service_dispute).click()
        # 点击进入律师调解中心
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div/div[2]/div/ul/li[3]/a/div[2]/span[2]').click()

    def verifivation_head_dispute_center_lawer(self):
        try:
            lawer = self.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[1]/div[1]/div/a').text
        except:
            lawer = "*None*"
        print "result:", lawer
        print "except:", u"律师调解中心"
        res = lawer == u"律师调解中心"
        return res

    def head_service_arbitration(self):
        """仲裁服务"""
        # 点击服务内容
        self.find_element_by_xpath(self.x_head_service).click()
        sleep(1)
        # 点击仲裁服务
        self.find_element_by_xpath('//div[@id="app"]/header/div[3]/div[2]/ul/li[2]/div/div[4]/a').click()

    def verification_arbitration(self):
        """校验仲裁服务"""
        try:
            url = self.driver.current_url
        except:
            url = "*None*"
        print "result:", url
        print "except:", 'http://122.112.249.117/user/login?redirect=%2Farb%2F%3F'
        res = url == 'http://122.112.249.117/user/login?redirect=%2Farb%2F%3F'
        return res

    def head_service_lawshit(self):
        """诉讼服务"""
        # 点击服务内容
        self.find_element_by_xpath(self.x_head_service).click()
        sleep(1)
        # 点击仲裁服务
        self.find_element_by_xpath('//div[@id="app"]/header/div[3]/div[2]/ul/li[2]/div/div[5]/a').click()

    def verification_lawshit(self):
        """校验诉讼服务"""
        try:
            url = self.driver.current_url
        except:
            url = "*None*"
        print "result:", url
        print "except:", 'http://ssfw.zjsfgkw.cn/'
        res = url == 'http://ssfw.zjsfgkw.cn/'
        return res

    def head_resource_organization_info(self):
        """服务资源机构详情"""
        # 点击服务资源
        self.find_element_by_xpath(self.x_head_resource).click()
        sleep(2)
        # 获取第一个法院名称
        ogr_name_11 = self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]').text
        # 点击第一个机构查看详情
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]').click()
        # 获取详情中法院名称
        ogr_name_12 = self.find_element_by_xpath('//div[@id="app"]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]').text
        return ogr_name_11, ogr_name_12

    def verification_head_resource_organization_info(self, ogr_name_11, ogr_name_12):
        """校验服务资源机构详情"""
        print "result:", ogr_name_12
        print "except:", ogr_name_11
        res = ogr_name_12 == ogr_name_11
        return res

    def head_resource_organization_search(self):
        """服务资源机构搜索"""
        # 点击服务资源
        self.find_element_by_xpath(self.x_head_resource).click()
        sleep(2)
        # 获取第二个法院名称
        ogr_name_21 = self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]').text
        # 搜索框输入法院名称
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[1]/div[2]/p/input').send_keys(ogr_name_21)
        # 点击搜索按钮
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[1]/div[2]/button').click()
        sleep(6)
        # 获取搜索后法院名称
        ogr_name_22 = self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[2]/div[1]/div/div[1]/div[2]/div[1]').text
        return ogr_name_21, ogr_name_22

    def verification_head_resource_organization_search(self, ogr_name_21, ogr_name_22):
        """校验服务资源机构搜索"""
        print "result:", ogr_name_21
        print "except:", ogr_name_22
        res = ogr_name_22 == ogr_name_21
        return res

    def head_resource_serpersonal_info(self):
        """服务资源服务人员详情"""
        # 点击服务资源
        self.find_element_by_xpath(self.x_head_resource).click()
        sleep(2)
        # 点击服务人员
        self.find_element_by_xpath(self.x_head_resource_serpersonal).click()
        # 获取第一个服务人员名称
        per_name_11 = self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/span[1]').text
        sleep(1)
        # 点击第一个服务人员查看详情
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div').click()
        # 获取详情服务人员名称
        per_name_12 = self.find_element_by_xpath('//div[@id="app"]/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]').text
        return per_name_11, per_name_12

    def verification_head_resource_serpersonal_info(self, per_name_11, per_name_12):
        """校验服务资源服务人员详情"""
        print "result:", per_name_12
        print "except:", per_name_11
        res = per_name_12 == per_name_11
        return res

    def head_resource_serpersonal_search(self):
        """服务资源服务人员搜索"""
        # 点击服务资源
        self.find_element_by_xpath(self.x_head_resource).click()
        sleep(2)
        # 点击服务人员
        self.find_element_by_xpath(self.x_head_resource_serpersonal).click()
        # 获取第二个服务人员名称
        per_name_21 = self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/span[1]').text
        # 搜索框输入服务人员名称
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[1]/div[2]/p/input').send_keys(per_name_21)
        # 点击搜索按钮
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[1]/div[2]/button').click()
        sleep(5)
        # 获取搜索后服务人员名称
        per_name_22 = self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[1]/span[1]').text
        return per_name_21, per_name_22

    def verification_head_resource_serpersonal_search(self, per_name_21, per_name_22):
        """校验服务资源服务人员搜索"""
        print "result:", per_name_22
        print "except:", per_name_21
        res = per_name_22 == per_name_21
        return res

    def head_resource_serpersonal_more(self):
        """服务资源服务人员更多擅长领域"""
        # 点击服务资源
        self.find_element_by_xpath(self.x_head_resource).click()
        sleep(2)
        # 点击服务人员
        self.find_element_by_xpath(self.x_head_resource_serpersonal).click()
        # 点击更多展开擅长领域
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[1]/div[3]/div[3]/div[2]/div[1]/span').click()

    def verification_head_resource_serpersonal_more(self):
        """校验服务资源服务人员更多擅长领域"""
        # 获取金融借款合同纠纷对比
        try:
            more = self.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div[1]/div[3]/div[3]/div[2]/ul/li[25]').text
        except:
            more = "*None*"
        print "resoult:", more
        print "except:", u"金融借款合同纠纷"
        res = more == u"金融借款合同纠纷"
        return res

    def head_news(self):
        """新闻动态"""
        # 点击进入新闻动态
        self.find_element_by_xpath('//div[@id="app"]/header/div[3]/div[2]/ul/li[4]/a').click()
        # 获取第一篇新闻的标题
        title_1 = self.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]').text
        # 点击进入第一篇新闻
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[1]').click()
        sleep(1)
        # 获取新闻标题
        title_2 = self.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div/div[1]/div/div[2]').text
        return title_1, title_2

    def verification_head_news(self, title_1, title_2):
        """校验服务资源服务人员搜索"""
        print "result:", title_2
        print "except:", title_1
        res = title_2 == title_1
        return res

    def head_help_common_enrol(self):
        """帮助中心常见问题用户注册"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题用户注册
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[1]/div[2]/div[1]/a[1]/span').click()

    def head_help_common_login(self):
        """帮助中心常见问题用户登陆"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题用户登陆
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[1]/div[2]/div[1]/a[2]/span').click()

    def head_help_common_password(self):
        """帮助中心常见问题忘记密码"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题忘记密码
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[1]/div[2]/div[2]/a[1]/span').click()

    def head_help_common_agreement(self):
        """帮助中心常见问题用户注册协议"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题用户注册协议
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[1]/div[2]/div[2]/a[2]/span').click()

    def verification_head_help_common(self):
        """校验帮助中心常见问题中新手指南,帮助中心常见问题校验"""
        try:
            text = self.find_element_by_xpath(self.x_head_common_first).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"1. 用户注册"
        res = text == u"1. 用户注册"
        return res

    def head_help_common_mediate(self):
        """帮助中心常见问题纠纷调解服务"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题用纠纷服务调解
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[2]/div[2]/div[1]/a[1]/span').click()

    def verification_head_help_common_mediate(self):
        """校验帮助中心常见问题纠纷调解服务"""
        try:
            text = self.find_element_by_xpath(self.x_head_common_first).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"1. 纠纷调解服务简介"
        res = text == u"1. 纠纷调解服务简介"
        return res

    def head_help_common_consult(self):
        """帮助中心常见问题法律咨询服务"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题用户法律咨询服务
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[2]/div[2]/div[1]/a[2]/span').click()

    def verification_head_help_common_consult(self):
        """校验帮助中心常见问题法律咨询服务"""
        try:
            text = self.find_element_by_xpath(self.x_head_common_first).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"1. 法律咨询服务简介"
        res = text == u"1. 法律咨询服务简介"
        return res

    def head_help_common_assess(self):
        """帮助中心常见问题在线评估服务"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题用在线评估服务
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[2]/div[2]/div[2]/a[1]/span').click()

    def verification_head_help_common_assess(self):
        """校验帮助中心常见问题在线评估服务"""
        try:
            text = self.find_element_by_xpath(self.x_head_common_first).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"1. 在线评估服务简介"
        res = text == u"1. 在线评估服务简介"
        return res

    def head_help_common_services(self):
        """帮助中心常见问题服务资源"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题服务资源
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[2]/div[2]/div[2]/a[2]/span').click()

    def verification_head_help_common_services(self):
        """校验帮助中心常见问题服务资源"""
        try:
            text = self.find_element_by_xpath(self.x_head_common_first).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"1. 什么是“调解员” ?"
        res = text == u"1. 什么是“调解员” ?"
        return res

    def head_help_common_apply(self):
        """帮助中心常见问题申请调解"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题用申请调解
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[3]/div[2]/div[1]/a[1]/span').click()

    def verification_head_help_common_apply(self):
        """校验帮助中心常见问题申请调解"""
        try:
            text = self.find_element_by_xpath(self.x_head_common_first).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"1. 如何申请调解 ?"
        res = text == u"1. 如何申请调解 ?"
        return res

    def head_help_common_online(self):
        """帮助中心常见问题在线评估"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题用在线评估
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[3]/div[2]/div[1]/a[2]/span').click()

    def verification_head_help_common_online(self):
        """校验帮助中心常见问题在线评估"""
        try:
            text = self.find_element_by_xpath(self.x_head_common_first).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"1. 如何申请 ?"
        res = text == u"1. 如何申请 ?"
        return res

    def head_help_common_law(self):
        """帮助中心常见问题法律咨询"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题法律咨询
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[3]/div[2]/div[2]/a[1]/span').click()

    def verification_head_help_common_law(self):
        """校验帮助中心常见问题法律咨询"""
        try:
            text = self.find_element_by_xpath(self.x_head_common_first).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"1. 如何进行智能咨询 ?"
        res = text == u"1. 如何进行智能咨询 ?"
        return res

    def head_help_common_result(self):
        """帮助中心常见问题查看结果"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题查看结果
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[3]/div[2]/div[2]/a[2]/span').click()

    def verification_head_help_common_result(self):
        """校验帮助中心常见问题查看结果"""
        try:
            text = self.find_element_by_xpath(self.x_head_common_first).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"1. 如何查看调解结果 ?"
        res = text == u"1. 如何查看调解结果 ?"
        return res

    def head_help_common_autonym(self):
        """帮助中心常见问题实名认证"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题实名认证
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[4]/div[2]/div[1]/a[1]/span').click()

    def verification_head_help_common_autonym(self):
        """校验帮助中心常见问题实名认证"""
        try:
            text = self.find_element_by_xpath(self.x_head_common_first).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"1. 如何完成实名认证 ?"
        res = text == u"1. 如何完成实名认证 ?"
        return res

    def head_help_common_modification(self):
        """帮助中心常见问题修改密码"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题修改密码
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[4]/div[2]/div[1]/a[2]/span').click()

    def verification_head_help_common_modification(self):
        """校验帮助中心常见问题修改密码"""
        try:
            text = self.find_element_by_xpath(self.x_head_common_first).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"1. 如何修改密码 ?"
        res = text == u"1. 如何修改密码 ?"
        return res

    def head_help_common_personal(self):
        """帮助中心常见问题个人信息"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题个人信息
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[4]/div[2]/div[2]/a[1]/span').click()

    def verification_head_help_common_personal(self):
        """校验帮助中心常见问题个人信息"""
        try:
            text = self.find_element_by_xpath(self.x_head_common_first).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"1. 如何完善个人信息 ?"
        res = text == u"1. 如何完善个人信息 ?"
        return res

    def head_help_common_signature(self):
        """帮助中心常见问题手写签名"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题手写签名
        self.find_element_by_xpath('//div[@id="app"]/div[4]/div[2]/ul/li[4]/div[2]/div[2]/a[2]/span').click()

    def verification_head_help_common_signature(self):
        """校验帮助中心常见问题手写签名"""
        try:
            text = self.find_element_by_xpath(self.x_head_common_first).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"1. 平台有哪些签名方式 ?"
        res = text == u"1. 平台有哪些签名方式 ?"
        return res

    def head_help_self_enrol(self):
        """帮助中心自助服务注册"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击注册
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[2]/ul/li[1]/a/div[1]/img').click()

    def verification_head_help_self_enrol(self):
        """校验帮助中心自助服务注册"""
        try:
            enrol = self.find_element_by_xpath('//div[@id="titleTips"]/div').text
        except:
            enrol = "*None*"
        print "result:", enrol
        print "except:", u"手机号注册"
        res = enrol == u"手机号注册"
        return res

    def head_help_self_forget(self):
        """帮助中心自助服务忘记密码"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击忘记密码
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[2]/ul/li[2]/a/div[1]/img').click()

    def verification_head_help_self_forget(self):
        """校验帮助中心自助服务忘记密码"""
        try:
            enrol = self.find_element_by_xpath('//form[@id="forgetPwdForm"]/div[7]/div/span').text
        except:
            enrol = "*None*"
        print "result:", enrol
        print "except:", u"已有账户，立即登录"
        res = enrol == u"已有账户，立即登录"
        return res

    def head_help_self_redirect(self):
        """帮助中心自助服务实名认证"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击实名认证
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[2]/ul/li[3]/a/div[1]/img').click()

    def head_help_self_consult(self):
        """帮助中心自制服务法律咨询"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击实名认证
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[2]/ul/li[4]/a/div[1]/img').click()

    def verification_head_help_self_consult(self):
        """校验帮助中心自制服务法律咨询,进入法律咨询校验方法"""
        try:
            enrol = self.find_element_by_xpath('//div[@id="app"]/div[1]/div[3]/div[1]').text
        except:
            enrol = "*None*"
        print "result:", enrol
        print "except:", u"人工咨询流程"
        res = enrol == u"人工咨询流程"
        return res

    def head_help_self_apply(self):
        """帮助中心自助服务申请调解"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击申请调解
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[2]/ul/li[5]/a/div[1]/img').click()
        # 弹出框点击确定
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()

    def head_help_self_assess(self):
        """帮助中心自助服务在线评估"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击申请调解
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[2]/ul/li[6]/a/div[1]/img').click()

    def head_help_self_result(self):
        """帮助中心自助服务查看结果"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击查看结果
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[2]/ul/li[7]/a/div[1]/img').click()
        sleep(1)
        # 弹出提示框点击确定
        self.find_element_by_xpath('//div[@id="layui-layer1"]/div[3]/a').click()

    def head_help_consult_robot(self):
        """帮助中心在线咨询智能机器人"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击智能机器人我要咨询
        self.find_element_by_xpath('//div[@id="app"]/div[6]/div[2]/div[2]/a').click()

    def head_help_comproblem(self):
        """帮助中心常见问题"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击常见问题
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div[3]/div[2]/ul/li[2]/a').click()

    def head_help_online(self):
        """帮助中心在线咨询"""
        # 点击帮助中心
        self.find_element_by_xpath(self.x_head_help).click()
        # 点击在线咨询
        self.find_element_by_xpath('//div[@id="app"]/div[1]/div[3]/div[2]/ul/li[3]/a').click()

    def mid_law(self):
        """法律咨询"""
        # 点击首页法律咨询
        self.find_element_by_xpath('//div[@id="app"]/div[3]/div/div[2]/div[1]/p[3]/a').click()

    def mid_assess(self):
        """在线评估"""
        # 点击首页在线评估
        self.find_element_by_xpath('//div[@id="app"]/div[3]/div/div[2]/div[2]/p[3]/a').click()

    def mid_mediate(self):
        """在线调解"""
        # 点击首页诉讼服务
        self.find_element_by_xpath('//div[@id="app"]/div[3]/div/div[2]/div[3]/p[3]/a').click()

    def verification_mid_mediate(self):
        """校验在线调解"""
        try:
            text = self.find_element_by_xpath('//div[@id="app"]/div[1]/div/div[1]/div[1]').text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"所有调解类别"
        res = text == u"所有调解类别"
        return res

    def mid_arbitration(self):
        """仲裁服务"""
        # 点击首页诉讼服务
        self.find_element_by_xpath('//div[@id="app"]/div[3]/div/div[2]/div[4]/p[3]/a').click()
        sleep(1)

    def mid_lawshit(self):
        """诉讼服务"""
        # 点击首页诉讼服务
        self.find_element_by_xpath('//div[@id="app"]/div[3]/div/div[2]/div[5]/p[3]/a').click()
        sleep(1)

    def tail_user_mediate(self):
        """如何申请调解"""
        # 点击如何申请调解
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[1]/li[2]/a').click()

    def tail_user_consult(self):
        """如何快速咨询"""
        # 点击如何快速咨询
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[1]/li[3]/a').click()

    def tail_user_assess(self):
        """如何申请评估"""
        # 点击如何申请评估
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[1]/li[4]/a').click()

    def tail_user_result(self):
        """如何查看结果"""
        # 点击查看结果
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[1]/li[5]/a').click()

    def tail_user_center(self):
        """调解中心"""
        # 点击调解中心
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[1]/li[6]/a').click()
        sleep(1)

    def verification_tail_user_center(self):
        """校验调解中心"""
        try:
            text = self.find_element_by_xpath('/html/body/div/div/div[3]/a').text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"邀请码登录"
        res = text == u"邀请码登录"
        return res

    def tail_service_mediate(self):
        """尾部纠纷调解"""
        # 点击纠纷调解
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[2]/li[2]/a').click()

    def tail_service_consult(self):
        """尾部法律咨询"""
        # 点击法律咨询
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[2]/li[3]/a').click()
        sleep(1)

    def tail_service_assess(self):
        """尾部在线评估"""
        # 点击在线评估
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[2]/li[4]/a').click()
        sleep(0.5)

    def tail_service_arbitration(self):
        """尾部在线仲裁"""
        # 点击在线仲裁
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[2]/li[5]/a').click()
        sleep(0.5)

    def tail_service_lawshit(self):
        """尾部诉讼服务"""
        # 点击诉讼服务
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[2]/li[6]/a').click()
        sleep(0.5)

    def tail_service_fjb(self):
        """尾部反家暴服务"""
        # 点击反家暴服务
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[2]/li[7]/a').click()
        sleep(0.5)

    def tail_law_marriage(self):
        """尾部婚姻继承"""
        # 点击尾部婚姻继承
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[3]/li[2]/a').click()

    def verification_tail_law_marriage(self):
        """校验尾部婚姻继承"""
        try:
            text = self.find_element_by_xpath(self.x_tail_law).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"婚姻继承"
        res = text == u"婚姻继承"
        return res

    def tail_law_argument(self):
        """尾部合同纠纷"""
        # 点击尾部合同纠纷
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[3]/li[3]/a').click()

    def verification_tail_law_argument(self):
        """校验尾部合同纠纷"""
        try:
            text = self.find_element_by_xpath(self.x_tail_law).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"合同纠纷"
        res = text == u"合同纠纷"
        return res

    def tail_law_traffic(self):
        """尾部交通事故"""
        # 点击尾部交通事故
        self.find_element_by_xpath('//*[@id="app"]/div[5]/div[1]/div[1]/ul[3]/li[4]/a').click()

    def verification_tail_law_traffic(self):
        """校验尾部交通事故"""
        try:
            text = self.find_element_by_xpath(self.x_tail_law).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"交通事故"
        res = text == u"交通事故"
        return res

    def tail_law_borrow(self):
        """尾部借贷纠纷"""
        # 点击尾部借贷纠纷
        self.find_element_by_xpath('//*[@id="app"]/div[5]/div[1]/div[1]/ul[3]/li[5]/a').click()

    def verification_tail_law_borrow(self):
        """校验尾部借贷纠纷"""
        try:
            text = self.find_element_by_xpath(self.x_tail_law).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"借贷纠纷"
        res = text == u"借贷纠纷"
        return res

    def tail_ours_business(self):
        """尾部商务合作"""
        # 点击尾部商务合作
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[4]/li[2]/a').click()

    def tail_ours_contant(self):
        """尾部联系方式"""
        # 点击尾部联系方式
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[4]/li[2]/a').click()

    def tail_ours_service(self):
        """尾部服务条款"""
        # 点击尾部服务条款
        self.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[4]/li[2]/a').click()

    def verification_tail_ours(self):
        """校验尾部关于我们"""
        try:
            text = self.find_element_by_xpath(self.x_head_common_first).text
        except:
            text = "*None*"
        print "result:", text
        print "except:", u"1. 商务合作"
        res = text == u"1. 商务合作"
        return res
