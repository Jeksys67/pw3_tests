from playwright.sync_api import Page

from pages.hovers_page import HoversPage


def test_hovers_show_user_info(page: Page, open_endpoint):
    expected_user_name_template = "name: user{number}"
    open_endpoint("hovers")

    hovers_page = HoversPage(page)

    users_count = hovers_page.get_users_count()

    assert users_count > 0, (
        "Users not found\n"
        "Expected: users_count > 0\n"
        f"Actual: {users_count!r}"
    )

    for index in range(users_count):
        hovers_page.hover_user_by_index(index)

        expected_user_name = expected_user_name_template.format(number=index + 1)

        actual_user_name = hovers_page.get_user_name_by_index(index)

        assert actual_user_name == expected_user_name, (
            "Incorrect user name after hover\n"
            f"Expected: {expected_user_name!r}\n"
            f"Actual: {actual_user_name!r}\n"
            f"User index: {index!r}"
        )
