from playwright.sync_api import Page


class DownloadPage:
    def __init__(self, page: Page):
        self.page = page
        self.file_links = page.locator(".example a")

    def get_file_name_by_index(self, index: int) -> str:
        return self.file_links.nth(index).inner_text()

    def click_file_by_index(self, index: int):
        self.file_links.nth(index).click()