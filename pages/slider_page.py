from playwright.sync_api import Page

from ui_tools.web_element import WebElement


class SliderPage:
    def __init__(self, page: Page):
        self.page = page
        self.slider = WebElement(
            page,
            "Slider",
            page.locator("input[type='range']")
        )
        self.slider_value = WebElement(
            page,
            "Slider value",
            page.locator("#range")
        )

    def set_slider_value_with_keyboard(self, target_value: float):
        min_value = float(self.slider.get_attribute("min"))
        max_value = float(self.slider.get_attribute("max"))
        step = float(self.slider.get_attribute("step"))

        if target_value < min_value or target_value > max_value:
            raise ValueError("Target value is outside slider range")

        steps_count = int((target_value - min_value) / step)

        self.slider.focus()
        self.slider.press("Home")

        for _ in range(steps_count):
            self.slider.press("ArrowRight")

    def get_slider_value_text(self) -> str:
        return self.slider_value.get_inner_text()

    def get_min_value(self) -> float:
        return float(self.slider.get_attribute("min"))

    def get_max_value(self) -> float:
        return float(self.slider.get_attribute("max"))

    def get_step(self) -> float:
        return float(self.slider.get_attribute("step"))
