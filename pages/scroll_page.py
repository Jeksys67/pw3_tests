from playwright.sync_api import Page

class ScrollPage:
    def __init__(self, page: Page):
        self.page = page
        self.paragraphs = page.locator(".jscroll-added")


    def scroll_page_down(self):
        self.page.mouse.wheel(0, 1000)

    def get_paragraphs_count(self) -> int:
        return self.paragraphs.count()

