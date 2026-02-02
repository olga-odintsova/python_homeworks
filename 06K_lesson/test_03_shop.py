import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


def test_form():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))

    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, '#password').send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
    driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
    driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Helga")
    driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Odintsova")
    driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys("0144")
    driver.find_element(By.CSS_SELECTOR, '#continue').click()

    result = driver.find_element(By.CSS_SELECTOR, '.summary_total_label').text
    print(result)

    driver.quit()

    assert result.split(" ")[1] == "$58.29"


