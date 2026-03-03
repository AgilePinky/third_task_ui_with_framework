import json
import os


class ConfigReader:
    CONFIG_PATH = "config_test_data.json"

    def __init__(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        # Build path to config file in same directory
        config_file = os.path.join(self.script_dir, "config_test_data.json")
        with open(config_file) as f:
            self.config = json.load(f)

    # 1
    def get_basic_authorization_username(self):
        return self.config["basic_authorization_username"]

    def get_basic_authorization_password(self):
        return self.config["basic_authorization_password"]

    def get_basic_authorization_url(self):
        return self.config["basic_authorization_url"]

    def get_basic_authorization_alert_expected(self):
        return self.config["basic_authorization_expected_alert"]

    # 2, 3
    def get_test_alert(self):
        return self.config["test_alert"]

    def get_test_alert_url(self):
        return self.config["test_alert_url"]

    def get_alert_result_expected_text(self):
        return self.config["alert_expected_result_text"]

    def get_alert_expected_text(self):
        return self.config["alert_expected_text"]

    def get_confirm_result_expected_text(self):
        return self.config["confirm_expected_result_text"]

    def get_confirm_expected_text(self):
        return self.config["confirm_expected_text"]

    def get_prompt_result_expected_text(self):
        return self.config["prompt_expected_result_text"]

    def get_prompt_expected_text(self):
        return self.config["prompt_expected_text"]

    # 4
    def get_test_alert_context_click_url(self):
        return self.config["test_alert_context_click_url"]

    def get_alert_context_click_expected_text(self):
        return self.config["alert_context_click_expected_text"]

    # 5
    def get_actions_url(self):
        return self.config["actions_url"]

    # 6
    def get_hovers_url(self):
        return self.config["hovers_url"]

    def get_profile_url(self):
        return self.config["profile_url"]

    # 7
    def get_handlers_main_page_url(self):
        return self.config["handlers_main_page_url"]

    def get_handlers_main_page_header(self):
        return self.config["handlers_main_page_header"]

    def get_handlers_main_page_title(self):
        return self.config["handlers_main_page_title"]

    def get_handlers_new_page_url(self):
        return self.config["handlers_new_page_url"]

    def get_handlers_new_page_header(self):
        return self.config["handlers_new_page_header"]

    # 8
    def get_iframe_page_url(self):
        return self.config["iframe_page_url"]

    def get_iframes_nested_frames_parent_frame_text(self):
        return self.config["iframes_nested_frames_parent_frame_text"]

    def get_iframes_nested_frames_child_frame_text(self):
        return self.config["iframes_nested_frames_child_frame_text"]

    # 9
    def get_dynamic_content_url(self):
        return self.config["dynamic_content_url"]

    # 10
    def get_infinity_scroll_page_url(self):
        return self.config["infinity_scroll_page_url"]

    def get_scroll_script(self):
        return self.config["scroll_script"]

    def get_employ_age(self):
        return self.config["employ_age"]

    # 11-13
    def get_upload_image_page_url(self):
        return self.config["upload_image_page_url"]

    def get_upload_image_page_file_path(self):
        parent_dir = os.path.dirname(self.script_dir)
        target_file = os.path.join(parent_dir, 'source',
                                   self.config["upload_image_page_file_path"])
        return target_file

    def get_upload_image_page_success_text(self):
        return self.config["upload_image_page_success_text"]

    def get_upload_image_page_dialog_window_success_text(self):
        return self.config["upload_image_page_dialog_window_success_text"]