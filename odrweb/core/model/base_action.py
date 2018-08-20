# coding:utf-8
from time import sleep
from selenium import webdriver


# base_url = 'https://train.odrcloud.cn:8443/'
base_url = "https://uatodr.odrcloud.net"


def user_login(driver):
    '''
    普通用户登录
    :param driver:
    :return:
    '''

    driver.get(base_url + "/")
    # 进入登录页面
    driver.find_element_by_xpath(u"//a[contains(text(),'立即登录')]").click()
    # 输入手机号码
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div/input').clear()
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div/input').send_keys("13913031374")
    # 输入密码
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').send_keys("100200")
    # 点击登录
    driver.find_element_by_id("login").click()
    sleep(2)
    driver.refresh()


def company_login(driver):
    '''
    企业登录
    :param driver:
    :return:
    '''
    driver.get(base_url + "/")
    driver.find_element_by_xpath(u"//a[contains(text(),'立即登录')]").click()
    sleep(2)
    driver.find_element_by_xpath('//ul[@id="titleTips"]/li[2]').click()
    sleep(2)
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div[1]/input').clear()
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div[1]/input').send_keys('')
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').send_keys('')

    # '//*[@id="titleTips"]/p'



def mediator_login(driver):
    '''
    调解员/办案法官登录
    :param driver:
    :return:
    '''
    driver.get(base_url + "/")
    # 进入登录页面
    driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[1]/a').click()
    # 输入手机号码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys("13817765056")
    # 输入密码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys('000000')
    # 确定登录
    driver.find_element_by_xpath('//button[@id="login"]/span').click()
    sleep(4)


def organization_user_login(driver):
    '''
    机构登记员登录
    :param driver:
    :return:
    '''
    driver.get(base_url + "/")
    # 进入登录页面
    driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[1]/a').click()
    # 切换
    driver.find_element_by_xpath('//div[@id="loginForm"]/div/ul/li[2]').click()
    # 输入手机号码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys("1805130007")
    # 输入密码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys('123456')
    # 确定登录
    driver.find_element_by_xpath('//button[@id="login"]/span').click()
    sleep(4)

def organization_login(driver):
    '''
    调解机构登录
    :param driver:
    :return:
    '''
    driver.get(base_url + "/")
    # 进入登录页面
    driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[1]/a').click()
    # 切换列表项
    driver.find_element_by_xpath('//div[@id="loginForm"]/div/ul/li[3]').click()
    # 输入手机号码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys("17612156739")
    # 输入密码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys('123456')
    # 确定登录
    driver.find_element_by_xpath('//button[@id="login"]/span').click()
    sleep(10)


def counselor_login(driver):
    '''
    咨询师登录
    :param driver:
    :return:
    '''


def customer_login(driver):
    '''
    客服人员登录
    :param driver:
    :return:
    '''
    driver.get(base_url + "/")
    # 进入登录页面
    driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[2]/a').click()
    # 切换列表项
    driver.find_element_by_xpath('//div[@id="loginForm"]/div/ul/li[2]').click()
    # 输入手机号码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys("13600527465")
    # 输入密码
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
    driver.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys('000000')
    # 确定登录
    driver.find_element_by_xpath('//button[@id="login"]/span').click()
    sleep(10)



def consult_input(driver):
    '''

    :param driver:
    :return:
    '''

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


def test():
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
    customer_login(browser)

if __name__ == '__main__':
    test()