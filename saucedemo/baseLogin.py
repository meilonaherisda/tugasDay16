import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PageObject.Locator import element

def test_success_login(driver): 
    url = "https://www.saucedemo.com/"
    driver.get(url)
    driver.find_element(By.ID, element.userName).send_keys("performance_glitch_user")
    driver.find_element(By.CSS_SELECTOR, element.password).send_keys("secret_sauce")
    driver.find_element(By.NAME, element.btnLogin).click()