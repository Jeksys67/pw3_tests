from playwright.sync_api import Page

from ui_tools.web_element import WebElement


class FramePage:
    TOP_FRAME = "frame[name='frame-top']"
    BOTTOM_FRAME = "frame[name='frame-bottom']"

    def __init__(self, page: Page):
        self.page = page

        self._left_frame_body = self._top_frame_body(
            frame_name="frame-left",
            description="Left frame body"
        )
        self._middle_frame_body = self._top_frame_body(
            frame_name="frame-middle",
            description="Middle frame body"
        )
        self._right_frame_body = self._top_frame_body(
            frame_name="frame-right",
            description="Right frame body"
        )
        self._bottom_frame_body = WebElement(
            page,
            "Bottom frame body",
            page.frame_locator(self.BOTTOM_FRAME).locator("body")
        )

    def _top_frame_body(self, frame_name: str, description: str) -> WebElement:
        return WebElement(
            self.page,
            description,
            self.page.frame_locator(self.TOP_FRAME)
                .frame_locator(f"frame[name='{frame_name}']")
                .locator("body")
        )

    def get_left_frame_text(self) -> str:
        return self._left_frame_body.get_inner_text()

    def get_middle_frame_text(self) -> str:
        return self._middle_frame_body.get_inner_text()

    def get_right_frame_text(self) -> str:
        return self._right_frame_body.get_inner_text()

    def get_bottom_frame_text(self) -> str:
        return self._bottom_frame_body.get_inner_text()