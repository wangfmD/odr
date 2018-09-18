# coding:utf-8
from time import sleep
from odrweb.page.browser import Page

class RolerChoose(Page):

    def NormalProxy(self):
        # 选择一般代理人身份
        self.find_element_by_xpath("//div[contains(text(),'我是代理人')]/../div/div/div/div[contains(text(),'申请调解')]").click()



if __name__ == '__main__':
    pass