import pytest
from faker import Faker
import inspect

from config_dir.config_reader import ConfigReader
from utils.pyautogui_utils import PyAutoGuiUtils
from logger_dir.logger import Logger
from utils.data_utils import DataUtils
from pages_dir.basic_authorization import BasicAuthorization
from pages_dir.alert_page import AlertPage
from pages_dir.alert_context_page import AlertContextPage
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
    config = ConfigReader()
    test_name = inspect.currentframe().f_code.co_name
    username = config.get_config(f"{test_name}_username")
    password = config.get_config(f"{test_name}_password")
    url = config.get_config(f"{test_name}_url")
    auth_url = f"https://{username}:{password}@{url}"
    browser.get(auth_url)

    # 2
    basic_authorization_page = BasicAuthorization(browser)
    basic_authorization_page.wait_for_open()

    expected_result = config.get_config(f"{test_name}_expected_result_text")
    actual_result = basic_authorization_page.get_result_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")


# 2
def test_alert(browser):
    # 1
    config = ConfigReader()
    test_name = inspect.currentframe().f_code.co_name
    browser.get(config.get_config(f"{test_name}_url"))

    alert_page = AlertPage(browser)
    alert_page.wait_for_open()

    # 2
    alert_page.click_alert_button()
    browser.wait_alert_present()

    expected_result = config.get_config(f"{test_name}_expected_text")
    actual_result = browser.get_alert_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")
    browser.accept_alert()

    # 3
    expected_result = config.get_config(f"{test_name}_expected_result_text")
    actual_result = alert_page.get_result_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    # 4
    alert_page.click_confirm_button()
    browser.wait_alert_present()

    expected_result = config.get_config(f"{test_name}_confirm_expected_text")
    actual_result = browser.get_alert_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")
    browser.accept_alert()

    # 5
    expected_result = config.get_config(f"{test_name}_confirm_expected_result_text")
    actual_result = alert_page.get_result_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    # 6
    alert_page.click_prompt_button()
    browser.wait_alert_present()

    expected_result = config.get_config(f"{test_name}_prompt_expected_text")
    actual_result = browser.get_alert_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    # 7
    fake = Faker()
    random_text = fake.name()
    browser.send_keys_alert(random_text)
    browser.accept_alert()

    expected_result = config.get_config(f"{test_name}_prompt_expected_result_text") + random_text
    actual_result = alert_page.get_result_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")


# 3
def test_alert_js(browser):
    # 1
    config = ConfigReader()
    test_name = inspect.currentframe().f_code.co_name
    browser.get(config.get_config(f"{test_name[:-3]}_url"))

    alert_page = AlertPage(browser)
    alert_page.wait_for_open()

    # 2
    alert_page.js_click_alert_button()
    browser.wait_alert_present()

    expected_result = config.get_config(f"{test_name[:-3]}_expected_text")
    actual_result = browser.get_alert_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")
    browser.accept_alert()

    # 3
    expected_result = config.get_config(f"{test_name[:-3]}_expected_result_text")
    actual_result = alert_page.get_result_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    # 4
    alert_page.js_click_confirm_button()
    browser.wait_alert_present()

    expected_result = config.get_config(f"{test_name[:-3]}_confirm_expected_text")
    actual_result = browser.get_alert_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")
    browser.accept_alert()

    # 5
    expected_result = config.get_config(f"{test_name[:-3]}_confirm_expected_result_text")
    actual_result = alert_page.get_result_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    # 6
    alert_page.js_click_prompt_button()
    browser.wait_alert_present()

    expected_result = config.get_config(f"{test_name[:-3]}_prompt_expected_text")
    actual_result = browser.get_alert_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    # 7
    fake = Faker()
    random_text = fake.name()
    browser.send_keys_alert(random_text)
    browser.accept_alert()

    expected_result = config.get_config(f"{test_name[:-3]}_prompt_expected_result_text") + random_text
    actual_result = alert_page.get_result_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")


