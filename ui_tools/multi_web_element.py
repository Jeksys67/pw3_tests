import logging
from playwright.sync_api import Locator, Page

from ui_tools.web_element import WebElement
from logger_config import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class MultiWebElement:
    def __init__(self, page: Page, description: str, locator: Locator) -> None:
        self.page = page
        self.description = description
        self.locator = locator

    def __str__(self) -> str:
        return f"MultiWebElement[{self.description}]"

    def nth(self, index: int) -> WebElement:
        logger.info(f"{self}: get element by index {index}")
        return WebElement(
            page=self.page,
            description=f"{self.description}[{index}]",
            locator=self.locator.nth(index),
        )

    def count(self) -> int:
        logger.info(f"{self}: count elements")
        result = self.locator.count()
        logger.info(f"{self}: count = {result}")
        return result
