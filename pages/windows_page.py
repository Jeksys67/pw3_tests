from playwright.sync_api import Page

from ui_tools.web_element import WebElement
from ui_tools.page_actions import PageActions


class WindowPage:
    def __init__(self, page: Page):
        self.page = page
        self.new_window_link = WebElement(
            page,
            "Click link new page",
            page.get_by_role("link", name="Click Here")
        )
        self.actions = PageActions(page)

    def open_new_window(self) -> Page:
        return self.actions.run_and_expect_new_page(
            self.new_window_link.click
        )

    def get_opened_pages_count(self) -> int:
        return len(self.page.context.pages)

    def bring_main_page_to_front(self) -> None:
        self.actions.bring_to_front()