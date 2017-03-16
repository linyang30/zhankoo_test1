from test_case.models import myunit, function
from test_case.page_obj.exhibition_sponsor_back import Exhibition_Sponsor_Back
from ddt import ddt,data
import random

@ddt
class IssueExhibitionTest(myunit.MyTest):

    industries = ['IT通信', '办公用品', '电子光电', '动漫游戏', '房产家居', '纺织纺机', '服装配饰', '钢铁冶金',
                       '购物年货', '广告传媒', '化工橡胶', '婚庆婚博', '机械工业', '家电数码', '建材五金', '节能环保',
                       '酒店用品', '劳保安防', '礼品玩具', '旅游行业', '贸易进出口', '美容美发', '能源矿产', '农林渔牧',
                       '暖通制冷', '皮革鞋业', '汽车交通', '汽摩配件', '奢侈品收藏', '食品饮料', '体育休闲', '投资加盟',
                       '文教艺术', '医疗保健', '仪器仪表', '音响乐器', '印刷包装', '孕婴童', '运输物流', '纸业制品']

    @data(*range(0, 20))
    def test_issue_exhibition(self, x):

        info = {
            'exhibition_title': '测试' + function.ran_char(random.randint(1, 15)),
            'exhibition_short_name': function.ran_char(random.randint(1, 10)),
            'exhibition_type': random.sample(self.industries, 1)[0],
            'frequency_year': str(random.randint(1, 5)),
            'frequency_num': str(random.randint(1, 9)),
            'start_holding_time': '2017/12/30',
            'end_holding_time': '2017/12/31',
            'exhibiton_description': '测试' + function.ran_char(random.randint(1, 150)),
            'exhibiton_scope': function.ran_char(random.randint(1, 150)),
            'exhibiton_tag': function.tag_gen(random.randint(1, 5)),
            'exhibition_organizer': '测试' + function.ran_char(random.randint(10, 50)),
            'exhibition_contractor': function.ran_char(random.randint(10, 50)),
            'exhibition_standard_price': str(random.randint(1000, 100000)),
            'exhibition_standard_area': str(random.randint(9, 500)),
            'exhibition_standard_remark': '测试' + function.ran_char(random.randint(5, 50)),
            'exhibition_space_price': str(random.randint(1000, 100000)),
            'exhibition_space_area': str(random.randint(10, 500)),
            'exhibition_space_remark': function.ran_char(random.randint(5, 50)),
            'exhibition_same_time_meeting_title': '测试' + function.ran_char(random.randint(10, 15)),
            'start_same_time_metting': '2017-12-30T00:00:00',
            'end_same_time_metting': '2017-12-31T00:00:00',
            'same_time_meeting_address': function.ran_char(random.randint(10, 20)),
            'same_time_meeting_organizer': function.ran_char(random.randint(10, 15)),
            'same_time_meeting_max_people': str(random.randint(1000, 100000)),
            'same_time_meeting_description': function.ran_char(random.randint(10, 90)),
            'exhibition_main_contact': '测试' + function.ran_char(random.randint(2, 6)),
            'exhibiton_phone': '0755' + str(random.randint(11111111, 99999999)),
            'exhibition_mobile': '138' + str(random.randint(11111111, 99999999)),
            'exhibition_fax': '0755' + str(random.randint(11111111, 99999999)),
            'exhibition_qq': str(random.randint(111111, 999999999)),
            'exhibition_email': 'fortestonly@zhankoo.com',
            'exhibition_area': '10000',
            'exhibition_netarea': str(random.randint(1000, 100000)),
            'exhibition_historynum': str(random.randint(1, 20)),
            'exhibition_viewer_quantity': str(random.randint(1000, 100000)),
            'exhibiton_viewer_name1': function.ran_char(random.randint(2, 5)),
            'exhibition_viewer_percent1': str(random.randint(10, 40)),
            'exhibiton_viewer_name2': function.ran_char(random.randint(2, 5)),
            'exhibition_viewer_percent2': str(random.randint(10, 40)),
            'exhibition_exhibitor_quantity': str(random.randint(1000, 100000)),
            'exhibition_exhibitor_name1': function.ran_char(random.randint(2, 5)),
            'exhibition_exhibitor_percent1': str(random.randint(10, 40)),
            'exhibition_exhibitor_name2': function.ran_char(random.randint(2, 5)),
            'exhibition_exhibitor_percent2': str(random.randint(10, 40)),
            'exhibition_viewer_satisfy': str(random.randint(0, 100)),
            'exhibition_exhibitor_satisfy': str(random.randint(0, 100)),
            'exhibiton_list': '测试,' + function.tag_gen(random.randint(10, 20))
        }

        Exhibition_Sponsor_Back(self.driver).issue_exhibition(info)