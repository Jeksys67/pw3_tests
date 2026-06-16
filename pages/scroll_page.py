from playwright.sync_api import Page

from ui_tools.multi_web_element import MultiWebElement


class ScrollPage:
    def __init__(self, page: Page):
        self.page = page

        self.paragraphs = MultiWebElement(
            page,
            "Infinite scroll paragraphs",
            page.locator(".jscroll-added")
        )

    def get_paragraphs_count(self) -> int:
        return self.paragraphs.count()
