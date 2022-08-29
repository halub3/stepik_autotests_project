from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        price = self.should_be_text_with_price_and_get_it()
        name = self.should_be_text_with_name_and_get_it()
        self.press_button(*ProductPageLocators.BASKET_BUTTON)
        self.solve_quiz_and_get_code()
        self.should_be_same_name_in_alert(name)
        self.should_be_same_price_in_alert(price)

    def press_button(self, how, what):
        self.should_be_button(how, what)
        self.browser.find_element(how, what).click()

    def should_be_text_with_price_and_get_it(self):
        price = self.get_element_text(*ProductPageLocators.PRICE_IN_CATALOG)
        assert price is not None, "Can not find price of product"
        return price

    def should_be_text_with_name_and_get_it(self):
        name = self.get_element_text(*ProductPageLocators.NAME_IN_CATALOG)
        assert name is not None, "Can not find name of product"
        return name

    def should_be_button(self, how, what):
        assert self.is_element_present(how, what), f"Can not find button with request {what}"

    def should_be_same_price_in_alert(self, price):
        new_price = self.get_element_text(*ProductPageLocators.PRICE_IN_ALERT)
        assert new_price is not None, "Can not find price in alert"
        assert new_price == price
    
    def should_be_same_name_in_alert(self, name):
        new_name = self.get_element_text(*ProductPageLocators.NAME_IN_ALERT)
        assert new_name is not None, "Can not find name in alert"
        assert new_name == name
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
