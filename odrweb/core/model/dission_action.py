# -*- coding: utf-8 -*-
from selenium import webdriver
import time


def test_jigoudjy_bctj(driver):

    '''
    机构登记员登记纠纷
    保存提交
    '''
    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/form/div/div/div/label[2]/span[2]").click()
    driver.find_element_by_css_selector("textarea.el-textarea__inner").clear()
    driver.find_element_by_css_selector("textarea.el-textarea__inner").send_keys("test2")
    driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").clear()
    driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").send_keys("test2")
    driver.find_element_by_css_selector("span.city-picker-span").click()
    driver.find_element_by_link_text(u"浙江省").click()
    driver.find_element_by_link_text(u"杭州市").click()
    driver.find_element_by_link_text(u"上城区").click()
    driver.find_element_by_link_text(u"清波街道").click()
    driver.find_element_by_link_text(u"清波门社区").click()
    driver.find_element_by_css_selector(
        "div.el-form-item__content > div > div.el-input > input.el-input__inner").click()
    time.sleep(1)
    driver.find_element_by_css_selector("button.choice").click()
    driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").send_keys(u"徐传珠")
    driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").send_keys("15295745648")
    driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("321281199507077775")
    time.sleep(1)
    driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/div/div[1]/form/div/div[6]/div/span').click()
    time.sleep(1)
    driver.find_element_by_link_text(u"浙江省").click()
    driver.find_element_by_link_text(u"杭州市").click()
    driver.find_element_by_link_text(u"上城区").click()
    driver.find_element_by_link_text(u"清波街道").click()
    driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").click()
    driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").send_keys("test2")
    driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").send_keys(u"钱桂林")
    driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").send_keys("13160077223")
    driver.find_element_by_css_selector("span.lastStep").click()
    time.sleep(1)
    driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
    time.sleep(1)
    driver.find_element_by_link_text(u"纠纷预览").click()
    driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
    time.sleep(1)
    driver.find_element_by_link_text(u"不发送").click()
    time.sleep(2)
    driver.find_element_by_xpath('//div[@id="layui-layer2"]/div[3]/a').click()
    driver.find_element_by_css_selector("button[type=\"button\"]").click()
    driver.find_element_by_link_text(u"机构登记").click()
    driver.find_element_by_xpath(u"(//a[contains(text(),'返回>')])[2]").click()
    # 保存提交方式



