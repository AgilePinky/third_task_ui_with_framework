import time

import pytest
from faker import Faker

from config_dir.config_reader import ConfigReader
from pages_dir.login_page import LoginPage
from pages_dir.alert_page import AlertPage
from pages_dir.context_menu_alert_page import ContextMenuAlertPage
from pages_dir.actions_page import ActionsPage


def test_basic_authorization(browser):
    # 1
    print()
    config = ConfigReader()
    username = config.get_username_basic_authorization()
    password = config.get_password_basic_authorization()
    url = config.get_url_basic_authorization()
    auth_url = f"https://{username}:{password}@{url}"
    browser.get(auth_url)

    # 2
    login_page = LoginPage(browser)
    login_page.wait_for_open()
    assert login_page.unique_element.get_text() == config.get_expected_basic_authorization_alert


def test_alert(browser):
    # 1
    config = ConfigReader()
    browser.get(config.get_test_alert())

    alert_page = AlertPage(browser)
    alert_page.wait_for_open()

    # 2
    alert_page.js_alert_button.click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_expected_js_alert_text()
    browser.accept_alert()

    # 3
    expected_text = config.get_expected_js_alert_result_text()
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text

    # 4
    alert_page.js_confirm_button.click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_expected_js_confirm_text()
    browser.accept_alert()

    # 5
    expected_text = config.get_expected_js_confirm_result_text()
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text

    # 6
    alert_page.js_prompt_button.click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_expected_js_prompt_text()

    # 7
    fake = Faker()
    random_text = fake.name()
    browser.send_keys_alert(random_text)
    browser.accept_alert()

    expected_text = config.get_expected_js_prompt_result_text() + random_text
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text

def test_alert_js(browser):
    # 1
    print()
    config = ConfigReader()
    browser.get(config.get_test_alert_js_url())

    alert_page = AlertPage(browser)
    alert_page.wait_for_open()

    # 2
    alert_page.js_alert_button.js_click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_expected_js_alert_text()
    browser.accept_alert()

    # 3
    expected_text = config.get_expected_js_alert_result_text()
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text

    # 4
    alert_page.js_confirm_button.js_click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_expected_js_confirm_text()
    browser.accept_alert()

    # 5
    expected_text = config.get_expected_js_confirm_result_text()
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text

    # 6
    alert_page.js_prompt_button.js_click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_expected_js_prompt_text()

    # 7
    fake = Faker()
    random_text = fake.name()
    browser.send_keys_alert(random_text)
    browser.accept_alert()

    expected_text = config.get_expected_js_prompt_result_text() + random_text
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text

def test_alert_context_click(browser):
    # 1
    print()
    config = ConfigReader()
    browser.get(config.get_test_alert_context_click_url())
    context_menu_alert_page = ContextMenuAlertPage(browser)
    context_menu_alert_page.wait_for_open()

    # 2
    context_menu_alert_page.box_to_right_click.wait_for_clickable()
    browser.right_click(context_menu_alert_page.box_to_right_click.wait_for_presence())
    browser.wait_alert_present()
    browser.get_alert_text()

    expected_text = config.get_expected_alert_context_click_text()
    actual_text = browser.get_alert_text()
    assert actual_text == expected_text

    # 3
    browser.accept_alert()

def test_actions(browser):
    # 1
    print()
    config = ConfigReader()
    browser.get(config.get_url_actions())
    actions_page = ActionsPage(browser)
    actions_page.wait_for_open()

    # 2
    fake = Faker()
    random_position = fake.random_int(min=0, max=5) * 0.5
    actions_page.move_slider_with_arrows(random_position)




