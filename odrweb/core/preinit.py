# coding=utf-8
"""
  preinit.py
  Desc:
  Maintainer: wangfm
  CreateDate: 2016/12/7
"""
import ConfigParser
import argparse
import os

from tools import cfg

try:
    from webmgr.common.bak.statusdocke import checkRunner
    from initrunner import TestRunner
    from logger import logger
except ImportError:
    from webmgr.common.bak.statusdocke import checkRunner
    from webmgr.common.initrunner import TestRunner
    from webmgr.common.logger import logger

home_path = cfg.home_path
CFG_PATH = os.path.join(home_path, 'webmgr', 'cfg')
DEFAULT_CONF = os.path.join(CFG_PATH, 'init_default.conf')


def _getcfgpath(cfg_file=None):
    """
      Function: _getcfgpath()
      Desc:
      Args:
         -
      Return: None
      Usage:
      Maintainer: wangfm
      CreateDate: 2016/12/7
    """

    if cfg_file:
        absolute_cfg_file = os.path.join(CFG_PATH, cfg_file)
    else:
        absolute_cfg_file = DEFAULT_CONF
    logger.info(absolute_cfg_file)
    if os.path.isfile(absolute_cfg_file):
        return absolute_cfg_file
    else:
        raise IOError('No such file: {}'.format(absolute_cfg_file))


def setcfghost(cfg_path=None,
               platformhost=None,
               mediahost=None,
               active_code=None,
               email=None):
    """
      Function: setcfghost()
      Desc:
      Args:
         -
      Return: None
      Usage:
      Maintainer: wangfm
      CreateDate: 2016/12/6
    """

    cf = ConfigParser.ConfigParser()
    cf.read(cfg_path)
    original_platform_add = cf.get('basedata', 'addr')
    original_media_add = cf.get('streaming_media', 'serverIps')
    original_email = cf.get('basedata', 'email')
    original_active_code = cf.get('basedata', 'active_code')
    logger.info("###################configure info###################")

    if platformhost is not None:
        cf.set('basedata', 'addr', platformhost)
        cf.set('db_conf', 'host', platformhost)
        cf.set('db_conf', 'hostadd', platformhost)
        logger.info("original platform add:{0} modfied to {1}".format(
            original_platform_add, platformhost))
    else:
        logger.info("waring: platform host address not configured.")

    if mediahost is not None:
        cf.set('streaming_media', 'serverIps', mediahost)
        logger.info("original media add:{0} modfied to {1}".format(
            original_media_add, mediahost))
    else:
        logger.warning("waring: media host address not configured.")

    if active_code is not None:
        cf.set('basedata', 'active_code', active_code)
        logger.info("original media add:{0} modfied to {1}".format(
            original_active_code, mediahost))
    else:
        logger.warning("waring: active_code not configured.")

    if email is not None:
        cf.set('basedata', 'email', email)
        logger.info("original media add:{0} modfied to {1}".format(
            original_email, email))
    else:
        logger.warning("waring: media host email not configured.")

    cf.write(open(cfg_path, "w"))

    logger.info("Configuration success: {}".format(cfg_path.split('\\')[-1]))


def parseargs():
    """
      Function: parse_args()
      Desc: CLI
      Args:
         -
      Return: args
      Usage:
      Maintainer: wangfm
      CreateDate: 2016/12/7
    """
    description = 'example: python Runner.py -f dev x.x.x.x x.x.x.x -r case'
    parser = argparse.ArgumentParser(description=description)
    helph = 'The host IP address of the platform.'
    parser.add_argument('-hip', '--host', help=helph)

    helpm = 'The host IP address of the media service.'
    # parser.add_argument('media', help=helpm, nargs='?')
    parser.add_argument('-mip', '--media', help=helpm)

    helpa = 'The active code of the platform.'
    parser.add_argument('-a', '--active', help=helpa)

    email = 'Enter your email format:In order to , The separated'
    parser.add_argument('-m', '--email', help=email)

    parser.add_argument(
        '-r', '--runner', help='foo help', choices=['case', 'check'])
    parser.add_argument('-c', '--conf', help=helph)
    _args = parser.parse_args()
    return _args


def preinit():
    """
      Function: preinit()
      Desc: 输入ip地址，修改配置文件，并返回平台ip
      Args:
         -
      Return: platfrom ip address
      Usage:
      Maintainer: wangfm
      CreateDate: 2016/12/7
    """
    _args = parseargs()
    host = _args.host
    media = _args.media
    runner = _args.runner
    active_code = _args.active
    email = _args.email
    cfg_file = _args.conf
    global DEFAULT_CONF
    DEFAULT_CONF = _getcfgpath(cfg_file)
    print("current cfg path:{}".format(DEFAULT_CONF))

    # modify cfg/ini.conf
    setcfghost(DEFAULT_CONF, host, media, active_code, email)
    if runner is None:
        logger.info("Warning: Not config runner!")
        return
    if runner == 'check':
        # check docker status
        checkRunner(host)
    else:
        # run testcase
        # if checkRunner(host) is True:
        # logger.info("...")
        # _runner = TestRunner(exectype=init_conf,generateHtmlType='no',email=email)
        # _runner.run()
        # else:
        # logger.info("Service error")
        logger.info("...")
        _runner = TestRunner(generateHtmlType='no', email=email)
        _runner.run()
        logger.info("Testcase run over!")


if __name__ == '__main__':
    '''__main__'''
    preinit()
    # _getcfgpath()
