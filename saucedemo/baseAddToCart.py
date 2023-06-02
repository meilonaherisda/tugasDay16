import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def test_add_cart(driver):
     url = "https://www.saucedemo.com/"
     driver.get(url)
     driver.find_element(By.CSS_SELECTOR, "[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    