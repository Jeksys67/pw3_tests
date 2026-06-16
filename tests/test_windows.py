from playwright.sync_api import Page, expect

from pages.windows_page import WindowPage
from ui_tools.page_actions import PageActions


def test_open_and_close_new_windows(page: Page, open_endpoint):
    expected_new_window_text = "New Window"
    expected_tabs_count = 1

    windows_page = WindowPage(page)
    page_actions = PageActions(page)

    open_endpoint("windows")

    first_new_page = windows_page.open_new_window()

    expect(first_new_page.get_by_role("heading")).to_have_text(
        expected_new_window_text
    )

    page_actions.bring_to_front()

    second_new_page = windows_page.open_new_window()

    expect(second_new_page.get_by_role("heading")).to_have_text(
        expected_new_window_text
    )

    page_actions.bring_to_front()

    first_new_page.close()
    second_new_page.close()

    actual_tabs_count = windows_page.get_opened_pages_count()

    assert actual_tabs_count == expected_tabs_count, (
        "Incorrect opened tabs count after closing new windows\n"
        f"Expected: {expected_tabs_count!r}\n"
        f"Actual: {actual_tabs_count!r}"
    )
