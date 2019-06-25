from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):

    def should_be_empty(self):
        self.should_be_empty()
        self.should_be_not_product_in_basket()

    def should_be_message(self):
        actual = self.browser.find_element(*CartPageLocators.EMPTY_BASKET_MESSAGE).text
        excepted = "Your basket is empty. Continue shopping"
        assert actual == excepted, "Incorrect empty basket message " \
                                   "\nexcepted = {}" \
                                   "\nactual = {}".format(excepted, actual)

    def should_be_not_product_in_basket(self):
        assert self.is_not_element_present(*CartPageLocators.BASTES_ITEMS), "Basket items present"
