from playwright.sync_api import Browser, BrowserContext, Page


class PageFactory:
    DEFAULT_TIMEOUT_MS = 10_000
    DEFAULT_NAVIGATION_TIMEOUT_MS = 15_000

    def __init__(self, browser: Browser, config: dict) -> None:
        self.browser = browser
        self.config = config

    def create_page(self) -> Page:
        context = self._create_context()
        page = context.new_page()
        page.set_default_timeout(self.config.get("default_timeout_ms", self.DEFAULT_TIMEOUT_MS))
        page.set_default_navigation_timeout(
            self.config.get(
                "navigation_timeout_ms",
                self.DEFAULT_NAVIGATION_TIMEOUT_MS,
            )
        )

        return page

    def _create_context(self) -> BrowserContext:
        context = self.browser.new_context(
            base_url=self.config["base_url"]
        )
        return context
