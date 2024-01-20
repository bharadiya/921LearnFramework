import unittest
import time

from selenium import webdriver
from Pages.Login import LoginPage


class AppTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("../drivers/chromedriver.exe")
        cls.driver.maximize_window()
        cls.driver.get("https://fb.com")

    def test_AssertGoogleTitle(self):
        lp = LoginPage(self.driver)
        lp.enterEmailOrPhoneNumber("XYZ")
        messageGotWhileAutomation = lp.getTagMessage()
        expectedMessage = "Facebook helps you in your life."

        # self.assertEqual(messageGotWhileAutomation,expectedMessage)

        lp.getTagMessage()
        lp.enterPassword("GHI")
        lp.clickLoginButton()
        time.sleep(15)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

