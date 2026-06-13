import pytest

from playwright.sync_api import Browser, Page

from core.page_factory import PageFactory
from logger_config import setup_logger
from config.config_reader import get_url, load_config


@pytest.fixture(scope="session")
def config():
    return load_config()


@pytest.fixture()
def endpoint_url():
    def _endpoint_url(endpoint_name: str):
        return get_url(endpoint_name)

    return _endpoint_url


@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()


@pytest.fixture()
def open_endpoint(page: Page, endpoint_url):
    def _open_endpoint(endpoint_name: str):
        page.goto(endpoint_url(endpoint_name))

    return _open_endpoint


@pytest.fixture()
def page(browser: Browser, config: dict):
    page_factory = PageFactory(browser, config)
    page = page_factory.create_page()

    yield page

    page.context.close()
