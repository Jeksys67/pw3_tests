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


def test_slider_random_value_with_keyboard(page: Page, config: dict, open_endpoint):
    slider_page = SliderPage(page)
    slider_data = config["slider"]

    min_value = slider_data["min_value"]
    max_value = slider_data["max_value"]
    step = slider_data["step"]

    target_value = get_random_slider_value(
        min_value=min_value,
        max_value=max_value,
        step=step
    )

    expected_value = format_slider_value(target_value)

    open_endpoint("slider")

    slider_page.set_slider_value_with_keyboard(
        target_value=target_value,
        min_value=min_value,
        step=step
    )

    expect(slider_page.slider_value).to_have_text(expected_value)