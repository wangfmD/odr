# coding=utf-8
import ConfigParser
import os

dir = os.path.dirname
home_path = dir(os.path.abspath(dir(__file__)))

class Users(object):
    user_wfm=''
    user_jgdjy=''
    user_tjy=''
    user_kf=''
    user_zxs=''
    user_bafg=''
    user_bmxlzxysxxjg=''
    user_xhfyfwjg=''
    user_shenadmin=''
    user_shiadmin=''
    user_quadmin=''

class Init(object):
    def __init__(self):
        path = os.path.join(home_path, 'cfg', 'default.conf')
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(path)
        self.browser = self.cf.get('common', 'browser')
        self.base_url = self.cf.get('common', 'base_url')

users = Users()
init = Init()




def get_cfg_path():
    path = os.path.join(home_path, 'cfg')
    cfg_file = os.path.join(path, 'users.conf')
    return cfg_file


def getCfgs(cfg_path):
    # 配置文件的学校、教室、设备信息

    cf = ConfigParser.ConfigParser()
    cf.read(cfg_path)
    # sections = cf.sections()

    # 普通用户
    username = cf.get('user_wfm', 'username')
    pwd = cf.get('user_wfm', 'pwd')
    users.user_wfm = {"username": username, 'pwd': pwd}


    # 机构登记员
    username = cf.get('user_jgdjy', 'username')
    pwd = cf.get('user_jgdjy', 'pwd')
    users.user_jgdjy = {"username": username, 'pwd': pwd}
    # [user_jgdjy]
    # username=1805130007
    # pwd=123456

    # 调解员宋红波
    username = cf.get('user_tjy', 'username')
    pwd = cf.get('user_tjy', 'pwd')
    users.user_tjy = {"username": username, 'pwd': pwd}
    # [user_tjy]
    # username=13817765056
    # pwd=000000

    # 客服
    username = cf.get('user_kf', 'username')
    pwd = cf.get('user_kf', 'pwd')
    users.user_kf = {"username": username, 'pwd': pwd}
    # [user_kf]
    # username=13600527465
    # pwd=000000

    # 咨询师
    username = cf.get('user_zxs', 'username')
    pwd = cf.get('user_zxs', 'pwd')
    users.user_zxs = {"username": username, 'pwd': pwd}
    # [user_zxs]
    # username=3606706616
    # pwd=000000

    # 办案法官
    username = cf.get('user_bafg', 'username')
    pwd = cf.get('user_bafg', 'pwd')
    users.user_bafg = {"username": username, 'pwd': pwd}
    # [user_bafg]
    # username=13067812519
    # pwd=000000

    # 北明心理咨询演示学习机构
    username = cf.get('user_bmxlzxysxxjg', 'username')
    pwd = cf.get('user_bmxlzxysxxjg', 'pwd')
    users.user_bmxlzxysxxjg = {"username": username, 'pwd': pwd}
    # [user_bmxlzxysxxjg]
    # username=17612156739
    # pwd=123456

    # 西湖法院服务机构管理
    username = cf.get('user_xhfyfwjg', 'username')
    pwd = cf.get('user_xhfyfwjg', 'pwd')
    users.user_xhfyfwjg = {"username": username, 'pwd': pwd}
    # [user_xhfyfwjg]
    # username=13800000000
    # pwd=123456

    # 省级账号
    username = cf.get('user_shenadmin', 'username')
    pwd = cf.get('user_shenadmin', 'pwd')
    users.user_shenadmin = {"username": username, 'pwd': pwd}
    # [user_shenadmin]
    # username=M330000
    # pwd=123456

    # 市级账号
    username = cf.get('user_shiadmin', 'username')
    pwd = cf.get('user_shiadmin', 'pwd')
    users.user_shiadmin = {"username": username, 'pwd': pwd}
    # [user_shiadmin]
    # username=M330100
    # pwd=123456

    # 西湖区级账号
    username = cf.get('user_quadmin', 'username')
    pwd = cf.get('user_quadmin', 'pwd')
    users.user_quadmin = {"username": username, 'pwd': pwd}
    # [user_quadmin]
    # username=M330106
    # pwd=123456

# class cfg(object):
#
#         logger.info(
#             "#############################Init basedata start#############################"
#         )
#         logger.info("\t{0:<12}\t{1:<12}".format('base_url', self.base_url))
#         logger.info("\t{0:<12}\t{1:<12}".format('cfg_path', self.cfg_path))
#         for k, v in self.streaming_media.items():
#             logger.info("\t{0:<12}\t{1:<12}".format(k, v))
#         for k, v in self.db_conf.items():
#             logger.info("\t{0:<12}\t{1:<12}".format(k, v))
#         for k, v in self.loginInfo.items():
#             logger.info("\t{0:<12}\t{1:<12}".format(k, v + u''))
#         logger.info(
#             "#############################Init basedata end#############################"
#         )


getCfgs(get_cfg_path())

if __name__ == "__main__":
    # print(get_cfg_path())
    # print(home_path)
    # getCfgs(get_cfg_path())

    # for k,v in users.iteritems():
    #     print(k,":",v)
    # print(users)
    print init.browser,init.base_url