from playwright.sync_api import Page


class WindowPage:
    def __init__(self, page: Page):
        self.page = page
        self.click_on_link_new_page = page.get_by_role("link", name="Click Here")

    def open_new_window(self) -> Page:
        with self.page.expect_popup() as popup_info:
            self.click_on_link_new_page.click()

        new_page = popup_info.value
        new_page.wait_for_load_state()

        return new_page

    def get_opened_pages_count(self) -> int:
        return len(self.page.context.pages)