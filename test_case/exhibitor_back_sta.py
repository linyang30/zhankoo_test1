from test_case.page_obj.exhibitor_back_page import Exhibitor_Back
from test_case.models.myunit import MyTest

class ExhibitorBackTest(MyTest):

    def test_exhibitor_back(self):
        Exhibitor_Back(self.driver).exhibitor_back_test()