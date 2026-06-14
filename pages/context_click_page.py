from playwright.sync_api import Page
from ui_tools.web_element import WebElement
from ui_tools.page_actions import PageActions


class ContextClickPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)
        self.hot_spot = WebElement(
            page,
            "Hot spot area",
            page.locator("#hot-spot")
        )

    def right_click_on_hot_spot_and_accept_alert(self) -> str:
        return self.actions.run_and_accept_alert(self.hot_spot.right_click)
