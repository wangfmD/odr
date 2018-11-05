# -*- coding: utf-8 -*-
import json

import requests


def login_by():
    url = 'https://performapi.bjsjsadr.com/userGateway/user/userLoginByMobile'
    headers = {
        'Content-Type': 'application/json',
        'cType': 'PC',
        'deviceId': 'ffea53b5-0377-4c7f-a53d-bb48a6cfb6e5',
        'Origin': 'http://htodr.odrcloud.com',
        'Referer': 'http://htodr.odrcloud.com/useraction/stafflogin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    formdata = {
        "mobilePhone": "13869372344",
        "password": "88888888",
        "loginType": "WORK_USER_LOGIN_TYPE"
    }
    formdata = json.dumps(formdata)
    r = requests.post(url, headers=headers, data=formdata)
    print(r.text)


# def req():
#     url = 'https://devhtodr.odrcloud.net/userGateway/home/getHomeDataCount'
#     headers = {
#         'cType': 'PC',
#         'Accept': '*/*',
#         'deviceId': 'ced685f1-b5bf-4ad5-ab0e-2794e15afb1b',
#         'Host': 'devhtodr.odrcloud.net',
#         'JWTToken': 'eyJhbGciOiJIUzUxMiJ9.eyJyb2xlcyI6WyJDT01NT04iXSwidXNlck5hbWUiOiLpg63lsI_mlY8iLCJwZXJzb25UeXBlIjoiQ09NTU9OIiwidXNlcklkIjoiMjAwOTYwIiwiZXhwIjoxNTQxMDcxNjA3fQ.kitZ0M7qp0qIk5vbkYEPrU4cwu3YmYzqnxKw5EgeEHCM9Zd5nWuNvndUvqJNWkRjmEn_J7AXtHgF6MgXD4ncEw',
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
#     }
#     r = requests.post(url, headers=headers)
#     print(r.text)


def login():
    url = 'https://devhtodr.odrcloud.net/userGateway/user/userLoginByMobile'
    formdate = {'mobilePhone': "15871775675",
                'password': "88888888"}
    data = json.dumps(formdate)
    # print(data)
    # 'mobilePhone: "15871775675",
    # 'password: "88888888"
    headers = {
        'Host': 'devhtodr.odrcloud.net',
        # 'Connection': 'keep-alive',
        # 'deviceId': 'eb831b70-14a2-478d-aa73-336e84914758',
        'cType': 'PC',
        'Origin': 'https://devhtodr.odrcloud.net',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        'Content-Type': 'application/json',
        # 'Accept': '*/*',
        'Referer': 'https://devhtodr.odrcloud.net/useraction/login',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    r = requests.post(url, headers=headers, data=data)
    print(r.text)


def search():
    headers = {
        # 'Access-Control-Allow-Credentials': 'true',
        # 'Access-Control-Allow-Headers': 'Origin,Content-Type,Accept,token,X-Requested-With,JWTToken,cType,deviceId,deviceModel,osVersion,appVersion,timer,appName',
        # 'Access-Control-Allow-Methods': '*',
        # 'Access-Control-Allow-Origin': '*',
        'cType': 'PC',
        'Content-Type': 'application/json;charset=UTF-8',
        # 'Expires': '0',
        # 'X-Content-Type-Options': 'nosniff',
        # 'X-XSS-Protection': '1; mode=block',
        # 'Accept': '*/*',
        # 'deviceId': 'ced685f1-b5bf-4ad5-ab0e-2794e15afb1b',
        'Host': 'devhtodr.odrcloud.net',
        'JWTToken': 'eyJhbGciOiJIUzUxMiJ9.eyJyb2xlcyI6WyJDT01NT04iXSwidXNlck5hbWUiOiLpg63lsI_mlY8iLCJwZXJzb25UeXBlIjoiQ09NTU9OIiwidXNlcklkIjoiMjAwOTYwIiwiZXhwIjoxNTQxMTUzMDc5fQ.j1h7zu1LokvYZjuTGTrl5AtlytjSTyHYAbtzyC3XEAKoB6My8MjMJC0DDtVeQuO5rLCEeoQ9rQ_q7QyMZOiMKg',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        # 'Cookie': 'JSESSIONID=2376C29B258F44E74F10F1DBA95EEF77'
    }
    data = {'roleType': "COMMON", 'pageIndex': 1, 'pageSize': 10}
    data = json.dumps(data)
    print(data)
    url = 'https://devhtodr.odrcloud.net/userGateway/personalCenter/getMediationListPage'
    r = requests.post(url, headers=headers, data=data)
    print(r.text)


def zjodr_search():
    url = 'https://uatodr.odrcloud.net/evaluate/listLawCaseEvaluate'
    data = {'data': {'status': 0, 'pageNo': 1}}
    data = json.dumps(data)
    header = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'JSESSIONID=F0FE6E8F3430F4177DCBF900D09E9C19;',
    }
    r = requests.post(url, headers=header, data=data)
    res = json.dumps(r.json(), indent=2)
    print(res)
    # print(data)


if __name__ == '__main__':
    # req()
    # login()
    # search()
    login_by()

    # zjodr_search()
