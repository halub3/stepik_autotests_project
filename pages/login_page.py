from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.should_be_email_form_registration()
        self.should_be_password1_form_registration()
        self.should_be_password2_form_registration()
        self.should_be_registration_button()

        self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD1_REGISTRATION_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2_REGISTRATION_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_email_form_registration(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_REGISTRATION_INPUT), "Email input for registration" \
                                                                                    " is not presented"

    def should_be_password1_form_registration(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD1_REGISTRATION_INPUT), \
                                        "Password1 input for registration is not presented"

    def should_be_password2_form_registration(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD2_REGISTRATION_INPUT), \
                                        "Password1 input for registration is not presented"
    
    def should_be_registration_button(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Can not find registration button"

    def should_be_login_url(self):
        assert self.is_word_in_url("login"), "Incorrect url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Can not find Login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Can not find Register form"