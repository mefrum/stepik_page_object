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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is_disappeared"

    def should_contains_product_name_in_success_message(self, product_name, success_message):
        excepted_message = "{} has been added to your basket.".format(product_name)
        assert excepted_message == success_message, \
            "Success message should contains product name " \
            "\nexcepted_message = {}" \
            "\nsuccess_message = {}".format(excepted_message, success_message)

    def should_contains_product_price_in_basket_total(self, product_price, basket_message):
        excepted_message = "Your basket total is now {}".format(product_price)
        assert excepted_message == basket_message, \
            "Basket message should contains product price " \
            "\nexcepted_message = {}" \
            "\nbasket_message = {}".format(excepted_message, basket_message)
