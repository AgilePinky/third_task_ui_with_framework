from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger_dir.logger import Logger
from pages_dir.base_page import BasePage
from elements_dir.label import Label
from elements_dir.button import Button


class AlertPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div[@id='content']//h3")
    JS_ALERT_BUTTON = (By.XPATH, "//button[contains(@onclick, 'jsAlert()')]")
    JS_CONFIRM_BUTTON = (By.XPATH, "//button[contains(@onclick, 'jsConfirm()')]")
    JS_PROMPT_BUTTON = (By.XPATH, "//button[contains(@onclick, 'jsPrompt()')]")
    RESULT_AFTER_ACTION = (By.ID, "result")

    def __init__(self, browser):
        super().__init__(browser)

        self.name = "Alert page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.js_alert_button = Button(browser, self.JS_ALERT_BUTTON, "Button JS Alert")
        self.js_confirm_button = Button(browser, self.JS_CONFIRM_BUTTON, "Button JS Confirm")
        self.js_prompt_button = Button(browser, self.JS_PROMPT_BUTTON, "Button JS Prompt")
        self.result_after_alert = Label(browser, self.RESULT_AFTER_ACTION, "Result")
