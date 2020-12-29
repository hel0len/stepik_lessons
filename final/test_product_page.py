import pytest
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import random
import time

# Data
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestProductPage():
    @pytest.mark.parametrize('promo', ["?promo=offer6",
                                       pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                       "?promo=offer8",])

    def test_guest_can_add_product_to_basket(self, browser, promo):
        # Arrange
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}"
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_book_name()
        page.should_be_book_price()


    def test_guest_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.should_not_be_success_message()

    @pytest.mark.xfail()
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.add_to_basket()
        page.is_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Arrange
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.should_be_login_link()


    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Arrange
        page = BasePage(browser, link)
        page.open()
        # Act
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.is_basket_empty()
        basket_page.should_be_basket_empty_message()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Arrange
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.login_page = LoginPage(browser, link)
        self.login_page.open()
        count = random.randint(1, 100)
        email = str(time.time()) + "@test.com"
        password = str(time.time() + count)
        # Act
        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        # Act
        page.should_not_be_success_message()

