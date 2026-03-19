from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium import webdriver
from data.urls import URL
from data.parametrize import DATA_FOR_ORDER
import pytest
import allure

class TestOrderPage:

  

    @allure.feature("Оформление заказа")
    @allure.title("Проверка успешного оформления заказа с различными данными") 
    @pytest.mark.parametrize("first_name, last_name, address, metro_station, phone_number, date, rental_period, color, order_button", DATA_FOR_ORDER)
    def test_order_success(self, driver_firefox, first_name, last_name, address, metro_station, phone_number, date, rental_period, color, order_button):
        self.driver = driver_firefox
        self.driver.get(URL)
        main_page = MainPage(self.driver)
        main_page.select_order_button(order_button)
        order_page = OrderPage(self.driver)
        order_page.fill_first_page(first_name, last_name, address, metro_station, phone_number)
        order_page.click_next_button()
        order_page.wait_second_page()
        order_page.fill_second_page(date, rental_period, color)
        order_page.click_order_button()
        order_page.wait_order_confirmation()
        order_page.confirm_order()
        success_message = order_page.wait_order_success_message()
        assert "Заказ оформлен" in success_message, f"Ожидали сообщение 'Заказ оформлен', получили {success_message}"