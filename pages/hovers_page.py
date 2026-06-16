from playwright.sync_api import Page
from ui_tools.multi_web_element import MultiWebElement
from ui_tools.web_element import WebElement


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

    def _get_user_name_element_by_index(self, index: int) -> WebElement:
        user_card = self.user_cards.nth(index)

        return user_card.find_child(
            selector=".figcaption h5",
            description="User name",
        )

    def get_user_name_by_index(self, index: int) -> str:
        return self._get_user_name_element_by_index(index).get_inner_text()
