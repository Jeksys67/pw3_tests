from playwright.sync_api import Page

from pages.frames_page import FramePage


def test_nested_frames_text(page: Page, open_endpoint):
    expected_left_text = "LEFT"
    expected_right_text = "RIGHT"
    expected_bottom_text = "BOTTOM"
    expected_middle_text = "MIDDLE"

    frames_page = FramePage(page)

    open_endpoint("frames")

    actual_left_text = frames_page.get_left_frame_text()

    assert actual_left_text == expected_left_text, (
        "Incorrect left frame text\n"
        f"Expected: {expected_left_text!r}\n"
        f"Actual: {actual_left_text!r}"
    )

    actual_right_text = frames_page.get_right_frame_text()

    assert actual_right_text == expected_right_text, (
        "Incorrect right frame text\n"
        f"Expected: {expected_right_text!r}\n"
        f"Actual: {actual_right_text!r}"
    )

    actual_bottom_text = frames_page.get_bottom_frame_text()

    assert actual_bottom_text == expected_bottom_text, (
        "Incorrect bottom frame text\n"
        f"Expected: {expected_bottom_text!r}\n"
        f"Actual: {actual_bottom_text!r}"
    )

    actual_middle_text = frames_page.get_middle_frame_text()

    assert actual_middle_text == expected_middle_text, (
        "Incorrect middle frame text\n"
        f"Expected: {expected_middle_text!r}\n"
        f"Actual: {actual_middle_text!r}"
    )
