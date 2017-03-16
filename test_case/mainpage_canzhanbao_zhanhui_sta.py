from test_case.models import myunit, function
from test_case.page_obj.login_page import Login
import random
from ddt import ddt, data

@ddt
class MainpageCanzhanbaoTest(myunit.MyTest):

    areas = ['9m²', '18m²', '27m²', '36m²', '45m²', '54m²', '72m²', '90m²', '108m²', '9-18m²', '19-36m²', '37-54m²', '55-72m²', '73-108m²', '109-200m²', '200m²以上']

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