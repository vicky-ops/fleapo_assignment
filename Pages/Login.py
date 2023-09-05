from elements import BasePageElement
from locators import C











class BasePage(object):
    "Initializing the base page"
    def __init__(self,driver):
        self.driver = driver



class LoginPage(BasePage):
    "Login Page action methods are mentioned here"

    #Declaring input fields
    PHONE_FIELD_ = TelElem()

