from playwright.sync_api import Page

from pages.scroll_page import ScrollPage
from ui_tools.page_actions import PageActions


def test_scroll_to_correct_paragraphs(page: Page, open_endpoint):
    scroll_page = ScrollPage(page)
    page_actions = PageActions(page)

    open_endpoint("scroll")

    while scroll_page.get_paragraphs_count() < 10:
        page_actions.scroll_page_down()

    actual_paragraphs_count = scroll_page.get_paragraphs_count()
    expected_min_paragraphs_count = 10

    assert actual_paragraphs_count >= expected_min_paragraphs_count, (
        "Incorrect paragraphs count after scrolling\n"
        f"Expected: >= {expected_min_paragraphs_count!r}\n"
        f"Actual: {actual_paragraphs_count!r}"
    )