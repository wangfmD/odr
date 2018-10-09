# -*- coding:utf-8 -*-

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from odrweb.page.browser import Page

class JudgePage(Page):
    x_search_input=''
    x_case_detail =''
    x_case_schedule = ''