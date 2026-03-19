import pytest
from selenium import webdriver
import allure

@pytest.fixture(scope="function")
def driver_firefox():
    with allure.step("Открываем браузер Firefox"):
        driver = webdriver.Firefox()
    yield driver
    with allure.step("Закрываем браузер"):
        driver.quit()