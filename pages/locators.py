from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT_BTN = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>div:first-child .alertinner")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages>div:last-child .alertinner > p:first-child")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")


class BasePageLocators(object):
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    VIEW_BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group a")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class CartPageLocators(object):
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASTES_ITEMS = (By.CSS_SELECTOR, ".basket-items")
