from typing_extensions import Self

from browser_dir.browser import Browser
from elements_dir.web_element import WebElement
from logger_dir.logger import Logger


class MultiWebElement:
    DEFAULT_TIMEOUT = 4

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
        description = f"{self.description}[{self.index}]"
        current_element = self._get_element(self.index, description)

        if current_element.is_exist(self.timeout if self.index == 1 else 0):
            self.index += 1
            return current_element

        raise StopIteration

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)

    def __len__(self):
        elements = self.get_all()
        result = len(elements)
        Logger.info(f"{self}: get len = {result}")
        return result

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError(f"Type of item not int: {type(item)}")

        xpath_index = item + 1

        description = f"{self.description}[{xpath_index}]"
        return self._get_element(xpath_index, description)

    def get_all(self):
        return [element for element in self]

    def _get_element(self, index, description):
        return WebElement(
            self.browser,
            self.formattable_xpath.format(index),
            description,
            timeout=self.timeout
        )
