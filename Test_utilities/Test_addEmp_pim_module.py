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


class AddPimEmpActions:

    def __init__(self):

        self.loginlocators = LoginPageLocators()
        self.pimlocator = PimModulelocator()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    # Test Case to Check whether the User is able to Add and Create Login for the New Employee
    def test_add_emp(self):
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
            PIM = self.wait.until(EC.presence_of_element_located((By.XPATH, self.pimlocator.PIM_locator)))
            self.action.move_to_element(PIM).click(PIM).perform()

            # Adding an Employee in PIM
            Add_Tab = self.wait.until(EC.presence_of_element_located((By.XPATH, self.pimlocator.AddEmp_locator)))
            self.action.move_to_element(Add_Tab).click(Add_Tab).perform()

            Add_Emp = self.wait.until(EC.presence_of_element_located((By.NAME, self.pimlocator.Add_firstname_locator)))
            Add_Emp.send_keys(credentials.FirstName)
            self.driver.find_element(by=By.NAME, value=self.pimlocator.Add_middlename_locator).send_keys(credentials.MiddleName)
            self.driver.find_element(by=By.NAME, value=self.pimlocator.Add_lastname_locator).send_keys(credentials.LastName)
            clear_input = self.wait.until(EC.presence_of_element_located((By.XPATH, self.pimlocator.Emp_ID_locator)))
            Add_Img = self.wait.until(EC.presence_of_element_located((By.XPATH, self.pimlocator.Add_image_locator)))
            Add_Img.click()
            Add_Img.send_keys('C:/Users/hp/PycharmProjects/project1_AT14_swati_orangehrm/Test_data/test1.png')
            self.action.move_to_element(clear_input).double_click(clear_input).send_keys(Keys.DELETE).perform()
            sleep(5)
            self.driver.find_element(by=By.XPATH, value=self.pimlocator.Emp_ID_locator).send_keys(credentials.Emp_ID)
            sleep(5)
            # self.driver.find_element(by=By.XPATH, value=self.pimlocator.Add_image_locator).send_keys(credentials.Emp_img)



            sleep(5)

            # Creating Login for the New Employee
            self.driver.find_element(by=By.XPATH, value=self.pimlocator.Create_login_locator).click()
            Emp_Login = self.wait.until(EC.presence_of_element_located((By.XPATH, self.pimlocator.Login_id_locator)))
            Emp_Login.send_keys(credentials.Login_ID)
            C_Login_P = self.wait.until(EC.presence_of_element_located((By.XPATH, self.pimlocator.Login_password_locator)))
            C_Login_P.send_keys(credentials.Login_password)
            self.driver.find_element(by=By.XPATH, value=self.pimlocator.Login_confirmpass_locator).send_keys(credentials.Login_password)
            sleep(2)
            Submit = self.wait.until(EC.presence_of_element_located((By.XPATH, self.pimlocator.Add_Emp_Submit_locator)))
            Submit.click()
            sleep(5)
            print('New Employee Data and Login Created Successfully')
        except NoSuchElementException:
            print('Element Missing')


Obj= AddPimEmpActions()
Obj.test_add_emp()
