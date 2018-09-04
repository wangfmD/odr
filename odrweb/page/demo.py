# coding:utf-8
# from time import sleep
# from selenium import webdriver
#
# # url = 'https://train.odrcloud.cn:8443/'
# base_url = "https://uatodr.odrcloud.net"
#
# def login(driver):
#     driver.get(base_url + "/")
#     driver.find_element_by_xpath(u"//a[contains(text(),'立即登录')]").click()
#     driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div/input').clear()
#     driver.find_element_by_xpath('//form[@id="loginForm"]/div[1]/div/div/input').send_keys("13913031374")
#     driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').clear()
#     driver.find_element_by_xpath('//form[@id="loginForm"]/div[2]/div/div/input').send_keys("100200")
#     driver.find_element_by_id("login").click()
#     sleep(2)
#     driver.refresh()
#
#
#
# def test_consult_py(driver):
#
#     driver.find_element_by_link_text(u"进入个人中心").click()
#     # driver.find_element_by_name("type").click()
#     driver.find_element_by_xpath('//div[@id="personal-content"]/div[1]/div[2]/div[1]/div[2]').click()
#     sleep(1)
#     driver.find_element_by_xpath("//option[@value='2']").click()
#     driver.find_element_by_id("textarea_title").click()
#     driver.find_element_by_id("textarea_title").clear()
#     driver.find_element_by_id("textarea_title").send_keys(u"劳动纠纷")
#     driver.find_element_by_id("textarea_content").click()
#     driver.find_element_by_id("textarea_content").click()
#     driver.find_element_by_id("textarea_content").clear()
#     driver.find_element_by_id("textarea_content").send_keys("1")
#     driver.find_element_by_id("textarea_title").click()
#     driver.find_element_by_id("textarea_content").click()
#     driver.find_element_by_id("textarea_content").click()
#     driver.find_element_by_id("textarea_content").clear()
#     driver.find_element_by_id("textarea_content").send_keys(u"解除劳动合同")
#     driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/div[6]/button").click()
#     # driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
#
# def test():
#     # browser = webdriver.Chrome()
#     browser=webdriver.Ie()
#     browser.maximize_window()
#
#     browser.implicitly_wait(5)
#
#     login(browser)
#     test_consult_py(browser)

if __name__ == '__main__':
    # test()
    from browser import TYPES
    print TYPES