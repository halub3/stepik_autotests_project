import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = None
    if language is None:
        raise pytest.UsageError("--language is not chosen")
    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(7)

    yield browser
    print("\nquit browser..")
    browser.quit()