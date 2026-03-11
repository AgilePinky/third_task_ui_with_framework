from selenium.webdriver.common.by import By

from pages_dir.base_page import BasePage
from elements_dir.label import Label


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    FIRST_IMG_XPATH = "(//div[contains(@class, 'large-2')]//img)[{}]"

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")

    @staticmethod
    def get_img_element(xpath, index):
        return xpath.format(index)

    def search_img_match(self):
        img_list = [Label(self.browser,
                          self.get_img_element(self.FIRST_IMG_XPATH, i + 1),
                          f"Img {i + 1}") for i in range(3)]

        for _ in range(10):
            src_list = []
            for i in range(len(img_list)):
                src_list.append(img_list[i].get_attribute('src'))

            if len(set(src_list)) < len(src_list):
                return [len(set(src_list)), len(src_list)]
            else:
                self.browser.refresh_page()

        raise AssertionError("Didn't catch match after 10 attempts")
