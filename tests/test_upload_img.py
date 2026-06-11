from pathlib import Path

from playwright.sync_api import Page
from pages.upload_img_page import UploadPage


def test_upload_image(page: Page, open_endpoint, config: dict):
    upload_page = UploadPage(page)

    test_data = config["upload"]

    file_name = test_data["file_name"]
    file_path = Path(__file__).resolve().parent.parent / "test_img" / file_name

    open_endpoint("upload")

    upload_page.set_file(file_path)
    upload_page.click_upload_button()

    assert upload_page.get_success_title_text() == test_data["success_text"]
    assert upload_page.get_uploaded_file_name() == file_name