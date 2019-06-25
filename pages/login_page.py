from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        actual = self.browser.current_url
        end_url = "/accounts/login/"
        assert str(actual).endswith(end_url), \
            "Url is incorrect. Acctual url is {} \nUrl must end with {}".format(actual, end_url)

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER form is not present"

    def register_new_user(self, email, password):
        self.type(*LoginPageLocators.REG_EMAIL, text=email)
        self.type(*LoginPageLocators.REG_PASSWORD, text=password)
        self.type(*LoginPageLocators.REG_PASSWORD_CONFIRM, text=password)
        self.click(*LoginPageLocators.REG_SUBMIT_BTN)
