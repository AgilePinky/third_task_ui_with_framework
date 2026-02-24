import json
import os

class ConfigReader:

    CONFIG_PATH = "config_test_data.json"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Build path to config file in same directory
    config_file = os.path.join(script_dir, "config_test_data.json")

    def __init__(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Build path to config file in same directory
        config_file = os.path.join(script_dir, "config_test_data.json")
        with open(config_file) as f:
            self.config = json.load(f)

    def get_username_basic_authorization(self):
        return self.config["username_basic_authorization"]

    def get_password_basic_authorization(self):
        return self.config["password_basic_authorization"]

    def get_url_basic_authorization(self):
        return self.config["url_basic_authorization"]

    def get_expected_basic_authorization_alert(self):
        return self.config["expected_basic_authorization_alert"]

    def get_expected_js_alert_result_text(self):
        return self.config["expected_js_alert_result_text"]

    def get_expected_js_alert_text(self):
        return self.config["expected_js_alert_text"]

    def get_expected_js_confirm_result_text(self):
        return self.config["expected_js_confirm_result_text"]

    def get_expected_js_confirm_text(self):
        return self.config["expected_js_confirm_text"]

    def get_expected_js_prompt_result_text(self):
        return self.config["expected_js_prompt_result_text"]

    def get_expected_js_prompt_text(self):
        return self.config["expected_js_prompt_text"]

