from test_case.page_obj.supervisor_back import SupervisorBack
from test_case.models.myunit import MyTest

class DecoratorFactoryBackText(MyTest):

    def test_supervisor_back(self):
        SupervisorBack(self.driver).supervisor_back_test()