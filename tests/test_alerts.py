import random
import string

from playwright.sync_api import Page

from pages.alert_page import AlertsPage

JS_ALERT_DIALOG_TEXT = "I am a JS Alert"
JS_CONFIRM_DIALOG_TEXT = "I am a JS Confirm"
JS_PROMPT_DIALOG_TEXT = "I am a JS prompt"

JS_ALERT_RESULT_TEXT = "You successfully clicked an alert"
JS_CONFIRM_OK_RESULT_TEXT = "You clicked: Ok"
JS_PROMPT_RESULT_TEMPLATE = "You entered: {text}"


def get_random_string(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))


def test_js_alert(page: Page, open_endpoint):
    alert_page = AlertsPage(page)

    open_endpoint("alerts")

    alert_text = alert_page.click_js_alert_and_accept()
    actual_result = alert_page.get_result_text()

    assert alert_text == JS_ALERT_DIALOG_TEXT, (
        "Incorrect JS Alert dialog text\n"
        f"Expected: {JS_ALERT_DIALOG_TEXT!r}\n"
        f"Actual: {alert_text!r}"
    )

    assert actual_result == JS_ALERT_RESULT_TEXT, (
        "Incorrect JS Alert result text\n"
        f"Expected: {JS_ALERT_RESULT_TEXT!r}\n"
        f"Actual: {actual_result!r}"
    )


def test_js_confirm_ok(page: Page, open_endpoint):
    alert_page = AlertsPage(page)

    open_endpoint("alerts")

    alert_text = alert_page.click_js_confirm_and_accept()
    actual_result = alert_page.get_result_text()

    assert alert_text == JS_CONFIRM_DIALOG_TEXT, (
        "Incorrect JS Confirm dialog text\n",
        f"Expected: {JS_CONFIRM_DIALOG_TEXT!r}\n",
        f"Actual: {alert_text!r}"
    )
    assert actual_result == JS_CONFIRM_OK_RESULT_TEXT, (
        "Incorrect JS Confirm result text\n",
        f"Expected: {JS_CONFIRM_OK_RESULT_TEXT!r}\n"
        f"Actual: {actual_result!r}"
    )


def test_js_prompt_ok(page: Page, open_endpoint):
    alert_page = AlertsPage(page)
    random_text = get_random_string()

    open_endpoint("alerts")

    alert_text = alert_page.click_js_prompt_and_accept(random_text)
    actual_result = alert_page.get_result_text()

    expected_result = JS_PROMPT_RESULT_TEMPLATE.format(text=random_text)

    assert alert_text == JS_PROMPT_DIALOG_TEXT, (
        "Incorrect JS Prompt dialog text\n",
        f"Expected: {JS_PROMPT_DIALOG_TEXT!r}\n",
        f"Actual: {alert_text!r}"
    )
    assert actual_result == expected_result, (
        "Incorrect JS Prompt result text\n",
        f"Expected: {JS_PROMPT_RESULT_TEMPLATE!r}\n",
        f"Actual: {actual_result!r}"
    )
