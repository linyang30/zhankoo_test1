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


    #参展商后台条目遍历
    def exhibitor_back_test(self):
        Login(self.driver).user_login(username='13500000018', password='123456')
        main_window = self.driver.current_window_handle
        self.find_element(*self.exhibitor_back_button_loc).click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != main_window:
                self.driver.switch_to_window(handle)
        #展会订单
        self.find_element(By.XPATH, '//*[@id="files"]/li[1]/ul/li[1]/a').click()
        assert int(self.find_element(By.XPATH, '//*[@id="MenuState"]/li[1]/a/span').text) >= 0

        #我的门票
        self.find_element(By.XPATH, '//*[@id="files"]/li[1]/ul/li[2]/a').click()
        assert '门票信息' in self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/table/tbody[1]/tr/th[1]').text

        #我的预定
        self.find_element(By.XPATH, '//*[@id="files"]/li[1]/ul/li[3]/a').click()
        assert '展会信息' in self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/table/tbody[1]/tr/th[1]').text

        #展装订单
        self.find_element(By.XPATH, '//*[@id="files"]/li[2]/ul/li[1]/a').click()
        assert int(self.find_element(By.XPATH, '//*[@id="blankRight"]/div[2]/ul/li[1]/a/span').text) >= 0

        #展装需求
        self.find_element(By.XPATH, '//*[@id="files"]/li[2]/ul/li[2]/a').click()
        assert int(self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/ul/li[1]/a/span').text) >= 0

        #账户明细
        self.find_element(By.XPATH, '//*[@id="files"]/li[3]/ul/li[1]/a').click()
        assert '展位钱包' in self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/ul/li[1]/div/span[1]').text

        #银行卡管理
        self.find_element(By.XPATH, '//*[@id="files"]/li[3]/ul/li[2]/a').click()
        assert '资金安全' in self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[1]/p').text

        #我的优惠券
        self.find_element(By.XPATH, '//*[@id="files"]/li[4]/ul/li[1]/a').click()
        assert '优惠' in self.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/a[3]').text

        #我的卡券
        self.find_element(By.XPATH, '//*[@id="files"]/li[4]/ul/li[2]/a').click()
        assert '我的卡券' in self.find_element(By.XPATH, '//*[@id="topHeader"]/div[2]/div/a[3]').text

        #我的关注
        self.find_element(By.XPATH, '//*[@id="files"]/li[5]/ul/li/a').click()
        assert '我的关注' in self.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/a[3]').text

        #我的点评
        self.find_element(By.XPATH, '//*[@id="files"]/li[6]/ul/li/a').click()
        assert '我的点评' in self.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/a[3]').text

        #基本资料
        self.find_element(By.XPATH, '//*[@id="files"]/li[7]/ul/li[1]/a').click()
        assert '个人资料' in self.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div/div[1]/h2').text

        #参展信息
        self.find_element(By.XPATH, '//*[@id="files"]/li[7]/ul/li[2]/a').click()
        assert '参展信息' in self.find_element(By.XPATH, '/html/body/div[3]/div/a[3]').text

        #修改密码
        self.find_element(By.XPATH, '//*[@id="files"]/li[7]/ul/li[3]/a').click()
        back_window = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != main_window and handle != back_window:
                self.driver.switch_to_window(handle)
        assert '修改密码' in self.find_element(By.XPATH, '/html/body/div[2]/div/h1/span').text
        self.driver.switch_to_window(back_window)

        #全部消息
        self.find_element(By.XPATH, '//*[@id="files"]/li[8]/ul/li/a').click()
        assert '全部消息' in self.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/a[3]').text






