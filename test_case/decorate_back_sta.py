from test_case.page_obj.decorator_back import DecoratorBack
from test_case.models.myunit import MyTest

class DecoratorBackText(MyTest):

    def test_decorator_back(self):
        DecoratorBack(self.driver).decorate_back_test()