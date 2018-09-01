# coding:utf-8
from time import sleep

from selenium import webdriver

from odrweb.core.initdata import users
from odrweb.page.homepage import HomePage
homepage = HomePage()

# base_url = 'https://train.odrcloud.cn:8443/'
base_url = "https://uatodr.odrcloud.net"

def different_identity():
    '''不同身份选择'''

    # 点击进入我要调解
    homepage.find_element_by_xpath('//div[@id="personal-content"]/div[1]/div[2]/div[3]/div[2]').click()
    # 弹出提示框
    homepage.find_element_by_xpath('//div[@id="layui-layer1"]/div[3]/a[1]').click()
    # 点击选择我是申请人申请调解
    homepage.find_element_by_xpath('//div[@id="app"]/div[1]/div[1]/div/div[2]/div[2]/div').click()

    # 选择纠纷类型
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[1]/div/div/label[2]/span[2]').click()
    # 填写纠纷描述、我的诉求
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[2]/div/div/div/textarea').send_keys('test')
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[3]/div/div/div/textarea').send_keys('test')
    # 选择纠纷发生地
    homepage.find_element_by_xpath( '//div[@id="app"]/div/div[2]/form/div[4]/div/div/div/div[2]/div[1]/dl[4]/dd/a[5]').click()
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[4]/div/div/div/div[2]/div[2]/dl/dd/a[1]').click()
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[4]/div/div/div/div[2]/div[3]/dl/dd/a[1]').click()
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[4]/div/div/div/div[2]/div[4]/dl/dd/a[1]').click()
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[4]/div/div/div/div[2]/div[5]/dl/dd/a[1]').click()
    # 选择调解机构
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[2]/form/div[6]/div/div/input').click()
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[3]/div/div/div[2]/div[2]/ul/li[1]/button').click()
    # 点击下一步
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[5]').click()

    # 选择申请人为法人
    homepage.find_element_by_xpath( '//div[@id="app"]/div/div[3]/div[2]/div[1]/form/div/div[1]/div/div/label[2]/span[2]').click()
    # 填写申请人企业信息、社会信用代码
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[3]/div[2]/div[1]/form/div/div[2]/div/input').send_keys( u'北明测试')
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[3]/div[2]/div[1]/form/div/div[3]/div/input').send_keys( '123456789123456789')
    # 点击下一步进入填写被申请人信息
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[3]/div[2]/div[2]/p[3]/span[2]').click()

    # 选择被申请人为法人
    homepage.find_element_by_xpath( '//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[1]/div/div/label[2]/span[2]').click()
    # 填写被申请人企业名称
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[2]/div/div/input').send_keys(u'北明测试被申请方 ')
    # 填写被申请人社会信用代码
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[3]/div/input').send_keys('123456789123456')
    # 填写被申请人法定代表人信息
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[4]/div/div/input').send_keys(u'钱桂林')
    # 被申请人联系电话
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[6]/div/div/input').send_keys('13160077223')
    # 被申请人单位地址
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[8]/div/span[2]').click()
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[8]/div/div/div/div[2]/div[1]/dl[4]/dd/a[5]').click()
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[8]/div/div/div/div[2]/div[2]/dl/dd/a[1]').click()
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[8]/div/div/div/div[2]/div[3]/dl/dd/a[1]').click()
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[8]/div/div/div/div[2]/div[4]/dl/dd/a[1]').click()
    # 被申请人详细地址
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[9]/div/input').send_keys('addr')
    # 点击提交
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[2]/p[3]/span[2]').click()
    # 弹出提示框，点击确定
    homepage.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()



    # 选择申请人为非法人组织
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[3]/div[2]/div[1]/form/div/div[1]/div/div/label[3]/span[2]').click()
    # 选择被申请人为非法人组织
    homepage.find_element_by_xpath('//div[@id="app"]/div/div[4]/div[2]/div[1]/form/div/div[1]/div/div/label[3]/span[2]').click()


