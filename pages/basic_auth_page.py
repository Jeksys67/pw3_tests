from playwright.sync_api import Page

from ui_tools.web_element import WebElement

class BasicAuthPage:
    def __init__(self, page: Page):
        self.page = page
        self._body = WebElement(
            page,
            "Basic auth body",
            page.locator("body")
        )

    def get_body_text(self) -> str:
        return self._body.get_inner_text()
