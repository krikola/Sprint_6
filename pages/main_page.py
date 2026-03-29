from selenium import webdriver
from pages.base_page import BasePage
from locators.base_locators import BasePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_locators import MainPageLocators
from data.urls import URL
import allure

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открытие главной страницы")
    def open(self):
        self.driver.get(URL)

    @allure.step("Клик по верхней кнопке 'Заказать'")
    def click_upper_order_button(self):
        self.click_element(MainPageLocators.UPPER_ORDER_BUTTON)

    @allure.step("Клик по нижней кнопке 'Заказать'")
    def click_lower_order_button(self):
        lower_order_button = self.find_element(MainPageLocators.LOWER_ORDER_BUTTON)
        self.js_scroll_into_view(lower_order_button)
        self.js_click(lower_order_button)

    @allure.step("Кликаем на вопрос FAQ с индексом {index}")
    def click_faq_question(self, index):
        question_locator = MainPageLocators.faq_question_locator(index)
        question = self.wait_for_element_visible(question_locator, timeout=20)
        self.js_scroll_into_view(question)
        self.js_click(question)

    @allure.step("Получаем текст ответа на вопрос FAQ с индексом {index}")
    def get_faq_answer_text(self, index):
        answer_locator = MainPageLocators.faq_answer_locator(index)
        answer = self.wait_for_element_visible(answer_locator, timeout=10)
        return answer.text

    @allure.step("Клик по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_element(BasePageLocators.YANDEX_LOGO)

    @allure.step("Клик по логотипу Самоката")
    def click_samokat_logo(self):
        self.click_element(BasePageLocators.SAMOKAT_LOGO)

    @allure.step("Переключение на новое окно")
    def switch_to_new_window(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[-1])

    @allure.step("Ожидаем загрузки страницы Дзена")
    def wait_dzen_loaded(self):
        self.wait_for_url_contains("dzen.ru")

    @allure.step("Ожидаем загрузки главной страницы")
    def wait_main_page_loaded(self):
        self.wait_for_url_to_be(URL)

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Выбираем кнопку для оформления заказа — {button_type}")
    def select_order_button(self, button_type):
        button_actions = {
            "lower": self.click_lower_order_button,
            "upper": self.click_upper_order_button
        }
        button_actions.get(button_type)()
        