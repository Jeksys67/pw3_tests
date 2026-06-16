from playwright.sync_api import Page, Locator
import logging
from pathlib import Path
from typing import Literal

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

    def get_inner_text(self) -> str:
        logger.info(f"{self}: get text content")
        result = self.locator.inner_text()
        logger.info(f"{self}: text content = {result}")
        return result

    def find_child(self, selector: str, description: str) -> "WebElement":
        logger.info(f"{self}: find child '{description}' by selector '{selector}'")

        return WebElement(
            page=self.page,
            description=f"{self.description} -> {description}",
            locator=self.locator.locator(selector)
        )

    def focus(self) -> None:
        logger.info(f"{self}: focus")
        self.locator.focus()

    def press(self, key: str) -> None:
        logger.info(f"{self}: press '{key}'")
        self.locator.press(key)

    def get_attribute(self, attribute: str) -> str:
        logger.info(f"{self}: get attribute '{attribute}'")
        result = self.locator.get_attribute(attribute)
        logger.info(f"{self}: attribute '{attribute}' = '{result}'")
        return result

    def set_input_files(self, file_path: Path) -> None:
        logger.info(f"{self}: File path '{file_path}'")
        self.locator.set_input_files(file_path)

    def wait_for(
            self,
            state: Literal["attached", "detached", "hidden", "visible"] = "visible",
    ) -> None:
        logger.info(f"{self}: wait for state '{state}'")
        self.locator.wait_for(state=state)

    def scroll_into_view_if_needed(self) -> None:
        logger.info(f"{self}: scroll into view if needed")
        self.locator.scroll_into_view_if_needed()
