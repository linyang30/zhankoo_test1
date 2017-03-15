from test_case.models import myunit
from test_case.page_obj.decorator_back import DecoratorBack
import random

class IssueDecoratedCaseTest(myunit.MyTest):

    def test_issue_decorated_case(self):
        info = {
            'case_title': '测试展装案例' + str(random.randint(11111, 99999)),
            'case_description': '测试展装案例描述',
            'case_industry': 'IT通信',
            'case_area': '9',
            'case_type': '单开门',
            'case_material': '木质材质',
            'case_style': '简约',
            'case_designer': '设计师1',
            'case_price': '2000',
            'case_order': '10'
        }

        DecoratorBack(self.driver).issue_decorated_case(info)