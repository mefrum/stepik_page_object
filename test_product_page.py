import time

import pytest

from base_test import setup_product_page, setup_page
from pages.login_page import LoginPage


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    page = setup_product_page(browser)
    page.click_btn_add_to_basket()
    page.should_contains_product_name_in_success_message(page.product_name(), page.success_message())
    page.should_contains_product_price_in_basket_total(page.product_price(), page.basket_message())


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    page = setup_product_page(browser)
    cart_page = page.go_to_basket_page()
    cart_page.should_be_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = setup_product_page(browser)
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = setup_page(browser, LoginPage, "http://selenium1py.pythonanywhere.com/accounts/login/")
        email = str(time.time()) + "@fakemail.org"
        password = "890YUIhjk"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = setup_product_page(browser)
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        page = setup_product_page(browser)
        page.click_btn_add_to_basket()
        page.should_contains_product_name_in_success_message(page.product_name(), page.success_message())
        page.should_contains_product_price_in_basket_total(page.product_price(), page.basket_message())
