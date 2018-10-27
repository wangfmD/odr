# coding:utf-8
import os
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pymysql
from pymysql import cursors

dir = os.path.dirname
HOMEPATH = dir(os.path.abspath(dir(__file__)))


class sqlOperating:
    '''数据库操作'''
    host = '10.1.41.20'
    # hostadd = db_conf['hostadd']
    user = 'root'
    passwd = 'Sanbu@123456'
    db = 'middle'
    port = 13306

    def __init__(self, host=host, user=user, passwd=passwd, db=db, port=13306):
        try:
            self.con = pymysql.connect(host=host,
                                       user=user,
                                       passwd=passwd,
                                       db=db,
                                       port=port,
                                       cursorclass=cursors.DictCursor)
            print "DB connection info:"
            print "  >>host: {0}\n  >>user: {1}\n  >>password: {2}\n  >>database: " \
                  "{3}\n  >>port:{4}".format(host, user, passwd, db, port)
        except pymysql.Error, e:
            print "Mysql Err %d:%s" % (e.args[0], e.args[1])

    def execQury(self, sql):
        cur = self.con.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        # print dir(cur)
        return res
        self.con.close()

    def updaeDb(self, sql):
        cur = self.con.cursor()
        try:
            cur.execute(sql)
            self.con.commit()
            print 'updated successful.'
        except:
            self.con.rollback()
            print 'updated failed.'
        self.con.close()
        print 'closed connection.'


def sendReportWithAtt(attachment, *args):
    """
      Function: sendReportWithAtt
      Desc: used to send test report
      Args:
         - : file
         - : 'xx@xx.com,xx@xx.com'
      Return: None
      Usage: sendReportWithAtt(attachment, receiver)
      Maintainer: wangfm
    """
    f = open(attachment, 'rb')
    sendfile = f.read()
    f.close()
    # set os path
    if os.name == 'nt':
        attName = str(attachment).split('\\')[-1]
    else:
        attName = str(attachment).split('/')[-1]
    # init
    smtpserver = 'smtp.exmail.qq.com'
    sender = 'devops@3bu.cn'  # 发件地址
    # receiver = 'liman@3bu.cn,wujp@3bu.cn,fuyj@3bu.cn,lubb@3bu.cn,lukai@3bu.cn,wangfm@3bu.cn,tengfei@3bu.cn,daiyd@3bu.cn,daicj@3bu.cn,wuf@3bu.cn>,xiahao@3bu.cn,'  # 收件人地址，多人以分号分隔
    receiver = args[0]
    user = 'devops@3bu.cn'
    password = 'Xungejiaoyu@2015'
    Subject = '自动化测试报告'
    # set mail
    msgRoot = MIMEMultipart('related')
    att = MIMEText(sendfile, 'html', 'utf-8')
    # att['Content-Type'] = 'application/octet-stream'
    # att['Content-Disposition'] = 'attachment, filename = "report.html"'
    msgRoot['Subject'] = Subject
    msgRoot['From'] = sender
    msgRoot['to'] = receiver
    msgRoot.attach(att)
    mime = MIMEBase('application', 'html', filename=attName)
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename=attName)
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(sendfile)
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msgRoot.attach(mime)
    # send mail
    smtp = smtplib.SMTP(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(msgRoot['From'], msgRoot['To'].split(','),
                  msgRoot.as_string())
    smtp.quit()


def sendReport(file_new):
    """
      Function: sendReport
      Desc:send mail without attachment
      Args:
      Return:None
      Usage: sendReport(file)
    """
    with open(file_new, 'rb') as f:
        mail_body = f.read()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = 'devops@3bu.cn'  # 发件地址
    msg['To'] = 'liman@3bu.cn,wujp@3bu.cn,fuyj@3bu.cn,lubb@3bu.cn,lukai@3bu.cn,\
        wangfm@3bu.cn,tengfei@3bu.cn,daiyd@3bu.cn,daicj@3bu.cn,wuf@3bu.cn>,xiahao@3bu.cn'
    # 收件人地址，多人以分号分隔

    smtp = smtplib.SMTP('smtp.exmail.qq.com')
    smtp.login('devops@3bu.cn', 'Xungejiaoyu@2015')  # 登录邮箱的账户和密码
    smtp.sendmail(msg['From'], msg['To'].split(','), msg.as_string())

    smtp.quit()


def is_male(user_id):
    """根据身份证id，判断性别
    """
    try:
        flag = int(user_id[16])
        if (flag % 2) == 0:
            return False
        else:
            return True
    except:
        res = True

    return res


def _funcname_docstring(self, docstr):
    """返回方法名称+docstring"""
    # docstr = getdoc(getattr(self, getframeinfo(currentframe()).function))
    prdfix, _ = self.__str__().split(" ")
    # print type(self.__doc__.decode('utf8'))
    file_name = "".join([prdfix, "_", docstr])
    return file_name


if __name__ == '__main__':
    # sql = "select CUR_VER from middle_db_version ORDER BY CUR_VER desc LIMIT 1"
    # c = sqlOperating()
    # result = c.execQury(sql)
    # for lie in result:
    #     for k, v in lie.iteritems():
    #         print k, "=", lie[k]
    # print is_male('321023199508166626')
    # print mediaAddr
    print HOMEPATH
