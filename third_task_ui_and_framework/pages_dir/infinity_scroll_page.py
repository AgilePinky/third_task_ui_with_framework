from selenium.webdriver.common.by import By

from config_dir.config_reader import ConfigReader
from pages_dir.base_page import BasePage
from elements_dir.label import Label
from elements_dir.multi_web_element import MultiWebElement
from logger_dir.logger import Logger


class InfinityScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    PARAGRAPH_LOC = "(//div[contains(@class, 'jscroll-added')])[{}]"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.paragraph_list = MultiWebElement(browser, self.PARAGRAPH_LOC, "Paragraph list")


    def scroll_n_times_in_container(self, n, browser):
        config = ConfigReader()

        elements = self.paragraph_list.get_all()
        while len(elements) < int(n):
            current_len = len(elements)
            last_element = elements[-1]

            if last_element.get_text() == 'Loading...':
                Logger.info(f"if {last_element.get_text()} == 'Loading...'")
                self.wait.until(lambda browser: last_element.get_text() != 'Loading...')
            else:
                Logger.info(f"{self}: Founded lust element. Text: {last_element.get_text()}")
                browser.execute_script("arguments[0].scrollIntoView({block: 'end', behavior: 'auto'});",
                                       last_element.wait_for_visible())

                old_count = len(elements)
                self.wait.until(lambda browser: len(self.paragraph_list.get_all()) > old_count)
                elements = self.paragraph_list.get_all()

        Logger.info(f"Length of elements list {len(elements)}")
        return len(elements)
