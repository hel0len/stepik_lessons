import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language for test")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    if language not in ["ru", "en-gb", "es", "fr"]:
        raise pytest.UsageError("test run should contain language for test")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print("\nopen browser for test..")

    result = webdriver.Chrome(options=options)
    result.maximize_window()
    result.implicitly_wait(5)
    result.user_language = language

    yield result

    print("\nquit browser..")
    result.quit()