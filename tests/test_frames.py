from playwright.sync_api import Page

from pages.frames_page import FramePage


def test_nested_frames_text(page: Page, config: dict, open_endpoint):
    frames_data = config["frames"]
    frames_page = FramePage(page)

    open_endpoint("frames")

    assert frames_page.get_left_frame_text() == frames_data["left_text"]
    assert frames_page.get_right_frame_text() == frames_data["right_text"]
    assert frames_page.get_bottom_frame_text() == frames_data["bottom_text"]
    assert frames_page.get_middle_frame_text() == frames_data["middle_text"]