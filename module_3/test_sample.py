from selenium import webdriver
import time

#Data
main_page_link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"

# Arrange
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get(main_page_link)

def test_check_basket_total_cost_after_adding_good():
    #Data
    success_message_change_value_basket = "Стоимость корзины теперь составляет"
    message_change_value_basket_locator = '//*[contains(text(), "Стоимость корзины теперь составляет")]'

    # Act
    browser.find_element_by_xpath('//form[@action="/ru/basket/add/209/"]/button').click()

    # Assert
    message_change_value_basket = browser.find_element_by_xpath(message_change_value_basket_locator)
    assert success_message_change_value_basket in message_change_value_basket.text, \
        f"Ожидалось, что сообщение '{success_message_change_value_basket}' присутствует на странице"

def test_watch_button_show_basket_after_adding_good():
    # Data
    success_button_show_basket = "Посмотреть корзину"
    button_show_basket_locator = '//p/a[contains(text(), "Посмотреть корзину")]'

    # Assert
    button_show_basket = browser.find_element_by_xpath(button_show_basket_locator)
    assert success_button_show_basket in button_show_basket.text, \
        f"Ожидалось, что кнопка '{success_button_show_basket}' присутствует на странице"

def test_watch_button_make_order_after_adding_good():
    # Data
    success_button_make_order = "Оформить"
    button_make_order_locator = '//p/a[contains(text(), "Оформить")]'

    # Assert
    button_make_order = browser.find_element_by_xpath(button_make_order_locator)
    assert success_button_make_order in button_make_order.text, \
        f"Ожидалось, что кнопка '{success_button_make_order}' присутствует на странице"

def test_page_has_word_basket_in_url():
    # Data
    success_current_url = "http://selenium1py.pythonanywhere.com/ru/basket/"
    button_show_basket_locator = '//p/a[contains(text(), "Посмотреть корзину")]'

    # Act
    browser.find_element_by_xpath(button_show_basket_locator).click()

    # Assert
    current_url = browser.current_url
    assert success_current_url == current_url, \
        f"Ожидалось, что текущая страница -'{success_current_url}'"

def test_page_has_word_basket_in_h1():
    # Data
    h1_locator = '//h1'
    success_h1 = "Корзина"

    # Assert
    h1 = browser.find_element_by_xpath(h1_locator)
    assert success_h1 == h1.text, \
        f"Ожидалось, что заголовок h1 - '{success_h1}'"

try:
    test_check_basket_total_cost_after_adding_good()
    test_watch_button_show_basket_after_adding_good()
    test_watch_button_make_order_after_adding_good()
    test_page_has_word_basket_in_url()
    test_page_has_word_basket_in_h1()

finally:
    time.sleep(3)
    browser.quit()


