from playwright.sync_api import Page

from ui_tools.page_actions import PageActions
from ui_tools.multi_web_element import MultiWebElement


class ScrollPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.paragraphs = MultiWebElement(
            page,
            "Infinite scroll paragraphs",
            page.locator(".jscroll-added")
        )

    def scroll_page_down(self):
        self.actions.scroll_page_down()

    def get_paragraphs_count(self) -> int:
        return self.paragraphs.count()
