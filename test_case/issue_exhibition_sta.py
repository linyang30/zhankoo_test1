from test_case.models import myunit, function
from test_case.page_obj.exhibition_sponsor_back import Exhibition_Sponsor_Back
from ddt import ddt,data

@ddt
class IssueExhibitionTest(myunit.MyTest):

    @data(*range(0, 20))
    def test_issue_exhibition(self, x):

        info = {
            'exhibition_type': 'IT通信',
            'frequency_year': '1',
            'frequency_num': '1',
            'start_holding_time': '2017/03/30',
            'end_holding_time': '2017/03/31',
            'exhibiton_description': '测试展会介绍',
            'exhibiton_scope': '测试展览范围',
            'exhibiton_tag': '标签1',
            'exhibition_organizer': '测试主办',
            'exhibition_contractor': '测试承办',
            'exhibition_standard_price': '5000',
            'exhibition_standard_area': '9',
            'exhibition_standard_remark': '测试标展',
            'exhibition_space_price': '1000',
            'exhibition_space_area': '25',
            'exhibition_space_remark': '测试光地',
            'exhibition_same_time_meeting_title': '测试同期展会',
            'start_same_time_metting': '2017-03-30T00:00:00',
            'end_same_time_metting': '2017-03-31T00:00:00',
            'same_time_meeting_address': '测试同期展会地址',
            'same_time_meeting_organizer': '测试同期展会主办方',
            'same_time_meeting_max_people': '100',
            'same_time_meeting_description': '测试同期展会描述',
            'exhibition_main_contact': '测试负责人',
            'exhibiton_phone': '075512345678',
            'exhibition_mobile': '18126127906',
            'exhibition_fax': '075587654321',
            'exhibition_qq': '123456',
            'exhibition_email': 'linyang@zhankoo.com',
            'exhibition_area': '10000',
            'exhibition_netarea': '10000',
            'exhibition_historynum': '2',
            'exhibition_viewer_quantity': '10000',
            'exhibiton_viewer_name1': '国内',
            'exhibition_viewer_percent1': '80',
            'exhibiton_viewer_name2': '国外',
            'exhibition_viewer_percent2': '20',
            'exhibition_exhibitor_quantity': '5000',
            'exhibition_exhibitor_name1': '省内',
            'exhibition_exhibitor_percent1': '60',
            'exhibition_exhibitor_name2': '省外',
            'exhibition_exhibitor_percent2': '40',
            'exhibition_viewer_satisfy': '98',
            'exhibition_exhibitor_satisfy': '85',
            'exhibiton_list': '测试参展商1,测试参展商2'
        }

        Exhibition_Sponsor_Back(self.driver).issue_exhibition(info)