def test_jigoudjy_tj(driver):

    '''
    机构登记员
    提交
    :param driver:
    :return:
    '''

    driver.find_element_by_xpath("//div[@id='app']/div/div[2]/form/div/div/div/label[2]/span[2]").click()
    # driver.find_element_by_xpath(u"//input[@value='消费维权']").click()
    driver.find_element_by_css_selector("textarea.el-textarea__inner").clear()
    driver.find_element_by_css_selector("textarea.el-textarea__inner").send_keys("test2")
    driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").clear()
    driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").send_keys("test2")
    driver.find_element_by_css_selector("span.city-picker-span").click()
    driver.find_element_by_link_text(u"浙江省").click()
    driver.find_element_by_link_text(u"杭州市").click()
    driver.find_element_by_link_text(u"上城区").click()
    driver.find_element_by_link_text(u"清波街道").click()
    driver.find_element_by_link_text(u"清波门社区").click()
    driver.find_element_by_css_selector(
        "div.el-form-item__content > div > div.el-input > input.el-input__inner").click()
    time.sleep(1)
    driver.find_element_by_css_selector("button.choice").click()
    driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").send_keys(u"徐传珠")
    driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").send_keys("15295745648")
    driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("321281199507077775")
    time.sleep(1)
    driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/div/div[1]/form/div/div[6]/div/span').click()
    time.sleep(1)
    driver.find_element_by_link_text(u"浙江省").click()
    driver.find_element_by_link_text(u"杭州市").click()
    driver.find_element_by_link_text(u"上城区").click()
    driver.find_element_by_link_text(u"清波街道").click()
    driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").click()
    driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").send_keys("test2")
    driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").send_keys(u"钱桂林")
    driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").send_keys("13160077223")
    driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[2]/p[3]/span[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
    # 直接点击保存方式


def test_tiaojiey_tj(driver):

    '''
    调解员登记纠纷
    提交
    :param driver:
    :return:
    '''

    driver.find_element_by_xpath("/html/body/div[4]/div[1]/button[2]").click()
    # 点击案件登记列表
    driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/a[2]').click()
    # 点击登记纠纷添加
    # driver.find_element_by_xpath(u"//input[@value='消费维权']").click()
    driver.find_element_by_css_selector("textarea.el-textarea__inner").clear()
    driver.find_element_by_css_selector("textarea.el-textarea__inner").send_keys("test2")
    driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").clear()
    driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").send_keys("test2")
    driver.find_element_by_css_selector("span.city-picker-span").click()
    driver.find_element_by_link_text(u"浙江省").click()
    driver.find_element_by_link_text(u"杭州市").click()
    driver.find_element_by_link_text(u"上城区").click()
    driver.find_element_by_link_text(u"清波街道").click()
    driver.find_element_by_link_text(u"清波门社区").click()
    # driver.find_element_by_css_selector(
    #     "div.el-form-item__content > div > div.el-input > input.el-input__inner").click()
    time.sleep(1)
    # driver.find_element_by_css_selector("button.choice").click()
    driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").send_keys(u"徐传珠")
    driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").send_keys("15295745648")
    driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("321281199507077775")
    time.sleep(1)
    driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/div/div[1]/form/div/div[6]/div/span').click()
    time.sleep(1)
    driver.find_element_by_link_text(u"浙江省").click()
    driver.find_element_by_link_text(u"杭州市").click()
    driver.find_element_by_link_text(u"上城区").click()
    driver.find_element_by_link_text(u"清波街道").click()
    driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").click()
    driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").send_keys("test2")
    driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").send_keys(u"钱桂林")
    driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").send_keys("13160077223")
    driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[2]/p[3]/span[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]/span').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
    # 直接提交方式


def test_tiaojiey_bctj(driver):

    '''
    调解员登记纠纷
    保存提交
    :param driver:
    :return:
    '''

    driver.find_element_by_xpath("/html/body/div[4]/div[1]/button[2]").click()
    # 点击案件登记列表
    driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/a[2]').click()
    # 点击登记纠纷添加
    # driver.find_element_by_xpath(u"//input[@value='消费维权']").click()
    driver.find_element_by_css_selector("textarea.el-textarea__inner").clear()
    driver.find_element_by_css_selector("textarea.el-textarea__inner").send_keys("test2")
    driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").clear()
    driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").send_keys("test2")
    driver.find_element_by_css_selector("span.city-picker-span").click()
    driver.find_element_by_link_text(u"浙江省").click()
    driver.find_element_by_link_text(u"杭州市").click()
    driver.find_element_by_link_text(u"上城区").click()
    driver.find_element_by_link_text(u"清波街道").click()
    driver.find_element_by_link_text(u"清波门社区").click()
    time.sleep(1)
    driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").send_keys(u"徐传珠")
    driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").send_keys("15295745648")
    driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("321281199507077775")
    time.sleep(1)
    driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/div/div[1]/form/div/div[6]/div/span').click()
    time.sleep(1)
    driver.find_element_by_link_text(u"浙江省").click()
    driver.find_element_by_link_text(u"杭州市").click()
    driver.find_element_by_link_text(u"上城区").click()
    driver.find_element_by_link_text(u"清波街道").click()
    driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").click()
    driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").send_keys("test2")
    driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").send_keys(u"钱桂林")
    driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").clear()
    driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").send_keys("13160077223")
    driver.find_element_by_css_selector("span.lastStep").click()
    time.sleep(1)
    driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
    time.sleep(1)
    driver.find_element_by_link_text(u"纠纷预览").click()
    driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
    time.sleep(1)
    driver.find_element_by_link_text(u"不发送").click()
    time.sleep(3)
    driver.find_element_by_xpath('//div[@id="layui-layer2"]/div[3]/a').click()
    driver.find_element_by_css_selector("button[type=\"button\"]").click()


def yonghu_sqtj(driver):

    '''
    用户申请调解
    :param chrome:
    :return:
    '''

    driver.find_element_by_xpath('//div[@id="personal-content"]/div[1]/div[2]/div[3]/div[2]').click()
    #点击选择我要调解
    time.sleep(1)
    driver.find_element_by_xpath('//div[@id="layui-layer1"]/div[3]/a[1]').click()
    #弹出提示框并点击
    driver.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div/div[2]/div[2]/div').click()
    #选择申请人身份为我是申请人
    time.sleep(1)
    driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div/label[2]/span[2]').click()
    #选择调解类型
    driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div/textarea').send_keys('test')
    driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[3]/div/div/div/textarea').send_keys('test')
    #输入纠纷描述、我的诉求
    driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[4]/div/span[2]').click()
    driver.find_element_by_link_text(u"浙江省").click()
    driver.find_element_by_link_text(u"杭州市").click()
    driver.find_element_by_link_text(u"上城区").click()
    driver.find_element_by_link_text(u"清波街道").click()
    #选择纠纷发生地
    driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[6]/div/div[1]/input').click()
    time.sleep(1)
    driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div[2]/ul/li[1]/button').click()
    driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
    #选择机构
    time.sleep(1)
    driver.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[5]').click()
    #点击下一步进入填写申请人信息页面
    driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/div[2]/div[2]/p[3]/span[2]').click()
    #申请人信息默认填写，直接点击下一步进入被申请人信息填写
    time.sleep(1)
    driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[2]/div/div/input').send_keys(u'钱桂林')
    driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[4]/div/div/input').send_keys('13160077223')
    #填写被申请人姓名、电话号码
    driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[2]/p[3]/span[2]').click()
    #点击提交弹出提示框
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
    #点击提示框确定
    time.sleep(1)
    driver.find_element_by_xpath('//div[@id="mediate"]/div[1]/div[4]/div[2]/a[1]').click()
    #点击查看纠纷详情
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/section[1]/button').click()
    #点击返回列表
    time.sleep(1)
    driver.find_element_by_xpath('//div[@id="app"]/header/div[1]/div[2]/ul/li[2]/a').click()
    #点击退出，退出页面返回登陆首页


def t():
    browser = webdriver.Chrome()
    # browser=webdriver.Ie()
    browser.maximize_window()

    browser.implicitly_wait(5)


if __name__ == '__main__':
    t()









