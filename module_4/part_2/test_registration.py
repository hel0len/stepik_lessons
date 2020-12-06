import pytest
import random
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/ru/"

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_registration_new_user(browser):
    #Data
    unique_var = random.randint(10000, 9999999)
    button_login_or_registr_locator = '//a[@ id = "login_link"]'
    input_email_locator = '//input[@name="registration-email"]'
    input_password_locator = '//input[@ name = "registration-password1"]'
    input_confirm_password_locator = '//input[@ name = "registration-password2"]'
    button_register_locator = '//button[@ name = "registration_submit"]'
    success_registration_message_locator = '//*[contains(text(), "Спасибо за регистрацию!")]'
    success_registration_message = "Спасибо за регистрацию!"

    #Arrange
    browser.get(link)

    #Act
    browser.find_element_by_xpath(button_login_or_registr_locator).click()
    input_email = browser.find_element_by_xpath(input_email_locator)
    input_email.send_keys("{}@mail.com".format(unique_var))
    input_password = browser.find_element_by_xpath(input_password_locator)
    input_password.send_keys(unique_var, unique_var)
    input_confirm_password = browser.find_element_by_xpath(input_confirm_password_locator)
    input_confirm_password.send_keys(unique_var, unique_var)
    browser.find_element_by_xpath(button_register_locator).click()

    #Assert
    registration_message = browser.find_element_by_xpath(success_registration_message_locator)
    assert success_registration_message == registration_message.text, \
        f"Ожидалось, что сообщение '{success_registration_message}' присутствует на странице"