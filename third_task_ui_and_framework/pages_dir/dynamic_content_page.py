from selenium.webdriver.common.by import By

from pages_dir.base_page import BasePage
from elements_dir.label import Label

class  DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    FIRST_IMG_LOC = (By.XPATH, "(//div[contains(@class, 'large-2')]//img)[1]")
    SECOND_IMG_LOC = (By.XPATH, "(//div[contains(@class, 'large-2')]//img)[2]")
    THIRD_IMG_LOC = (By.XPATH, "(//div[contains(@class, 'large-2')]//img)[3]")

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.first_img = Label(browser, self.FIRST_IMG_LOC, "First img")
        self.second_img = Label(browser, self.SECOND_IMG_LOC, "Second img")
        self.third_img = Label(browser, self.THIRD_IMG_LOC, "Third img")

    def search_img_match(self, browser):
        try:
            for _ in range(10):
                first_img = self.first_img.get_attribute('src')
                second_img = self.second_img.get_attribute('src')
                third_img = self.third_img.get_attribute('src')
                if first_img == second_img:
                    return [first_img, second_img]
                elif second_img == third_img:
                    return [second_img, third_img]
                elif third_img == first_img:
                    return [third_img, first_img]
                else:
                    browser.refresh_page()
        except:
            raise AssertionError("Didn't catch match after 10 attempts")