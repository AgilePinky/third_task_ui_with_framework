import pytest
from browser_dir.browser_factory import BrowserFactory
from browser_dir.browser import Browser

@pytest.fixture(scope='function')
def browser():
    driver = BrowserFactory()
    browser = Browser(driver.get_driver())
    yield browser
    browser.quit()
