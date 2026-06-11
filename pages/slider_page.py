from playwright.sync_api import Page


class SliderPage:
    def __init__(self, page: Page):
        self.page = page
        self.slider = page.locator("input[type='range']")
        self.slider_value = page.locator("#range")

    def set_slider_value_with_keyboard(
            self,
            target_value: float,
            min_value: float,
            step: float
    ):
        steps_count = int((target_value - min_value) / step)

        self.slider.focus()
        self.slider.press("Home")

        for _ in range(steps_count):
            self.slider.press("ArrowRight")
