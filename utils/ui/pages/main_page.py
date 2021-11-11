from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    # передаем полученные аргументы в родительский класс
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_personal_area(self):
        go_to_personal_area = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        go_to_personal_area.click()

    def go_to_login_page(self):
        go_to_login_page = self.browser.find_element(*MainPageLocators.PERSONAL_AREA)
        go_to_login_page.click()

    # метод перехода на вкладку команды
    def go_to_team_tab(self):
        go_to_team_tab = self.browser.find_element(*MainPageLocators.TEAM_LINK)
        go_to_team_tab.click()


