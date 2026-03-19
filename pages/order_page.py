from locators.order_locators import OrderPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.common.keys import Keys
import allure
from pages.base_page import BasePage
from locators.base_locators import BasePageLocators

class OrderPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по кнопке 'Далее'")
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполняем имя: {first_name}")
    def fill_first_name(self, first_name):
        self.fill_input(OrderPageLocators.FIRST_NAME, first_name)

    @allure.step("Заполняем фамилию: {last_name}")
    def fill_last_name(self, last_name):
        self.fill_input(OrderPageLocators.LAST_NAME, last_name)

    @allure.step("Заполняем адрес: {address}")
    def fill_address(self, address):
        self.fill_input(OrderPageLocators.ADDRESS, address)

    @allure.step("Заполняем станцию метро: {metro_station}")
    def fill_metro_station(self, metro_station):
        self.fill_input(OrderPageLocators.METRO_STATION, metro_station)
        metro_option = (By.XPATH, f"//div[text()='{metro_station}']")
        self.click_when_clickable(metro_option)

    @allure.step("Заполняем номер телефона: {phone_number}")
    def fill_phone_number(self, phone_number):
        self.fill_input(OrderPageLocators.PHONE_NUMBER, phone_number)

    @allure.step("Ожидаем загрузки второй страницы заказа")
    def wait_second_page(self):
        self.wait_for_element_clickable(OrderPageLocators.DATE_PICKER)

    @allure.step("Заполняем дату доставки: {date}")
    def fill_date(self, date):
        self.fill_input(OrderPageLocators.DATE_PICKER, date)
        self.send_keys(OrderPageLocators.DATE_PICKER, Keys.ENTER)
        

    @allure.step("Выбираем период аренды: {period}")
    def select_rental_period(self, period):
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        period_option = (By.XPATH, f"//div[text()='{period}']")
        self.click_when_clickable(period_option)

    @allure.step("Выбираем цвет самоката: {color}")
    def select_color(self, color):
        if color == "black":
            self.click_element(OrderPageLocators.BLACK_COLOR_CHECKBOX)
        elif color == "grey":
            self.click_element(OrderPageLocators.GREY_COLOR_CHECKBOX)
        else:
            raise ValueError(f"Unknown color: {color}")
        
    @allure.step("Клик по кнопке 'Заказать'")
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Ожидаем появления окна подтверждения заказа")
    def wait_order_confirmation(self):
        self.wait_for_element_clickable(OrderPageLocators.YES_BUTTON)

    @allure.step("Кликаем на кнопку 'Да' в окне подтверждения заказа")
    def confirm_order(self):
        self.click_element(OrderPageLocators.YES_BUTTON)

    @allure.step("Ожидаем появления сообщения об успешном оформлении заказа")
    def wait_order_success_message(self):
        message = self.wait_for_element_visible(OrderPageLocators.ORDER_SUCCESS_MESSAGE)
        return message.text
    
    @allure.step("Заполняем первую страницу заказа")
    def fill_first_page(self, first_name, last_name, address, metro_station, phone_number):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_address(address)
        self.fill_metro_station(metro_station)
        self.fill_phone_number(phone_number)

    @allure.step("Заполняем вторую страницу заказа")
    def fill_second_page(self, date, rental_period, color):
        self.fill_date(date)
        self.select_rental_period(rental_period)
        self.select_color(color)