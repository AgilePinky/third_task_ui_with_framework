import pyautogui
import time
from logger_dir.logger import Logger

class PyAutoGuiUtils:

    def __init__(self):
        pass

    def upload_image_dialog_window(self, path):
        Logger.info(f"{self}: opened dialog window")
        time.sleep(1)

        prepared_path = r"{}".format(path)

        pyautogui.write(prepared_path)
        Logger.info(f"{self}: img loaded\nPath: {prepared_path}")
        pyautogui.press('enter')
        time.sleep(1)