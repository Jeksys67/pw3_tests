from playwright.sync_api import Page

from ui_tools.multi_web_element import MultiWebElement
from ui_tools.page_actions import PageActions


class DownloadPage:
    def __init__(self, page: Page):
        self.page = page
        self.file_links = MultiWebElement(
            page,
            "Download file links",
            page.locator(".example a")
        )
        self.actions = PageActions(page)

    def get_file_name_by_index(self, index: int) -> str:
        return self.file_links.nth(index).get_inner_text()

    def download_file_by_index(self, index: int):
        file_link = self.file_links.nth(index)
        return self.actions.run_and_expect_download(file_link.click)
