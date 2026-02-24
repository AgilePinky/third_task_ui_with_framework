from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger_dir.logger import Logger
from pages_dir.base_page import BasePage
from elements_dir.label import Label

class LoginPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//p")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Login page"

        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT_LOC,
                                    description="text 'Congratulations'")
