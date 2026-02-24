from enum import StrEnum

from selenium import webdriver

from logger_dir.logger import Logger
from selenium.webdriver.remote.webdriver import WebDriver

class AvailableDriverName(StrEnum):
    CHROME = "chrome"

class BrowserFactory:
        @staticmethod
        def get_driver(
                driver_name: AvailableDriverName = AvailableDriverName.CHROME,
                options: list[str] = None
        ) -> WebDriver:
            if options is None:
                options = []

            print()
            Logger.info(f"Start webdriver '{driver_name}' with options '{options}'")
            if driver_name == AvailableDriverName.CHROME:
                chrome_options = webdriver.ChromeOptions()

                for option in options:
                    chrome_options.add_argument(option)

                driver = webdriver.Chrome(options=chrome_options)
            else:
                raise NotImplementedError(f"{driver_name} not implemented.")
            return driver