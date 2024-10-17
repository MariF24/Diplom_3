import pytest
from selenium import webdriver
from config import URL

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = None
    if request.param == 'chrome':
        browser = webdriver.Chrome()
    elif request.param == 'firefox':
        browser = webdriver.Firefox()
    browser.get(f'{URL}')

    yield browser

    browser.quit()