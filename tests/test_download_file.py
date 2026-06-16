from playwright.sync_api import Page
from pages.download_page import DownloadPage


def test_download_third_file(page: Page, open_endpoint):
    download_page = DownloadPage(page)

    open_endpoint("download")

    third_file_index = 2

    expected_file_name = download_page.get_file_name_by_index(third_file_index)

    downloaded_file = download_page.download_file_by_index(third_file_index)

    actual_file_name = downloaded_file.suggested_filename

    assert actual_file_name == expected_file_name, (
        "Incorrect downloaded file name\n"
        f"Expected: {expected_file_name!r}\n"
        f"Actual: {actual_file_name!r}"
    )