from selenium.webdriver.common.by import By
from utils.base_page import BaseClass


class LoginPage(BaseClass):
    def __init__(self):
        super().__init__()
        self.user_email = "maxiivanov1984@gmail.com"
        self.sign_in = (By.XPATH, '//a[@data-action="sign in"]')
        self.input_email = (By.XPATH, "//input[@type='email']")
        self.next_button = (By.XPATH, "//span[text()='Далее']")
        self.input_password = (By.XPATH, "//input[@name='Passwd']")

    def login(self):
        elem = self.custom_driver.wait_web_element(self.sign_in)
        elem.click()
        input_field = self.custom_driver.wait_web_element(self.input_email)
        input_field.send_keys(self.user_email)
        next_button = self.custom_driver.wait_web_element(self.next_button)
        next_button.click()
