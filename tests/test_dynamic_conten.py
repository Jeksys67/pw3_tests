from playwright.sync_api import Page
from pages.dynamic_content_page import DynamicContentPage

def is_one_pair(items: list[str]) -> bool:
    return len(items) != len(set(items))


def test_dynamic_content_img(page: Page, open_endpoint):
    dynamic_page = DynamicContentPage(page)

    open_endpoint("dynamic_content")

    max_attempts = 50
    attempts = 0
    pair_img = False

    while not pair_img and attempts < max_attempts:
        image_sources = dynamic_page.get_image_sources()

        actual_images_count = len(image_sources)
        expected_images_count = 3

        assert actual_images_count == expected_images_count, (
            "Incorrect dynamic content images count\n"
            f"Expected: {expected_images_count!r}\n"
            f"Actual: {actual_images_count!r}"
        )

        pair_img = is_one_pair(image_sources)

        if not pair_img:
            dynamic_page.reload_page()

        attempts += 1

    assert pair_img, (
        "Failed to find a pair of matching images in dynamic content\n"
        "Expected: True\n"
        f"Actual: {pair_img!r}\n"
        f"Attempts: {attempts!r}\n"
        f"Max attempts: {max_attempts!r}"
    )