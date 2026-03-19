from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from elements_dir.button import Button
from elements_dir.label import Label
from pages_dir.base_page import BasePage
from logger_dir.logger import Logger

class AlertContextPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    BOX_TO_RIGHT_CLICK_LOC = (By.ID, "hot-spot")

    def __init__(self, browser):
        super().__init__(browser)

        self.name = "Context Menu page"

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.box_to_right_click = Button(browser, self.BOX_TO_RIGHT_CLICK_LOC, "Right Click Box")

    def right_click_on_box(self):
        Logger.info(f"{self}: right click at {self.box_to_right_click}")
        ActionChains(self.browser.driver).context_click(
            self.box_to_right_click.wait_for_clickable()).perform()
