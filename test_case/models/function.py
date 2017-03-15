import os
from test_case.models.driver import browser
import win32con
import win32gui
import time


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

if __name__ == '__main__':
    driver = browser()
    driver.get('http://www.baidu.com')
    insert_img(driver, 'baidu.jpg')
    driver.quit()