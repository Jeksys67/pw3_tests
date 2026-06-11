from playwright.sync_api import Page


class AlertsPage:
    def __init__(self, page: Page):
        self.page = page

        self.js_alert_button = page.get_by_role("button", name="Click for JS Alert")
        self.js_confirm_button = page.get_by_role("button", name="Click for JS Confirm")
        self.js_prompt_button = page.get_by_role("button", name="Click for JS Prompt")

        self.result = page.locator("#result")

    def click_js_alert_and_accept(self) -> str:
        dialog_text = {}

        def handle_dialog(dialog):
            dialog_text["message"] = dialog.message
            dialog.accept()

        self.page.once("dialog", handle_dialog)
        self.js_alert_button.click()

        return dialog_text["message"]

    def click_js_confirm_and_accept(self) -> str:
        dialog_text = {}

        def handle_dialog(dialog):
            dialog_text["message"] = dialog.message
            dialog.accept()

        self.page.once("dialog", handle_dialog)
        self.js_confirm_button.click()

        return dialog_text["message"]

    def click_js_prompt_and_accept(self, text: str) -> str:
        dialog_text = {}

        def handle_dialog(dialog):
            dialog_text["message"] = dialog.message
            dialog.accept(text)

        self.page.once("dialog", handle_dialog)
        self.js_prompt_button.click()

        return dialog_text["message"]
