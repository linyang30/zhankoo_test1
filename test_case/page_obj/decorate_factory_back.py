from base import Page
from login_page import Login
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.select import Select
import time
from test_case.models.function import upload_img

class DecorateFactoryBack(Page):
    '''展装工厂后台'''

    url = '/'

    def decorate_factory_back_test(self):
        Login(self.driver).user_login(username='18126127906', password='123456')
        main_window = self.driver.current_window_handle
        self.find_element(By.XPATH, '//*[@id="pg"]/div/ul/li[2]/a[2]').click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != main_window:
                self.driver.switch_to_window(handle)
        #订单管理
        self.find_element(By.XPATH, '//*[@id="files"]/li[1]/ul/li/a').click()
        assert '订单管理' in self.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/a[3]').text

        #账户明细
        self.find_element(By.XPATH, '//*[@id="files"]/li[2]/ul/li[1]/a').click()
        assert float(self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/ul/li[1]/div/span[2]').text) >= 0

        #银行卡管理
        self.find_element(By.XPATH, '//*[@id="files"]/li[2]/ul/li[2]/a').click()
        assert '银行卡管理' in self.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/a[3]').text

        #基本资料
        self.find_element(By.XPATH, '//*[@id="files"]/li[3]/ul/li[1]/a').click()
        assert '基本资料' in self.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[1]/h2').text

        #修改密码
        self.find_element(By.XPATH, '//*[@id="files"]/li[3]/ul/li[2]/a').click()
        assert '修改密码' in self.find_element(By.XPATH, '/html/body/div[2]/div/h1/span').text
        self.driver.back()

        #全部消息
        self.find_element(By.XPATH, '//*[@id="files"]/li[4]/ul/li/a').click()
        self.driver.back()
