import json
import os
from pathlib import Path


class ConfigReader:
    CONFIG_PATH = "config_test_data.json"

    def __init__(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        # Build path to config file in same directory
        config_file = os.path.join(self.script_dir, "config_test_data.json")
        with open(config_file) as f:
            self.config = json.load(f)

    def get_config(self, key):
        return self.config[key]

    def get_upload_image_page_file_path(self):
        parent_dir = Path(self.script_dir).parent
        target_file = parent_dir / 'source' / self.config["test_upload_image_file_path"]
        return str(target_file)
