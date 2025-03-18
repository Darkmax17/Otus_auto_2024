import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# Регистрируем пользовательские аргументы командной строки
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="browser to execute tests (chrome, firefox, edge)")
    parser.addoption("--url", action="store", default="http://localhost", help="base OpenCart URL")


# Фикстура для инициализации браузера
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise pytest.UsageError("--browser should be chrome, firefox or edge")

    yield driver
    #driver.quit()


# Фикстура для получения базового URL
@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")