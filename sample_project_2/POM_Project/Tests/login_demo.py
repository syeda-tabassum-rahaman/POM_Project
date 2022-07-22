from selenium import webdriver
import time
import unittest

import HTMLTestRunner

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from sample_project_2.POM_Project.Pages.login_page import LoginPage
from sample_project_2.POM_Project.Pages.home_page import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_loginbutton()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")


if __name__ == '__main__':
    unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(
        output='C:/page_object_model_project/sample_project_2/HTML_Report'))
