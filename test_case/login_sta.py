from test_case.models import myunit, function
from test_case.page_obj.login_page import Login


class LoginTest(myunit.MyTest):
    '''用户登录测试'''

    def user_login_verify(self, username='', password=''):
        Login(self.driver).user_login(username, password)

    def test_login1(self):
        '''用户名、密码为空登录'''
        self.user_login_verify()
        po = Login(self.driver)
        self.assertTrue('请输入手机号/邮箱' in po.user_error_hint())
        self.assertTrue('请输入密码' in po.password_error_hint())

    def test_login2(self):
        '''用户名正确，密码为空'''
        self.user_login_verify(username='13690769964')
        po = Login(self.driver)
        self.assertTrue('请输入密码' in po.password_error_hint())

    def test_login3(self):
        '''用户名或密码不正确'''
        self.user_login_verify(username='13690769964', password='654321')
        po = Login(self.driver)
        self.assertTrue('用户名或密码错误' in  po.user_or_password_error_hint())

    def test_login4(self):
        '''观察员正常登陆'''
        self.user_login_verify(username='13690769964', password='123456')
        po = Login(self.driver)
        self.assertTrue('观察员' in po.user_login_success())

    def test_login5(self):
        '''参展商正常登陆'''
        self.user_login_verify(username='13500000018', password='123456')
        po = Login(self.driver)
        self.assertTrue('参展商' in po.user_login_success())

    def test_login6(self):
        '''主办方正常登陆'''
        self.user_login_verify(username='18320836325', password='123456')
        po = Login(self.driver)
        self.assertTrue('主办方' in po.user_login_success())

    def test_login7(self):
        '''搭建商正常登陆'''
        self.user_login_verify(username='18019237332', password='123456')
        po = Login(self.driver)
        self.assertTrue('搭建商' in po.user_login_success())

    def test_login8(self):
        '''监理正常登陆'''
        self.user_login_verify(username='18165702771', password='123456')
        po = Login(self.driver)
        self.assertTrue('监理' in po.user_login_success())

    def test_login9(self):
        '''工厂正常登陆'''
        self.user_login_verify(username='18126127906', password='123456')
        po = Login(self.driver)
        self.assertTrue('工厂' in po.user_login_success())
