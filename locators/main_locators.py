from selenium.webdriver.common.by import By

class MainPageLocators:
    UPPER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")
    LOWER_ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button[text()='Заказать']")

    @staticmethod
    def faq_question_locator(index):
        return (By.ID, f"accordion__heading-{index}")
    
    @staticmethod
    def faq_answer_locator(index):
        return (By.ID, f"accordion__panel-{index}")