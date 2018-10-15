# -*- coding: utf-8 -*-
from odrweb.core.initdata import users
from odrweb.core.parsexls import XlsFile
from odrweb.page.disputepage import DisputePageTjy
from odrweb.page.homepage import HomePage
from odrweb.page.personalpage import PersonalPage
import time
url = 'https://uatodr.odrcloud.net'

jf_info_all = {
    "jf_appeal": u"假一赔十",
    "applicant_name": u"企业或机构名称",  #
    "world_credit_id": "abcde1234567890",
    "applicant": u"钱桂林",
    "applicant_tel": "13160077223",
    "applicant_id": "321023199508166636",
    "applicant_addr": u"1栋2单元303",

    "disputer": u"王发明",
    "disputer_tel": "13913031374",
    "disputer_world_credit_id": "zxcvbnmasdfghjk123",
    "disputer_name": u"企业或机构名称",
    "disputer_id": "",
    "disputer_addr": u"10栋1单元101",

    "agent_name": u"徐传珠",
    "agent_tel": "15295745648",
    "agent_id": "321281199507077775",

    "agent_b_name": u"段志勇",
    "agent_b_tel": "15895996954",
    "agent_b_id": ""
}

def add_jf_tiaojiey_tj():
    jf_info = {"jf_desc": u"调解员-登记纠纷提交-申自然人代理人-被自然人",
               "applicant_type": u"自然人",  # 自然人 法人 非法人组织
               "disputer_type": u"自然人",  # 自然人 法人 非法人组织
               "agent_type": "special",  # "" common special,
               "agent_b_type": "",  # common special,

               }

    jf_info_all.update(jf_info)

    xls = XlsFile(xls_name=r"gentestdata.xlsx")
    rowlist = xls.parse_xls_by_col("gentestdata")
    for it in rowlist:
        for k in it:
            print k, ":", it[k],":", type(it[k])
    jf_info_xls = rowlist[0]
    homepage = HomePage()
    homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    disputepage = DisputePageTjy(homepage)
    disputepage.commit(**jf_info_xls)

if __name__ == '__main__':
    add_jf_tiaojiey_tj()