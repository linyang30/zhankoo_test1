#-*- coding: UTF-8 -*-

from models import myunit, function
from page_obj.login_page import Login


class LoginTest(myunit.MyTest):
    '''用户登录测试'''

    def user_login_verify(self, username='', password=''):
        Login(self.driver).user_login(username, password)

    def test_login1(self):
        '''用户名、密码为空登录'''
        self.user_login_verify()
        po = Login(self.driver)
        # print po.user_error_hint().encode('utf-8')
        # assert po.user_error_hint().encode('utf-8') == '请输入手机号/邮箱'
        # assert po.password_error_hint().encode('utf-8') == '请输入密码'
        print type(po.user_error_hint())
        print type(u'请输入手机号/邮箱')
        assert po.user_error_hint() == '请输入手机号/邮箱'.decode('utf-8')
