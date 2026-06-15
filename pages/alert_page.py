from playwright.sync_api import Page

from ui_tools.page_actions import PageActions
from ui_tools.web_element import WebElement


class AlertsPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)
        self.js_alert_button = WebElement(
            page,
            "JS Alert button",
            page.get_by_role("button", name="Click for JS Alert")
        )
        self.js_confirm_button = WebElement(
            page,
            "JS Confirm button",
            page.get_by_role("button", name="Click for JS Confirm")
        )
        self.js_prompt_button = WebElement(
            page,
            "JS Prompt button",
            page.get_by_role("button", name="Click for JS Prompt")
        )

        self._result = WebElement(
            page,
            "Alert result text",
            page.locator("#result")
        )

    def click_js_alert_and_accept(self) -> str:
        return self.actions.run_and_accept_alert(self.js_alert_button.click)

    def click_js_confirm_and_accept(self) -> str:
        return self.actions.run_and_accept_alert(self.js_confirm_button.click)

    def click_js_prompt_and_accept(self, text: str) -> str:
        return self.actions.run_and_accept_prompt(self.js_prompt_button.click,
                                                  text, )

    def get_result_text(self) -> str:
        return self._result.get_inner_text()
