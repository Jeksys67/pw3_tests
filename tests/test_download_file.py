from playwright.sync_api import Page
from pages.download_page import DownloadPage


def test_download_third_file(page: Page, open_endpoint):
    download_page = DownloadPage(page)

    open_endpoint("download")

    third_file_index = 2

    expected_file_name = download_page.get_file_name_by_index(third_file_index)

    with page.expect_download() as download_info:
        download_page.click_file_by_index(third_file_index)

    downloaded_file = download_info.value

    assert downloaded_file.suggested_filename == expected_file_name