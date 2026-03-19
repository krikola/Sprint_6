from locators.base_locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data.urls import URL
import allure

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Поиск элемента по локатору")
    def find_element(self, locator):
        return self.driver.find_element(*locator)
    
    @allure.step("Клик по элементу")
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step("Ожидаем, что URL содержит:: {url_part}")
    def wait_for_url_contains(self, url_part, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.url_contains(url_part))
    
    @allure.step("Ожидаем, что URL равен: {url}")
    def wait_for_url_to_be(self, url, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.url_to_be(url))
    
    @allure.step("Прокручиваем элемент в видимую область с помощью скрипта js")
    def js_scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликаем по элементу с помощью скрипта js")
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидаем видимости элемента")
    def wait_for_element_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
    
    @allure.step("Заполняем поле ввода текстом: {text}")
    def fill_input(self, locator, text):
        input_field = self.find_element(locator)
        input_field.clear()
        input_field.send_keys(text)

    @allure.step("Кликаем по элементу, когда он станет кликабельным")
    def click_when_clickable(self, locator, timeout=20):
        element = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ожидаем кликабельности элемента")
    def wait_for_element_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
    
    @allure.step("Отправляем клавиши в элемент")
    def send_keys(self, locator, keys):
        element = self.find_element(locator)
        element.send_keys(keys)

    @allure.step("Переключаемся на новое окно браузера")
    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Получаем текущий URL страницы")
    def get_url(self):
        return self.driver.current_url
