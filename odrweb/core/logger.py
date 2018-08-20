# coding:utf-8
import logging
import sys
import os
from tools import cfg


def __setlogfile(filepath):
    fh = logging.FileHandler(filepath)
    return fh


def __setstream():
    ch = logging.StreamHandler()
    return ch


def __ststreamstdout():
    cho = logging.StreamHandler(sys.stdout)
    return cho


def init_log(filepath):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    fh = __setlogfile(filepath)
    ch = __setstream()
    # format = '[%(asctime)s %(name)s %(filename)s line:%(lineno)d %(levelname)s] %(message)s'
    # format = '[%(asctime)s %(name)s.py %(levelname)s] %(message)s'
    format = '[%(asctime)s %(filename)s line:%(lineno)d %(levelname)s] %(message)s'
    formatstream = '%(message)s'
    formatter = logging.Formatter(format)
    formatterstream = logging.Formatter(formatstream)

    fh.setFormatter(formatter)
    ch.setFormatter(formatterstream)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


def T_INFO(logger, msg):
    # print msg
    logger.info(msg)


def getlogfile():
    logpath = cfg.webmgr_log_path
    logfile = os.path.join(logpath, "webmgr.log")

    if os.path.exists(logpath) is True:
        print ">>\nLog path: {}".format(logpath)
    else:
        print "Create report directory..."
        os.mkdir(logpath)
        print ">>Log path:  {}".format(logpath)
    return logfile


logger = init_log(getlogfile())

print cfg.webmgr_log_path
