from playwright.sync_api import Page, Locator


class HoversPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_icon = page.locator(".figure")

    def get_users_count(self) -> int:
        return self.user_icon.count()

    def hover_user_by_index(self, index: int):
        self.user_icon.nth(index).hover()

    def get_user_name_by_index(self, index: int) -> Locator:
        return self.user_icon.nth(index).locator(".figcaption h5")
