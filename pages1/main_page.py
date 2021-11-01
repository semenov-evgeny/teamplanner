from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators


class MainPage(BasePage):

    # передаем полученные аргументы в родительский класс
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # метод перехода на вкладку команды
    def go_to_team_tab(self):
        go_to_team_tab = self.browser.find_element(*MainPageLocators.TEAM_LINK)
        go_to_team_tab.click()
        # self.solve_quiz_and_get_code()
