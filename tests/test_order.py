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
    @pytest.mark.parametrize("first_name, last_name, address, metro_station, phone_number, date, rental_period, color_locator, comment,  order_button", DATA_FOR_ORDER)
    def test_order_success(self, driver_firefox, first_name, last_name, address, metro_station, phone_number, date, rental_period, color_locator, comment, order_button):
        main_page = MainPage(driver_firefox)
        order_page = OrderPage(driver_firefox)
        main_page.open()
        main_page.select_order_button(order_button)
        order_page.fill_first_page(first_name, last_name, address, metro_station, phone_number)
        order_page.click_next_button()
        order_page.wait_second_page()
        order_page.fill_second_page(date, rental_period, color_locator, comment)
        order_page.click_order_button()
        order_page.wait_order_confirmation()
        order_page.confirm_order()
        success_element = order_page.find_order_success_message_element()
        assert success_element.is_displayed(), "Элемент с сообщением об успешном заказе не отображается"