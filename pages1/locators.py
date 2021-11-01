from selenium.webdriver.common.by import By


class MainPageLocators():
    #проверить необходимость лолин линка в мейн пейдже
    LOGIN_LINK = (By.CSS_SELECTOR, ".MuiAvatar-img")
    TEAM_LINK = (By.LINK_TEXT, "/teams")

class LoginPageLocators():
    LOGIN_LINK_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_LINK_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_LINK_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_LINK_LOG_IN = (By.CSS_SELECTOR, "login_submit")
    REG_LINK_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_LINK_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_LINK_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_LINK_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_LINK_REGISTRATION = (By.CSS_SELECTOR, "#register_form .btn-primary")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BUTTON_WRITE_A_REVIEW = (By.CSS_SELECTOR, "#write_review")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_AT_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_TITLE_AT_BASKET = (By.CSS_SELECTOR, "#messages .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(2) .alertinner")
    PRICE_ON_CARD = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_ON_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_PRODUCT_FORM = (By.CSS_SELECTOR, "#content_inner col-sm-6 h3")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(2) .alertinner")
