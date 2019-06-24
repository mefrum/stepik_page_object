from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_btn_add_to_basket(self):
        self.click(*ProductPageLocators.ADD_TO_BASKET_BTN)

    def product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def success_message(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

    def basket_message(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE).text

    def should_contains_product_name_in_success_message(self, product_name, success_message):
        assert product_name in success_message, "Success message should contains product name " \
                                                "\nproduct_name = {}" \
                                                "\nsuccess_message = {}".format(product_name, success_message)

    def should_contains_product_price_in_basket_total(self, product_price, basket_message):
        assert product_price in basket_message, "Basket message should contains product price " \
                                                "\nproduct_price = {}" \
                                                "\nbasket_message = {}".format(product_price, basket_message)
