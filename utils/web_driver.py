from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomDriver():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.google.com/intl/ru/gmail/about/"
        self.timeout = 30

    def wait_web_element(self, element):
        wait_lib = WebDriverWait(self.driver, self.timeout)
        web_element = wait_lib.until(EC.presence_of_element_located((element[0], element[1])))
        return web_element

    def navigation_to_page (self):
        self.driver.get(self.url)
        assert "Gmail" in self.driver.title

    def close_browser(self):
        self.driver.close()


