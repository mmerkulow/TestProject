import unittest
from utils.login_page import LoginPage


class TestsGmail(unittest.TestCase):
    login_class = LoginPage()

    @classmethod
    def setUpClass(cls):
        super(TestsGmail, cls).setUpClass()
        cls.login_class.custom_driver.navigation_to_page()

    def test_gmail_login(self):
        self.login_class.login()

    @classmethod
    def tearDownClass(cls):
        super(TestsGmail, cls).setUpClass()
        cls.login_class.custom_driver.close_browser()
