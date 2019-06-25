import math
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


class BasePage(object):

    def __init__(self, browser: WebDriver, url, timeout=10) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def click(self, how, what):
        self.browser.find_element(how, what).click()

    def type(self, how, what, text):
        el = self.browser.find_element(how, what)
        el.clear()
        el.send_keys(text)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        self.click(*BasePageLocators.LOGIN_LINK)
        from .login_page import LoginPage
        return LoginPage(browser=self.browser, url=self.browser.current_url)

    def go_to_basket_page(self):
        self.click(*BasePageLocators.VIEW_BASKET_LINK)
        from .cart_page import CartPage
        return CartPage(browser=self.browser, url=self.browser.current_url)
