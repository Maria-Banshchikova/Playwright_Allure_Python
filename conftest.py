import pytest
from playwright.sync_api import Browser, Page, sync_playwright
from pages.main_page import MainPage

@pytest.fixture(scope="session")
def browser():  #  -> Browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Headless если True, то не работает
        yield browser
        browser.close()


@pytest.fixture
def page(browser: Browser):  # -> Page
    context = browser.new_context(base_url="https://www.effective-mobile.ru/")
    page = context.new_page()
    page.goto("/")  # Явно открываем главную
    page.wait_for_load_state('networkidle')  # Ждём загрузки
    yield page
    context.close()


@pytest.fixture
def main_page(page: Page) -> MainPage:
    page.wait_for_load_state('networkidle', timeout=60000)
    return MainPage(page)  # Инъекция Page Object
