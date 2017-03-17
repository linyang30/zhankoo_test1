from test_case.models import myunit, function
from test_case.page_obj.login_page import Login
import random
from ddt import ddt, data

@ddt
class MainpageCooprationTest(myunit.MyTest):

    @data(*range(0, 20))
    def test_exhibition(self, x):

        info = {
            'company_name': function.ran_char(random.randint(5, 15)),
            'exhibition_name': function.ran_char(random.randint(5, 15)),
            'contact_name': function.ran_char(random.randint(2, 6)),
            'mobile': '138' + str(random.randint(11111111, 99999999)),
            'phone': '0755-' + str(random.randint(11111111, 99999999)),
            'email': 'fortestonly@zhankoo.com'
        }

        Login(self.driver).exhibition_coopration(info)

    @data(*range(0, 20))
    def test_decorate(self, x):

        info = {
            'company_name': function.ran_char(random.randint(5, 15)),
            'contact_name': function.ran_char(random.randint(2, 6)),
            'mobile': '138' + str(random.randint(11111111, 99999999)),
            'phone': '0755-' + str(random.randint(11111111, 99999999)),
            'email': 'fortestonly@zhankoo.com'
        }

        Login(self.driver).decorate_coopration(info)