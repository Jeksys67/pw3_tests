from playwright.sync_api import Page

from ui_tools.web_element import WebElement


class FramePage:
    def __init__(self, page: Page):
        self.page = page
        self.top_frame = page.frame_locator("frame[name='frame-top']")

        self.left_frame = self.top_frame.frame_locator("frame[name='frame-left']")
        self.middle_frame = self.top_frame.frame_locator("frame[name='frame-middle']")
        self.right_frame = self.top_frame.frame_locator("frame[name='frame-right']")

        self.bottom_frame = page.frame_locator("frame[name='frame-bottom']")

        self.left_frame_body = WebElement(
            page,
            "Left frame body",
            self.left_frame.locator("body")
        )
        self.middle_frame_body = WebElement(
            page,
            "Middle frame body",
            self.middle_frame.locator("body")
        )
        self.right_frame_body = WebElement(
            page,
            "Right frame body",
            self.right_frame.locator("body")
        )
        self.bottom_frame_body = WebElement(
            page,
            "Bottom frame body",
            self.bottom_frame.locator("body")
        )

    def get_left_frame_text(self) -> str:
        return self.left_frame_body.get_inner_text().strip()

    def get_middle_frame_text(self) -> str:
        return self.middle_frame_body.get_inner_text().strip()

    def get_right_frame_text(self) -> str:
        return self.right_frame_body.get_inner_text().strip()

    def get_bottom_frame_text(self) -> str:
        return self.bottom_frame_body.get_inner_text().strip()
