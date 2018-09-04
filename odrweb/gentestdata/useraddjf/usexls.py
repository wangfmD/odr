# -*- coding: utf-8 -*-

from odrweb.core.parsexls import XlsFile
from odrweb.page.homepage import HomePage
from odrweb.page.personalpage import PersonalPage
import time
url = 'https://uatodr.odrcloud.net'


def add_jf_tiaojiey_tj():


    xls = XlsFile(xls_name=r"gentestdata.xlsx")
    rowlist = xls.parse_xls_by_col("gentestdata")
    for it in rowlist:
        for k in it:
            print k, ":", it[k],":", type(it[k])
    jf_info=rowlist[0]
    homepage = HomePage()
    homepage.user_login(jf_info['applicant_tel'],jf_info['applicant_pwd'])
    homepage.user_personal_center()
    per = PersonalPage(homepage)
    per.apply_mediate(**jf_info)

if __name__ == '__main__':
    add_jf_tiaojiey_tj()