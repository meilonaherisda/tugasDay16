import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import baseLogin
from PageObject.Locator import element
from PageObject.Data import inputan

class TestAddCart(unittest.TestCase):
     def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

     def test_Add_toCart(self):
         driver = self.browser
         driver.get(inputan.baseUrl)
         baseLogin.test_success_login(driver)
         driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
         driver.find_element(By.CLASS_NAME, element.cart).click()
         currentUrl = driver.current_url
         self.assertIn(currentUrl, inputan.baseUrl  +"cart.html")
    
     def test_checkout(self):
         driver = self.browser
         driver.get(inputan.baseUrl)
         baseLogin.test_success_login(driver)
         driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
         driver.find_element(By.CLASS_NAME, element.cart).click()
         driver.find_element(By.CSS_SELECTOR, element.btnCheckout).click()
         driver.find_element(By.ID,element.firstName).send_keys(inputan.firstName)
         driver.find_element(By.ID,element.lastName).send_keys(inputan.lastName)
         driver.find_element(By.ID,element.zipcode).send_keys(inputan.zipcode)
         driver.find_element(By.CSS_SELECTOR, element.btnContinue).click()
         currentUrl = driver.current_url
         self.assertIn(currentUrl, inputan.baseUrl  +"checkout-step-two.html")
         response_data = driver.find_element(By.CLASS_NAME,"title").text

if __name__ == '__main__':
    unittest.main()
