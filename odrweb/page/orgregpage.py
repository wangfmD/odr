# coding:utf-8
from time import sleep
from odrweb.page.browser import Page

class OrgRegCase(Page):

    def action_input_case_info(self, **kwargs):
        self._choose_case_type(**kwargs)
        self._input_case_detail(**kwargs)
        self._input_my_reason(**kwargs)
        self._choose_case_city(**kwargs)
        self._choose_case_city(**kwargs)
        self._choose_case_mediator(**kwargs)

    def action_input_proposers(self, **kwargs):
        print("有" + str(len(kwargs["roler"])) + "个申请人")

        for i in range(1,len(kwargs["roler"])+1):
            print("正在录入第" + str(i) + "个申请人")
            self._proposer_check(i, **kwargs)
            print("第" + str(i) + "个申请人录入完成")

    def _proposer_check(self, count, **kwargs):
        j = count - 1  # 取数据字典信息，数组下标从0开始，统一转换
        MainXpath = '//div[@class="applyForm applyForm' + str(j) + '"]'

        #自然人
        if kwargs["roler"][j]["申请人类型"] == "自然人":
            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="申请人："]/../div/div/input').send_keys(kwargs["roler"][j]["申请人"])  # 填写申请人名字
            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="申请人性别："]/../div/div/label/span/input[@value="'+ kwargs["roler"][j]["申请人性别"] + '"]/../span').click()  # 自然人性别点选
            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="手机号："]/../div/div/input').send_keys(
                kwargs["roler"][j]["手机号"])  # 自然人电话


    #def action_input_claimants(self, **kwargs):




    def _choose_case_type(self, **kwargs):
        """点选纠纷类型"""
        self.find_element_by_xpath('//span[text()="' + kwargs["纠纷类型"] + '"]').click()

    def _input_case_detail(self, **kwargs):
        """填写纠纷描述"""
        self.find_element_by_xpath('//label[text()="纠纷描述："]/..//div[@class="el-textarea"]/textarea').click()
        self.find_element_by_xpath('//label[text()="纠纷描述："]/..//div[@class="el-textarea"]/textarea').send_keys(kwargs["纠纷描述"])

    def _input_my_reason(self, **kwargs):
        """填写我的诉求"""
        self.find_element_by_xpath('//label[text()="我的诉求："]/..//div[@class="el-textarea"]/textarea').click()
        self.find_element_by_xpath('//label[text()="我的诉求："]/..//div[@class="el-textarea"]/textarea').send_keys(kwargs["我的诉求"])

    def _choose_case_city(self, **kwargs):
        self.find_element_by_xpath('//label[text()="纠纷发生地："]/..//span[@class="city-picker-span"]').click()  # 唤出纠纷发生地选项卡
        self.find_element_by_xpath('//label[text()="纠纷发生地："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select province"]//a[text()="'+kwargs["纠纷发生省份"]+'"]').click()  # 点选纠纷发生省份

        if kwargs["纠纷发生市区"] != "":
            self.find_element_by_xpath('//label[text()="纠纷发生地："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select city"]//a[text()="'+kwargs["纠纷发生市区"]+'"]').click() # 点选纠纷发生市区
        else:
            self._close_case_city()
            return

        if kwargs["纠纷发生区县"] != "":
            self.find_element_by_xpath('//label[text()="纠纷发生地："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select district"]//a[text()="'+kwargs["纠纷发生区县"]+'"]').click()   # 点选纠纷发生区县
        else:
            self._close_case_city()
            return

        if kwargs["纠纷发生街道"] != "":
            self.find_element_by_xpath('//label[text()="纠纷发生地："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select county"]//a[text()="'+kwargs["纠纷发生街道"]+'"]').click()  # 点选纠纷发生街道
        else:
            self._close_case_city()
            return

        if kwargs["纠纷发生社区"] != "":
            self.find_element_by_xpath('//label[text()="纠纷发生地："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select community"]//a[text()="'+kwargs["纠纷发生社区"]+'"]').click()  #点选纠纷发生社区
        else:
            self._close_case_city()
            return

    def _close_case_city(self):
        # 收起纠纷发生城市选项卡
        self.find_element_by_xpath('//label[text()="纠纷发生地："]/../div/span/span[@class="title"]').click()

    def _choose_case_mediator(self, **kwargs):
        # 选择调解员
        if kwargs["调解员"] != "":
            return
        else:
            self.find_element_by_xpath('//label[text()="调解员："]/..//input').click()
            sleep(0.5)
            self.find_element_by_xpath('//div[@class="search-counselor"]/input').send_keys(kwargs["调解员"])
            self.find_element_by_xpath('//div[@class="search-counselor"]/button').click()  # 点击搜索
            sleep(0.5)
            self.find_element_by_xpath('//p[text()="' + kwargs["调解员"] + '"]/../../button').click()  # 点击确定
