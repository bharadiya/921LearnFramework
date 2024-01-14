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
        lp.enterEmailOrPhoneNumber(self.driver,"XYZ")
        messageGotWhileAutomation = lp.getTagMessage(self.driver)
        expectedMessage = "Facebook helps you in your life."

        self.assertEqual(messageGotWhileAutomation,expectedMessage)

        lp.getTagMessage(self.driver)
        lp.enterPassword(self.driver,"GHI")
        lp.clickLoginButton(self.driver)
        time.sleep(15)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()

