from pathlib import Path
from playwright.sync_api import Page

from ui_tools.web_element import WebElement


class UploadPage:
    def __init__(self, page: Page):
        self.page = page
        self.file_input = WebElement(
            page,
            "File upload",
            page.locator("#file-upload")
        )
        self.upload_button = WebElement(
            page,
            "Upload button",
            page.locator("#file-submit")
        )
        self.uploaded_files = WebElement(
            page,
            "Uploaded files",
            page.locator("#uploaded-files")
        )

        self.success_title = WebElement(
            page,
            "Success title",
            page.locator("h3")
        )

    def set_file(self, file_path: Path):
        self.file_input.set_input_files(file_path)

    def click_upload_button(self):
        self.upload_button.click()

    def get_success_title_text(self) -> str:
        return self.success_title.get_inner_text()

    def get_uploaded_file_name(self) -> str:
        return self.uploaded_files.get_inner_text()