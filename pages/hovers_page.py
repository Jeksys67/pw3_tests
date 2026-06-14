from playwright.sync_api import Page
from ui_tools.multi_web_element import MultiWebElement


class HoversPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_cards = MultiWebElement(
            page,
            "User avatar",
            page.locator(".figure")
        )

    def get_users_count(self) -> int:
        return self.user_cards.count()

    def hover_user_by_index(self, index: int):
        self.user_cards.nth(index).hover()

    def get_user_name_by_index(self, index: int):
        user_card = self.user_cards.nth(index)

        user_name = user_card.find_child(
            selector=".figcaption h5",
            description="User name",
        )

        return user_name.locator
