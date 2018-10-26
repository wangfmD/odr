# coding: utf-8
import sys
import unittest

from odrweb.core.initdata import users
from odrweb.core.utils import _funcname_docstring

from odrweb.page.homepage import HomePage
from odrweb.page.personalpage import PersonalPage

reload(sys)
sys.setdefaultencoding("utf-8")

old = users.user_wfm['pwd']
new = '22222222'


class UserSecure(unittest.TestCase):
    ''' 普通用户-安全设置'''

    def setUp(self):
        self.homepage = HomePage()
        print "\n--------------------"

    def tearDown(self):
        self.homepage.driver.quit()

    def test_01(self):
        '''用户修改密码'''
        print "oldpwd: ", old
        try:
            self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
            self.homepage.user_personal_center()
            personalpage = PersonalPage(self.homepage)
            personalpage.modify_passwd(old, new)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise

    def test_02(self):
        '''用户改回原密码'''
        print "oldpwd: ", old
        try:
            self.homepage.user_login(users.user_wfm['username'], new)
            self.homepage.user_personal_center()
            personalpage = PersonalPage(self.homepage)
            personalpage.modify_passwd(new, old)
        except Exception as msg:
            print "EXCEPTION >> {}".format(msg)
            # class function name_class docstring
            name = _funcname_docstring(self)
            # 截图
            self.homepage.save_screen_shot(name)
            raise


if __name__ == '__main__':
    unittest.main()
