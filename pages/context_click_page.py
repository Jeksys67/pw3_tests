from playwright.sync_api import Page


class ContextClickPage:
    def __init__(self, page: Page):
        self.page = page
        self.hot_spot = page.locator("#hot-spot")

    def right_click_on_hot_spot_and_accept_alert(self) -> str:
        dialog_text = {}

        def handle_dialog(dialog):
            dialog_text["message"] = dialog.message
            dialog.accept()

        self.page.once("dialog", handle_dialog)
        self.hot_spot.click(button="right")

        return dialog_text["message"]
