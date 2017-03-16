from test_case.models import myunit, function
from test_case.page_obj.exhibitor_back_page import Exhibitor_Back
from ddt import ddt, data
import random

@ddt
class ExhibitionBackTest(myunit.MyTest):

    service_types = ['会展搭建', '会展设计+搭建', '会展设计']

    @data(*range(0, 20))
    def test_exhibiton_back(self, x):

        info = {
            'title': function.ran_char(random.randint(10, 15)),
            'exhibition_name': '测试2017011901',
            'num': 1,
            'service_type': random.sample(self.service_types, 1)[0],
            'finish_time': '2017/12/30',
            'design_req': function.ran_char(random.randint(10, 90)),
            'decorate_req': function.ran_char(random.randint(10, 90))
        }


        Exhibitor_Back(self.driver).issue_decorating_requirement(info)
