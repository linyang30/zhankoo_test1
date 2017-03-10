from test_case.models import myunit, function
from test_case.page_obj.exhibitor_back_page import Exhibitor_back

class ExhibitionBackTest(myunit.MyTest):

    def test_exhibiton_back(self):
        Exhibitor_back(self.driver).issue_decorating_requirement()