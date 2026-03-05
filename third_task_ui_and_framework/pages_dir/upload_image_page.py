from selenium.webdriver.common.by import By
import pyautogui
import time
from pathlib import Path

from config_dir.config_reader import ConfigReader
from pages_dir.base_page import BasePage
from elements_dir.label import Label
from elements_dir.input import Input
from elements_dir.button import Button
from logger_dir.logger import Logger


class UploadImagePage(BasePage):
    UNIQUE_ELEMENT_LOC = (By.XPATH, "//*[@id='content']//h3")
    INPUT_FILE_LOC = (By.ID, "file-upload")
    INPUT_FILE_SUBMIT_LOC = (By.ID, "file-submit")
    INPUT_DIALOG_WINDOW_BOX_LOC = (By.ID, "drag-drop-upload")
    DIALOG_WINDOW_UPLOAD_SUCCESS_MARKER_LOC = \
        (By.XPATH, "//*[@id='drag-drop-upload']//div[contains(@class, 'dz-success-mark')]//span")

    def __init__(self, browser):
        super().__init__(browser)

        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, "Header")
        self.input_file_element = Input(browser, self.INPUT_FILE_LOC, "Input file")
        self.input_file_submit_element = Button(browser,
                                                self.INPUT_FILE_SUBMIT_LOC,
                                                "Input file submit")
        self.input_dialog_window_box = Button(browser, self.INPUT_DIALOG_WINDOW_BOX_LOC,
                                              "Input dialog window box")
        self.dialog_window_upload_success_marker_element = \
            Label(browser, self.DIALOG_WINDOW_UPLOAD_SUCCESS_MARKER_LOC, "Success marker")


    @staticmethod
    def get_upload_image_page_file_path():
        config = ConfigReader()
        parent_dir = Path(config.script_dir).parent
        target_file = parent_dir / 'source' / config.config["test_upload_image_file_path"]
        return str(target_file)

    def send_keys_input_file_element(self):
        self.input_file_element.send_keys(self.get_upload_image_page_file_path())


    def click_input_file_submit_element(self):
        self.input_file_submit_element.wait_for_clickable()
        self.input_file_submit_element.click()

    def get_unique_element_text(self):
        return self.unique_element.get_text()

    def click_input_dialog_window_box(self):
        self.input_dialog_window_box.wait_for_clickable()
        self.input_dialog_window_box.click()