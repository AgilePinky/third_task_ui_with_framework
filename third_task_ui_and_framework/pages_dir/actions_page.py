import time
from faker import Faker

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from logger_dir.logger import Logger


from pages_dir.base_page import BasePage
from elements_dir.label import Label
from elements_dir.input import Input

class ActionsPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    HORIZONTAL_SLIDER_LOC = (By.XPATH, "//input[contains(@type,'range')]")

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.horizontal_slider = Input(browser, self.HORIZONTAL_SLIDER_LOC, "Horizontal slider")


    def move_slider_with_arrows(self, target_value: float):
        slider = self.horizontal_slider.wait_for_clickable()
        step = float(slider.get_attribute('step'))

        slider.click()
        current_value = float(slider.get_attribute('value'))

        diff = target_value - current_value
        presses = int(diff / step)

        if presses > 0:
            key = Keys.ARROW_RIGHT
        elif presses < 0:
            key = Keys.ARROW_LEFT
        else:
            return current_value

        for i in range(abs(presses)):
            slider.send_keys(key)
            time.sleep(0.1)

        Logger.info(f"{self}: set slider value {self.horizontal_slider.get_attribute('value')}")
        return float(slider.get_attribute('value'))

    @staticmethod
    def get_random_position():
        fake = Faker()
        return fake.random_int(min=0, max=5) * 0.5