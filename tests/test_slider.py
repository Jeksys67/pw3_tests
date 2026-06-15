import random

from playwright.sync_api import Page, expect

from pages.slider_page import SliderPage


def format_slider_value(value: float) -> str:
    if value.is_integer():
        return str(int(value))

    return str(value)


def get_random_slider_value(
        min_value: float,
        max_value: float,
        step: float
) -> float:
    steps_count = int((max_value - min_value) / step)

    values = [
        min_value + step * step_number
        for step_number in range(1, steps_count)
    ]

    return random.choice(values)


def test_slider_random_value_with_keyboard(page: Page, open_endpoint):
    slider_page = SliderPage(page)

    open_endpoint("slider")

    min_value = slider_page.get_min_value()
    max_value = slider_page.get_max_value()
    step = slider_page.get_step()

    target_value = get_random_slider_value(
        min_value=min_value,
        max_value=max_value,
        step=step,
    )

    expected_value = format_slider_value(target_value)

    slider_page.set_slider_value_with_keyboard(target_value)

    actual_value = slider_page.get_slider_value_text()

    assert actual_value == expected_value, (
        "Incorrect slider value\n"
        f"Expected: {expected_value!r}\n"
        f"Actual: {actual_value!r}"
    )
