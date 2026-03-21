from pages.main_page import MainPage
from selenium import webdriver
from data.parametrize import FAQ_ANSWERS
from data.urls import URL
import pytest
import allure

class TestMainPage:

    @allure.feature("FAQ")
    @allure.title("Проверка всех ответов")
    @pytest.mark.parametrize("index, expected_answer", FAQ_ANSWERS)
    def test_faq_answer(self, driver_firefox, index, expected_answer):
        main_page = MainPage(driver_firefox)
        main_page.open()
        main_page.click_faq_question(index)
        answer_text = main_page.get_faq_answer_text(index)
        assert answer_text == expected_answer, f"Ожидаемый ответ: {expected_answer}, полученный ответ: {answer_text}"

    @allure.feature("Логотипы")
    @allure.title("Проверка клика по Яндекс логотипу")
    def test_yandex_logo_click_success(self, driver_firefox):
        main_page = MainPage(driver_firefox)
        main_page.open()
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()
        main_page.wait_dzen_loaded()
        assert "dzen.ru" in main_page.get_current_url(), f"Ожидали 'dzen.ru' в URL, получили {main_page.get_current_url()}"

    @allure.feature("Логотипы")
    @allure.title("Проверка клика по логотипу Самоката")
    def test_samokat_logo_click_success(self, driver_firefox):
        main_page = MainPage(driver_firefox)
        main_page.open()
        main_page.click_lower_order_button()
        main_page.click_samokat_logo()
        main_page.wait_main_page_loaded()
        assert main_page.get_current_url() == URL, f"Ожидали URL '{URL}', получили {main_page.get_current_url()}"

    @allure.feature("Заказ")
    @allure.title("Проверка верхней кнопки 'Заказать'")
    def test_upper_order_button_click_success(self, driver_firefox):
        main_page = MainPage(driver_firefox)
        main_page.open()
        main_page.click_upper_order_button()
        assert "/order" in main_page.get_current_url(), f"Ожидали URL с '/order', получили {main_page.get_current_url()}"

    @allure.feature("Заказ")
    @allure.title("Проверка нижней кнопки 'Заказать'")
    def test_lower_order_button_click_success(self, driver_firefox):
        main_page = MainPage(driver_firefox)
        main_page.open()
        main_page.click_lower_order_button()
        assert "/order" in main_page.get_current_url(), f"Ожидали URL с '/order', получили {main_page.get_current_url()}"
