import pytest
from playwright.sync_api import Page

from config.config_reader import load_config, get_url


@pytest.fixture(scope="session")
def config() -> dict:
    return load_config()


@pytest.fixture()
def endpoint_url():
    def _endpoint_url(endpoint_name: str):
        return get_url(endpoint_name)

    return _endpoint_url


@pytest.fixture()
def open_endpoint(page: Page, endpoint_url):
    def _open_endpoint(endpoint_name: str):
        page.goto(endpoint_url(endpoint_name))

    return _open_endpoint