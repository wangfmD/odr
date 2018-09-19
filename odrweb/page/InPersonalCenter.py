# coding:utf-8
from time import sleep
from odrweb.page.browser import Page

class PersonalCenter(Page):

    def InConciliation(self):
        #选择我要调解
        self.find_element_by_xpath('//div[text()="我要调解"]').click() #点击我要调解
        sleep(1)
        self.find_element_by_xpath('//div[text()="重要提示"]/..//a[text()="确定"]').click() #重要提示-确定

if __name__ == '__main__':
    pass