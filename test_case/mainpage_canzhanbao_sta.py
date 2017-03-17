from test_case.models import myunit, function
from test_case.page_obj.login_page import Login
import random
from ddt import ddt, data

@ddt
class MainpageCanzhanbaoTest(myunit.MyTest):

    areas = ['9m²', '18m²', '27m²', '36m²', '45m²', '54m²', '72m²', '90m²', '108m²', '9-18m²', '19-36m²', '37-54m²', '55-72m²', '73-108m²', '109-200m²', '200m²以上']
    prices = ['2万以下', '2~3万', '3~5万', '5~8万', '8~12万', '12~18万', '18~25万', '25~30万', '30万以上']
    service_types = ['会展设计', '会展搭建', '会展设计+搭建']

    @data(*range(0, 20))
    def test_zhanhui(self, x):

        info = {
            'canzhanbao_name': function.ran_char(random.randint(2, 6)),
            'canzhanbao_phone': '138' + str(random.randint(11111111, 99999999)),
            'canzhanbao_company_name': function.ran_char(random.randint(5, 15)),
            'canzhanbao_exhibit': function.ran_char(random.randint(5, 15)),
            'canzhanbao_first': str(random.randint(1, 2)),
            'canzhanbao_intent_city': function.ran_char(random.randint(2, 6)),
            'time': '2017-12',
            'canzhanbao_area': random.sample(self.areas, 1)[0],
            'canzhanbao_intent_exhibition': function.ran_char(random.randint(5, 15))
        }

        Login(self.driver).canzhanbao_zhanhui(info)

    @data(*range(0, 20))
    def test_zhanzhuang(self, x):

        info = {
            'canzhanbao_name': function.ran_char(random.randint(2, 6)),
            'canzhanbao_phone': '138' + str(random.randint(11111111, 99999999)),
            'service_type': random.sample(self.service_types, 1)[0],
            'exhibition_name': function.ran_char(random.randint(5, 15)),
            'area': str(random.randint(9, 500)),
            'time': '2017-12-30',
            'price': random.sample(self.prices, 1)[0],
            'company_name': function.ran_char(random.randint(5, 15))
        }

        Login(self.driver).canzhanbao_zhanzhuang(info)