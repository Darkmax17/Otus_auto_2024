import pytest
from selenium import webdriver
from selenium.webdriver.ie.service import Service


# Добавляем опции командной строки
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="browser to execute tests (chrome, firefox, edge)")
    parser.addoption("--url", action="store", default="http://localhost",
                     help="base OpenCart URL (default: http://localhost)")


# Фикстура для инициализации браузера
@pytest.fixture (scope="function")
def browser(request):
    browser = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")

    if browser == "chrome":
        service = Service()
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "yandex":
        options = webdriver.ChromeOptions()
        service = Service(executable_path=os.path.join(drivers, "yandexdriver"))
        options.binary_location = "usr/bin/yandex-browser"
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception ("Driver not supported")

    driver.implicity_wait(2)

    request.addfinalizer(driver.quit)

    return driver

# Фикстура для получения базового URL
@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")
