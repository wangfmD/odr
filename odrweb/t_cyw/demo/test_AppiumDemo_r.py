# -*- coding: utf-8 -*-
import os
import re
import unittest
from time import sleep
import sys
from appium import webdriver
import traceback
from appium.webdriver.common.touch_action import TouchAction

reload(sys)
sys.setdefaultencoding("utf-8")

def swipe_down(driver, t=500, n=1):
    '''向下拉滑'''
    size = driver.get_window_size()
    x1 = size['width'] * 0.5          # x坐标
    y1 = size['height'] * 0.25        # 起始y坐标
    y2 = size['height'] * 0.75         # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def swipe_up(driver, t=500, n=1):
    '''向上推滑'''
    size = driver.get_window_size()
    x1 = size['width'] * 0.5          # x坐标
    y1 = size['height'] * 0.75        # 起始y坐标
    y2 = size['height'] * 0.25         # 终点y坐标
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


def tap(driver, getx, gety, **kwargs):
    a = getx/float(kwargs["width"])
    b = gety/float(kwargs["height"])
    #  获取当前手机屏幕大小x,y
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    #  屏幕坐标乘以系数即为用户要点击位置的具体坐标
    driver.tap([(a*x, b*y)])

def from_adb_input_text(devicecode, text):
    commad = 'adb -s ' + devicecode + ' shell input text ' + text
    os.popen(commad)

def from_adb_tap(driver, devicecode, getx, gety, **kwargs):
    a = getx/float(kwargs["width"])
    b = gety/float(kwargs["height"])
    #  获取当前手机屏幕大小x,y
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    targetx = str(int(a * x))
    targety = str(int(b * y))
    #  屏幕坐标乘以系数即为用户要点击位置的具体坐标
    commad = 'adb -s ' + devicecode + ' shell input tap ' + targetx + ' ' + targety
    print(commad)
    os.popen(commad)


#设备码获取
cmd = os.popen("adb devices")
key= cmd.read()
s= re.findall("(.*).*\tdevice",key)
phonecode=s[0]
print("当前手机设备码："+phonecode)



HUAWEI_MATE_8 = {"width": "1080",
                 "height": "1810"
                 }


desired_caps = {}
desired_caps['automationName']='Appium'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0.0'
desired_caps['deviceName'] = 'Huawei Mate 8'
desired_caps['appPackage'] = 'com.tencent.mm'
desired_caps['appActivity'] = '.ui.LauncherUI'
desired_caps['noReset'] = True
desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:appbrand1'}
#desired_caps["unicodeKeyboard"] = "True"
#desired_caps["resetKeyboard"] = "True"


