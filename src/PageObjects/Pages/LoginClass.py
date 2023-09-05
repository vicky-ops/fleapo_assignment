
import sys

sys.path.append(sys.path[0]+"/...")

# might need add sys.path(OS.getcwd())

from selenium.webdriver.common.by import By
from src.PageObjects.Locators import Locator

class LOGIN(object):
    def __int__(self,driver):
        self.driver = driver
        self.logo = driver.find_element(By.XPATH,Locator.WISH_BOX_LOGO)
        self.continue_btn = driver.find_element(By.XPATH,Locator.CONTINUE_BUTTON)



    # Methods

    def getLogo(self):
        return self.logo
    def getContinue(self):
        return self.continue_btn

