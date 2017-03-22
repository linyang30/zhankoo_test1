from test_case.page_obj.exhibition_sponsor_back import Exhibition_Sponsor_Back
from test_case.models.myunit import MyTest

class ExhibitionSponsorBackTest(MyTest):

    def test_exhibition_sponsor_back(self):
        Exhibition_Sponsor_Back(self.driver).exhibition_sponsor_back_test()