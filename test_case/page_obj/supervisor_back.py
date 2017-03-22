from base import Page
from login_page import Login
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.select import Select
import time
from test_case.models.function import upload_img

class SupervisorBack(Page):
    '''监理后台'''

    url = '/'

    def supervisor_back_test(self):
        Login(self.driver).user_login(username='18165702771', password='123456')
        main_window = self.driver.current_window_handle
        self.find_element(By.XPATH, '//*[@id="pg"]/div/ul/li[2]/a[2]').click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != main_window:
                self.driver.switch_to_window(handle)

        #展装订单
        self.find_element(By.XPATH, '//*[@id="files"]/li[1]/ul/li/a').click()
        assert int(self.find_element(By.XPATH, '//*[@id="blankRight"]/div[2]/ul/li[1]/a/span').text) >= 0

        #个人资料
        self.find_element(By.XPATH, '//*[@id="files"]/li[2]/ul/li[1]/a').click()
        assert '个人资料' in self.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[1]/h2').text

        #修改密码
        self.find_element(By.XPATH, '//*[@id="files"]/li[2]/ul/li[2]/a').click()
        assert '修改密码' in self.find_element(By.XPATH, '/html/body/div[2]/div/h1/span').text
        self.driver.back()

        #全部消息
        self.find_element(By.XPATH, '//*[@id="files"]/li[3]/ul/li/a').click()
        assert '全部消息' in self.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/a[3]').text