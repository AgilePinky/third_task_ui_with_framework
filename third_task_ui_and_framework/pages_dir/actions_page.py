from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from logger_dir.logger import Logger


from pages_dir.base_page import BasePage
from elements_dir.label import Label
from elements_dir.input import Input

class ActionsPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//div[@id='content']//h3")
    HORIZONTAL_SLIDER_LOC = (By.XPATH, "//input[contains(@type,'range')]")

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.horizontal_slider = Input(browser, self.HORIZONTAL_SLIDER_LOC, "Horizontal slider")

    def move_slider_with_arrows(self, target_value: float):
        slider = self.horizontal_slider.wait_for_clickable()

        min_value = float(slider.get_attribute('min'))
        max_value = float(slider.get_attribute('max'))
        slider_width = slider.size['width']

        value_range = max_value - min_value
        target_value = - (max_value / 2 - target_value)
        target_percentage = (target_value - min_value) / value_range
        x_offset = int(slider_width * target_percentage)

        ActionChains(self.browser.driver)\
            .click_and_hold(slider)\
            .move_by_offset(x_offset,0)\
            .release()\
            .perform()

        Logger.info(f"{self}: set slider value {self.horizontal_slider.get_attribute('value')}")
        return self.horizontal_slider.get_attribute('value')