from playwright.sync_api import Browser, BrowserContext, Page


class PageFactory:
    DEFAULT_TIMEOUT_MS = 10_000
    DEFAULT_NAVIGATION_TIMEOUT_MS = 15_000

    def __init__(self, browser: Browser, config: dict) -> None:
        self.browser = browser
        self.config = config

    def create_page(
            self,
            http_credentials: dict[str, str] | None = None,
    ) -> Page:
        context = self._create_context(http_credentials=http_credentials)
        page = context.new_page()

        page.set_default_timeout(
            self.config.get("default_timeout_ms", self.DEFAULT_TIMEOUT_MS)
        )

        page.set_default_navigation_timeout(
            self.config.get(
                "navigation_timeout_ms",
                self.DEFAULT_NAVIGATION_TIMEOUT_MS,
            )
        )

        return page

    def _create_context(
            self,
            http_credentials: dict[str, str] | None = None,
    ) -> BrowserContext:
        context_options = {
            "base_url": self.config["base_url"],
        }

        if http_credentials is not None:
            context_options["http_credentials"] = http_credentials

        return self.browser.new_context(**context_options)
