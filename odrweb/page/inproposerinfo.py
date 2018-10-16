# coding:utf-8
from time import sleep
from odrweb.page.browser import Page

class InProposerInfo(Page):

    def input_proposer_info(self, **kwargs):
        print("有"+str(len(kwargs["roler"]))+"个申请人")

        for i in range(1,len(kwargs["roler"])+1):
            print("正在录入第" + str(i) + "个申请人")
            self._ProposerCheck(i, **kwargs)
            print("第" + str(i) + "个申请人录入完成")

            if i == 1:
                try:
                    self._UpdateFile()
                    print("授权委托书上传成功")
                except:
                    print("授权委托书上传失败")

            if i < len(kwargs["roler"]):
                self.find_element_by_xpath('//p[text()=" + 新增申请人"]').click()
                sleep(0.5)

        self.find_element_by_xpath('//span[text()="下一步"]').click()



    def _ProposerCheck(self,count, **kwargs):

        #print("count=", count)
        j=count-1 #取数据字典信息，数组下标从0开始，统一转换
        MainXpath = '//div[@class="proposer unActive stepActive"]/div/div/form/div[@class="formMain"][' + str(count) + ']'


        #自然人
        if kwargs["roler"][j]["申请人类型"] == "自然人":

            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="申请人："]/../div/div/input').send_keys(kwargs["roler"][j]["申请人"])  # 填写申请人名字
            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="申请人性别："]/../div/div/label/span/input[@value="'+ kwargs["roler"][j]["申请人性别"] + '"]/../span').click()  # 自然人性别点选
            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="联系电话："]/../div/div/input').send_keys(
                kwargs["roler"][j]["联系电话"])  # 自然人电话
            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="身份证号："]/../div/div/input').send_keys(
                kwargs["roler"][j]["身份证号"])  # 自然人身份证号

            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="常住地区："]/../div/span[@class="city-picker-span"]').click()  # 唤出常住地区选项卡


            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="常住地区："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select province"]/dl/dd/a[text()="'+ kwargs["roler"][j]["常住省份"] + '"]').click()  # 点选常住省份

            if kwargs["roler"][j]["常住市区"] != "":
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="常住地区："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select city"]/dl/dd/a[text()="'+ kwargs["roler"][j]["常住市区"] + '"]').click()  # 点选常住市区
            else:
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="常住地区："]').click()

            if kwargs["roler"][j]["常住区县"] != "":
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="常住地区："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select district"]/dl/dd/a[text()="'+ kwargs["roler"][j]["常住区县"] + '"]').click()  # 点选常住区县
            else:
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="常住地区："]').click()

            if kwargs["roler"][j]["常住街道"] != "":
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="常住地区："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select street"]/dl/dd/a[text()="'+ kwargs["roler"][j]["常住街道"] + '"]').click()  # 点选常住街道
            else:
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="常住地区："]').click()

            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="详细地址："]/../div/div/input').send_keys(kwargs["roler"][j]["详细地址"])  # 自然人详细地址

        #法人
        if kwargs["roler"][j]["申请人类型"] == "法人":
            self.find_element_by_xpath(
                MainXpath + '/div/div/div/label/span[text()="' + kwargs["roler"][j]["申请人类型"] + '"]').click() #点选法人标签
            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="申请人："]/../div/input').send_keys(kwargs["roler"][j]["申请人"])  # 填写申请人名字
            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="社会信用码："]/../div/input').send_keys(kwargs["roler"][j]["社会信用码"])  # 填写社会信用码
            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="法定代表人："]/../div/div/input').send_keys(kwargs["roler"][j]["法定代表人"])  # 填写机构代表人
            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="申请人性别："]/../div/div/label/span/input[@value="'+ kwargs["roler"][j]["申请人性别"] + '"]/../span').click()  # 性别点选
            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="联系电话："]/../div/div/input').send_keys(kwargs["roler"][j]["联系电话"]) #联系电话

            if kwargs["roler"][j]["身份证号"] == "":
                pass
            else:
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="身份证号："]/../div/div/input').send_keys(kwargs["roler"][j]["身份证号"]) #身份证号

            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="单位地址："]/../div/span[@class="city-picker-span"]').click()  # 唤出单位地址选项卡


            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="单位地址："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select province"]/dl/dd/a[text()="'+ kwargs["roler"][j]["单位省份"] + '"]').click()  # 点选常住省份

            if kwargs["roler"][j]["单位市区"] != "":
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="单位地址："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select city"]/dl/dd/a[text()="'+ kwargs["roler"][j]["单位市区"] + '"]').click()  # 点选常住市区
            else:
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="单位地址："]').click()

            if kwargs["roler"][j]["单位区县"] != "":
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="单位地址："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select district"]/dl/dd/a[text()="'+ kwargs["roler"][j]["单位区县"] + '"]').click()  # 点选常住区县
            else:
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="单位地址："]').click()

            if kwargs["roler"][j]["单位街道"] != "":
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="单位地址："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select street"]/dl/dd/a[text()="'+ kwargs["roler"][j]["单位街道"] + '"]').click()  # 点选常住街道
            else:
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="单位地址："]').click()


            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="详细地址："]/../div/div/input').send_keys(kwargs["roler"][j]["详细地址"])  # 详细地址


        #非法人组织
        if kwargs["roler"][j]["申请人类型"] == "非法人组织":
            self.find_element_by_xpath(
                MainXpath + '/div/div/div/label/span[text()="' + kwargs["roler"][j]["申请人类型"] + '"]').click() #点选非法人组织标签
            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="申请人："]/../div/input').send_keys(kwargs["roler"][j]["申请人"])  # 填写申请人名字

            if kwargs["roler"][j]["社会信用码"] != "":
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="社会信用码："]/../div/input').send_keys(kwargs["roler"][j]["社会信用码"])  # 填写社会信用码
            else:
                pass

            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="机构代表人："]/../div/div/input').send_keys(kwargs["roler"][j]["机构代表人"])  # 填写机构代表人
            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="申请人性别："]/../div/div/label/span/input[@value="'+ kwargs["roler"][j]["申请人性别"] + '"]/../span').click()  # 性别点选
            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="联系电话："]/../div/div/input').send_keys(kwargs["roler"][j]["联系电话"]) #联系电话

            if kwargs["roler"][j]["身份证号"] == "":
                pass
            else:
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="身份证号："]/../div/div/input').send_keys(kwargs["roler"][j]["身份证号"]) #身份证号

            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="单位地址："]/../div/span[@class="city-picker-span"]').click()  # 唤出单位地址选项卡


            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="单位地址："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select province"]/dl/dd/a[text()="'+ kwargs["roler"][j]["单位省份"] + '"]').click()  # 点选常住省份

            if kwargs["roler"][j]["单位市区"] != "":
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="单位地址："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select city"]/dl/dd/a[text()="'+ kwargs["roler"][j]["单位市区"] + '"]').click()  # 点选常住市区
            else:
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="单位地址："]').click()

            if kwargs["roler"][j]["单位区县"] != "":
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="单位地址："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select district"]/dl/dd/a[text()="'+ kwargs["roler"][j]["单位区县"] + '"]').click()  # 点选常住区县
            else:
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="单位地址："]').click()

            if kwargs["roler"][j]["单位街道"] != "":
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="单位地址："]/../div/div/div/div[@class="city-select-content"]/div[@class="city-select street"]/dl/dd/a[text()="'+ kwargs["roler"][j]["单位街道"] + '"]').click()  # 点选常住街道
            else:
                self.find_element_by_xpath(
                    MainXpath + '/div/label[text()="单位地址："]').click()


            self.find_element_by_xpath(
                MainXpath + '/div/label[text()="详细地址："]/../div/div/input').send_keys(kwargs["roler"][j]["详细地址"])  # 详细地址

    def _UpdateFile(self):
        js = 'app.$data.dynamicValidateForm.domains.forEach(e=>{e.Dfile={createId:null,createPersonnelRole:null,deleteMark:null,fileName:".gitconfig",filePath:"/powerOfAttorney/201808/4872c3f0440046aea35df9a6b6c2e7ee.gitconfig",fileSuffix:"gitconfig",id:null,lawCaseId:null,litigantId:null,name:"授权委托书",remarks:null,syncMark:"0",type:null}})'
        self.driver.execute_script(js)
