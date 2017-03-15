from test_case.models import myunit, function
from test_case.page_obj.exhibitor_back_page import Exhibitor_Back

class ExhibitionBackTest(myunit.MyTest):

    def test_exhibiton_back1(self):
        '''会展搭建需求'''
        info = {
            'title': '测试展会需求auto',
            'exhibition_name': '测试2017011901',
            'num': 1,
            'service_type': '会展搭建',
            'finish_time': '2017/03/30',
            'design_req': '设计师需求',
            'decorate_req': '展装需求'
        }


        Exhibitor_Back(self.driver).issue_decorating_requirement(info)

    def test_exhibiton_back2(self):
        '''会展设计+搭建需求'''
        info = {
            'title': '测试展会需求auto',
            'exhibition_name': '测试2017011901',
            'num': 1,
            'service_type': '会展设计+搭建',
            'finish_time': '2017/03/30',
            'design_req': '设计师需求',
            'decorate_req': '展装需求'
        }


        Exhibitor_Back(self.driver).issue_decorating_requirement(info)


    def test_exhibiton_back3(self):
        '''会展设计需求'''
        info = {
            'title': '测试展会需求auto',
            'exhibition_name': '测试2017011901',
            'num': 1,
            'service_type': '会展设计',
            'finish_time': '2017/03/30',
            'design_req': '设计师需求',
            'decorate_req': '展装需求'
        }


        Exhibitor_Back(self.driver).issue_decorating_requirement(info)