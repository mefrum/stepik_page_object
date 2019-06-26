from base_test import setup_page
from pages.main_page import MainPage


def test_quest_can_go_to_login_page(browser):
    page = setup_page(browser, MainPage, "http://selenium1py.pythonanywhere.com/")
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = setup_page(browser, MainPage, "http://selenium1py.pythonanywhere.com/")
    page.should_be_login_link()
