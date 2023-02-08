import uuid
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdrivermanager.chrome import ChromeDriverManager


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.options = Options()
    chrome_options.options.add_argument("--headless")
    chrome_options.options.add_argument("--disable-gpu")
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--log-level=DEBUG')

    return chrome_options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    # Эта функция помогает определить, что какой-то тест не прошел
    # и передать эту информацию в отчет:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


