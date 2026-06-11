from pathlib import Path
from playwright.sync_api import Page


class UploadPage:
    def __init__(self, page: Page):
        self.page = page
        self.file_input = page.locator("#file-upload")
        self.upload_button = page.locator("#file-submit")
        self.success_title = page.locator("h3")
        self.uploaded_file_name = page.locator("#uploaded-files")

    def set_file(self, file_path: Path):
        self.file_input.set_input_files(file_path)

    def click_upload_button(self):
        self.upload_button.click()

    def get_success_title_text(self) -> str:
        return self.success_title.inner_text()

    def get_uploaded_file_name(self) -> str:
        return self.uploaded_file_name.inner_text()