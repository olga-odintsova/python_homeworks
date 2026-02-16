import pytest
from pages.CalcPage import CalcPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_submission_flow(driver):
    page = CalcPage(driver)
    page.open()
    page.fill_delay()
    page.fill_form()
    page.check_result()

