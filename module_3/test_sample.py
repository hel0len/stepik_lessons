from selenium import webdriver
import time

# Думаю, что лучше разбить этот тест на 5 маленьких тестов, по одному Assert в каждом,
# Но по заданию было нужно автоматизировать целый свой сценарий из ДЗ модуля №1, поэтому пока так.

# Arrange
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/")

# Act
button1=browser.find_element_by_xpath('//form[@action="/ru/basket/add/209/"]/button').click()

# Assert
success_message_change_value_basket = "Стоимость корзины теперь составляет"
message_change_value_basket = browser.find_element_by_xpath('//*[contains(text(), "Стоимость корзины теперь составляет")]').text
assert success_message_change_value_basket in message_change_value_basket, \
f"Ожидалось, что сообщение '{success_message_change_value_basket}' присутствует на странице"

# Assert
success_button_show_basket = "Посмотреть корзину"
button_show_basket = browser.find_element_by_xpath('//p/a[contains(text(), "Посмотреть корзину")]').text
assert success_button_show_basket in button_show_basket, \
f"Ожидалось, что кнопка '{success_button_show_basket}' присутствует на странице"

# Assert
success_button_make_order = "Оформить"
button_make_order = browser.find_element_by_xpath('//p/a[contains(text(), "Оформить")]').text
assert success_button_make_order in button_make_order, \
f"Ожидалось, что кнопка '{success_button_make_order}' присутствует на странице"

# Act
button_show_basket = browser.find_element_by_xpath('//p/a[contains(text(), "Посмотреть корзину")]').click()

# Assert
success_current_url = "http://selenium1py.pythonanywhere.com/ru/basket/"
current_url = browser.current_url
assert success_current_url == current_url, \
f"Ожидалось, что текущая страница -'{success_current_url}'"

# Assert
success_h1 = "Корзина"
h1 = browser.find_element_by_xpath('//h1').text
assert success_h1 == h1, \
f"Ожидалось, что заголовок h1 - '{success_h1}'"

time.sleep(3)
browser.quit()

