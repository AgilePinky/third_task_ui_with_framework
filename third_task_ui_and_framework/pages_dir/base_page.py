from selenium.webdriver.support.wait import WebDriverWait

from browser_dir.browser import Browser
from logger_dir.logger import Logger

class BasePage:
    UNIQUE_ELEMENT_LOC = None
    TIMEOUT = 10

    def __init__(self, browser: Browser):
        self.browser = browser
        
        self.page_name = None

        self.unique_element = None

        self.wait = WebDriverWait(browser.driver, self.TIMEOUT)

    def wait_for_open(self) -> None:
        Logger.info(f"{self}: wait for open")
        self.unique_element.wait_for_presence()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.page_name}]"

    def __repr__(self) -> str:
        return str(self)