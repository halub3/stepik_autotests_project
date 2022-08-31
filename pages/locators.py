from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_REGISTRATION_INPUT = (By.CSS_SELECTOR, "input[name=\"registration-email\"]")
    PASSWORD1_REGISTRATION_INPUT = (By.CSS_SELECTOR, "input[name=\"registration-password1\"]")
    PASSWORD2_REGISTRATION_INPUT = (By.CSS_SELECTOR, "input[name=\"registration-password2\"]")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name=\"registration_submit\"]")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button[type=\"submit\"].btn-add-to-basket")
    NAME_IN_CATALOG = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_IN_CATALOG = (By.CSS_SELECTOR, "div.col-sm-6.product_main p:nth-child(2)")
    NAME_IN_ALERT = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon:nth-child(1) .alertinner strong")
    PRICE_IN_ALERT = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon:nth-child(3) .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages div.alert")


class BasketPageLocators():
    EMPTY_BASKET_NOTIFY = (By.CSS_SELECTOR, "div#content_inner p")
    BASKET_FORM_WITH_OBJECTS = (By.CSS_SELECTOR, "div#content_inner form.basket_summary")

