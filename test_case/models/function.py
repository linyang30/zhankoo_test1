# coding=utf-8

import os
from test_case.models.driver import browser
import win32con
import win32gui
import time
import random


def insert_img(driver, file_name):
    base_dir = os.path.dirname(__file__)
    base = base_dir.split('/test_case')[0]
    file_path = base + '/report/image/' + file_name
    driver.get_screenshot_as_file(file_path)

def upload_img(path):
    uploadwindow = win32gui.FindWindow('#32770', '打开')
    parent = win32gui.FindWindowEx(uploadwindow, None, 'ComboBoxEx32', None)
    Combobox_real = win32gui.FindWindowEx(parent, None, 'ComboBox', None)
    Edit_box = win32gui.FindWindowEx(Combobox_real, None, 'Edit', None)
    button = win32gui.FindWindowEx(uploadwindow, None, 'Button', None)
    win32gui.SendMessage(Edit_box, win32con.WM_SETTEXT, None, path)
    win32gui.SendMessage(uploadwindow, win32con.WM_COMMAND, 1, button)
    time.sleep(2)

def ran_char(length):
    s = "1234567890()-、abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ对酒当歌人生几何譬如朝露去日苦多慨当以慷忧思难忘何以解忧惟有杜康青青子衿悠悠我心但为君故沉吟至今呦呦鹿鸣食野之苹我有嘉宾鼓瑟吹笙明明如月何时可掇忧从中来不可断绝关关雎鸠在河之洲窈窕淑女君子好逑参差荇菜左右流之窈窕淑女寤寐求之求之不得寤寐思服悠哉悠哉辗转反侧参差荇菜左右采之窈窕淑女琴瑟友之参差荇菜左右芼之窈窕淑女钟鼓乐之"
    res = ''
    while length > 0:
        res += random.sample(s, 1)[0]
        length -= 1
    return res

def tag_gen(num):
    res = ''
    while num > 0:
        t = ran_char(random.randint(2, 5))
        res = res +  ',' + t
        num -= 1
    return res[1:]


if __name__ == '__main__':
    # driver = browser()
    # driver.get('http://www.baidu.com')
    # insert_img(driver, 'baidu.jpg')
    # driver.quit()
    # print(ran_char(200))
    print(tag_gen(5))