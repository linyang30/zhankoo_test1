from base import Page
from login_page import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import random
from test_case.models.function import upload_img

class DecoratorBack(Page):
    '''服务商后台'''
    url = '/'

    def issue_decorated_case(self, info):
        Login(self.driver).user_login(username='18019237332', password='123456')
        main_window = self.driver.current_window_handle
        self.find_element(By.XPATH, '//*[@id="pg"]/div/ul/li[2]/a[2]').click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != main_window:
                self.driver.switch_to_window(handle)
        self.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]/a').click()
        time.sleep(1)
        self.find_element(By.XPATH, '//*[@id="companycase"]/div[2]/span[2]/a').click()

        # self.find_element(By.XPATH, '//*[@id="Title"]').send_keys(info['case_title'])
        js_case_title = "$('input[id=Title]').attr('value','%s')" % info['case_title']
        self.script(js_case_title)

        # self.find_element(By.XPATH, '//*[@id="Description"]').send_keys(info['case_description'])
        js_case_description = "$('textarea[id=Description]').attr('value','%s')" % info['case_description']
        self.script(js_case_description)

        Select(self.find_element(By.XPATH, '//*[@id="IndustryID"]')).select_by_visible_text(info['case_industry'])
        self.find_element(By.XPATH, '//*[@id="Area"]').send_keys(info['case_area'])
        Select(self.find_element(By.XPATH, '//*[@id="BoothStandardType"]')).select_by_visible_text(info['case_type'])
        Select(self.find_element(By.XPATH, '//*[@id="Material"]')).select_by_visible_text(info['case_material'])
        Select(self.find_element(By.XPATH, '//*[@id="Style"]')).select_by_visible_text(info['case_style'])
        Select(self.find_element(By.XPATH, '//*[@id="DesignerID"]')).select_by_visible_text(info['case_designer'])
        self.find_element(By.XPATH, '//*[@id="Price"]').send_keys(info['case_price'])
        # self.find_element(By.XPATH, '//*[@id="Order"]').send_keys(info['case_order'])
        js_case_order = "$('input[id=Order]').attr('value','%s')" % info['case_order']
        self.script(js_case_order)
        color_elems = random.sample(self.find_elements(By.CSS_SELECTOR, '#tbInit input')[:-1], 3)
        for elem in color_elems:
            elem.click()

        self.driver.switch_to_frame('DecorateCaseImageIframe')
        for elem in self.find_elements(By.CSS_SELECTOR, '#FileUpload1'):
            elem.click()
            time.sleep(1)
            upload_img('D:\\Temp\\1.jpg')

        self.driver.switch_to_default_content()
        self.find_element(By.XPATH, '//*[@id="BtnDecorateCaseSubmit"]').click()
        time.sleep(5)

