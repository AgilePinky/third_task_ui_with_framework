import time

from selenium.webdriver.common.by import By

from pages_dir.base_page import BasePage
from elements_dir.label import Label
from elements_dir.button import Button
from elements_dir.web_element import WebElement


class IframePage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//header//img")
    ALERTS_FRAME_WINDOWS_LOC = (
    By.XPATH, "(//div[contains(@class, 'element-group')])[3]//span[contains(@class,'group-header')]")
    NESTED_FRAMES_LOC = (By.XPATH, "(//div[contains(@class, 'element-group')])[3]//*[contains(@id,'item-3')]//span")
    NESTED_FRAMES_PARENT_FRAME_LOC = (By.ID, "frame1")
    NESTED_FRAMES_PARENT_FRAME_TEXT_LOC = (By.XPATH, "//body")
    NESTED_FRAMES_CHILD_FRAME_LOC = (By.XPATH, "//iframe[@srcdoc='<p>Child Iframe</p>']")
    NESTED_FRAMES_CHILD_FRAME_TEXT_LOC = (By.XPATH, "//body//p")
    FRAMES_LOC = (By.XPATH, "(//div[contains(@class, 'element-group')])[3]//*[contains(@id,'item-2')]//span")
    FRAMES_FIRST_FRAME_LOC = (By.ID, "frame1")
    FRAMES_SECOND_FRAME_LOC = (By.ID, "frame2")
    FRAMES_TEXT_LOC = (By.ID, "sampleHeading")

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header Logo")
        self.alerts_frame_windows_button = Button(browser,
                                                  self.ALERTS_FRAME_WINDOWS_LOC,
                                                  "Alerts frame windows button")
        self.nested_frames_button = Button(browser,
                                           self.NESTED_FRAMES_LOC,
                                           "Nested frames button")
        self.nested_frames_parent_frame_element = WebElement(browser,
                                                             self.NESTED_FRAMES_PARENT_FRAME_LOC,
                                                             "IFrame Parent")
        self.nested_frames_parent_frame_text = Label(browser,
                                                     self.NESTED_FRAMES_PARENT_FRAME_TEXT_LOC,
                                                     "IFrame Parent text")
        self.nested_frames_child_frame_element = WebElement(browser,
                                                            self.NESTED_FRAMES_CHILD_FRAME_LOC,
                                                            "IFrame Child")
        self.nested_frames_child_frame_text = Label(browser,
                                                    self.NESTED_FRAMES_CHILD_FRAME_TEXT_LOC,
                                                    "IFrame Child text")

        self.frames_button = Button(browser,
                                    self.FRAMES_LOC,
                                    "Frames button")
        self.frames_first_frame_element = WebElement(browser,
                                                     self.FRAMES_FIRST_FRAME_LOC,
                                                     "IFrame first")
        self.frames_second_frame_element = WebElement(browser,
                                                      self.FRAMES_SECOND_FRAME_LOC,
                                                      "IFrame second")
        self.frames_frame_text = Label(browser,
                                       self.FRAMES_TEXT_LOC,
                                       "IFrame text")

    def click_alerts_frame_windows_button(self):
        self.alerts_frame_windows_button.click()

    def click_nested_frames_button(self):
        self.nested_frames_button.click()

    def switch_to_nested_frames_parent_frame(self):
        self.browser.switch_to_frame(self.nested_frames_parent_frame_element)

    def get_nested_frames_parent_frame_text(self):
        self.switch_to_nested_frames_parent_frame()
        self.nested_frames_parent_frame_text.wait_for_visible()
        text = self.nested_frames_parent_frame_text.get_text()
        self.switch_to_default_frame()
        return text

    def switch_to_nested_frames_child_frame(self):
        self.browser.switch_to_frame(self.nested_frames_child_frame_element)

    def get_nested_frames_child_frame_text(self):
        self.switch_to_nested_frames_parent_frame()
        self.switch_to_nested_frames_child_frame()
        self.nested_frames_child_frame_text.wait_for_visible()
        text = self.nested_frames_child_frame_text.get_text()
        self.switch_to_default_frame()
        return text

    def switch_to_default_frame(self):
        self.browser.switch_to_default_frame()

    def click_frames_button(self):
        self.frames_button.click()

    def switch_to_frames_first_frame(self):
        self.browser.switch_to_frame(self.frames_first_frame_element)

    def get_frames_frame_text(self):
        return self.frames_frame_text.get_text()

    def switch_to_parent_frame(self):
        self.browser.switch_to_parent_frame()

    def switch_frames_second_frame_element(self):
        self.browser.switch_to_frame(self.frames_second_frame_element)
