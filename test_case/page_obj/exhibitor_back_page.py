from base import Page
from login_page import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys


class Exhibitor_Back(Page):
    '''参展商后台'''

    url = '/'
    exhibitor_back_button_loc = (By.XPATH, '//*[@id="pg"]/div/ul/li[2]/a[2]')

    #发布展装需求
    def issue_decorating_requirement(self, info):
        Login(self.driver).user_login(username='13500000018', password='123456')
        main_window = self.driver.current_window_handle
        self.find_element(*self.exhibitor_back_button_loc).click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != main_window:
                self.driver.switch_to_window(handle)
        back_window = self.driver.current_window_handle
        self.find_element(By.XPATH, '//*[@id="files"]/li[2]/ul/li[2]/a').click()
        current_req_num = int(self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/ul/li[1]/a/span').text)
        self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/ul/li/a').click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != main_window and handle != back_window:
                self.driver.switch_to_window(handle)
        #填写标题
        self.find_element(By.XPATH, '//*[@id="Subject"]').send_keys(info['title'])
        #填写展会名称
        self.find_element(By.XPATH, '//*[@id="ExhibitionName"]').send_keys(info['exhibition_name'])
        time.sleep(1)
        self.find_element(By.XPATH, '//*[@id="ExhibitionName"]').send_keys(Keys.ENTER)
        #填写展会编号
        self.find_element(By.XPATH, '//*[@id="BoothName"]').send_keys(info['num'])
        time.sleep(1)
        self.find_element(By.XPATH, '//*[@id="BoothName"]').send_keys(Keys.ENTER)
        #选择服务类型
        sel_service_type = self.find_element(By.ID, 'ServiceItem')
        Select(sel_service_type).select_by_value(info['service_type'])
        #选择展装公司地点
        sel_province = self.find_element(By.ID, 'ProvinceCode')
        Select(sel_province).select_by_value('440000')
        sel_city = self.find_element(By.ID, 'CityCode')
        Select(sel_city).select_by_value('440300')
        #填写交工时间
        js_finish_time = "$('input[name=FinishOn]').attr('value','%s')" % info['finish_time']
        self.script(js_finish_time)
        #填写设计师需求
        self.find_element(By.ID, 'DesignerDemand').send_keys(info['design_req'])
        #填写展装需求
        self.find_element(By.ID, 'DecorateDemand').send_keys(info['decorate_req'])
        #提交需求
        self.find_element(By.ID, 'btnDecorateBookSave').click()
        req_num = int(self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/ul/li[1]/a/span').text)
        assert req_num == current_req_num + 1





