from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    # тест кейс проверок
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.click_login_form()
        self.click_password_form()
        self.click_submit()

    # реализована проверка на корректный url адрес
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, \
        "Word login is not presented in url"
        assert True

    # реализована проверка, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK_FORM), \
        "Login form is not presented"
        assert True

    def click_login_form(self):
        glogin_form = self.browser.find_element(*LoginPageLocators.LOGIN_LINK_FORM)
        glogin_form.click()
        glogin_form.send_keys("EvgenySemenov")

    def click_password_form(self):
        password_form = self.browser.find_element(*LoginPageLocators.LOGIN_LINK_PASSWORD)
        password_form.click()
        password_form.send_keys("Kikimora1237!")

    def click_submit(self):
        click_submit = self.browser.find_element(*LoginPageLocators.LOGIN_LINK_LOG_IN)
        click_submit.click()

