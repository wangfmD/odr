# -*- coding:utf-8 -*-
from time import sleep

jf_info = {"jf_desc": u"假冒商品",
           "jf_appeal": u"假一赔十",
           "applicant": u"徐传珠",
           "applicant_tel": "15295745648",
           "applicant_id": "321281199507077775",
           "applicant_addr": u"addr",
           "disputer": u"钱桂林",
           "disputer_tel": "13160077223"
           }


class DisputePage(object):
    def __init__(self, page=None):
        self.driver = page.driver

    def _dispute_djy_input(self, **kwargs):
        '''
        机构登记员登记纠纷
        保存提交

        '''
        # 点击消费维权
        self.driver.find_element_by_xpath("//div[@id='app']/div/div[2]/form/div/div/div/label[2]/span[2]").click()
        # 输入纠纷描述
        self.driver.find_element_by_css_selector("textarea.el-textarea__inner").clear()
        self.driver.find_element_by_css_selector("textarea.el-textarea__inner").send_keys(kwargs["jf_desc"])
        # 输入我的诉求
        self.driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").clear()
        self.driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").send_keys(
            kwargs["jf_appeal"])
        #  点击纠纷发生地
        self.driver.find_element_by_css_selector("span.city-picker-span").click()
        self.driver.find_element_by_link_text(u"浙江省").click()
        self.driver.find_element_by_link_text(u"杭州市").click()
        self.driver.find_element_by_link_text(u"上城区").click()
        self.driver.find_element_by_link_text(u"清波街道").click()
        self.driver.find_element_by_link_text(u"清波门社区").click()
        # click选择调解员
        self.driver.find_element_by_css_selector(
            "div.el-form-item__content > div > div.el-input > input.el-input__inner").click()
        sleep(1)
        # 确定调解员
        self.driver.find_element_by_css_selector("button.choice").click()
        # 申请人
        self.driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").clear()
        self.driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").send_keys(
            kwargs["applicant"])
        # 电话
        self.driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").clear()
        self.driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").send_keys(
            kwargs["applicant_tel"]
        )
        # 身份证
        self.driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        self.driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(kwargs["applicant_id"])
        sleep(1)
        # 选择常驻地址
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/div/div[1]/form/div/div[6]/div/span').click()
        sleep(1)
        self.driver.find_element_by_link_text(u"浙江省").click()
        self.driver.find_element_by_link_text(u"杭州市").click()
        self.driver.find_element_by_link_text(u"上城区").click()
        self.driver.find_element_by_link_text(u"清波街道").click()
        #
        self.driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").click()
        # 详细地址
        self.driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").clear()
        self.driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").send_keys(kwargs['applicant_addr'])

        # 被申请人姓名
        self.driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").clear()
        self.driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").send_keys(kwargs['disputer'])
        # 电话
        self.driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").clear()
        self.driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").send_keys(
            kwargs['disputer_tel'])

    def dispute_djy_save(self, **kwargs):
        '''
        机构登记员登记纠纷
        保存提交
        '''

        self._dispute_djy_input(**kwargs)

        # 保存
        self.driver.find_element_by_css_selector("span.lastStep").click()
        sleep(1)
        # 查看案件列表
        self.driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
        sleep(1)
        # 纠纷预览
        self.driver.find_element_by_link_text(u"纠纷预览").click()
        # 提交
        self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        sleep(1.5)
        # 不发送
        self.driver.find_element_by_link_text(u"不发送").click()
        sleep(2)
        # 确定
        self.driver.find_element_by_xpath('//div[@id="layui-layer2"]/div[3]/a').click()
        # 返回列表
        self.driver.find_element_by_css_selector("button[type=\"button\"]").click()
        #
        # self.driver.find_element_by_link_text(u"机构登记").click()
        # self.driver.find_element_by_xpath(u"(//a[contains(text(),'返回>')])[2]").click()
        # 保存提交方式

    def dispute_djy_commit(self, **kwargs):
        '''
        机构登记员
        提交
        :param driver:
        :return:
        '''
        self._dispute_djy_input(**kwargs)
        # 提交
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[2]/p[3]/span[2]').click()
        sleep(1)
        # 短信提醒
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]/span').click()
        sleep(2)
        # 确认
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
        # 直接点击保存方式

    def dispute_djy_commit_verification(self, jf_desc):
        try:
            jf_desc = self.driver.find_element_by_xpath(
                '/html/body/div[4]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
        except:
            jf_desc = "*None*"
        print "expect: ", jf_desc
        print "result: ", jf_info["jf_desc"]
        return jf_desc == jf_info["jf_desc"]




    def _dispute_tjy_input(self,**kwargs):
        '''
        调解员登记纠纷
        提交
        :param self.driver:
        :return:
        '''

        self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/button[2]").click()
        # 点击案件登记列表
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[1]/a[2]').click()
        # 点击登记纠纷添加
        self.driver.find_element_by_css_selector("textarea.el-textarea__inner").clear()
        self.driver.find_element_by_css_selector("textarea.el-textarea__inner").send_keys(kwargs["jf_desc"])
        self.driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").clear()
        self.driver.find_element_by_css_selector("div.appeal.el-textarea > textarea.el-textarea__inner").send_keys(
            kwargs["jf_appeal"])
        self.driver.find_element_by_css_selector("span.city-picker-span").click()
        self.driver.find_element_by_link_text(u"浙江省").click()
        self.driver.find_element_by_link_text(u"杭州市").click()
        self.driver.find_element_by_link_text(u"上城区").click()
        self.driver.find_element_by_link_text(u"清波街道").click()
        self.driver.find_element_by_link_text(u"清波门社区").click()
        sleep(1)
        self.driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").clear()
        self.driver.find_element_by_css_selector("div.el-input.page2Name0 > input.el-input__inner").send_keys(kwargs["applicant"])
        self.driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").clear()
        self.driver.find_element_by_css_selector("div.el-input.page2Num0 > input.el-input__inner").send_keys(
            kwargs["applicant_tel"])
        self.driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        self.driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys(kwargs["applicant_id"])
        sleep(1)
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[3]/div/div[1]/form/div/div[6]/div/span').click()
        sleep(1)
        self.driver.find_element_by_link_text(u"浙江省").click()
        self.driver.find_element_by_link_text(u"杭州市").click()
        self.driver.find_element_by_link_text(u"上城区").click()
        self.driver.find_element_by_link_text(u"清波街道").click()
        self.driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").click()
        # 住址
        self.driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").clear()
        self.driver.find_element_by_css_selector("div.el-input.page2Xxdz0 > input.el-input__inner").send_keys(kwargs[
                                                                                                                  "applicant_addr"])
        self.driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").clear()
        self.driver.find_element_by_css_selector("div.el-input.page3Bname0 > input.el-input__inner").send_keys(
            kwargs['disputer'])
        self.driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").clear()
        self.driver.find_element_by_css_selector("div.el-input.page3Bphone0 > input.el-input__inner").send_keys(
            kwargs['disputer_tel'])


    def dispute_tjy_commit(self,**kwargs):
        '''
        调解员登记纠纷
        提交
        :param self.driver:
        :return:
        '''
        self._dispute_tjy_input(**kwargs)

        # 提交
        self.driver.find_element_by_xpath('//div[@id="app"]/div/div[4]/div/div[2]/p[3]/span[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[1]/span').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button/span').click()
        # 直接提交方式


    def dispute_tjy_save(self,**kwargs):
        '''
        调解员登记纠纷
        保存提交
        :param self.driver:
        :return:
        '''
        self._dispute_tjy_input(**kwargs)

        # 保存
        self.driver.find_element_by_css_selector("span.lastStep").click()
        sleep(1)
        # 查看案件列表
        self.driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
        sleep(1)


    def dispute_tjy_save_verification(self, jf_desc):
        try:
            jf_desc = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[6]/p').text
        except:
            jf_desc = "*None*"
        print "expect: ", jf_desc
        print "result: ", jf_info["jf_desc"]
        return jf_desc == jf_info["jf_desc"]


    def dispute_tjy_save_commit(self):
        self.driver.find_element_by_link_text(u"纠纷预览").click()
        self.driver.find_element_by_xpath("(//button[@type='button'])[5]").click()
        sleep(1)
        self.driver.find_element_by_link_text(u"不发送").click()
        sleep(3)
        self.driver.find_element_by_xpath('//div[@id="layui-layer2"]/div[3]/a').click()
        self.driver.find_element_by_css_selector("button[type=\"button\"]").click()


def jf1():
    from odrweb.core.page.homepage import HomePage
    from odrweb.core.initdata import users
    homepage = HomePage()
    homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    sleep(10)
    # dis = DisputePage(homepage)
    # dis.dispute_tjy_save()
    # dis.dispute_tjy_commit()


def jf2():
    from odrweb.core.page.homepage import HomePage
    from odrweb.core.initdata import users
    homepage = HomePage()
    homepage.organization_user_login(users.user_jgdjy['username'], users.user_jgdjy['pwd'])
    # sleep(10)
    dis = DisputePage(homepage)
    # dis.dispute_djy_commit()
    dis.dispute_djy_save(**jf_info)


if __name__ == '__main__':
    jf2()
