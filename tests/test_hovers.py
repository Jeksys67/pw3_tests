from playwright.sync_api import Page, expect

from pages.hovers_page import HoversPage


def test_hovers_show_user_info(page: Page, config: dict, open_endpoint):
    open_endpoint("hovers")

    hovers_page = HoversPage(page)
    hovers_data = config["hovers"]

    users_count = hovers_page.get_users_count()

    assert users_count > 0, "На странице не найдено пользователей"

    for index in range(users_count):
        hovers_page.hover_user_by_index(index)

        expected_user_name = hovers_data["expected_user_name_template"].format(
            number=index + 1
        )

        user_name = hovers_page.get_user_name_by_index(index)

        expect(user_name).to_be_visible()
        expect(user_name).to_have_text(expected_user_name)