from playwright.sync_api import Page

class DynamicContentPage:
    def __init__(self, page: Page):
        self.page = page
        self.images = page.locator("#content img")


    def reload_page(self):
        self.page.reload(wait_until="domcontentloaded")

    def wait_images_attached(self):
        self.images.nth(2).wait_for(state="attached")

    def get_image_sources(self) -> list[str]:
        self.wait_images_attached()

        return [
            self.images.nth(1).get_attribute("src")
            for i in range(self.images.count())
        ]