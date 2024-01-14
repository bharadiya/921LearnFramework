from selenium.webdriver.common.by import By
from selenium import  webdriver

class LoginPage:

    # constructor to initialize all the weblocators of particular page and also to pass instance of driver
    def __init__(self,driver):
        self.driver=driver
        self.emailOrPhoneNumber_input_id="email"
        self.password_input_xpath="//input[@name='pass']"
        self.loginButton_button_cssselector ="[name='login']"
        self.fbTagLineMessage_h2_xpath="//div[@id='content']//h2"

    # Here every weblocator has method , if 5 locators on page, then 5 methods

    def enterEmailOrPhoneNumber(self,driver,username):
        self.driver.find_element(By.ID,self.emailOrPhoneNumber_input_id).send_keys(username)

    def enterPassword(self,driver,password):
        self.driver.find_element(By.XPATH,self.password_input_xpath).send_keys(password)

    def clickLoginButton(self,driver):
        self.driver.find_element(By.CSS_SELECTOR,self.loginButton_button_cssselector).click()

    def getTagMessage(self,driver):
        tagLineMsg = self.driver.find_element(By.XPATH,self.fbTagLineMessage_h2_xpath).text
        return tagLineMsg

# <webelement name_tag-name_locatortype>
