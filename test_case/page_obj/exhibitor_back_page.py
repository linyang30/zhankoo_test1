from base import Page
from login_page import Login
from selenium.webdriver.common.by import By

class Exhibitor_back(Page):
    '''参展商后台'''

    url = '/'
    exhibitor_back_button_loc = (By.XPATH, '//*[@id="pg"]/div/ul/li[2]/a[2]')

    #发布展装需求
    def issue_decorating_requirement(self, title, exhibition_name, num):
        Login(self.driver).user_login(username='13500000018', password='123456')
        main_window = self.driver.current_window_handle
        self.find_element(*self.exhibitor_back_button_loc).click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != main_window:
                self.driver.switch_to_window(handle)
        back_window = self.driver.current_window_handle
        self.find_element(By.XPATH, '//*[@id="files"]/li[2]/ul/li[2]/a').click()
        self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/ul/li/a').click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != main_window and handle != back_window:
                self.driver.switch_to_window(handle)
        #填写标题
        self.find_element(By.XPATH, '//*[@id="Subject"]').send_keys(title)
        #填写展会名称
        self.find_element(By.XPATH, '//*[@id="ExhibitionName"]').send_keys(exhibition_name)
        #填写展会编号
        self.find_element(By.XPATH, '//*[@id="BoothName"]').send_keys(num)





