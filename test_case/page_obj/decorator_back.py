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

    #服务商后台条目遍历
    def decorate_back_test(self):
        Login(self.driver).user_login(username='18019237332', password='123456')
        main_window = self.driver.current_window_handle
        self.find_element(By.XPATH, '//*[@id="pg"]/div/ul/li[2]/a[2]').click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != main_window:
                self.driver.switch_to_window(handle)

        #商家资料
        self.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]/a').click()
        assert '基本资料' in self.find_element(By.XPATH, '//*[@id="baseinfo"]/div[2]/span[1]').text

        #数据统计
        self.find_element(By.XPATH, '//*[@id="DecoratorLeft"]/div/div[1]/ul/li[2]/a').click()
        assert int(self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[4]/ul/li[1]/span[2]').text) >= 0

        #订单管理
        self.find_element(By.XPATH, '//*[@id="DecoratorLeft"]/div/div[2]/ul/li/a').click()
        assert int(self.find_element(By.XPATH, '//*[@id="blankRight"]/div[2]/ul/li[1]/a/span').text) >= 0

        #工厂列表
        self.find_element(By.CSS_SELECTOR, 'div.left_box:nth-child(3) li:nth-child(1)').click()
        assert '工厂' in self.find_element(By.XPATH, '//*[@id="FactoryType"]/li[1]/a').text

        #工厂订单
        self.find_element(By.CSS_SELECTOR, 'div.left_box:nth-child(3) li:nth-child(2)').click()
        assert '订单' in self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/ul/li[1]/a').text

        #展装申请
        self.find_element(By.CSS_SELECTOR, 'div.left_box:nth-child(4) li:nth-child(1)').click()
        assert int(self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/ul/li[1]/a/span').text) >= 0

        #发布优惠券
        self.find_element(By.CSS_SELECTOR, 'div.left_box:nth-child(5) li:nth-child(1)').click()
        assert '优惠券' in self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/span[1]').text

        #所有优惠券
        self.find_element(By.CSS_SELECTOR, 'div.left_box:nth-child(5) li:nth-child(2)').click()
        assert '优惠券' in self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/span[1]').text

        #已发放优惠券
        self.find_element(By.CSS_SELECTOR, 'div.left_box:nth-child(5) li:nth-child(3)').click()
        assert '请求' in self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/span[1]').text

        #优惠券验证
        self.find_element(By.CSS_SELECTOR, 'div.left_box:nth-child(5) li:nth-child(4)').click()
        assert '优惠券' in self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/span').text

        #H5工具


        #短信营销
        self.find_element(By.CSS_SELECTOR, 'div.left_box:nth-child(5) li:nth-child(6)').click()
        assert int(self.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[2]/h2/strong').text) >= 0

        #账户明细
        self.find_element(By.CSS_SELECTOR, 'div.left_box:nth-child(6) li:nth-child(1)').click()
        assert float(self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/ul/li[1]/div/span[2]').text.replace(',', '')) >= 0

        #账户管理
        self.find_element(By.CSS_SELECTOR, 'div.left_box:nth-child(6) li:nth-child(2)').click()
        assert '提现' in self.find_element(By.XPATH, '//*[@id="divNew"]/div/span[1]').text

        #收到的评论
        self.find_element(By.CSS_SELECTOR, 'div.left_box:nth-child(7) li:nth-child(1)').click()
        assert '我的点评' in self.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/a[3]').text

        #基本资料
        self.find_element(By.CSS_SELECTOR, 'div.left_box:nth-child(8) li:nth-child(1)').click()
        assert '基本资料' in self.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[1]/h2').text

        #公司信息
        self.find_element(By.CSS_SELECTOR, 'div.left_box:nth-child(8) li:nth-child(2)').click()
        assert '企业信息' in self.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[1]/h2').text

        #修改密码
        self.find_element(By.CSS_SELECTOR, 'div.left_box:nth-child(8) li:nth-child(3)').click()
        back_window = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != main_window and handle != back_window:
                self.driver.switch_to_window(handle)
        assert '修改密码' in self.find_element(By.XPATH, '/html/body/div[2]/div/h1/span').text
        self.driver.switch_to_window(back_window)

