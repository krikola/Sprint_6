from selenium.webdriver.common.by import By

class OrderPageLocators:
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    FIRST_NAME = (By.XPATH, "//input[contains(@placeholder, '* Имя')]")
    LAST_NAME = (By.XPATH, "//input[contains(@placeholder, '* Фамилия')]")
    ADDRESS = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    METRO_STATION = (By.XPATH, "//input[contains(@placeholder, 'Станция метро')]")
    PHONE_NUMBER = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    DATE_PICKER = (By.XPATH, "//input[contains(@placeholder, 'Когда привезти')]")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(text(), 'Срок аренды')]/..")
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    COMMENT_FOR_COURIER = (By.XPATH, "//input[contains(@placeholder, 'Комментарий для курьера')]")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[text()='Заказать']")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")