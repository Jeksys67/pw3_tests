from playwright.sync_api import Page, Locator
import logging

from logger_config import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class WebElement:
    def __init__(self, page: Page, description: str, locator: Locator) -> None:
        self.page = page
        self.description = description
        self.locator = locator

    def __str__(self) -> str:
        return f"WebElement[{self.description}]"

    def click(self) -> None:
        logger.info(f"{self}: click")
        self.locator.click()

    def right_click(self) -> None:
        logger.info(f"{self}: right click")
        self.locator.click(button="right")

    def hover(self) -> None:
        logger.info(f"{self}: hover")
        self.locator.hover()

    def get_inner_text(self) -> None:
        logger.info(f"{self}: get text content")
        result = self.locator.text_content()
        logger.info(f"{self}: text content = {result}")
        return result

    def find_child(self, selector: str, description: str) -> "WebElement":
        logger.info(f"{self}: find child '{description}' by selector '{selector}'")

        child_locator = self.locator.locator(selector)

        return WebElement(
            page=self.page,
            description=f"{self.description} -> {description}",
            locator=child_locator,
        )

    def focus(self) -> None:
        logger.info(f"{self}: focus")
        self.locator.focus()

    def press(self, key: str) -> None:
        logger.info(f"{self}: press '{key}'")
        self.locator.press(key)





































