from test_case.models import myunit,function
from test_case.page_obj.decorator_back import DecoratorBack
import random
from ddt import ddt, data

@ddt
class IssueDecoratedCaseTest(myunit.MyTest):

    case_industries = ['IT通信', '办公用品', '电子光电', '动漫游戏', '房产家居', '纺织纺机', '服装配饰', '钢铁冶金',
                       '购物年货', '广告传媒', '化工橡胶', '婚庆婚博', '机械工业', '家电数码', '建材五金', '节能环保',
                       '酒店用品', '劳保安防', '礼品玩具', '旅游行业', '贸易进出口', '美容美发', '能源矿产', '农林渔牧',
                       '暖通制冷', '皮革鞋业', '汽车交通', '汽摩配件', '奢侈品收藏', '食品饮料', '体育休闲', '投资加盟',
                       '文教艺术', '医疗保健', '仪器仪表', '音响乐器', '印刷包装', '孕婴童', '运输物流', '纸业制品']
    case_types = ['单开门', '双开门', '三开门', '岛型', '双层展位']
    case_materials = ['木质材质', '桁架型材', '环保材料']
    case_styles = ['简约', '现代', '中式', '欧式', '美式', '田园', '新古典', '混搭']
    case_designers = ['小强2sfs', '设计师1']


    @data(*range(0, 20))
    def test_issue_decorated_case(self, x):
        info = {
            'case_title': '测试' + function.ran_char(random.randint(1, 15)),
            'case_description': function.ran_char(random.randint(1, 130)),
            'case_industry': random.sample(self.case_industries, 1)[0],
            'case_area': str(random.randint(1, 500)),
            'case_type': random.sample(self.case_types, 1)[0],
            'case_material': random.sample(self.case_materials, 1)[0],
            'case_style': random.sample(self.case_styles, 1)[0],
            'case_designer': random.sample(self.case_designers, 1)[0],
            'case_price': str(random.randint(1, 2000000)),
            'case_order': str(random.randint(0, 999))
        }

        DecoratorBack(self.driver).issue_decorated_case(info)