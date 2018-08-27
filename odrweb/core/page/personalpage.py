# coding:utf-8
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select


class PersonalPage(object):

    def __init__(self, driver):
        if isinstance(driver, webdriver.Firefox):
            self.driver = driver
        if isinstance(driver, webdriver.Chrome):
            self.driver = driver
        if isinstance(driver, webdriver.Ie):
            self.driver = driver

        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def consult(self):
        '''咨询录入'''
        # 进入我要咨询输入页面
        self.driver.find_element_by_xpath('//*[@id="personal-content"]/div[1]/div[2]/div[1]/div[2]').click()
        select_xpath = '/html/body/div[2]/div/div/div/form/div[1]/div/select'
        Select(self.driver.find_element_by_xpath(select_xpath)).select_by_visible_text(u'消费维权')
        self.driver.find_element_by_xpath('//textarea[@id="textarea_title"]').send_keys(u'离婚咨询')
        self.driver.find_element_by_xpath('//textarea[@id="textarea_content"]').send_keys('ddd')
        # 申请提交
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div[6]/button').click()
        # 确认
        self.driver.find_element_by_xpath('//a[text()="是"]').click()
        sleep(5)

    def consult_input_verification(self):

        try:
            res = self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[2]/counselors/div/div[1]/div[2]/div[1]/button')
        except:
            res = ""
        # 校验搜索按键名称
        return res == u"搜索"

    # 婚姻继承
    def evaluate(self):
        '''评估录入'''
        # 进入我要评估输入页面
        self.driver.find_element_by_xpath('//div[text()="我要评估"]').click()
        select_xpath = '/html/body/div[2]/div/div/div/form/div[1]/div/select'
        Select(self.driver.find_element_by_xpath(select_xpath)).select_by_visible_text(u'消费维权')
        self.driver.find_element_by_xpath('//textarea[@id="textarea_title"]').send_keys('dasfadsf')
        self.driver.find_element_by_xpath('//textarea[@id="textarea_content"]').send_keys('das1111111111')
        # 申请提交
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/form/div[6]/button').click()
        # 确认
        self.driver.find_element_by_xpath('//a[text()="是"]').click()

    def _security_settings(self):
        ''''''
        self.driver.find_element_by_xpath('//div[@id="personal-title"]/div[2]/ul/li[2]/a').click()

    def modify_passwd(self):
        '''修改密码'''
        self._security_settings()
        # 点击修改
        self.driver.find_element_by_xpath('//div[@id="personal"]/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[4]/a').click()
        # 输入原密码
        self.driver.find_element_by_xpath('//div[@id="login_password"]/div/div/div[2]/form/div[1]/div/div[1]/input').send_keys('100200')
        # 输入新密码
        self.driver.find_element_by_xpath('//div[@id="login_password"]/div/div/div[2]/form/div[2]/div/div/input').send_keys('100200')
        # 确认新密码
        self.driver.find_element_by_xpath('//div[@id="login_password"]/div/div/div[2]/form/div[3]/div/div/input').send_keys('100200')
        # 提交
        self.driver.find_element_by_xpath('//div[@id="login_password"]/div/div/div[2]/form/div[4]/div/button[1]/span').click()

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
