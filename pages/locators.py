from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button[type=\"submit\"].btn-add-to-basket")
    NAME_IN_CATALOG = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_IN_CATALOG = (By.CSS_SELECTOR, "div.col-sm-6.product_main p:nth-child(2)")
    NAME_IN_ALERT = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon:nth-child(1) .alertinner strong")
    PRICE_IN_ALERT = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon:nth-child(3) .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div#messages div.alert")

