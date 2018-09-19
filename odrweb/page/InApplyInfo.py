# coding:utf-8
from time import sleep
from odrweb.page.browser import Page

class InApplyInfo(Page):

    def InputApplyInfo(self, **kwargs):
        print("有"+str(len(kwargs["roler"]))+"个申请人")

