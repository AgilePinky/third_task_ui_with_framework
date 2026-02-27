from selenium.webdriver.common.by import By

from pages_dir.base_page import BasePage
from elements_dir.label import Label

class ProfilePage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//h1")

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")
