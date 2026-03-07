from faker import Faker
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from logger_dir.logger import Logger
from pages_dir.base_page import BasePage
from elements_dir.label import Label
from elements_dir.button import Button


class AlertPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    JS_ALERT_BUTTON_LOC = (By.XPATH, "//button[contains(@onclick, 'jsAlert()')]")
    JS_CONFIRM_BUTTON_LOC = (By.XPATH, "//button[contains(@onclick, 'jsConfirm()')]")
    JS_PROMPT_BUTTON_LOC = (By.XPATH, "//button[contains(@onclick, 'jsPrompt()')]")
    RESULT_AFTER_ACTION_LOC = (By.ID, "result")

    def __init__(self, browser):
        super().__init__(browser)

        self.name = "Alert page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.alert_button = Button(browser, self.JS_ALERT_BUTTON_LOC, "Button JS Alert")
        self.confirm_button = Button(browser, self.JS_CONFIRM_BUTTON_LOC, "Button JS Confirm")
        self.prompt_button = Button(browser, self.JS_PROMPT_BUTTON_LOC, "Button JS Prompt")
        self.result_after_alert = Label(browser, self.RESULT_AFTER_ACTION_LOC, "Result")

    def click_alert_button(self) -> None:
        self.alert_button.wait_for_clickable()
        Logger.info(f"{self.alert_button}: click")
        self.alert_button.click()

    def click_confirm_button(self) -> None:
        self.confirm_button.wait_for_clickable()
        Logger.info(f"{self.confirm_button}: click")
        self.confirm_button.click()

    def click_prompt_button(self) -> None:
        self.prompt_button.wait_for_clickable()
        Logger.info(f"{self.prompt_button}: click")
        self.prompt_button.click()

    def js_click_alert_button(self) -> None:
        element = self.alert_button.wait_for_presence()
        Logger.info(f"{self}: js click")
        self.browser.execute_script(
            "arguments[0].click();", element)

    def js_click_confirm_button(self) -> None:
        element = self.confirm_button.wait_for_presence()
        Logger.info(f"{self}: js click")
        self.browser.execute_script(
            "arguments[0].click();", element)

    def js_click_prompt_button(self) -> None:
        element = self.prompt_button.wait_for_presence()
        Logger.info(f"{self}: js click")
        self.browser.execute_script(
            "arguments[0].click();", element)

    def get_result_text(self):
        return self.result_after_alert.get_text()