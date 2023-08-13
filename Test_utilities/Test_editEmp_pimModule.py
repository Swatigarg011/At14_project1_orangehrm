# import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from Test_Locators.pim_module import PimModulelocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from Test_data import credentials
from Test_Locators.login_page import LoginPageLocators



class EditpimEmpActions:

    def __init__(self):

        self.loginlocators = LoginPageLocators()
        self.pimlocator = PimModulelocator()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # Test Case to Check whether the User is able to Edit the existing details of an Employee.
    def test_edit_emp(self):
        try:
            self.driver.get(credentials.url)
            username_webelement = self.driver.find_element(By.NAME, self.loginlocators.username_locator)
            username_webelement.clear()
            username_webelement.send_keys(credentials.username)
            password_webelement = self.driver.find_element(By.NAME, self.loginlocators.password_locator)
            password_webelement.clear()
            password_webelement.send_keys(credentials.password)
            login_button_webelement = self.driver.find_element(By.XPATH, self.loginlocators.login_button_xpath)
            login_button_webelement.click()

            # Navigating to PIM Tab
            PIM = self.wait.until(EC.presence_of_element_located((By.XPATH,self.pimlocator.PIM_locator)))
            self.action.move_to_element(PIM).click(PIM).perform()

            # Search the Existing Employee with Name and Employee ID
            Search_Name = self.wait.until(EC.presence_of_element_located((By.XPATH,self.pimlocator.Searchby_Name_locator)))
            Search_Name.send_keys(credentials.Search_Name)
            self.driver.find_element(by=By.XPATH, value=self.pimlocator.Searchby_ID_locator).send_keys(credentials.Emp_ID)
            self.driver.find_element(by=By.XPATH, value=self.pimlocator.Search_locator).click()
            sleep(2)

            # Edit and Save the Last Name of the Existing Employee
            Edit_data = self.wait.until(EC.presence_of_element_located((By.XPATH, self.pimlocator.Edit_locator)))
            Edit_data.click()
            Edit_last_name = self.wait.until(EC.presence_of_element_located((By.NAME, self.pimlocator.Add_lastname_locator)))
            self.action.move_to_element(Edit_last_name).double_click(Edit_last_name).send_keys(Keys.DELETE).perform()
            Edit_last_name.send_keys(credentials.New_LastName)
            sleep(3)
            Save_Edit = self.wait.until(EC.presence_of_element_located((By.XPATH, self.pimlocator.Save_locator)))
            Save_Edit.click()
            print('Employee details Edited Successfully')
        except NoSuchElementException:
            print('Element Missing')

Obj = EditpimEmpActions()
Obj.test_edit_emp()
