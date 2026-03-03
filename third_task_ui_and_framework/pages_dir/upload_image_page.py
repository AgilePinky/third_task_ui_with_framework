from selenium.webdriver.common.by import By
import pyautogui
import time
import os

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

    def upload_image_dialog_window(self, browser, path):
        Logger.info(f"{self}: opened dialog window")
        time.sleep(1)

        prepared_path = r"{}".format(path)

        pyautogui.write(prepared_path)
        Logger.info(f"{self}: img loaded\nPath: {prepared_path}")
        pyautogui.press('enter')
        time.sleep(1)
