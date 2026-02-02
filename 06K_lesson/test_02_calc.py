from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def test_form():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    delay_field = driver.find_element(By.CSS_SELECTOR, '#delay')
    delay_field.clear()
    delay_field.send_keys("45")

    driver.find_element(By.XPATH, "//*[text()='7']").click()
    driver.find_element(By.XPATH, "//*[text()='+']").click()
    driver.find_element(By.XPATH, "//*[text()='8']").click()
    driver.find_element(By.XPATH, "//*[text()='=']").click()

    result = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15')
    )

    assert result

    driver.quit()
