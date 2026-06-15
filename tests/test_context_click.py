from playwright.sync_api import Page

from pages.context_click_page import ContextClickPage


def test_context_click_shows_alert(page: Page, open_endpoint):
    expected_alert_text = "You selected a context menu"
    context_click_page = ContextClickPage(page)

    open_endpoint("context_click")

    alert_text = context_click_page.right_click_on_hot_spot_and_accept_alert()

    assert alert_text == expected_alert_text, (
        "Incorrect context click alert text\n"
        f"Expected: {expected_alert_text!r}\n"
        f"Actual: {alert_text!r}"
    )