# 4
def test_alert_context_click(browser):
    # 1
    config = ConfigReader()
    test_name = inspect.currentframe().f_code.co_name
    browser.get(config.get_config(f"{test_name}_url"))
    context_menu_alert_page = AlertContextPage(browser)
    context_menu_alert_page.wait_for_open()

    # 2
    context_menu_alert_page.right_click_on_box()
    browser.wait_alert_present()
    browser.get_alert_text()

    expected_result = config.get_config(f"{test_name}_expected_result_text")
    actual_result = browser.get_alert_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    # 3
    browser.accept_alert()


# 5
def test_actions(browser):
    # 1
    config = ConfigReader()
    test_name = inspect.currentframe().f_code.co_name
    browser.get(config.get_config(f"{test_name}_url"))
    actions_page = ActionsPage(browser)
    actions_page.wait_for_open()

    # 2
    random_position = actions_page.get_random_position()
    slider_value = actions_page.move_slider_with_arrows(random_position)

    expected_result = random_position
    actual_result = slider_value
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")


# 6
@pytest.mark.parametrize("profile_num, expected_profile_name",
                         [('1', 'name: user1'),
                          ('2', 'name: user2'),
                          ('3', 'name: user3')])
def test_hovers(browser, profile_num, expected_profile_name):
    # 1
    config = ConfigReader()
    test_name = inspect.currentframe().f_code.co_name
    browser.get(config.get_config(f"{test_name}_url"))
    hover_page = HoverPage(browser)
    hover_page.wait_for_open()

    # 2
    hover_page.hover_element(profile_num)

    profile_name = hover_page.get_profile_name(profile_num)

    expected_result = expected_profile_name
    actual_result = profile_name
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    # 3
    hover_page.click_profile_url(profile_num)
    current_url = hover_page.get_current_url()

    profile_page = ProfilePage(browser)
    profile_page.wait_for_open()

    expected_result = config.get_config(f"{test_name}_profile_url").format(profile_num)
    actual_result = current_url
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    # 4
    browser.driver.back()
    hover_page.wait_for_open()
    current_url = hover_page.get_current_url()

    expected_result = config.get_config(f"{test_name}_url")
    actual_result = current_url
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")


# 7
def test_handlers(browser):
    # 1
    config = ConfigReader()
    test_name = inspect.currentframe().f_code.co_name
    browser.get(config.get_config(f"{test_name}_main_page_url"))
    handlers_main_page = HandlersMainPage(browser)
    handlers_main_page.wait_for_open()

    # 2
    handlers_main_page.click_new_tab()

    # Another way to solve it
    # all_tabs = browser.driver.window_handles
    # browser.switch_to_window(all_tabs[1])
    handlers_main_page.switch_to_tab(config.get_config(f"{test_name}_new_page_header"))
    handlers_new_page_first = HandlersNewPage(browser)
    handlers_new_page_first.wait_for_open()

    expected_result = config.get_config(f"{test_name}_new_page_header")
    actual_result = handlers_new_page_first.get_header_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    expected_result = config.get_config(f"{test_name}_new_page_header")
    actual_result = browser.get_title()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    # 3
    browser.switch_to_default_window()

    expected_result = config.get_config(f"{test_name}_main_page_header")
    actual_result = handlers_main_page.get_header_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    # 4
    handlers_main_page.click_new_tab()

    handlers_main_page.switch_to_tab(config.get_config(f"{test_name}_new_page_header"))
    handlers_new_page_second = HandlersNewPage(browser)
    handlers_new_page_second.wait_for_open()

    expected_result = config.get_config(f"{test_name}_new_page_header")
    actual_result = handlers_new_page_second.get_header_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    expected_result = config.get_config(f"{test_name}_new_page_header")
    actual_result = browser.get_title()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    # 5
    browser.switch_to_default_window()

    expected_result = config.get_config(f"{test_name}_main_page_header")
    actual_result = handlers_main_page.get_header_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    # 6
    handlers_main_page.switch_to_tab(config.get_config(f"{test_name}_new_page_header"))
    browser.close()

    # 7
    handlers_main_page.switch_to_tab(config.get_config(f"{test_name}_new_page_header"))
    browser.close()


