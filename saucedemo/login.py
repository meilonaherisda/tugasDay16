import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import baseLogin
from PageObject.Locator import element
from PageObject.Data import inputan

class TestLogin(unittest.TestCase):
     def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

     def test_success_login(self): 
        driver = self.browser
        driver.get(inputan.baseUrl)
        baseLogin.test_success_login(driver)
        response_data = driver.find_element(By.CLASS_NAME, element.titleLogin).text
        currentUrl = driver.current_url
        self.assertIn(currentUrl, inputan.baseUrl  +"inventory.html")

     def test_failed_login(self): 
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.find_element(By.ID, element.userName).send_keys(inputan.validUser)
        driver.find_element(By.NAME, element.btnLogin).click()
        error_message = driver.find_element(By.CSS_SELECTOR, element.errMessage).text
        self.assertIn("Epic sadface: Password is required", error_message)

if __name__ == '__main__':
    unittest.main()
