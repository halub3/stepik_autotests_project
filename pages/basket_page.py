from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_notify_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_NOTIFY), "Can not find text about empty basket"

    def should_bot_be_basket_with_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM_WITH_OBJECTS), "Can see basket with products"

