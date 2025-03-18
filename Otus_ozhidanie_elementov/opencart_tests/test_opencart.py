from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

#Тест для главной страницы
def test_home_page(browser, base_url):
    browser.get(base_url)

    # Проверяем наличие элементов на главной странице
    WebDriverWait(browser, 5).until(EC.title_is("Your Store"))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav#menu")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#search")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content h3")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer")))

#Тест для страницы каталога
def test_catalog_page(browser, base_url):
    browser.get(base_url + "/index.php?route=product/category&path=20")

    # Проверяем наличие элементов на странице каталога
    WebDriverWait(browser, 5).until(EC.title_contains("Desktops"))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#product-category")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content h2")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.product-layout")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#column-left")))

#Тест для карточки товара
def test_product_page(browser, base_url):
    browser.get(base_url + "/index.php?route=product/product&path=57&product_id=49")

    # Проверяем наличие элементов на странице товара
    WebDriverWait(browser, 5).until(EC.title_contains("Samsung Galaxy Tab 10.1"))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#product")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button#button-cart")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.thumbnails")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.rating")))

#Тест для страницы логина в админку
def test_admin_login_page(browser, base_url):
    browser.get(base_url + "/admin")

    # Проверяем наличие элементов на странице логина в админку
    WebDriverWait(browser, 5).until(EC.title_contains("Administration"))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.panel-heading")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#input-username")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#input-password")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

#Тест для страницы регистрации пользователя
def test_register_page(browser, base_url):
    browser.get(base_url + "/index.php?route=account/register")

    # Проверяем наличие элементов на странице регистрации
    WebDriverWait(browser, 5).until(EC.title_contains("Register Account"))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#content h1")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#input-firstname")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#input-lastname")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#input-email")))
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#input-password")))