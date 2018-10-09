# coding:utf-8
from time import sleep
from odrweb.page.browser import Page

class PersonalCenter(Page):

    def conciliation_list(self):
        # 点开调解列表
        self.find_element_by_xpath('//a[text()="调解"]').click()

    def get_last_conciliation_number(self):
        # 获取最新的纠纷编号
        number = self.find_element_by_xpath('//div[@class="list-item"][1]//div[@class="case-detail"]//li[2]').text
        return number

    def in_conciliation(self):
        #选择我要调解
        self.find_element_by_xpath('//div[text()="我要调解"]').click() #点击我要调解
        sleep(1)
        self.find_element_by_xpath('//div[text()="重要提示"]/..//a[text()="确定"]').click() #重要提示-确定


if __name__ == '__main__':
    pass