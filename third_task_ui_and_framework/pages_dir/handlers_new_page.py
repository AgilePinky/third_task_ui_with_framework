from selenium.webdriver.common.by import By

from pages_dir.base_page import BasePage
from elements_dir.label import Label

class HandlersNewPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[contains(@class, 'example')]//h3")

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.header = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")

    def get_header_text(self):
        return self.header.get_text()
