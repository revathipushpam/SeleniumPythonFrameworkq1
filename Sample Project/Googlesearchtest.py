from selenium import webdriver
import unittest
import HtmlTestRunner

class GoogleSearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("D:\Python\Testing\SeleniumFramework\Drivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def testOneSearchGoogle(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Automation step by step raghav")
        self.driver.find_element_by_name("btnK").click()

    def testTwoSearchGoogle(self):
        self.driver.get("http://google.com")
        self.driver.find_element_by_name("q").send_keys("Way2Automation")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Python/Testing/SeleniumFramework/Reports'))

