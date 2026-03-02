import time

import pytest
from faker import Faker
import os

from config_dir.config_reader import ConfigReader
from pages_dir.login_page import LoginPage
from pages_dir.alert_page import AlertPage
from pages_dir.context_menu_alert_page import ContextMenuAlertPage
from pages_dir.actions_page import ActionsPage
from pages_dir.hovers_page import HoverPage
from pages_dir.profile_page import ProfilePage
from pages_dir.handlers_main_page import HandlersMainPage
from pages_dir.handlers_new_page import HandlersNewPage
from pages_dir.iframes_page import IframePage
from pages_dir.dynamic_content_page import DynamicContentPage
from pages_dir.infinity_scroll_page import InfinityScrollPage
from pages_dir.upload_image_page import UploadImagePage


# 1
def test_basic_authorization(browser):
    # 1
    print()
    config = ConfigReader()
    username = config.get_basic_authorization_username()
    password = config.get_basic_authorization_password()
    url = config.get_basic_authorization_url()
    auth_url = f"https://{username}:{password}@{url}"
    browser.get(auth_url)

    # 2
    login_page = LoginPage(browser)
    login_page.wait_for_open()
    assert login_page.unique_element.get_text() == config.get_basic_authorization_alert_expected


# 2
def test_alert(browser):
    # 1
    config = ConfigReader()
    browser.get(config.get_test_alert())

    alert_page = AlertPage(browser)
    alert_page.wait_for_open()

    # 2
    alert_page.js_alert_button.click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_alert_expected_text()
    browser.accept_alert()

    # 3
    expected_text = config.get_alert_result_expected_text()
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text

    # 4
    alert_page.js_confirm_button.click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_confirm_expected_text()
    browser.accept_alert()

    # 5
    expected_text = config.get_confirm_result_expected_text()
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text

    # 6
    alert_page.js_prompt_button.click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_prompt_expected_text()

    # 7
    fake = Faker()
    random_text = fake.name()
    browser.send_keys_alert(random_text)
    browser.accept_alert()

    expected_text = config.get_prompt_result_expected_text() + random_text
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text


# 3
def test_alert_js(browser):
    # 1
    print()
    config = ConfigReader()
    browser.get(config.get_test_alert_url())

    alert_page = AlertPage(browser)
    alert_page.wait_for_open()

    # 2
    alert_page.js_alert_button.js_click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_alert_expected_text()
    browser.accept_alert()

    # 3
    expected_text = config.get_alert_result_expected_text()
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text

    # 4
    alert_page.js_confirm_button.js_click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_confirm_expected_text()
    browser.accept_alert()

    # 5
    expected_text = config.get_confirm_result_expected_text()
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text

    # 6
    alert_page.js_prompt_button.js_click()
    browser.wait_alert_present()
    assert browser.get_alert_text() == config.get_prompt_expected_text()

    # 7
    fake = Faker()
    random_text = fake.name()
    browser.send_keys_alert(random_text)
    browser.accept_alert()

    expected_text = config.get_prompt_result_expected_text() + random_text
    actual_text = alert_page.result_after_alert.get_text()
    assert actual_text == expected_text


# 4
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

    expected_text = config.get_alert_context_click_expected_text()
    actual_text = browser.get_alert_text()
    assert actual_text == expected_text

    # 3
    browser.accept_alert()


# 5
def test_actions(browser):
    # 1
    print()
    config = ConfigReader()
    browser.get(config.get_actions_url())
    actions_page = ActionsPage(browser)
    actions_page.wait_for_open()

    # 2
    fake = Faker()
    random_position = fake.random_int(min=0, max=5) * 0.5
    slider_value = float(actions_page.move_slider_with_arrows(random_position))

    assert random_position == slider_value


# 6
@pytest.mark.parametrize("profile_num, expected_profile_name",
                         [('1', 'name: user1'),
                          ('2', 'name: user2'),
                          ('3', 'name: user3')])
def test_hovers(browser, profile_num, expected_profile_name):
    # 1
    print()
    config = ConfigReader()
    browser.get(config.get_hovers_url())
    hover_page = HoverPage(browser)
    hover_page.wait_for_open()

    # 2
    hover_page.hover_element(profile_num)


    profile_name = hover_page.profile_name_element.get_text()
    assert expected_profile_name == profile_name

    # 3
    hover_page.profile_url_element.click()
    current_url = browser.driver.current_url

    profile_page = ProfilePage(browser)
    profile_page.wait_for_open()
    assert current_url == config.get_profile_url().format(profile_num)

    # 4
    browser.driver.back()
    hover_page.wait_for_open()
    current_url = browser.driver.current_url

    assert current_url == config.get_hovers_url()

