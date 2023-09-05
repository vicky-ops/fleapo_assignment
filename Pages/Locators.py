from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    "A class for holding all the login page locators"
    # Wishbox login
    WISH_BOX_LOGO="//img[@alt='Logo']"
    LOGIN_HEADER="//h2[normalize-space()='Log in']"
    C_CODE_DROPDOWN="//div[@class='flag in']"
    PHONE_NUMBER_FIELD="//input[@placeholder='1 (702) 123-4567']"
    CONTINUE_BUTTON="//input[@placeholder='1 (702) 123-4567']"
