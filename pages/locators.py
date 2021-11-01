from selenium.webdriver.common.by import By


class MainPageLocators:
    # проверить необходимость логин линка
    LOGIN_LINK = (By.CSS_SELECTOR, ".MuiAvatar-img")
    TEAM_LINK = (By.LINK_TEXT, "/teams")


class LoginPageLocators:
    LOGIN_LINK_FORM = (By.CSS_SELECTOR, "#username")
    LOGIN_LINK_PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_LINK_LOG_IN = (By.CSS_SELECTOR, "#kc-form-buttons")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
