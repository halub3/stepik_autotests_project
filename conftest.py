import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")
    parser.addoption('--headless', action='store', default='true',
                     help="Open a browser invisible")
    parser.addoption('--imp_wait', action='store', default='false',
                    help="Add implicitly wait 7 sec")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    headless = request.config.getoption("headless")
    wait = request.config.getoption("imp_wait")
    browser = None
    if language is None:
        raise pytest.UsageError("--language is not chosen")
    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if headless == 'true':
        options.add_argument("headless")

    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    if wait == 'true':
        browser.implicitly_wait(7)

    yield browser
    print("\nquit browser..")
    browser.quit()