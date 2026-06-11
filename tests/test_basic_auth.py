from playwright.sync_api import Browser, expect


def test_basic_authorization(browser: Browser, config: dict, endpoint_url):
    basic_auth_data = config["basic_auth"]
    url = endpoint_url("basic_auth")

    context = browser.new_context(
        http_credentials={
            "username": basic_auth_data["username"],
            "password": basic_auth_data["password"]
        }
    )

    page = context.new_page()

    response = page.goto(url)

    assert response is not None, "Authorization error: страница не вернула ответ"

    assert response.status == 200, (
        "Authorization error: ожидался статус 200, "
        f"но пришёл статус {response.status}"
    )

    expect(
        page.locator("body"),
        "Authorization error: успешный текст после авторизации не найден"
    ).to_contain_text(basic_auth_data["success_text"])

    context.close()