# 8
def test_iframes(browser):
    # 1
    config = ConfigReader()
    test_name = inspect.currentframe().f_code.co_name
    browser.get(config.get_config(f"{test_name}_url"))
    iframe_page = IframePage(browser)
    iframe_page.wait_for_open()

    # 2
    # default condition is opened, make double click
    iframe_page.click_alerts_frame_windows_button()
    iframe_page.click_alerts_frame_windows_button()
    iframe_page.click_nested_frames_button()

    expected_result = config.get_config(f"{test_name}_nested_frames_parent_frame_text")
    actual_result = iframe_page.get_nested_frames_parent_frame_text()
    assert (actual_result == expected_result), \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    expected_result = config.get_config(f"{test_name}_nested_frames_child_frame_text")
    actual_result = iframe_page.get_nested_frames_child_frame_text()
    assert (actual_result == expected_result), \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")

    # 3
    iframe_page.click_frames_button()
    iframe_page.switch_to_frames_first_frame()
    first_frame_text = iframe_page.get_frames_frame_text()
    iframe_page.switch_to_parent_frame()

    iframe_page.switch_frames_second_frame_element()
    second_frame_text = iframe_page.get_frames_frame_text()
    iframe_page.switch_to_parent_frame()

    assert first_frame_text == second_frame_text


# 9
def test_dynamic_content(browser):
    # 1
    config = ConfigReader()
    test_name = inspect.currentframe().f_code.co_name
    browser.get(config.get_config(f"{test_name}_url"))
    dynamic_content_page = DynamicContentPage(browser)
    dynamic_content_page.wait_for_open()

    # 2
    compare_results = dynamic_content_page.search_img_match()

    assert compare_results[0] < compare_results[1], \
        Logger.error(f"Images don't match")


# 10
def test_infinity_scroll(request, browser):
    # 1
    config = ConfigReader()
    test_name = inspect.currentframe().f_code.co_name
    browser.get(config.get_config(f"{test_name}_url"))
    infinity_scroll_page = InfinityScrollPage(browser)
    infinity_scroll_page.wait_for_open()

    # 2
    employee_age = config.get_config(f"{test_name}_employee_age")

    expected_result = int(employee_age)
    actual_result = infinity_scroll_page.scroll_n_times_in_container(employee_age, browser)
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")


# 11
def test_upload_image(browser):
    # 1
    data_utils = DataUtils()
    config = ConfigReader()
    test_name = inspect.currentframe().f_code.co_name
    browser.get(config.get_config(f"{test_name}_url"))
    upload_image_page = UploadImagePage(browser)
    upload_image_page.wait_for_open()

    # 2
    path_to_img = data_utils.get_upload_image_page_file_path()
    upload_image_page.send_keys_input_file_element(path_to_img)
    upload_image_page.click_input_file_submit_element()
    upload_image_page.wait_for_open()

    expected_result = config.get_config(f"{test_name}_success_text")
    actual_result = upload_image_page.get_header_text()
    assert actual_result == expected_result, \
        Logger.error(f"Actual result = {actual_result}"
                     f"Expected result = {expected_result}")


# 12
def test_upload_image_dialog_window(browser):
    # 1
    data_utils = DataUtils()
    config = ConfigReader()
    test_name = inspect.currentframe().f_code.co_name
    browser.get(config.get_config(f"{test_name[:-14]}_url"))
    upload_image_page = UploadImagePage(browser)
    upload_image_page.wait_for_open()

    # 2
    upload_image_page.click_input_dialog_window_box()

    # 3
    pyautogui_util = PyAutoGuiUtils()
    pyautogui_util.upload_image_dialog_window(
        upload_image_page,
        data_utils.get_upload_image_page_file_path())

    assert upload_image_page.dialog_window_upload_success_marker_element.wait_for_visible(), \
        Logger.error(f"Success marker isn't visible")
