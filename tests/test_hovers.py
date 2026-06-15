from playwright.sync_api import Page, expect

from pages.hovers_page import HoversPage


def test_hovers_show_user_info(page: Page, open_endpoint):
    expected_user_name_template = "name: user{number}"
    open_endpoint("hovers")

    hovers_page = HoversPage(page)

    users_count = hovers_page.get_users_count()

    assert users_count > 0, (
        "На странице не найдено пользователей\n"
        "Expected: users_count > 0\n"
        f"Actual: {users_count!r}"
    )

    for index in range(users_count):
        hovers_page.hover_user_by_index(index)

        expected_user_name = expected_user_name_template.format(number=index + 1)

        user_name = hovers_page.get_user_name_by_index(index)

        expect(user_name).to_be_visible()
        expect(user_name).to_have_text(expected_user_name)
