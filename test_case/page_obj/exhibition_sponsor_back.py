from base import Page
from login_page import Login
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.select import Select
import time
from test_case.models.function import upload_img

class Exhibition_Sponsor_Back(Page):
    '''主办方后台'''

    url = '/'

    # 主办方发布展会
    def issue_exhibition(self, info):
        ran_int = random.randint(11111, 99999)
        Login(self.driver).user_login(username='18320836325', password='123456')
        main_window = self.driver.current_window_handle
        self.find_element(By.XPATH, '//*[@id="pg"]/div/ul/li[2]/a[2]').click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != main_window:
                self.driver.switch_to_window(handle)
        self.find_element(By.XPATH, '//*[@id="menu"]/ul[1]/li[2]/a').click()
        #基本信息
        self.find_element(By.XPATH, '//*[@id="BtnBasic"]').click()
        self.find_element(By.XPATH, '//*[@id="Name"]').send_keys(info['exhibition_title'])
        self.find_element(By.XPATH, '//*[@id="ShortName"]').send_keys(info['exhibition_short_name'])
        Select(self.find_element(By.XPATH, '//*[@id="IndustryID"]')).select_by_visible_text(info['exhibition_type'])
        self.find_element(By.XPATH, '//*[@id="2"]').click()
        self.find_element(By.XPATH, '//*[@id="3"]').click()
        self.find_element(By.XPATH, '//*[@id="HoldFrequencyWithYear"]').send_keys(info['frequency_year'])
        self.find_element(By.XPATH, '//*[@id="HoldFrequency"]').send_keys(info['frequency_num'])
        js_start_holding_time = "$('input[id=FromOn]').attr('value','%s')" % info['start_holding_time']
        self.script(js_start_holding_time)
        js_end_holding_time = "$('input[id=ToOn]').attr('value','%s')" % info['end_holding_time']
        self.script(js_end_holding_time)
        self.find_element(By.XPATH, '//*[@id="DivBasic"]/table/tbody/tr[7]/td[2]/button').click()
        time.sleep(1)
        self.driver.switch_to_frame('layui-layer-iframe1')
        self.find_element(By.XPATH, '//*[@id="PavilionPaged"]/div[1]/ul/li[1]/input').click()
        self.find_element(By.XPATH, '//*[@id="SelectPavilion"]').click()
        self.find_element(By.XPATH, '//*[@id="Site"]').send_keys('www.zhankoo.com')
        self.find_element(By.XPATH, '//*[@id="DivBasic"]/div/button[1]').click()
        time.sleep(1)
        assert '测试' in self.find_element(By.XPATH, '//*[@id="BasicDetail"]/table/tbody/tr[1]/td[2]').text

        #展会介绍
        self.find_element(By.XPATH, '//*[@id="BtnIntro"]').click()
        self.find_element(By.XPATH, '//*[@id="Description"]').send_keys(info['exhibiton_description'])
        self.find_element(By.XPATH, '//*[@id="Scope"]').send_keys(info['exhibiton_scope'])
        self.find_element(By.XPATH, '//*[@id="Tag"]').send_keys(info['exhibiton_tag'])
        self.find_element(By.XPATH, '//*[@id="DivIntro"]/div/button[1]').click()
        time.sleep(1)
        assert '测试' in self.find_element(By.XPATH, '//*[@id="DivIntro2"]/table/tbody/tr[1]/td[2]').text

        #举办机构
        self.find_element(By.XPATH, '//*[@id="BtnInsti"]').click()
        self.find_element(By.XPATH, '//*[@id="Organizer"]').send_keys(info['exhibition_organizer'])
        self.find_element(By.XPATH, '//*[@id="Contractor"]').send_keys(info['exhibition_contractor'])
        self.find_element(By.XPATH, '//*[@id="DivInsti"]/div/button[1]').click()
        time.sleep(1)
        assert '测试' in self.find_element(By.XPATH, '//*[@id="DivInsti2"]/table/tbody/tr[1]/td[2]').text

        #展位信息
        self.find_element(By.XPATH, '//*[@id="BtnBasicBooth"]').click()
        self.find_element(By.XPATH, '//*[@id="StandardBoothMoney"]').send_keys(info['exhibition_standard_price'])
        self.find_element(By.XPATH, '//*[@id="StandardBoothArea"]').send_keys(info['exhibition_standard_area'])
        self.find_element(By.XPATH, '//*[@id="StandardBoothRemark"]').send_keys(info['exhibition_standard_remark'])
        self.find_element(By.XPATH, '//*[@id="BareSpaceBoothMoney"]').send_keys(info['exhibition_space_price'])
        self.find_element(By.XPATH, '//*[@id="BareSpaceBoothArea"]').send_keys(info['exhibition_space_area'])
        self.find_element(By.XPATH, '//*[@id="BareSpaceBoothRemark"]').send_keys(info['exhibition_space_remark'])
        self.find_element(By.XPATH, '//*[@id="BasicBoothInsert"]/div[2]/button[1]').click()
        time.sleep(1)
        assert '测试' in self.find_element(By.XPATH, '//*[@id="BasicBoothDetail"]/table/tbody/tr[2]/td[4]').text

        #展会图片
        self.find_element(By.XPATH, '//*[@id="BtnPicture"]').click()
        picUploadElems = self.driver.find_elements_by_id('FileUpload1')
        for picUpload in picUploadElems:
            picUpload.click()
            time.sleep(1)
            upload_img('D:\\Temp\\1.jpg')
        self.find_element(By.XPATH, '//*[@id="DivPicture"]/div[3]/button[1]').click()
        time.sleep(1)

        #同期会议
        self.find_element(By.ID, 'BtnMeeting').click()
        time.sleep(1)
        # self.find_element(By.CSS_SELECTOR, '#Name').send_keys(info['exhibition_same_time_meeting_title'])
        js_same_time_meeting_title = "$('input[id=Name]').attr('value','%s')" % info['exhibition_same_time_meeting_title']
        self.script(js_same_time_meeting_title)

        js_meeting_from_on = "$('input[id=MeetingFromOn]').attr('value','%s')" % info['start_same_time_metting']
        self.script(js_meeting_from_on)
        js_meeting_to_on = "$('input[id=MeetingToOn]').attr('value','%s')" % info['end_same_time_metting']
        self.script(js_meeting_to_on)
        self.find_element(By.XPATH, '//*[@id="Address"]').send_keys(info['same_time_meeting_address'])

        # self.find_element(By.XPATH, '//*[@id="Organizer"]').send_keys(info['same_time_meeting_organizer'])
        js_same_time_meeting_organizer = "$('input[id=Organizer]').attr('value','%s')" % info['same_time_meeting_organizer']
        self.script(js_same_time_meeting_organizer)

        self.find_element(By.XPATH, '//*[@id="MaxPeople"]').send_keys(info['same_time_meeting_max_people'])
        self.find_element(By.XPATH, '//*[@id="MeetingSave"]/table/tbody/tr[6]/td[2]/button').click()
        time.sleep(1)
        upload_img('D:\\Temp\\1.jpg')

        # self.find_element(By.ID, 'Description').send_keys(info['same_time_meeting_description'])
        js_same_time_meeting_description = "$('textarea[id=Description]').attr('value','%s')" % info['same_time_meeting_description']
        self.script(js_same_time_meeting_description)

        self.find_element(By.XPATH, '//*[@id="MeetingSave"]/div/button[1]').click()
        time.sleep(1)
        assert '测试' in self.find_element(By.XPATH, '//*[@id="meetinglist"]/div/div[1]/ul/li[2]/span[1]').text

        #联系方式
        self.find_element(By.XPATH, '//*[@id="BtnContact"]').click()
        self.find_element(By.XPATH, '//*[@id="Contact"]').send_keys(info['exhibition_main_contact'])
        self.find_element(By.XPATH, '//*[@id="Telephone"]').send_keys(info['exhibiton_phone'])
        self.find_element(By.XPATH, '//*[@id="Mobile"]').send_keys(info['exhibition_mobile'])
        self.find_element(By.XPATH, '//*[@id="Fax"]').send_keys(info['exhibition_fax'])
        self.find_element(By.XPATH, '//*[@id="QQ"]').send_keys(info['exhibition_qq'])
        self.find_element(By.XPATH, '//*[@id="Email"]').send_keys(info['exhibition_email'])
        self.find_element(By.XPATH, '//*[@id="DivContact"]/div/button[1]').click()
        time.sleep(1)
        assert '测试' in self.find_element(By.XPATH, '//*[@id="DivContact2"]/table/tbody/tr[1]/td[2]').text

        #展会数据
        self.find_element(By.XPATH, '//*[@id="BtnData"]').click()
        self.find_element(By.XPATH, '//*[@id="Area"]').send_keys(info['exhibition_area'])
        self.find_element(By.XPATH, '//*[@id="NetArea"]').send_keys(info['exhibition_netarea'])
        self.find_element(By.XPATH, '//*[@id="HistoryNum"]').send_keys(info['exhibition_historynum'])
        self.find_element(By.XPATH, '//*[@id="ViewerQuantity"]').send_keys(info['exhibition_viewer_quantity'])
        self.find_element(By.XPATH, '//*[@id="DivData"]/table/tbody/tr[5]/td[2]/a').click()
        self.find_element(By.XPATH, '//*[@id="DivData"]/table/tbody/tr[7]/td[2]/a').click()
        name_elements= self.find_elements(By.ID, 'textfield3')
        percent_elements = self.find_elements(By.ID, 'textfield6')
        name_elements[0].send_keys(info['exhibiton_viewer_name1'])
        percent_elements[0].send_keys(info['exhibition_viewer_percent1'])

        name_elements[1].send_keys(info['exhibiton_viewer_name2'])
        percent_elements[1].send_keys(info['exhibition_viewer_percent2'])
        self.find_element(By.XPATH, '//*[@id="ExhibitorQuantity"]').send_keys(info['exhibition_exhibitor_quantity'])
        name_elements[2].send_keys(info['exhibition_exhibitor_name1'])
        percent_elements[2].send_keys(info['exhibition_exhibitor_percent1'])

        name_elements[3].send_keys(info['exhibition_exhibitor_name2'])
        percent_elements[3].send_keys(info['exhibition_exhibitor_percent2'])
        self.find_element(By.XPATH, '//*[@id="ViewerSatisfy"]').send_keys(info['exhibition_viewer_satisfy'])
        self.find_element(By.XPATH, '//*[@id="ExhibitorSatisfy"]').send_keys(info['exhibition_exhibitor_satisfy'])
        self.find_element(By.XPATH, '//*[@id="DivData"]/div/button[1]').click()
        time.sleep(1)
        assert '10000' in self.find_element(By.XPATH, '//*[@id="DivData2"]/table/tbody/tr[1]/td[2]').text

        #展商名录
        self.find_element(By.XPATH, '//*[@id="BtnExhibitor"]').click()
        self.find_element(By.XPATH, '//*[@id="ExhibitorList"]').send_keys(info['exhibiton_list'])
        self.find_element(By.XPATH, '//*[@id="DivExhibitor"]/div/button[1]').click()
        time.sleep(1)
        assert '测试' in self.find_element(By.XPATH, '//*[@id="DivExhibitor2"]/table/tbody/tr/td[2]').text




