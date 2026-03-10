from pathlib import Path
import os


class DataUtils:
    PATH_TO_IMG = "image.jpg"

    def __init__(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        # Build path to config file in same directory

    def get_upload_image_page_file_path(self):
        parent_dir = Path(self.script_dir).parent
        target_file = parent_dir / 'source' / self.PATH_TO_IMG
        return str(target_file)