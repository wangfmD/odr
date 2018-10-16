# coding: utf-8
import sys
import unittest

from odrweb.core.initdata import users
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
        self.homepage.quit()

    def test_01(self):
        '''用户修改密码'''
        print "oldpwd: ", old
        self.homepage.user_login(users.user_wfm['username'], users.user_wfm['pwd'])
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.modify_passwd(old, new)

    def test_02(self):
        '''用户改回原密码'''
        print "oldpwd: ", old
        self.homepage.user_login(users.user_wfm['username'], new)
        self.homepage.user_personal_center()
        personalpage = PersonalPage(self.homepage)
        personalpage.modify_passwd(new, old)


if __name__ == '__main__':
    unittest.main()