# 7
def test_handlers(browser):
    # 1
    print()
    config = ConfigReader()
    browser.get(config.get_handlers_main_page_url())
    handlers_main_page = HandlersMainPage(browser)
    handlers_main_page.wait_for_open()

    # 2
    handlers_main_page.new_tab_maker.click()

    # Another way to solve it
    # all_tabs = browser.driver.window_handles
    # browser.switch_to_window(all_tabs[1])
    browser.switch_to_window(config.get_handlers_new_page_header())
    handlers_new_page_first = HandlersNewPage(browser)
    handlers_new_page_first.wait_for_open()

    assert handlers_new_page_first.unique_element.get_text() == config.get_handlers_new_page_header()
    assert browser.get_title(browser) == config.get_handlers_new_page_header()

    # 3
    # browser.driver.switch_to.window(all_tabs[0])
    browser.switch_to_default_window()

    assert handlers_main_page.unique_element.get_text() == config.get_handlers_main_page_header()

    # 4
    handlers_main_page.new_tab_maker.click()

    # all_tabs = browser.driver.window_handles
    # browser.driver.switch_to.window(all_tabs[2])
    browser.switch_to_window(config.get_handlers_new_page_header())
    handlers_new_page_second = HandlersNewPage(browser)
    handlers_new_page_second.wait_for_open()

    assert handlers_new_page_second.unique_element.get_text() == config.get_handlers_new_page_header()
    assert browser.get_title(browser) == config.get_handlers_new_page_header()

    # 5
    # browser.driver.switch_to.window(all_tabs[0])
    browser.switch_to_default_window()

    assert handlers_main_page.unique_element.get_text() == config.get_handlers_main_page_header()

    # 6
    browser.switch_to_window(config.get_handlers_new_page_header())
    browser.close()

    # 7
    browser.switch_to_window(config.get_handlers_new_page_header())
    browser.close()

# 8
def test_iframe(browser):
    # 1
    print()
    config = ConfigReader()
    browser.get(config.get_iframe_page_url())
    iframe_page = IframePage(browser)
    iframe_page.wait_for_open()

    # 2
    # default condition is opened, make double click
    iframe_page.alerts_frame_windows_button.click()
    iframe_page.alerts_frame_windows_button.click()
    iframe_page.nested_frames_button.click()

    browser.switch_to_frame(iframe_page.nested_frames_parent_frame_element)
    assert (iframe_page.nested_frames_parent_frame_text.get_text() ==
            config.get_iframes_nested_frames_parent_frame_text())

    browser.switch_to_frame(iframe_page.nested_frames_child_frame_element)
    assert (iframe_page.nested_frames_child_frame_text.get_text() ==
            config.get_iframes_nested_frames_child_frame_text())
    browser.switch_to_default_frame()

    # 3
    iframe_page.frames_button.click()
    browser.switch_to_frame(iframe_page.frames_first_frame_element)
    first_frame_text = iframe_page.frames_frame_text.get_text()
    browser.switch_to_parent_frame()

    browser.switch_to_frame(iframe_page.frames_second_frame_element)
    second_frame_text = iframe_page.frames_frame_text.get_text()
    browser.switch_to_parent_frame()

    assert first_frame_text == second_frame_text

# 9
def test_dynamic_content(browser):
    # 1
    print()
    config = ConfigReader()
    browser.get(config.get_dynamic_content_url())
    dynamic_content_page = DynamicContentPage(browser)
    dynamic_content_page.wait_for_open()

    # 2
    compare_results = dynamic_content_page.search_img_match(browser)
    assert compare_results[0] == compare_results[1]

# 10
def test_infinity_scroll(browser):
    # 1
    print()
    config = ConfigReader()
    browser.get(config.get_infinity_scroll_page_url())
    infinity_scroll_page = InfinityScrollPage(browser)
    infinity_scroll_page.wait_for_open()

    # 2
    employ_age = config.get_employ_age()
    assert int(employ_age) == infinity_scroll_page.scroll_n_times_in_container(employ_age, browser)

# 11
def test_upload_image(browser):
    # 1
    print()
    config = ConfigReader()
    browser.get(config.get_upload_image_page_url())
    upload_image_page = UploadImagePage(browser)
    upload_image_page.wait_for_open()

    # 2
    upload_image_page.input_file_element.send_keys(config.get_upload_image_page_file_path())
    upload_image_page.input_file_submit_element.wait_for_clickable()
    upload_image_page.input_file_submit_element.click()
    upload_image_page.wait_for_open()

    assert upload_image_page.unique_element.get_text() == \
        config.get_upload_image_page_success_text()

# 12
def test_upload_image_dialog_window(browser):
    # 1
    print()
    config = ConfigReader()
    browser.get(config.get_upload_image_page_url())
    upload_image_page = UploadImagePage(browser)
    upload_image_page.wait_for_open()

    # 2
    upload_image_page.input_dialog_window_box.wait_for_clickable()
    upload_image_page.input_dialog_window_box.click()

    # 3
    upload_image_page.upload_image_dialog_window(browser, config.get_upload_image_page_file_path())

    assert upload_image_page.dialog_window_upload_success_marker_element.wait_for_visible()
    











