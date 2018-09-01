# -*- coding: utf-8 -*-

from odrweb.core.parsexls import XlsFile
from selenium import webdriver
import time
url = 'https://uatodr.odrcloud.net'


# def use():
#     xls = XlsFile(xls_name=r"test_jf.xlsx")
#     rowlist = xls.parse_xls_by_row("gentestdata")
#     # for it in rowlist:
#     #     for k in it:
#     #         jf_info =  k, ":", it[k]
#     #         print jf_info
#     jf_info = rowlist[0]


def add_jf_tiaojiey_tj():


    xls = XlsFile(xls_name=r"test_jf.xlsx")
    rowlist = xls.parse_xls_by_row("gentestdata")
    # for it in rowlist:
    #     for k in it:
    #         jf_info =  k, ":", it[k]
    #         print jf_info
    jf_info = rowlist[0]


    chrome.get(url)
    # 进入登录页面
    chrome.find_element_by_xpath('//div[@id="app"]/div[1]/div[2]/div[6]/span[1]/a').click()
    # 输入手机号码
    chrome.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').clear()
    chrome.find_element_by_xpath('//div[@id="loginForm"]/form/div[1]/div/div/input').send_keys('13817765056')
    # 输入密码
    chrome.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div/input').clear()
    chrome.find_element_by_xpath('//div[@id="loginForm"]/form/div[2]/div/div[1]/input').send_keys('000000')
    # 确定登录
    chrome.find_element_by_xpath('//button[@id="login"]/span').click()
    time.sleep(2)
    chrome.find_element_by_xpath("/html/body/div[4]/div[1]/button[2]").click()
    # 点击案件登记列表
    chrome.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/a[2]').click()
    # 点击登记纠纷添加
    chrome.find_element_by_css_selector("textarea.el-textarea__inner").clear()
    chrome.find_element_by_css_selector("textarea.el-textarea__inner").send_keys(jf_info["jf_desc"])
    chrome.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").clear()
    chrome.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").send_keys(jf_info["jf_appeal"])
    chrome.find_element_by_css_selector("span.city-picker-span").click()
    chrome.find_element_by_link_text(u"浙江省").click()
    chrome.find_element_by_link_text(u"杭州市").click()
    chrome.find_element_by_link_text(u"上城区").click()
    chrome.find_element_by_link_text(u"清波街道").click()
    chrome.find_element_by_link_text(u"清波门社区").click()
    time.sleep(1)
    # driver.find_element_by_css_selector("button.choice").click()
    chrome.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").clear()
    chrome.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").send_keys(jf_info["applicant"])
    chrome.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").clear()
    chrome.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").send_keys(jf_info["applicant_tel"])
    chrome.find_element_by_xpath("(//input[@type='text'])[8]").clear()
    chrome.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(jf_info["applicant_id"])
    time.sleep(1)
    chrome.find_element_by_xpath('//div[@id="app"]/div/div[3]/div/div[1]/form/div/div[6]/div/span').click()
    time.sleep(1)
    chrome.find_element_by_link_text(u"浙江省").click()
    chrome.find_element_by_link_text(u"杭州市").click()
    chrome.find_element_by_link_text(u"上城区").click()
    chrome.find_element_by_link_text(u"清波街道").click()
    chrome.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").click()
    chrome.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").clear()
    chrome.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").send_keys(jf_info["applicant_addr"])
    chrome.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").clear()
    chrome.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").send_keys(jf_info["disputer"])
    chrome.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").clear()
    chrome.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").send_keys(jf_info["disputer_tel"])
    chrome.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[2]/p[3]/span[2]').click()
    time.sleep(1)
    chrome.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]/span').click()
    time.sleep(2)
    chrome.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
    # 直接提交方式


if __name__ == '__main__':
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    add_jf_tiaojiey_tj()