from selenium.webdriver.common.action_chains import ActionChains

class Page:

    url = 'http://www.zhankoo-uat.com'

    def __init__(self, selenium_driver, base_url = url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open(self.url)

    def script(self, src):
        return self.driver.execute_script(src)

    def move_on(self, element):
        ActionChains(self.driver).move_to_element(element).perform()