import unittest
from selenium import webdriver
import pages


class test_wishbox_loginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.firefox()
        self.driver.get("https://wishbox2.vercel.app/")


    def test_check_logo_and_header(self):
        login_page = pages.LoginPage(self.driver)

        ## filling up the phone number field
        login_page.