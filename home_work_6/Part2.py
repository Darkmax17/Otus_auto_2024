import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("url, elements", [
    ("/", ["#logo", "#search", ".nav > li"]),
    ("/index.php?route=product/category", ["#content", ".catalog-items"]),
    ("/index.php?route=product/product&product_id=43", ["#product", ".price", ".button-cart"]),
    ("/administration", ["#header", "#login-form"]),
    ("/index.php?route=account/register", ["#content", "#register-form", ".form-group"])
])
def test_elements_on_pages(browser, url, elements):
    browser.get(browser.current_url + url)
    for element in elements:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, element)))
