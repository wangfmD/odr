# coding:utf-8
from time import sleep
from odrweb.page.browser import Page

class ConciliationInfo(Page):

    def InputConciliationInfo(self, **kwargs):

        self.find_element_by_xpath('//label[text()="纠纷类型："]/../div/div/label/span[text()="'+kwargs["纠纷类型"]+'"]').click() #纠纷类型点选
        self.find_element_by_xpath('//label[text()="纠纷描述："]/../div/div/div/textarea').send_keys(kwargs["纠纷描述"]) #纠纷描述录入
        self.find_element_by_xpath('//label[text()="我的诉求："]/../div/div/div/textarea').send_keys(kwargs["我的诉求"]) #我的诉求录入

        self.find_element_by_xpath('//label[text()="纠纷发生地："]/../div/span[@class="city-picker-span"]').click() #唤出纠纷发生地选项卡
        self.find_element_by_xpath('//label[text()="纠纷发生地："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select province"]/dl/dd/a[text()="'+kwargs["纠纷发生省份"]+'"]').click()  # 点选纠纷发生省份
        self.find_element_by_xpath('//label[text()="纠纷发生地："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select city"]/dl/dd/a[text()="'+kwargs["纠纷发生市区"]+'"]').click() # 点选纠纷发生市区

        if kwargs["纠纷发生区县"] != "":
            self.find_element_by_xpath('//label[text()="纠纷发生地："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select district"]/dl/dd/a[text()="'+kwargs["纠纷发生区县"]+'"]').click()   # 点选纠纷发生区县
        else:
            self._CloseCitySelectCard()

        if kwargs["纠纷发生街道"] != "":
            self.find_element_by_xpath('//label[text()="纠纷发生地："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select county"]/dl/dd/a[text()="'+kwargs["纠纷发生街道"]+'"]').click()  # 点选纠纷发生街道
        else:
            self._CloseCitySelectCard()

        if kwargs["纠纷发生社区"] != "":
            self.find_element_by_xpath('//label[text()="纠纷发生地："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select community"]/dl/dd/a[text()="'+kwargs["纠纷发生社区"]+'"]').click()  #点选纠纷发生社区
        else:
            self._CloseCitySelectCard()

        self.find_element_by_xpath('//label[text()="调解机构："]/../div/div/input').click() #唤出调解机构筛选
        self.find_element_by_xpath('//em[text()="调解机构筛选 "]/../../../div/div/div/button[text()="搜索"]/../input').send_keys(unicode(kwargs["调解机构"])) #输入调解机构
        self.find_element_by_xpath('//em[text()="调解机构筛选 "]/../../../div/div/div/button[text()="搜索"]').click() #点击搜索
        sleep(1)
        self.find_element_by_xpath('//p[text()="'+kwargs["调解机构"]+'"]/../../button').click()  #点击选择

        self.find_element_by_xpath('//div[text()="下一步"]').click() #下一步

    def _CloseCitySelectCard(self):
        # 收起纠纷发生城市选项卡
         self.find_element_by_xpath('//label[text()="纠纷发生地："]/../div/span/span[@class="title"]').click()

if __name__ == '__main__':
    pass



