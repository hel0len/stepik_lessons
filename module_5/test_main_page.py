import pytest
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

# Data
link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage:
    @pytest.mark.login_guest
    class TestLoginFromMainPage():
        def test_guest_can_go_to_login_page(self, browser):
            # Arrange
            page = BasePage(browser, link)
            page.open()
            # Act
            page.go_to_login_page()
            login_page = LoginPage(browser, browser.current_url)
            login_page.should_be_login_page()

        def test_guest_should_see_login_link(self, browser):
            # Arrange
            page = MainPage(browser, link)
            page.open()
            # Act
            page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        # Arrange
        page = BasePage(browser, link)
        page.open()
        # Act
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.is_basket_empty()
        basket_page.should_be_basket_empty_message()
