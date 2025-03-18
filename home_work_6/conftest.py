import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("browser")
    base_url = request.config.getoption("base_url")

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise ValueError("Browser not supported!")

    driver.get(base_url)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Выбор браузера: chrome или firefox")
    parser.addoption("--base_url", action="store", default="http://localhost/opencart", help="Базовый URL для opencart")