class AppiumDemo(unittest.TestCase):
    """
    微信小程序Demo
    """

    def setUp(self):
        print "\n--------------------"

    def tearDown(self):
        print "\n--------------------"

    def test_01(self):
        """
        案件录入
        :return:
        """
        print("正在启动微信")
        self.dr = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        print("微信启动成功")
        print('==========================================')
        sleep(4)

        print('尝试下拉微信顶部展示小程序列表')
        swipe_down(self.dr)
        print('成功')
        print('==========================================')
        sleep(1)

        print('进入微法院')
        self.dr.find_element_by_xpath("//android.widget.TextView[@text='江苏微法院']").click()
        print('成功')
        print('==========================================')
        sleep(5)

        print('进入诉讼服务')
        self.dr.find_element_by_xpath("//android.widget.TextView[@text='诉讼服务']").click()
        print('成功')
        print('==========================================')
        sleep(4)

        print('点击在线立案')
        from_adb_tap(self.dr, phonecode, 669, 954, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')
        sleep(3)

        print('点击涉及案由')
        from_adb_tap(self.dr, phonecode, 422, 400, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')
        sleep(1.5)

        print('选择人格权纠纷')
        from_adb_tap(self.dr, phonecode, 64, 276, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')
        sleep(0.5)

        print('选择确定')
        from_adb_tap(self.dr, phonecode, 516, 1631, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')
        sleep(0.5)

        print('提交确定')
        from_adb_tap(self.dr, phonecode, 830, 1069, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')
        sleep(2)


        print('填写申请人电话')
        self.dr.find_element_by_xpath("//android.view.View[@content-desc='申请人电话']/../../android.view.View[2]/android.view.View/android.view.View/android.view.View[@content-desc='必填']").click()
        sleep(1)
        print('输入法切换成数字模式（根据安装的输入法和键位布局，每部手机都可能不一样！如想保持一致尽量用安卓默认的原始输入法，否则需要个性化设置！）')
        tap(self.dr, 268, 1753, **HUAWEI_MATE_8)
        from_adb_input_text(phonecode, '17625908729')
        print('成功')
        print('==========================================')
        sleep(0.5)

        print('填写申请标的金额')
        self.dr.find_element_by_xpath("//android.view.View[@content-desc='申请标的金额']/../../android.view.View[2]").click()
        print('输入法切换成数字模式（根据安装的输入法和键位布局，每部手机都可能不一样！如想保持一致尽量用安卓默认的原始输入法，否则需要个性化设置！）')
        from_adb_input_text(phonecode, '100')
        tap(self.dr, 1044, 1042, **HUAWEI_MATE_8)
        sleep(2)
        tap(self.dr, 541, 1080, **HUAWEI_MATE_8)
        sleep(0.5)
        print('成功')
        print('==========================================')

        print('添加原告')
        tap(self.dr, 524, 1300, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')
        sleep(0.5)

        print('原告自然人')
        tap(self.dr, 506, 661, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')
        sleep(1)

        print('电话')
        tap(self.dr, 382, 910, **HUAWEI_MATE_8)
        sleep(0.5)
        from_adb_input_text(phonecode, '17625908729')
        tap(self.dr, 1044, 1042, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')
        sleep(0.5)


        print('地址')
        self.dr.find_element_by_xpath("//android.view.View[@content-desc='地址']/../../android.view.View[2]/android.view.View").click()
        sleep(0.5)
        from_adb_input_text(phonecode, 'jiangsunanjing')
        print("拼音输入完毕")
        from_adb_tap(self.dr, phonecode, 240, 1800, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')
        sleep(2)

        print("提交")
        #dr.find_element_by_xpath("//android.view.View[@content-desc='提交']").click()
        from_adb_tap(self.dr, phonecode, 530, 1660, **HUAWEI_MATE_8)
        from_adb_tap(self.dr, phonecode, 530, 1660, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')
        sleep(2)

        print('选择确定')
        from_adb_tap(self.dr, phonecode, 820, 1060, **HUAWEI_MATE_8)  # 820 1060
        print('成功')
        print('==========================================')
        sleep(3)

        print('添加被告')
        from_adb_tap(self.dr, phonecode, 500, 1520, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')
        sleep(2)

        print('被告自然人')
        tap(self.dr, 506, 661, **HUAWEI_MATE_8)
        sleep(3)
        print('成功')
        print('==========================================')


        print('被告自然人')
        tap(self.dr, 400, 280, **HUAWEI_MATE_8)
        sleep(2)
        print('成功')
        print('==========================================')


        print('被告姓名')
        tap(self.dr, 400, 280, **HUAWEI_MATE_8)
        sleep(1)
        from_adb_input_text(phonecode, 'wangfaming')
        print("拼音输入完毕")
        from_adb_tap(self.dr, phonecode, 240, 1800, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')


        print('被告性别：男')
        tap(self.dr, 400, 420, **HUAWEI_MATE_8)
        sleep(1)
        from_adb_tap(self.dr, phonecode, 983, 1011, **HUAWEI_MATE_8)  # 1000 1020
        print('成功')
        print('==========================================')


        print('被告地址')
        from_adb_tap(self.dr, phonecode, 380, 889, **HUAWEI_MATE_8)  # 1000 1020
        sleep(0.5)
        from_adb_input_text(phonecode, 'jiangsunanjing')
        print("拼音输入完毕")
        from_adb_tap(self.dr, phonecode, 240, 1800, **HUAWEI_MATE_8)
        sleep(0.5)
        print('成功')
        print('==========================================')

        print("提交")
        #dr.find_element_by_xpath("//android.view.View[@content-desc='提交']").click()
        from_adb_tap(self.dr, phonecode, 530, 1600, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')
        sleep(2)

        print('选择确定')
        #dr.find_element_by_xpath("//android.view.View[@content-desc='确定']").click()  # 820 1060
        from_adb_tap(self.dr, phonecode, 804, 1070, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')
        sleep(3)

        #往下翻翻
        swipe_up(self.dr)

        print('点击诉讼请求')
        self.dr.find_element_by_xpath("//android.widget.EditText[@text='请填写诉讼请求']").click()
        from_adb_input_text(phonecode, 'susongqingqiu')
        from_adb_tap(self.dr, phonecode, 240, 1800, **HUAWEI_MATE_8)
        print('成功')
        print('==========================================')
        sleep(3)


        print('点击完成')
        self.dr.find_element_by_xpath("//android.widget.TextView[@text='完成']").click()
        print('成功')
        print('==========================================')
        sleep(1)

        #往下翻翻
        swipe_up(self.dr)

        print('下一步')
        self.dr.find_element_by_xpath("//android.view.View[@content-desc='下一步']").click()
        print('成功')
        print('==========================================')
        sleep(3)


        print('提交确认')
        self.dr.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        print('成功')
        print('==========================================')
        sleep(3)


        print("纠纷材料页面")

        print('起诉状')
        self.dr.find_element_by_xpath("//android.view.View[@content-desc='* 起诉状']/../android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View").click()
        print('成功')
        print('==========================================')
        sleep(2)

        print('选一张图片，默认第一张，完成')
        from_adb_tap(self.dr, phonecode, 473, 255, **HUAWEI_MATE_8)
        print('成功')
        self.dr.find_element_by_xpath("//android.widget.TextView[@text='完成']").click()
        print('==========================================')
        sleep(13)


        print('当事人身份证明')
        self.dr.find_element_by_xpath("//android.view.View[@content-desc='* 当事人身份证明']/../android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View").click()
        print('成功')
        print('==========================================')
        sleep(2)

        print('选一张图片，默认第一张，完成')
        from_adb_tap(self.dr, phonecode, 473, 255, **HUAWEI_MATE_8)
        print('成功')
        self.dr.find_element_by_xpath("//android.widget.TextView[@text='完成']").click()
        print('==========================================')
        sleep(13)


        print('证据材料')
        self.dr.find_element_by_xpath("//android.view.View[@content-desc='* 证据材料']/../android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View").click()
        print('成功')
        print('==========================================')
        sleep(2)

        print('选一张图片，默认第一张，完成')
        from_adb_tap(self.dr, phonecode, 473, 255, **HUAWEI_MATE_8)
        print('成功')
        self.dr.find_element_by_xpath("//android.widget.TextView[@text='完成']").click()
        print('==========================================')
        sleep(13)



        print('当事人送达地址确认书')
        self.dr.find_element_by_xpath("//android.view.View[@content-desc='* 当事人送达地址确认书']/../android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View").click()
        print('成功')
        print('==========================================')
        sleep(2)

        print('选一张图片，默认第一张，完成')
        from_adb_tap(self.dr, phonecode, 473, 255, **HUAWEI_MATE_8)
        print('成功')
        self.dr.find_element_by_xpath("//android.widget.TextView[@text='完成']").click()
        print('==========================================')
        sleep(13)


        #往下翻翻
        swipe_up(self.dr)

        print('提交')
        self.dr.find_element_by_xpath("//android.view.View[@content-desc='提交']").click()
        print('成功')
        print('==========================================')
        sleep(3)

        print('提交确认')
        self.dr.find_element_by_xpath("//android.widget.Button[@text='确认']").click()
        print('成功')
        print('==========================================')
        sleep(3)



        sleep(10)

        self.dr.quit()




