from base import Page
from selenium.webdriver.common.by import By
from time import sleep


class Login(Page):
    '''
    用户登录界面
    '''


    url = '/'
    zhankoo_login_button_loc = (By.PARTIAL_LINK_TEXT, '请登录')

    #进入登录页面
    def zhankoo_login(self):
        self.find_element(*self.zhankoo_login_button_loc).click()

    login_username_loc = (By.ID, 'Name')
    login_password_loc = (By.ID, 'Password')
    login_button_loc = (By.ID, 'js-login')

    #登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)

    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    user_error_hint_loc = (By.XPATH, '//*[@id="form0"]/label[1]')
    password_error_hint_loc = (By.XPATH, '//*[@id="form0"]/label[2]')
    user_or_password_hint_loc = (By.XPATH, '/html/body/div[3]/div/div/label')

    #用户名错误提示
    def user_error_hint(self):
        return self.find_element(*self.user_error_hint_loc).text

    #密码错误提示
    def password_error_hint(self):
        return self.find_element(*self.password_error_hint_loc).text

    #用户名或密码错误提示
    def user_or_password_error_hint(self):
        return self.find_element(*self.user_or_password_hint_loc).text

    #登录过程
    def user_login(self, username='13690769964', password='123456'):
        self.open()
        self.zhankoo_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)

    user_login_success_loc = (By.XPATH, '//*[@id="pg"]/div/ul/li[2]/a[1]/em')

    #登录成功
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text

    search_input_loc = (By.XPATH, '//*[@id="searchText"]')
    search_button_loc = (By.ID, 'searchButton')
    search_select_loc = (By.XPATH, '/html/body/div[5]/div/div[1]/div[1]')
    search_type_zhaozhanhui_loc = (By.XPATH, '/html/body/div[5]/div/div[1]/div[1]/ul/li/div/span[1]')
    seach_type_zhaozhanzhuang_loc = (By.XPATH, '/html/body/div[5]/div/div[1]/div[1]/ul/li/div/span[2]')

    #选择搜索类型，type=0展会，type=1展装
    def search_select_type(self, type):
        self.move_on(self.find_element(*self.search_select_loc))
        self.find_elements(By.CSS_SELECTOR, 'div.oh span')[type].click()

    #点击搜索按钮
    def search_button(self):
        self.find_element(*self.search_button_loc).click()

    #填写搜索关键字
    def search_keywords(self, keyword):
        self.find_element(*self.search_input_loc).send_keys(keyword)

    #搜索过程
    def search(self, type=1, keyword=''):
        self.open()
        self.search_select_type(type)
        self.search_keywords(keyword)
        self.search_button()
        sleep(1)
