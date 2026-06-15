from pathlib import Path

from playwright.sync_api import Page

from pages.upload_img_page import UploadPage


def test_upload_image(page: Page, open_endpoint, tmp_path: Path):
    file_name = "upload_test_file.txt"
    expected_success_text = "File Uploaded!"

    file_path = tmp_path / file_name
    file_path.write_text("test upload content", encoding="utf-8")

    upload_page = UploadPage(page)

    open_endpoint("upload")

    upload_page.set_file(file_path)
    upload_page.click_upload_button()

    actual_success_text = upload_page.get_success_title_text()
    actual_uploaded_file_name = upload_page.get_uploaded_file_name()

    assert actual_success_text == expected_success_text, (
        "Incorrect upload success title\n"
        f"Expected: {expected_success_text!r}\n"
        f"Actual: {actual_success_text!r}"
    )

    assert actual_uploaded_file_name == file_name, (
        "Incorrect uploaded file name\n"
        f"Expected: {file_name!r}\n"
        f"Actual: {actual_uploaded_file_name!r}"
    )
