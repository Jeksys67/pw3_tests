from playwright.sync_api import Page

from pages.context_click_page import ContextClickPage


def test_context_click_shows_alert(page: Page, config: dict, open_endpoint):
    context_click_page = ContextClickPage(page)
    test_data = config["context_click"]

    open_endpoint("context_click")

    alert_text = context_click_page.right_click_on_hot_spot_and_accept_alert()

    assert alert_text == test_data["alert_text"]