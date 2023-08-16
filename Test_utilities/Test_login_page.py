import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.wait import WebDriverWait
# from time import sleep
from Test_data import credentials
from Test_Locators.login_page import LoginPageLocators

class Test_loginPageActions():

    # def __init__(self):
    #     self.loginlocators = LoginPageLocators()
    #     self.driver = webdriver.Chrome()
    #     self.driver.get(credentials.url)
    #     self.driver.implicitly_wait(10)
    @pytest.fixture()
    def browser(self):
        self.loginlocators = LoginPageLocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # actions = Actionchains(self.driver)
        yield
        self.driver.close()

    # Test Case to Check whether the User is able to login Orange HRM with Valid Username and Password
    def test_orangehrm_login(self,browser):
        try:
            self.driver.get(credentials.url)
            cookie_before = self.driver.get_cookies()[0]['value']
            username_webelement = self.driver.find_element(By.NAME, self.loginlocators.username_locator)
            username_webelement.clear()

            username_webelement.send_keys(credentials.username)
            password_webelement = self.driver.find_element(By.NAME, self.loginlocators.password_locator)
            password_webelement.clear()
            password_webelement.send_keys(credentials.password)
            login_button_webelement = self.driver.find_element(By.XPATH, self.loginlocators.login_button_xpath)
            login_button_webelement.click()


            cookie_after = self.driver.get_cookies()[0]['value']
            assert cookie_before != cookie_after
            print('User Logged in successfully!')
        except NoSuchElementException:
            print('Element Missing')
            self.driver.close()

            # Test Case to Check whether the User is not allowed to login Orange HRM with Invalid Password

    def test_invalid_login(self,browser):
        print("trying invalid Login Orangehrm")
        try:
            self.driver.get(credentials.url)
            cookie_before = self.driver.get_cookies()[0]['value']
            username_webelement = self.driver.find_element(By.NAME, self.loginlocators.username_locator)
            username_webelement.clear()
            username_webelement.send_keys(credentials.username)
            password_webelement = self.driver.find_element(By.NAME, self.loginlocators.password_locator)
            password_webelement.clear()
            password_webelement.send_keys(credentials.invpassword)
            login_button_webelement = self.driver.find_element(By.XPATH, self.loginlocators.login_button_xpath)
            login_button_webelement.click()

            cookie_after = self.driver.get_cookies()[0]['value']
            assert cookie_before == cookie_after
            print('Invalid Password, Login Unsuccessful!')
        except NoSuchElementException:
            print('Element Missing')
