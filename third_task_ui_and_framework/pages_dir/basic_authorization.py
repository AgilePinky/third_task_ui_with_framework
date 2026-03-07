from selenium.webdriver.common.by import By
from pages_dir.base_page import BasePage
from elements_dir.label import Label

class BasicAuthorization(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//p")

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Basic Authorization page"

        self.unique_element = Label(self.browser, self.UNIQUE_ELEMENT_LOC,
                                    description="text 'Congratulations'")
        self.congratulations = Label(self.browser, self.UNIQUE_ELEMENT_LOC,
                                   description="text 'Congratulations'")

    def get_result_text(self):
        return self.congratulations.get_text()