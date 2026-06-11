from playwright.sync_api import Page
from pages.scroll_page import ScrollPage

def test_scroll_to_correct_paragraphs(page: Page, open_endpoint):
    scroll_page = ScrollPage(page)


    open_endpoint("scroll")

    while scroll_page.get_paragraphs_count() < 10:
        scroll_page.scroll_page_down()

    assert scroll_page.get_paragraphs_count() >= 10