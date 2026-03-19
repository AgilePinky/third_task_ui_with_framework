import pyautogui
import time
from logger_dir.logger import Logger

class PyAutoGuiUtils:

    @staticmethod
    def upload_image_dialog_window(page, path):
        Logger.info(f"{page}: opened dialog window")
        time.sleep(1)

        prepared_path = str(path)

        pyautogui.write(prepared_path)
        Logger.info(f"{page}: img loaded\nPath: {prepared_path}")
        pyautogui.press('enter')
        time.sleep(1)