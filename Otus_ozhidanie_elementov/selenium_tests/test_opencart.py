def test_open_opencart(browser, base_url):
    # Открываем базовый URL
    browser.get(base_url)

    # Проверяем, что заголовок страницы не пустой
    assert browser.title != "", "Заголовок страницы пустой"

    # Выводим фактический заголовок для отладки
    print(f"Фактический заголовок: {browser.title}")