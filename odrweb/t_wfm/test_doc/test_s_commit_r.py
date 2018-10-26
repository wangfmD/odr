# coding: utf-8
import sys
import unittest

from odrweb.core.utils import _funcname_docstring

reload(sys)
sys.setdefaultencoding("utf-8")


class JudicialInputCommit(unittest.TestCase):
    """调解员-司法确认提交"""

    def setUp(self):
        print "\n--------------------"

    def tearDown(self):
        pass

    def _funcname_docstring(self):
        """返回方法名称+docstring"""
        prdfix, _ = self.__str__().split(" ")
        file_name = "".join([prdfix,"_",self.__doc__])
        print self.__str__()
        return file_name

    def test_06(self):
        """调解员-司法确认-法人-非法人组织-代
        """
        print _funcname_docstring(self)
        print self._funcname_docstring()


if __name__ == '__main__':
    unittest.main()
