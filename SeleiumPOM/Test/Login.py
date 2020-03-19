import HtmlTestRunner
import allure
from selenium import webdriver
import time
import unittest
from SeleiumPOM.Pages.LoginPage import LoginPage
from SeleiumPOM.Pages.HomePage import HomePage



class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("D:/Python/Testing/SeleniumFramework/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test1LoginCase(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
       # time.sleep(5)
        login = LoginPage(driver)

        #login = LoginPage(driver)

        login.enter_username("Admin")
        time.sleep(5)
        login.enter_password("admin123")
        time.sleep(5)
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

    def test2InvalidCredentials(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin1")
        time.sleep(5)
        login.enter_password("admin123")
        time.sleep(5)
        login.click_login()
        message = login.check_invalid_message()
        self.assertEqual(message, "Invalid credentials")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Python/Testing/SeleniumFramework/Reports'))


