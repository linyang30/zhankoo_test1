from test_case.page_obj.login_page import Login
from test_case.models import myunit, function

class SearchTest(myunit.MyTest):
    def test_search_zhanhui(self):
        po = Login(self.driver)
        po.open()
        po.search_select_type()
        po.search()
