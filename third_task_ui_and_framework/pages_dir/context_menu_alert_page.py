from selenium.webdriver.common.by import By

from elements_dir.button import Button
from elements_dir.label import Label

from pages_dir.base_page import BasePage

class ContextMenuAlertPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    BOX_TO_RIGHT_CLICK_LOC = (By.ID, "hot-spot")

    def __init__(self, browser):
        super().__init__(browser)

        self.name = "Context Menu page"

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.box_to_right_click = Button(browser, self.BOX_TO_RIGHT_CLICK_LOC, "Right Click Box")

