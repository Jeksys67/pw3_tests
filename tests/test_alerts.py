import random
import string

from playwright.sync_api import Page, expect

from pages.alert_page import AlertsPage


def get_random_string(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))


def test_js_alert(page: Page, config: dict, open_endpoint):
    alert_page = AlertsPage(page)
    alert_data = config["alerts"]

    open_endpoint("alerts")

    alert_text = alert_page.click_js_alert_and_accept()

    assert alert_text == alert_data["dialogs"]["js_alert"]
    expect(alert_page.result).to_have_text(alert_data["results"]["js_alert"])


def test_js_confirm_ok(page: Page, config: dict, open_endpoint):
    alert_page = AlertsPage(page)
    alert_data = config["alerts"]

    open_endpoint("alerts")

    alert_text = alert_page.click_js_confirm_and_accept()

    assert alert_text == alert_data["dialogs"]["js_confirm"]
    expect(alert_page.result).to_have_text(alert_data["results"]["js_confirm_ok"])


def test_js_prompt_ok(page: Page, config: dict, open_endpoint):
    alert_page = AlertsPage(page)
    alert_data = config["alerts"]

    random_text = get_random_string()

    open_endpoint("alerts")

    alert_text = alert_page.click_js_prompt_and_accept(random_text)

    expected_result = alert_data["results"]["js_prompt_template"].format(
        text=random_text
    )

    assert alert_text == alert_data["dialogs"]["js_prompt"]
    expect(alert_page.result).to_have_text(expected_result)
