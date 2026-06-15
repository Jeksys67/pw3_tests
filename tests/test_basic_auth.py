from playwright.sync_api import Browser

from core.page_factory import PageFactory
from pages.basic_auth_page import BasicAuthPage


def test_basic_authorization(browser: Browser, config: dict, open_endpoint):
    username = "admin"
    password = "admin"
    expected_success_text = "Congratulations! You must have the proper credentials."

    page_factory = PageFactory(browser, config)

    page = page_factory.create_page(
        http_credentials={
            "username": username,
            "password": password,
        }
    )

    open_endpoint("basic_auth", target_page=page)

    basic_auth_page = BasicAuthPage(page)

    actual_text = basic_auth_page.get_body_text()

    assert expected_success_text in actual_text, (
    "Basic auth success text не найден на странице\n"
    f"Expected text: {expected_success_text!r}\n"
    f"Actual page text: {actual_text!r}"
)

    page.context.close()