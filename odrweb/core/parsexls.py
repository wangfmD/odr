# -*- coding:utf-8 -*-

import json
import logging
import os
import sys
from datetime import datetime

from xlrd import xldate_as_tuple

try:
    import xlrd
except:
    os.system('pip install -U xlrd')
    import xlrd

base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

# base_path = os.path.join(f_path ,'data')
#

class XlsFile(object):
    def __init__(self, absolute_path=None, xls_name=None):
        """
        文件名和绝对路径二选一，如都传参取绝对路径
        推荐使用文件
        :param absolute_path: 绝对路径
        :param xls_name: 文件名称
        """
        # logging.info("xls_path: {}".format(self.xls_path))
        # 当没有全路径和文件名时，报错；有全路径时，读全路径；没有全路径读默认路径下指定文件（全路径要包含文件名啊）
        if absolute_path is None and xls_name is None:
            raise TypeError(u"error: 缺少绝对路径或者相对路径")
        elif absolute_path is not None:
            # print 0
            self.xls_path = absolute_path
        else:
            # print 1
            self.xls_path = os.path.join(base_path, "data", xls_name)
        print("xls_path: {}".format(self.xls_path))

    def parse_xls_by_row(self, sheetName):
        # 按行来解析excel
        # 当文件路径不存在时报错退出
        if not os.path.exists(self.xls_path):
            logging.error('...测试用例文件不存在！！！')
            sys.exit()
        # 打开xls_path路径指向的excel文件
        testCase = xlrd.open_workbook(self.xls_path)
        # 通过名称查找excel里面的表单
        table = testCase.sheet_by_name(sheetName)
        # table.row_values返回给定行中的单元格数量。
        # 每一行都作为一个字典，包在列表里面，取第一行为key对应下面的值
        keys = table.row_values(0)
        # print 'keys:', keys
        list_result = []
        for i in range(1, table.nrows):
            row = table.row_values(i)
            list_result.append(dict(zip(keys, row)))
        return list_result

    def parse_xls_by_col(self, sheetName):
        if not os.path.exists(self.xls_path):
            logging.error('...测试用例文件不存在！！！')
            sys.exit()
        testCase = xlrd.open_workbook(self.xls_path)
        table = testCase.sheet_by_name(sheetName)
        keys = table.col_values(0)
        list_result = []
        for i in range(1, table.ncols):
            row = table.col_values(i)
            list_result.append(dict(zip(keys, row)))
        return list_result

    def parse_xls_by_row_data(self, sheetName, flag=0):
        if flag not in [0, 1]:
            logging.error('...flag must be 0 or 1')
            sys.exit()
        if not os.path.exists(self.xls_path):
            logging.error('...测试用例文件不存在！！！')
            sys.exit()
        testCase = xlrd.open_workbook(self.xls_path)
        table = testCase.sheet_by_name(sheetName)
        print table
        keys = table.row_values(0)
        list_result = []
        for i in range(1, table.nrows):
            row = table.row_values(i)
            row1 = []
            for cell in row:
                if type(cell) == float:
                    date = datetime(*xldate_as_tuple(cell, 0))
                    if flag == 0:
                        value = date.strftime('%Y/%m/%d %H:%M')
                    else:
                        value = date.strftime('%Y/%m/%d')
                    row1.append(value)
                else:
                    row1.append(cell)
            list_result.append(dict(zip(keys, row1)))
        return list_result


def example():
    xls_f1 = XlsFile(xls_name=r"test_jf.xlsx")
    rowlist = xls_f1.parse_xls_by_row("test_adddata_school")
    print json.dumps(rowlist, indent=2, ensure_ascii=False)
    # collist = xls_f1.parse_xls_by_col("noticelist")
    # print json.dumps(collist, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    example()
    pass
