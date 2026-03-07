from typing_extensions import Self

from browser_dir.browser import Browser
from elements_dir.web_element import WebElement
from logger_dir.logger import Logger


class MultiWebElement:
    DEFAULT_TIMEOUT = 1

    def __init__(
            self,
            browser: Browser,
            formattable_xpath: str,
            description: str = None,
            timeout: int = None
    ) -> None:
        self.index = 1

        self.browser = browser
        self.formattable_xpath = formattable_xpath
        self.timeout = timeout if timeout is not None \
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

        raise StopIteration

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)

    def __len__(self):
        counter = sum(1 for _ in self)
        Logger.info(f"{self}: get len = {counter}")
        return counter

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError(f"Type of item not int: {type(item)}")

        xpath_index = item + 1

        return WebElement(
            self.browser,
            self.formattable_xpath.format(xpath_index),
            f"{self.description}[{xpath_index}]",
            timeout=1)

    def get_all(self):
        return [self[i] for i in range(len(self))]