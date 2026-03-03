from selenium.webdriver.common.by import By

from pages_dir.base_page import BasePage
from elements_dir.label import Label
from elements_dir.button import Button

class HandlersMainPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    NEW_TAB_MAKER_LOC = (By.XPATH, "//div[@class='example']//a")

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.new_tab_maker = Button(browser, self.NEW_TAB_MAKER_LOC, "'Click Here'")
