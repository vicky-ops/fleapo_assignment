from selenium.webdriver.support.ui import WebDriverWait
class BasePageElement(object):
    "Base page classs"
    def __set__(self,obj,value):
        # Sets the text value supplied
        driver = obj.driver
        WebDriverWait(driver,100).until(lambda driver:driver.find_element_by_id(self.locator))
        driver.find_element_by(self.)