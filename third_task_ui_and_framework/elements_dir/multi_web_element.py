from typing_extensions import Self
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

from browser_dir.browser import Browser
from elements_dir.web_element import WebElement
from logger_dir.logger import Logger

class MultiWebElement(WebElement):
    DEFAULT_TIMEOUT = 10

    def __init__(
            self,
            browser: Browser,
            formattable_xpath: str,
            description: str = None,
            timeout: int = None
    ) -> None:
        super().__init__(browser, formattable_xpath)
        self.index = 1

        self.browser = browser
        self.formattable_xpath = formattable_xpath
        self.timeout = timeout if timeout \
            else self.DEFAULT_TIMEOUT
        self.description = description if description \
            else self.formattable_xpath.format("'i'")

    def __iter__(self) -> Self:
        self.index = 1
        return self

    def __next__(self) -> WebElement:
        current_element = WebElement(
            self.browser,
            self.formattable_xpath.format(self.index),
            f"{self.description}[{self.index}]",
            timeout=self.timeout
            )

        if current_element.is_exist():
            self.index += 1
            return current_element
        else:
            raise StopIteration

    def _wait_for(self, EC) -> WebElement:
        try:
            Logger.info(f"{self}: wait for {EC.__name__}")
            element = self._wait.until(method=EC(self.locator))
            return element
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            raise

    def _wait_for_not(self, EC) -> None:
        try:
            Logger.info(f"{self}: wait for not {EC.__name__}")
            element = self._wait.until_not(method=EC(self.locator))
            return element
        except TimeoutException as err:
            Logger.error(f"{self}: {err}")
            raise

    def wait_for_presence(self) -> WebElement:
        return self._wait_for(EC=EC.presence_of_element_located)

    def wait_for_clickable(self) -> WebElement:
        return self._wait_for(EC=EC.element_to_be_clickable)

    def wait_for_visible(self) -> WebElement:
        return self._wait_for(EC=EC.visibility_of_element_located)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)