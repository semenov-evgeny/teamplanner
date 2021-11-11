from selenium.webdriver.common.by import By


class MainPageLocators:
    # проверить необходимость логин линка
    LOGIN_LINK = (By.CSS_SELECTOR, ".MuiAvatar-root")
    PERSONAL_AREA = (By.TAG_NAME, "menuitem:nth-child(2)")
    TEAM_LINK = (By.LINK_TEXT, "Команды")


class LoginPageLocators:
    LOGIN_LINK_FORM = (By.CSS_SELECTOR, "#username")
    LOGIN_LINK_PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_LINK_LOG_IN = (By.CSS_SELECTOR, "#kc-login")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class PersonaAreaPageLocators:
    PERSONAL_AREA_MENU_NAME = (By.CSS_SELECTOR, ".x5-x5683.x5-x5693")
    PERSONAL_AREA_NAME = (By.CSS_SELECTOR, ".x5-x56258.x5-x5683.x5-x5684")
