from playwright.sync_api import Locator, Page

from ui_tools.web_element import WebElement


class MultiWebElement:
    def __init__(self, page: Page, description: str, locator: Locator) -> None:
        self.page = page
        self.description = description
        self.locator = locator

    def __str__(self) -> str:
        return f"MultiWebElement[{self.description}]"

    def nth(self, index: int) -> WebElement:
        return WebElement(
            page=self.page,
            description=f"{self.description}[{index}]",
            locator=self.locator.nth(index),
        )

    def count(self) -> int:
        return self.locator.count()
