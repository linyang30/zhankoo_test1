from test_case.page_obj.login_page import Login
from test_case.models import myunit, function
import time

class SearchTest(myunit.MyTest):
    def search_verify(self, type=0, keyword=''):
        Login(self.driver).search(type, keyword)

    #搜索展会，关键字为空
    def test_search_zhanhui(self):
        self.search_verify(type=0, keyword='')


    #搜索展装，关键字为空
    def test_search_zhanzhuang(self):
        self.search_verify(type=1, keyword='')

    #搜索展会，关键词为“测试”
    def test_search_zhanhui2(self):
        self.search_verify(type=0, keyword='测试')

    #搜索展会，关键词为“测试”
    def test_search_zhanzhuang2(self):
        self.search_verify(type=1, keyword='测试')
