from test_case.page_obj.decorate_factory_back import DecorateFactoryBack
from test_case.models.myunit import MyTest

class DecoratorFactoryBackText(MyTest):

    def test_decorator_factory_back(self):
        DecorateFactoryBack(self.driver).decorate_factory_back_test()