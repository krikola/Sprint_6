from selenium.webdriver.common.by import By

class BasePageLocators:
    YANDEX_LOGO = (By.CSS_SELECTOR, "a[href*='yandex']")
    SAMOKAT_LOGO = (By.CSS_SELECTOR, "a[href='/']")