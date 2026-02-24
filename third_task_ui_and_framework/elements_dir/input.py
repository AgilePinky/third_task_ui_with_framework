from selenium.common import WebDriverException

from logger_dir.logger import Logger
from elements_dir.base_element import BaseElement


class Input(BaseElement):

    def clear(self) -> None:
        element = self.wait_for_visible()
        Logger.info(f"{self}: clear")
        try:
            element.clear()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def js_clear(self) -> None:
        element = self.wait_for_presence()
        Logger.info(f"{self}: js_clear")
        self.browser.execute_script("arguments[0].value = ''", element)

    def send_keys(self, keys: str, clear: bool= True) -> None:
        if clear:
            self.clear()

        element = self.wait_for_visible()
        Logger.info(f"{self}: send_keys = '{keys}'")
        try:
            element.send_keys(keys)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def js_send_keys(self, keys: str, clear: bool= True) -> None:
        if clear:
            self.js_clear()

        element = self.wait_for_visible()
        Logger.info(f"{self}: send_keys = '{keys}'")
        self.browser.execute_script("arguments[0].value = ''", element, keys)


