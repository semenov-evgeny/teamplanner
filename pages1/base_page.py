from selenium.common.exceptions import NoSuchElementException
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

   # метод поиска элементов
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # метод открытия страницы
    def open(self):
        self.browser.get(self.url)

    # метод перехода на страницу логина
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    # метод проверки наличия линка логина
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
        "Login link is not presented"

    # реализована проверка авторизации клиента
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), \
        "User icon is not presented, probably unauthorised user"
