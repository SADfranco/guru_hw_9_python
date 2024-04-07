import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True)
def configuration():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'
    # options = webdriver.ChromeOptions()
    # options.page_load_strategy = 'none'
    # browser.config.driver_options = options
    yield
    browser.quit()