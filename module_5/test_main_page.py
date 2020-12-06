import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    # вызываем фикстуру в тесте, передав ее как параметр, фикстура описана в файле conftest.py
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")