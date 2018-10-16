# -*- coding:utf-8 -*-
from time import sleep

import win32api
import win32clipboard as w
import SendKeys
import win32con


def file_upload():
    """文件上传：ctrl-v & enter
    """
    sleep(1)
    # ctrl+v
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(86, 0, 0, 0)  # V键位码是73
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)    # 释放按键
    win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)    # 释放按键
    # enter
    SendKeys.SendKeys('{ENTER}')  # 发送回车键


def set_windows_clipboard(coper_string):
    """设置windows的黏贴板内容
    """
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_TEXT, coper_string)
    w.CloseClipboard()


def get_windows_text():
    """获取windows黏贴板内容
    """
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d

def demo():
    from odrweb.core.initdata import users
    from odrweb.page.homepage import HomePage
    homepage = HomePage()
    homepage.mediator_login(users.user_tjy['username'], users.user_tjy['pwd'])
    homepage.find_element_by_xpath('//font[text()="新增司法确认"]').click()
    sleep(2)
    homepage.find_element_by_xpath('//div[text()="证据附件："]/following-sibling::div').click()
    set_windows_clipboard('D:\\00jt\\1.png')
    file_upload()
