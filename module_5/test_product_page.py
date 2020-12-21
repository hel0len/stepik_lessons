from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize('promo', ["?promo=offer0",
                                  "?promo=offer1",
                                  "?promo=offer2",
                                  "?promo=offer3",
                                  "?promo=offer4",
                                  "?promo=offer5",
                                  "?promo=offer6",
                                  "?promo=offer7",
                                  "?promo=offer8",
                                  "?promo=offer9"])


class TestProductPage():
    def test_guest_can_add_product_to_basket(self, browser, promo):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_book_name()
        page.should_be_book_price()


