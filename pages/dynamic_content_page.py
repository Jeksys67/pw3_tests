from playwright.sync_api import Page

from ui_tools.multi_web_element import MultiWebElement
from ui_tools.page_actions import PageActions


class DynamicContentPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)
        self.images = MultiWebElement(
            page,
            "Dynamic content images",
            page.locator("#content img")
        )

    def wait_images_attached(self, expected_count: int) -> None:
        self.images.nth(expected_count - 1).locator.wait_for(state="attached")

    def get_image_sources(self) -> list[str]:
        images_count = self.images.count()

        return [
            self.images.nth(index).get_attribute("src")
            for index in range(images_count)
        ]
