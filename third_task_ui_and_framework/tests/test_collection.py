import time
import pytest
from faker import Faker

from pages_dir.login_page import LoginPage
from pages_dir.alert_page import AlertPage
from config_dir.config_reader import ConfigReader


def test_basic_authorization(browser):
    print()
    config = ConfigReader()
    username = config.get_username_basic_authorization()
    password = config.get_password_basic_authorization()
    url = config.get_url_basic_authorization()
    auth_url = f"https://{username}:{password}@{url}"

    browser.get(auth_url)
    login_page = LoginPage(browser)
    login_page.wait_for_open()

    assert login_page.unique_element.get_text() == config.get_expected_basic_authorization_alert


def test_alert(browser):
    url  = "https://the-internet.herokuapp.com/javascript_alerts"
    browser.get(url)
    config = ConfigReader()

    alert_page = AlertPage(browser)
    alert_page.wait_for_open()

    alert_page.js_alert_button.js_click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_expected_js_alert_text()
    browser.accept_alert()

    expected_text = config.get_expected_js_alert_result_text()
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text

    alert_page.js_confirm_button.js_click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_expected_js_confirm_text()
    browser.accept_alert()

    expected_text = config.get_expected_js_confirm_result_text()
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text

    alert_page.js_prompt_button.js_click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_expected_js_prompt_text()

    fake = Faker()
    random_text = fake.name()
    browser.send_keys_alert(random_text)
    browser.accept_alert()

    expected_text = config.get_expected_js_prompt_result_text() + random_text
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text



