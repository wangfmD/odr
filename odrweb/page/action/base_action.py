# coding:utf-8
from time import sleep

from selenium import webdriver

from odrweb.core.initdata import users

# base_url = 'https://train.odrcloud.cn:8443/'
base_url = "https://uatodr.odrcloud.net"


def user_login(driver, name, pwd):
    """
    普通用户登录
    :param driver:
    :return:
    """

    driver.get(base_url + "/")
    # 进入登录页面
    driver.find_element_by_xpath(u"//a[contains(text(),'立即登录')]").click()
    # 输入手机号码
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div/input').clear()
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div/input').send_keys(name)
    # 输入密码
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').send_keys(pwd)
    # 点击登录
    driver.find_element_by_id("login").click()
    sleep(2)
    driver.refresh()


def company_login(driver, name, pwd):
    """
    企业登录
    :param driver:
    :return:
    """
    driver.get(base_url + "/")
    driver.find_element_by_xpath(u"//a[contains(text(),'立即登录')]").click()
    sleep(2)
    driver.find_element_by_xpath('//ul[@id="titleTips"]/li[2]').click()
    sleep(2)
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div[1]/input').clear()
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div[1]/input').send_keys(name)
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').send_keys(pwd)

    # '//*[@id="titleTips"]/p'


def mediator_login(driver, name, pwd):
    """
    调解员/办案法官登录
    :param driver:
    :return:
    """
    driver.get(base_url + "/")
    # 进入登录页面
    driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[1]/a').click()
    # 输入手机号码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys(name)
    # 输入密码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys(pwd)
    # 确定登录
    driver.find_element_by_xpath('//button[@id="login"]/span').click()
    sleep(4)


def organization_user_login(driver, name, pwd):
    """
    机构登记员登录
    :param driver:
    :return:
    """
    driver.get(base_url + "/")
    # 进入登录页面
    driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[1]/a').click()
    # 切换
    driver.find_element_by_xpath('//div[@id="loginForm"]/div/ul/li[2]').click()
    # 输入手机号码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys(name)
    # 输入密码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys(pwd)
    # 确定登录
    driver.find_element_by_xpath('//button[@id="login"]/span').click()
    sleep(4)


def organization_login(driver, name, pwd):
    """
    调解机构登录
    :param driver:
    :return:
    """
    driver.get(base_url + "/")
    # 进入登录页面
    driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[1]/a').click()
    # 切换列表项
    driver.find_element_by_xpath('//div[@id="loginForm"]/div/ul/li[3]').click()
    # 输入手机号码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys(name)
    # 输入密码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys(pwd)
    # 确定登录
    driver.find_element_by_xpath('//button[@id="login"]/span').click()
    sleep(10)


def counselor_login(driver, name, pwd):
    """
    咨询师登录
    :param driver:
    :return:
    """
    driver.get(base_url + "/")
    # 进入登录页面
    driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[2]/a').click()
    # 输入手机号码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys(name)
    # 输入密码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys(pwd)
    # 确定登录
    driver.find_element_by_xpath('//button[@id="login"]/span').click()
    sleep(10)


def customer_login(driver, name, pwd):
    """
    客服人员登录
    :param driver:
    :return:
    """
    driver.get(base_url + "/")
    # 进入登录页面
    driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[2]/a').click()
    # 切换列表项
    driver.find_element_by_xpath('//div[@id="loginForm"]/div/ul/li[2]').click()
    # 输入手机号码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys(name)
    # 输入密码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys(pwd)
    # 确定登录
    driver.find_element_by_xpath('//button[@id="login"]/span').click()
    sleep(10)


def consult_input(driver):
    """

    :param driver:
    :return:
    """

    driver.find_element_by_link_text(u"进入个人中心").click()
    # driver.find_element_by_name("type").click()
    driver.find_element_by_xpath('//div[@id="personal-content"]/div[1]/div[2]/div[1]/div[2]').click()
    sleep(1)
    driver.find_element_by_xpath("//option[@value='2']").click()
    driver.find_element_by_id("textarea_title").click()
    driver.find_element_by_id("textarea_title").clear()
    driver.find_element_by_id("textarea_title").send_keys(u"劳动纠纷")
    driver.find_element_by_id("textarea_content").click()
    driver.find_element_by_id("textarea_content").click()
    driver.find_element_by_id("textarea_content").clear()
    driver.find_element_by_id("textarea_content").send_keys("1")
    driver.find_element_by_id("textarea_title").click()
    driver.find_element_by_id("textarea_content").click()
    driver.find_element_by_id("textarea_content").click()
    driver.find_element_by_id("textarea_content").clear()
    driver.find_element_by_id("textarea_content").send_keys(u"解除劳动合同")
    # driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[6]/button").click()
    # driver.find_element_by_xpath("(//button[@type='button'])[2]").click()


def login_yun(driver, name, pwd):
    """

    :param driver:
    :return:
    """
    driver.get(base_url + "/")
    # 进入云解登录page
    driver.find_element_by_xpath('//div[@id="app"]/div[6]/div[1]/div[1]/ul[1]/li[6]/a').click()
    windows = driver.window_handles
    driver.switch_to_window(windows[1])
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/input[1]').clear()
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/input[1]').send_keys(name)
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/input[2]').clear()
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/input[2]').send_keys(pwd)
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/input').click()
    sleep(10)





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
    organization_login(browser, users.user_quadmin['username'], users.user_quadmin['pwd'])
    # organization_login(browser, users.user_shiadmin['username'], users.user_shiadmin['pwd'])


if __name__ == '__main__':
    t()
