from playwright.sync_api import Page, expect

from pages.windows_page import WindowPage


def test_open_and_close_new_windows(page: Page, config: dict, open_endpoint):
    windows_data = config["windows"]

    windows_page = WindowPage(page)

    open_endpoint("windows")

    first_new_page = windows_page.open_new_window()

    expect(first_new_page.get_by_role("heading")).to_have_text(
        windows_data["new_window_text"]
    )

    page.bring_to_front()

    second_new_page = windows_page.open_new_window()

    expect(second_new_page.get_by_role("heading")).to_have_text(
        windows_data["new_window_text"]
    )

    page.bring_to_front()

    first_new_page.close()
    second_new_page.close()

    assert windows_page.get_opened_pages_count() == windows_data["expected_tabs_count"]