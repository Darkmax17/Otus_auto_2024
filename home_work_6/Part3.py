def test_login_logout_admin(browser):
    browser.get(browser.current_url + "/administration")
    # Логин
    browser.find_element(By.NAME, "username").send_keys("your_username")
    browser.find_element(By.NAME, "password").send_keys("your_password")
    browser.find_element(By.XPATH, "//button[text()='Login']").click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#header")))

    # Логаут
    browser.find_element(By.XPATH, "//a[text()='Logout']").click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#login-form")))


def test_add_to_cart(browser):
    browser.get(browser.current_url + "/")
    first_product = browser.find_element(By.CSS_SELECTOR, ".product-thumb a")
    first_product.click()
    browser.find_element(By.CSS_SELECTOR, "#button-cart").click()

    browser.get(browser.current_url + "/index.php?route=checkout/cart")
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-details")))


def test_currency_switch_home(browser):
    browser.get(browser.current_url + "/")
    currency_button = browser.find_element(By.CSS_SELECTOR, ".currency-switcher")
    currency_button.click()
    # Выбрать другую валюту (например, USD) - селектор будет зависеть от реализации
    browser.find_element(By.XPATH, "//option[text()='USD']").click()
    # Проверка, что цена обновилась - добавить соответствующие проверки по селекторам цен


def test_currency_switch_catalog(browser):
    browser.get(browser.current_url + "/index.php?route=product/category")
    currency_button = browser.find_element(By.CSS_SELECTOR, ".currency-switcher")
    currency_button.click()
    # Выбрать другую валюту (например, USD)
    browser.find_element(By.XPATH, "//option[text()='USD']").click()
    # Проверка, что цены в каталоге обновились
