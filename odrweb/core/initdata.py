# coding=utf-8
import ConfigParser
# import os
import sys

from webmgr.common.logger import logger


def get_cfg_path():
    from webmgr.common.preinit import DEFAULT_CONF
    return DEFAULT_CONF


def getCfgs(cfg_path):
    logger.info(cfg_path)
    # 配置文件的学校、教室、设备信息
    classroom_para = []

    classroom_tmp = []

    # 测试平台的访问路径前缀
    base_url = ''

    # 管理平台数据库信息配配置
    db_conf = {}

    loginInfo = {}

    execEnv = {}

    # 流媒体地址配置
    streaming_media = {}

    cf = ConfigParser.ConfigParser()
    cf.read(cfg_path)
    sections = cf.sections()
    # 从配置文件中读取用户登录信息

    for s in sections:
        if s.lower().find('classroom_para') != -1:
            classroom_tmp.append(s)
        if s.lower().find('basedata') != -1:
            base_url = 'http://' + cf.get(s, 'addr')
            child_interact_ip = cf.get(s, 'interact_1')
            loginInfo.setdefault('username', cf.get(s, 'username'))
            loginInfo.setdefault('platformname', cf.get(s, 'platformname'))
            loginInfo.setdefault('email', cf.get(s, 'email'))
        if s.lower().find('db_conf') != -1:
            # host = cf.get(s, 'host')
            db_conf.setdefault('host', cf.get(s, 'host'))
            # hostadd = cf.get(s, 'hostadd')
            db_conf.setdefault('hostadd', cf.get(s, 'hostadd'))
            # user = cf.get(s, 'user')
            db_conf.setdefault('user', cf.get(s, 'user'))
            # passwd = cf.get(s, 'passwd')
            db_conf.setdefault('passwd', cf.get(s, 'passwd'))
            # db = cf.get(s, 'db')
            db_conf.setdefault('db', cf.get(s, 'db'))
            db_conf.setdefault('port', cf.get(s, 'port'))
        if s.lower().find('env_para') != -1:
            execEnv.setdefault('execType', cf.get(s, 'execType'))
            execEnv.setdefault('remoteUrl', cf.get(s, 'remoteUrl'))
        if s.lower().find('streaming_media') != -1:
            streaming_media.setdefault('serverIps', cf.get(s, 'serverIps'))
    # from conf get classroom_para
    for s in classroom_tmp:
        opts = cf.options(s)
        arr = {}
        for o in opts:
            name = cf.get(s, o)
            arr.setdefault(o, unicode(name).encode("utf-8"))
        classroom_para.append(arr)
    return classroom_para, base_url, db_conf, loginInfo, execEnv, streaming_media, child_interact_ip


def get_active_code(cfg_path):
    logger.info(cfg_path)
    cf = ConfigParser.ConfigParser()
    cf.read(cfg_path)
    active_code = cf.get('basedata', 'active_code')
    # cf.set('basedata', 'addr', 'www')
    # cf.write(open(cfg_path, "w"))
    return active_code


class cfg(object):
    def __init__(self):
        # self.logFile = getLogFile()
        self.cfg_path = get_cfg_path()
        print("init cfg path:{}".format(self.cfg_path))
        self.tmpData = getCfgs(self.cfg_path)
        self.classroom_para = self.tmpData[0]
        self.base_url = self.tmpData[1]
        self.db_conf = self.tmpData[2]

        self.email = self.tmpData[3]["email"]
        self.loginInfo = self.tmpData[3]
        self.execEnv = self.tmpData[4]
        self.streaming_media = self.tmpData[5]
        self.child_interact_ip = self.tmpData[6]
        #   读取路径
        # data_path = getSqlPath(self.base_url, self.db_conf)
        # data_path = getSqlPath(self.base_url)
        # self.sqlFilePath = data_path[0]
        # self.sqlStatements = data_path[1]
        self.active_code = get_active_code(self.cfg_path)
        #         self.sqlFilePathVer = data_path[1]
        logger.info(
            "#############################Init basedata start#############################"
        )
        logger.info("\t{0:<12}\t{1:<12}".format('base_url', self.base_url))
        logger.info("\t{0:<12}\t{1:<12}".format('cfg_path', self.cfg_path))
        for k, v in self.streaming_media.items():
            logger.info("\t{0:<12}\t{1:<12}".format(k, v))
        for k, v in self.db_conf.items():
            logger.info("\t{0:<12}\t{1:<12}".format(k, v))
        for k, v in self.loginInfo.items():
            logger.info("\t{0:<12}\t{1:<12}".format(k, v + u''))
        logger.info(
            "#############################Init basedata end#############################"
        )


def a():
    cf = cfg()
    ic = cf.classroom_para
    def cc():
        tmp = []
        return set([i.get('schoolid') for i in ic])

    def _gorup(sch):
        return  [i for i in ic if i.get('schoolid') == sch]

    d = [_gorup(i) for i in cc() ]
    print d

def cc():
    cf = cfg()
    ic = cf.classroom_para
    tmp = []
    return set([i.get('schoolid') for i in ic if i.get('schoolid') not in tmp])

init = cfg()
if __name__ == "__main__":
    # _path = getCfgPath()
    # cfg = cfg()
    # # getCfgs(_path)
    # # print cfg.classroom_para
    # for c in cfg.classroom_para:
    #     if isinstance(c,dict):
    #         for k,v in c.iteritems():
    #             print k,":",v
    # d = [i for i in cfg.classroom_para if ]
    a()