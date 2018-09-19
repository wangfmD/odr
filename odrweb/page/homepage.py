# coding:utf-8
from time import sleep

from selenium import webdriver

# base_url = 'https://train.odrcloud.cn:8443'
# IE11URL_ytj = 'https://train.odrcloud.cn:8443/jsp/pages/accountLogin.jsp?page=14588154523857'
# from selenium.common.exceptions import ElementNotInteractableException
from odrweb.core.initdata import init
from odrweb.page.browser import Page

base_url = init.base_url
IE11URL_ytj = 'https://uatodr.odrcloud.net/jsp/pages/accountLogin.jsp?page=14588154523857'


class HomePage(Page):

    select_user_quit_a = '//div[@id="app"]/header/div[2]/div[2]/ul/li[2]/a'  # 个人中心页面 头部的 （退出）

    def quit(self):
        self.driver.quit()

    def _get_register_text(self):
        '''获取 立刻注册 link内容: 立即注册>'''
        try:
            text = self.driver.find_element_by_xpath('//div[@id="app"]/div[2]/div[3]/a').text
        except:
            text = "**None**"
        return text

    def user_login(self, name, pwd):
        '''
        普通用户登录
        :param driver:
        :return:
        '''

        self.driver.get(base_url + "/")
        # 进入登录页面
        self.driver.find_element_by_xpath(u"//a[contains(text(),'立即登录')]").click()
        # 输入手机号码
        self.driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div/input').clear()
        self.driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div/input').send_keys(name)
        # 输入密码
        self.driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').clear()
        self.driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').send_keys(pwd)
        # 点击登录
        self.driver.find_element_by_id("login").click()
        sleep(2)
        self.driver.refresh()

    def user_head_login(self, name, pwd):
        '''
        普通用户头部登录
        :param driver:
        :return:
        '''

        self.driver.get(base_url + "/")
        # 进入登录页面
        self.driver.find_element_by_xpath('//div[@id="app"]/header/div[2]/div[2]/ul/li[1]/a').click()
        # 输入手机号码
        self.driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div/input').clear()
        self.driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div/input').send_keys(name)
        # 输入密码
        self.driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').clear()
        self.driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').send_keys(pwd)
        # 点击登录
        self.driver.find_element_by_id("login").click()
        sleep(2)
        self.driver.refresh()

    def user_login_verification(self):
        try:
            quit_link = self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[3]/a').text
        except:
            quit_link = "**None**"
        print "result: ", quit_link
        print "expect: ", u'退出'
        result = quit_link == u'退出'
        return result

    def user_login_quit(self):
        self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[3]/a').click()
        sleep(1)

    def user_login_quit_verification(self):
        login_link = ""
        try:
            login_link = self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[5]/a').text
        except:
            login_link = "**None**"
        print "result: ", login_link
        print "expect: ", u'立即登录'
        result = login_link == u'立即登录'
        return result

    def user_head_login_quit(self):
        '''用户头部登出'''
        self.driver.find_element_by_xpath(self.select_user_quit_a).click()
        sleep(1)

    def user_personal_center(self):
        ''''''
        self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[2]/a').click()
        return self.driver

    def company_login(self, name, pwd):
        '''
        企业登录
        :param driver:
        :return:
        '''
        self.driver.get(base_url + "/")
        self.driver.find_element_by_xpath(u"//a[contains(text(),'立即登录')]").click()
        sleep(2)
        self.driver.find_element_by_xpath('//ul[@id="titleTips"]/li[2]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div[1]/input').clear()
        self.driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div[1]/input').send_keys(name)
        self.driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').clear()
        self.driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').send_keys(pwd)
        sleep(2)

        # '//*[@id="titleTips"]/p'

    def mediator_login(self, name, pwd):
        '''
        调解员/办案法官登录
        :param driver: 调解员宋红波：13817765056 000000  / 办案法官：13067812519 000000
        :return:
        '''
        self.driver.get(base_url + "/")
        # 进入登录页面
        self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[1]/a').click()
        # 输入手机号码
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys(name)
        # 输入密码
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys(pwd)
        # 确定登录
        self.driver.find_element_by_xpath('//button[@id="login"]/span').click()
        sleep(2)

    def mediator_bafg_login_verification(self):
        '''

        :return:
        '''
        try:
            quit_link = self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/a').text
        except:
            quit_link = "**None**"
        print "result: ", quit_link
        print "expect: ", u'退出'
        result = quit_link == u'退出'
        return result

    def mediator_login_verification(self):
        '''

        :return:
        '''
        try:
            quit_link = self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/a[2]').text
        except:
            quit_link = "**None**"
        print "result: ", quit_link
        print "expect: ", u'退出'
        result = quit_link == u'退出'
        return result

    def mediator_quit(self):
        '''

        :return:
        '''
        self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/a[2]').click()
        sleep(1)

    def mediator_quit_bafg(self):
        '''

        :return:
        '''
        self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/a').click()
        sleep(1)

    def mediator_login_quit_sverification(self):
        '''

        :return:
        '''
        reg_link = self._get_register_text()
        print "result: ", reg_link
        print "expect: ", u'立即注册>'

        result = reg_link == u'立即注册>'
        return result

    def organization_user_login(self, name, pwd):
        '''
        机构登记员登录
        :param driver: 机构登记员：1805130007 密码：123456
        :return:
        '''
        self.driver.get(base_url + "/")
        # 进入登录页面
        self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[1]/a').click()
        # 切换
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/div/ul/li[2]').click()
        # 输入手机号码
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys(name)
        # 输入密码
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys(pwd)
        # 确定登录
        self.driver.find_element_by_xpath('//button[@id="login"]/span').click()
        sleep(3)

    def organization_user_login_verification(self):
        '''

        :return:
        '''
        try:
            # back_link = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[2]/a[2]').text
            back_link = self.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/a[2]').text
        except:
            back_link = "**None**"
        print "result: ", back_link
        print "expect: ", u'返回>'
        result = back_link == u'返回>'
        return result

    def organization_user_login_quit(self):
        '''

        :return:
        '''
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/a[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/a[2]').click()
        sleep(1)

    def organization_user_login_quit_verification(self):
        '''

        :return:
        '''
        reg_link = self._get_register_text()
        print "result: ", reg_link
        print "expect: ", u'立即注册>'

        result = reg_link == u'立即注册>'
        return result

    def organization_login(self, name, pwd):
        '''
        调解机构登录
        :param driver: 北明心理咨询演示学习机构：17612156739 123456
        :return:
        '''
        self.driver.get(base_url + "/")
        # 进入登录页面
        self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[1]/a').click()
        # 切换列表项
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/div/ul/li[3]').click()
        # 输入手机号码
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys(name)
        # 输入密码
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys(pwd)
        # 确定登录
        self.driver.find_element_by_xpath('//button[@id="login"]/span').click()
        sleep(2)

    def organization_login_verification(self):
        '''

        :return:
        '''
        try:
            quit_link = self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/a[2]').text
        except:
            quit_link = "**None**"
        print "result: ", quit_link
        print "expect: ", u'退出'
        res = quit_link == u'退出'
        return res

    def organization_login_quit(self):
        '''

        :return:
        '''
        try:
            self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/a[2]').click()
        except:
            self.driver.refresh()
            self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/a[2]').click()

        sleep(1)

    def organization_login_quit_verfication(self):
        '''

        :return:
        '''
        reg_link = self._get_register_text()
        print "result: ", reg_link
        print "expect: ", u'立即注册>'
        result = reg_link == u'立即注册>'
        # result = reg_link == u'立即登录'
        return result

    def counselor_login(self, name, pwd):
        '''
        咨询师登录  3606706616 000000
        :param driver:
        :return:
        '''
        self.driver.get(base_url + "/")
        # 进入登录页面
        self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[2]/a').click()
        # 输入手机号码
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys(name)
        # 输入密码
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys(pwd)
        # 确定登录
        self.driver.find_element_by_xpath('//button[@id="login"]/span').click()
        sleep(2)

    def counselor_login_verification(self):
        '''

        :return:
        '''
        try:
            back_link = self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/a').text
        except:
            back_link = "**None**"
        print "result: ", back_link
        print "expect: ", u'退出'
        res = back_link == u'退出'
        return res

    def counselor_quit(self):
        '''

        :return:
        '''
        self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/a').click()
        sleep(1)

    def counselor_quit_verification(self):
        '''

        :return:
        '''
        reg_link = self._get_register_text()
        print "result: ", reg_link
        print "expect: ", u'立即注册>'
        result = reg_link == u'立即注册>'
        return result

    def customer_login(self, name, pwd):
        '''
        客服人员登录 13600527465 000000
        :param driver:
        :return:
        '''
        self.driver.get(base_url + "/")
        # 进入登录页面
        self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[2]/a').click()
        # 切换列表项
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/div/ul/li[2]').click()
        # 输入手机号码
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys(name)
        # 输入密码
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
        self.driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys(pwd)
        # 确定登录
        self.driver.find_element_by_xpath('//button[@id="login"]/span').click()
        sleep(2)

    def customer_login_verification(self):
        '''

        :return:
        '''
        try:
            quit_link = self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/a[2]').text
        except:
            quit_link = "**None**"
        print "result: ", quit_link
        print "expect: ", u'退出'
        res = quit_link == u'退出'
        return res

    def customer_login_quit(self):
        '''

        :return:
        '''
        self.driver.find_element_by_xpath('/html/body/nav/div/div[2]/a[2]').click()
        sleep(1)

    def customer_login_quit_verification(self):
        '''

        :return:
        '''
        reg_link = self._get_register_text()
        print "result: ", reg_link
        print "expect: ", u'立即注册>'
        result = reg_link == u'立即注册>'
        return result

    def consult_input(self):
        '''

        :param driver:
        :return:
        '''

        self.driver.find_element_by_link_text(u"进入个人中心").click()
        self.driver.find_element_by_xpath('//div[@id="personal-content"]/div[1]/div[2]/div[1]/div[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath("//option[@value='2']").click()
        self.driver.find_element_by_id("textarea_title").click()
        self.driver.find_element_by_id("textarea_title").clear()
        self.driver.find_element_by_id("textarea_title").send_keys(u"劳动纠纷")
        self.driver.find_element_by_id("textarea_content").click()
        self.driver.find_element_by_id("textarea_content").click()
        self.driver.find_element_by_id("textarea_content").clear()
        self.driver.find_element_by_id("textarea_content").send_keys("1")
        self.driver.find_element_by_id("textarea_title").click()
        self.driver.find_element_by_id("textarea_content").click()
        self.driver.find_element_by_id("textarea_content").click()
        self.driver.find_element_by_id("textarea_content").clear()
        self.driver.find_element_by_id("textarea_content").send_keys(u"解除劳动合同")
        # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[6]/button").click()
        # driver.find_element_by_xpath("(//button[@type='button'])[2]").click()

    def login_yun(self, name, pwd):
        '''

        :param driver:
        :return:
        '''
        self.driver.get(IE11URL_ytj)
        # 进入云解登录page
        # 首页优化
        # self.driver.find_element_by_xpath('//div[@id="app"]/div[6]/div[1]/div[1]/ul[1]/li[6]/a').click()
        # 首页优化
        # self.driver.find_element_by_xpath('//div[@id="app"]/div[5]/div[1]/div[1]/ul[1]/li[6]/a').click()
        # windows = self.driver.window_handles
        # self.driver.switch_to_window(windows[1])
        # self.driver.switch_to.window(windows[1])
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/input[1]').clear()
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/input[1]').send_keys(name)
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/input[2]').clear()
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/input[2]').send_keys(pwd)
        self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/input').click()
        sleep(2)

    def login_yun_verification(self):
        '''

        :return:
        '''

        try:
            quit_link = self.driver.find_element_by_xpath(self.select_user_quit_a).text
        except:
            quit_link = "**None**"
        print "result: ", quit_link
        print "expect: ", u'退出'
        result = quit_link == u'退出'
        return result

    def login_yun_quit(self):
        '''

        :return:
        '''
        self.driver.find_element_by_xpath(self.select_user_quit_a).click()
        sleep(1)

    def login_yun_quit_verification(self):
        '''

        :return:
        '''
        try:
            login_link = self.driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[5]/a').text
        except:
            login_link = "**None**"
        print "result: ", login_link
        print "expect: ", u'立即登录'
        result = login_link == u'立即登录'
        return result


def t():
    browser = webdriver.Chrome()
    # browser=webdriver.Ie()
    browser.maximize_window()

    browser.implicitly_wait(5)

    # login(browser)
    # consult_input(browser)
    # company_login(browser)

    # mediator_login(browser)
    # organization_user_login(browser)
    # organization_login(browser)
    # mediator_login(browser)
    # customer_login(browser)
    # counselor_login(browser)
    # login_yun(browser)

    # user_login(browser, users.user_wfm['username'], users.user_wfm['pwd'])
    # mediator_login(browser, users.user_tjy['username'], users.user_tjy['pwd'])
    # mediator_login(browser, users.user_bafg['username'], users.user_bafg['pwd'])
    # organization_user_login(browser, users.user_jgdjy['username'], users.user_jgdjy['pwd'])
    # organization_login(browser, users.user_bmxlzxysxxjg['username'], users.user_bmxlzxysxxjg['pwd'])
    # customer_login(browser, users.user_kf['username'], users.user_kf['pwd'])
    # counselor_login(browser, users.user_zxs['username'], users.user_zxs['pwd'])
    # login_yun(browser, users.user_wfm['username'], users.user_wfm['pwd'])

    # organization_login(browser, users.user_shenadmin['username'], users.user_shenadmin['pwd'])
    # organization_login(browser, users.user_quadmin['username'], users.user_quadmin['pwd'])
    # organization_login(browser, users.user_shiadmin['username'], users.user_shiadmin['pwd'])


if __name__ == '__main__':
    t()
