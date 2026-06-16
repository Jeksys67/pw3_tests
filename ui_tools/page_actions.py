import logging
from typing import Literal
from collections.abc import Callable

from playwright.sync_api import Page, Dialog

from logger_config import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class PageActions:
    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self, url: str) -> None:
        logger.info(f"PageActions: goto '{url}'")
        self.page.goto(url)

    def run_and_accept_alert(self, action: Callable[[], None]) -> str:
        logger.info("PageActions: accept dialog")
        return self._handle_dialog(action, mode="accept")

    def run_and_dismiss_alert(self, action: Callable[[], None]) -> str:
        logger.info("PageActions: dismiss dialog")
        return self._handle_dialog(action, mode="dismiss")

    def run_and_accept_prompt(
            self,
            action: Callable[[], None],
            prompt_text: str,
    ) -> str:
        logger.info("PageActions: accept prompt")
        return self._handle_dialog(action, mode="accept", prompt_text=prompt_text)

    def _handle_dialog(
            self,
            action: Callable[[], None],
            mode: str,
            prompt_text: str | None = None,
    ) -> str:
        logger.info("PageActions: expect dialog")

        message = ""

        def handle_dialog(dialog: Dialog) -> None:
            nonlocal message

            message = dialog.message
            logger.info(
                f"PageActions: dialog '{dialog.type}' with message '{message}'"
            )

            if mode == "dismiss":
                dialog.dismiss()
                return

            if prompt_text is None:
                dialog.accept()
                return

            dialog.accept(prompt_text)

        self.page.once("dialog", handle_dialog)

        action()

        if not message:
            raise RuntimeError("Expected dialog was not shown")

        return message

    def run_and_expect_download(self, action: Callable[[], None]):
        logger.info(f"PageActions: expect download")

        with self.page.expect_download() as download_info:
            action()

        download = download_info.value
        logger.info(f"PageActions: downloaded file '{download.suggested_filename}'")

        return download

    def run_and_expect_new_page(self, action: Callable[[], None]):
        logger.info(f"PageAction: expect new page")

        with self.page.expect_popup() as popup_info:
            action()

        new_page = popup_info.value
        new_page.wait_for_load_state()

        logger.info(f"PageActions: new page opened with url '{new_page.url}'")

        return new_page

    def bring_to_front(self) -> None:
        logger.info(f"PageActions: bring page to front")
        self.page.bring_to_front()

    def reload_page(
            self,
            wait_until: Literal["commit", "domcontentloaded", "load", "networkidle"] = "domcontentloaded",
    ) -> None:
        logger.info(f"PageActions: reload page with wait_until='{wait_until}'")
        self.page.reload(wait_until=wait_until)

    def scroll_page_down(self, delta_y: int = 1000) -> None:
        logger.info(f"PageActions: scroll page down by {delta_y}")
        self.page.mouse.wheel(delta_x=0, delta_y=delta_y)
