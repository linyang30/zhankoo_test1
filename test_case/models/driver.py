from selenium import webdriver

def browser():
    driver = webdriver.Chrome('F:\\web_test\\selenium\\zhankoo_test\\driver\\chromedriver.exe')
    return driver


if __name__ == '__main__':
    dr = browser()
    dr.get('http://www.baidu.com')
    dr.quit()