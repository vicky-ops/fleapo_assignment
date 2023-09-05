import sys
sys.path.append(sys.path[0],"/...")
import unittest

from src.test.WebDriverSetup import WebDriverSetup
from src.PageObjects.Pages.LoginClass import LOGIN
from selenium import webdriver


class Home_page(self)

   def test_home_page(self):
       driver = self.driver
       self.driver.get("https://wishbox2.vercel.app/")
       # we will add settime later if needed
       web_page_url = "https://wishbox2.vercel.app/"
       web_page_title = "https://wishbox2.vercel.app/"
      try:
         if(driver.title == web_page_title)
             print("Login Web page loaded successfully")
             self.assertionEqual(driver.title,web_page_title)

