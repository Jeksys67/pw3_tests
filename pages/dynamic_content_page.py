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

    def reload_page(self):
        self.actions.reload_page()

    def wait_images_attached(self):
        self.images.nth(2)

    def get_image_sources(self) -> list[str]:
        self.wait_images_attached()

        return [
            self.images.nth(i).get_attribute("src")
            for i in range(self.images.count())
        ]