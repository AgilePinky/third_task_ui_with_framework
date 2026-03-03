import time

from selenium.webdriver.common.by import By

from config_dir.config_reader import ConfigReader
from pages_dir.base_page import BasePage
from elements_dir.label import Label
from logger_dir.logger import Logger


class InfinityScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    PARAGRAPH_LOC = (By.XPATH, "//div[contains(@class, 'jscroll-added')]")

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.paragraph_list = Label(browser, self.PARAGRAPH_LOC, "Paragraph list")


    def scroll_n_times_in_container(self, n, browser):
        config = ConfigReader()
        elements = browser.find_elements(self.PARAGRAPH_LOC)

        while len(elements) < int(n):
            last_element = elements[-1]
            if len(elements) >= int(n):
                continue
            else:
                if last_element.text == 'Loading...':
                    self.wait.until(lambda browser: last_element.text != 'Loading...')
                else:
                    Logger.info(f"{self}: Founded lust element. Text: {last_element.text[:30]}")
                    browser.execute_script(config.get_scroll_script(), last_element)

                    self.wait.until(lambda browser:
                                    len(browser.find_elements(*self.PARAGRAPH_LOC)) > len(elements))

                    elements = browser.find_elements(self.PARAGRAPH_LOC)

        Logger.info(f"Length of elements list {len(elements)}")
        return len(elements)
