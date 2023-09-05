from selenium import webdriver
import time
from time import sleep
import warnings
import urllib3


class WebDriverSetup():
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.driver = webdriver.chrome
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def cleanUp(self):
        if(self.driver != None):
            print("Cleaning up test environment")
            self.driver.close()
            self.driver.quit()
