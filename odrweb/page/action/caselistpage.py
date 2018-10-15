# coding:utf-8

from time import sleep

from odrweb.page.browser import Page


class TjyBaseOperation(Page):
    x_case_input_list_a = '//div[text()="案件登记列表"]'          # 案件登记列表链接

    def _into_mydispute(self):
        """进入我的案件列表"""
        self.find_element_by_xpath('/html/body/div[4]/div[1]/button[1]').click()

    def _into_mydispult_info(self):
        """进入我的案件列表纠纷详情页面"""
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[4]/div[2]/a').click()
        sleep(1)

    def _get_mydispute_id(self):
        """我的案件列表获取案件编号"""
        # 获取案件编号
        try:
            jf_id = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[1]').text
            dispute_id = jf_id.split(u'：')[-1]
        except:
            dispute_id = None
            return dispute_id

    def _choose_mydispute_wait(self):
        """选择案件状态为等待调解"""
        # 点击选择案件状态
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[4]/select').click()
        # 选择案件状态为等待调解
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[4]/select/option[2]').click()
        sleep(1)

    def _get_mydispute_desc(self):
        """我的案件列表页面获取纠纷描述"""
        sleep(1)
        jf_desc = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[4]/div[1]/div[9]/p').text
        return jf_desc



    def _into_disputelist(self):
        """进入案件登记列表"""
        self.find_element_by_xpath(self.x_case_input_list_a).click()

    def _choose_commit(self):
        """选择已提交案件"""
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[1]/select').click()
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[1]/select/option[3]').click()
        sleep(1)

    def _dispute_add(self):
        """进入增加纠纷页面"""
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[2]/a[2]').click()
        sleep(1)


    def _dispute_add_commit(self):
        """增加纠纷页面提交"""
        # 点击提交按钮
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[1]/p/span[2]').click()
        sleep(1)
        # 不发送短信
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]/span').click()
        sleep(2)
        # 点击提交成功
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
        sleep(1)
        # 获取第二条案件纠纷详情
        jf_desc_add = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[3]/div/div/div/div[2]/div[1]/div[6]/p').text
        return jf_desc_add

    def _dispute_add_save(self):
        """增加纠纷页面保存"""
        # 点击提交按钮
        self.find_element_by_xpath('//div[@id="app"]/div/div[2]/div[1]/p/span[1]').click()
        sleep(1)
        # 点击查看案件列表
        self.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()

    def _dispute_delete(self):
        """纠纷列表删除保存纠纷"""
        # 点击删除按钮
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[2]/a[3]').click()
        sleep(1)
        # 点击确定
        try:
            # self.find_element_by_xpath('//div[@id="layui-layer4"]/div[3]/a[2]').click()
            self.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        except:
            sleep(1)
            self.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        sleep(1)
        # 点击确定
        try:
            self.find_element_by_xpath('//a[contains(text(),"确定")]').click()
            sleep(1)
        except:
            self.find_element_by_xpath('//a[contains(text(),"确定")]').click()
        sleep(1)
        # find_res = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]').text
        # res = find_res == u'没有案件登记记录'
        # return res

    def verfication_dispute_delete(self):
        expect = u"没有案件登记记录"
        try:
            find_res = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]').text
        except:
            find_res="**None**"
        sleep(2)
        print "expect: ", expect
        print "result: ", find_res
        res = find_res == expect
        return res

    def _choose_save(self):
        """选择未提交案件"""
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[1]/select').click()
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[1]/select/option[2]').click()
        sleep(1)

    def _get_dispute_id(self):
        """案件登记列表获取案件纠纷编号"""
        # 获取案件编号
        try:
            jf_id = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[1]/div[1]').text
            dispute_id = jf_id.split(u'：')[-1]
        except:
            dispute_id = None
            return dispute_id
        # jf_id = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[1]/div[1]').text
        # dispute_id = jf_id.split(u'：')[-1]
        return dispute_id

    def _get_dispute_info_id(self):
        """案件详情页面获取案件登记编号"""
        dispute_id = self.find_element_by_xpath('/html/body/section[2]/div[1]/div/span[2]').text
        return dispute_id

    def _find_scan(self, dispute_id):
        """案件编号查询案件"""
        # 输入案件编号
        self.find_element_by_xpath('//input[@id="searchInput2"]').send_keys(dispute_id)
        # 点击搜索按钮
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div/span').click()

    def _get_jf_desc(self):
        """获取纠纷描述"""
        jf_desc = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
        return jf_desc

    def _into_dispute_info(self):
        """进入纠纷详情页面"""
        # 点击进入纠纷预览
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[2]/a[1]').click()
        sleep(1)

    def _dispute_info_change(self):
        # 纠纷描述后添加-修改纠纷描述-保存-返回列表
        # self.find_element_by_xpath('//div[@id="checkCaseform"]/form/div[2]/p/textarea').clear()
        self.find_element_by_xpath('//div[@id="checkCaseform"]/form/div[2]/p/textarea').send_keys(u'-修改纠纷描述')
        # 点击保存按钮
        self.find_element_by_xpath('/html/body/section[2]/div[1]/edit/div[4]/button').click()
        # 提示框点击确定
        self.find_element_by_xpath('//div[@id="layui-layer1"]/div[3]/a').click()
        # 点击返回列表按钮
        self.find_element_by_xpath('/html/body/section[1]/button').click()

    def verification_dispute_id(self):
        """案件编号校验"""
        dispute_id = self._get_dispute_id()
        if dispute_id:
            print  dispute_id
        else:
            print u"案件编号搜索失败"
        res = dispute_id != u"案件编号搜索失败"
        return res

    # def verification_dispute_info(self, **kwargs):
    #     """进入纠纷详情页面校验纠纷描述"""
    #     try:
    #         jf_desc = self.find_element_by_xpath('//div[@id="checkCaseform"]/form/div[2]/p/textarea').text
    #     except:
    #         jf_desc = "*None*"
    #     print "result", jf_desc
    #     print "except", kwargs["jf_desc"]
    #     res = jf_desc == kwargs["jf_desc"]
    #     return res
    #
    # def verification_dispute_info_change(self,**kwargs):
    #     """纠纷描述保存后校验"""
    #     try:
    #         jf_desc = self.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
    #     except:
    #         jf_desc = "*None*"
    #     print "result",jf_desc
    #     print "except",kwargs["jf_desc"]
    #     res = jf_desc == kwargs["jf_desc"]
    #     return res

    def dispute_info_change(self):
        """已提交案件纠纷详情页面修改保存并校验"""
        self._into_disputelist()
        self._choose_commit()
        jf_desc_before = self._get_jf_desc()
        self._into_dispute_info()
        self._dispute_info_change()
        jf_desc_after = self._get_jf_desc()
        res = jf_desc_before != jf_desc_after
        return res

    def into_dispute_info(self):
        """已提交案件进入纠纷详情页面并校验"""
        self._into_disputelist()
        self._choose_commit()
        dispute_id_out = self._get_dispute_id()
        self._into_dispute_info()
        dispute_id_in = self._get_dispute_info_id()
        res = dispute_id_out == dispute_id_in
        return res

    def mydispute_find(self):
        """已提交案件我的案件列表搜索"""
        self._into_disputelist()
        self._choose_commit()
        dispute_id = self._get_dispute_id()
        # 进入案件登记列表第五页
        self.find_element_by_xpath('/html/body/div[4]/div[2]/div[7]/ul/li[8]/a').click()
        self._find_scan(dispute_id)

    def dispute_add_commit(self):
        """已提交案件列表增加纠纷-提交"""
        self._into_disputelist()
        self._choose_commit()
        self._dispute_add()
        jf_desc_add = self._dispute_add_commit()
        jf_desc = self._get_jf_desc()
        res = jf_desc_add == jf_desc
        return res

    def dispute_add_save_delete(self):
        """已提交案件列表增加纠纷-保存-删除"""
        self._into_disputelist()
        self._choose_commit()
        self._dispute_add()
        self._dispute_add_save()
        self._choose_save()
        dispute_id = self._get_dispute_id()
        self._dispute_delete()
        self._find_scan(dispute_id)



    def into_mydispult_info(self):
        """进入我的案件列表纠纷详情"""
        dispult_id_out = self._get_mydispute_id()
        self._into_mydispult_info()
        dispult_id_in = self._get_dispute_info_id()
        res = dispult_id_out == dispult_id_in
        return res

    def mydispute_info_change(self):
        """我的案件列表等待调解案件修改保存"""
        self._choose_mydispute_wait()
        mydispult_desc_before = self._get_mydispute_desc()
        self._into_mydispult_info()
        self._dispute_info_change()
        mydispult_desc_after = self._get_mydispute_desc()
        res = mydispult_desc_after == mydispult_desc_before
        return  res





